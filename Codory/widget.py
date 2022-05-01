import math
import random
import piecewise
import base
import time
import easingFunc
import pygame

pygame.init()


class EffectTrack:
    W = 40  # width of each bar
    T = 1  # 每个Hit的有效时间
    N = 8
    K = 7000
    B = 5

    def __init__(self, surface, x, y, track1, track2):
        self.surface = surface
        self.x = x  # 通常是 0
        self.y = y  # 通常是 0
        self.track1 = track1
        self.track2 = track2
        self.width = base.SCREENWIDTH
        self.height = base.SCREENHEIGHT
        self.track1HitList = []
        self.track2HitList = []

    def AddHit(self, pos, trackType, noteType):
        # trackType: 1 -> 下方轨道
        #            2 -> 上方轨道
        # noteType: 1 <- Tap
        #           4 <- Drag
        if noteType == "Tap":
            noteType = 1
        else:
            noteType = 4

        if trackType == 1:
            self.track1HitList.append([time.time(), pos, noteType])
        else:
            self.track2HitList.append([time.time(), pos, noteType])

    def Draw(self, playTime):
        # 删去过时hit
        nowTime = time.time()
        while self.track1HitList and self.track1HitList[0][0] + self.T < nowTime:
            self.track1HitList.pop(0)

        while self.track2HitList and self.track2HitList[0][0] + self.T < nowTime:
            self.track2HitList.pop(0)

        # 先绘制下方柱形图
        W = EffectTrack.W
        for i in range(base.SCREENWIDTH // W + 1):
            barHeight = 0
            for hitTime, pos, noteType in self.track1HitList:
                t = nowTime - hitTime
                if t < 0.2:
                    barHeight += (-25 * t * t + 10 * t) / (abs(pos - i * W + W / 2) + W) / noteType
                else:
                    barHeight += math.cos(math.pi * 5 / 8 * t - math.pi / 8) / (abs(pos - i * W + W / 2) + W) / noteType

            barHeight = math.log((barHeight + 1), EffectTrack.N)
            barHeight = barHeight * EffectTrack.K * (1 + len(self.track1HitList) / 20)
            barHeight += EffectTrack.B
            pygame.draw.lines(self.surface, (255, 255, 255, 155), True,
                              [(i * W - W / 2, self.y + base.SCREENHEIGHT / 2),
                               (i * W + W / 2, self.y + base.SCREENHEIGHT / 2),
                               (i * W + W / 2, self.y + base.SCREENHEIGHT / 2 + barHeight),
                               (i * W - W / 2, self.y + base.SCREENHEIGHT / 2 + barHeight)]
                              )

        # 绘制上方柱形图
        for i in range(base.SCREENWIDTH // W + 1):
            barHeight = 0
            for hitTime, pos, noteType in self.track2HitList:
                t = nowTime - hitTime
                if t < 0.2:
                    barHeight += (-25 * t * t + 10 * t) / (abs(pos - i * W + W / 2) + W) / noteType
                else:
                    barHeight += math.cos(math.pi * 5 / 8 * t - math.pi / 8) / (abs(pos - i * W + W / 2) + W) / noteType

            barHeight = math.log((barHeight + 1), EffectTrack.N)
            barHeight = barHeight * EffectTrack.K * (1 + len(self.track1HitList) / 20)
            barHeight += EffectTrack.B
            pygame.draw.lines(self.surface, (255, 255, 255, 155), True,
                              [(i * W - W / 2, self.y + base.SCREENHEIGHT / 2),
                               (i * W + W / 2, self.y + base.SCREENHEIGHT / 2),
                               (i * W + W / 2, self.y + base.SCREENHEIGHT / 2 - barHeight),
                               (i * W - W / 2, self.y + base.SCREENHEIGHT / 2 - barHeight)]
                              )
        # 绘制波浪图
        # index = 0
        # W = widget.EffectTrack.W
        #
        # for bar in EffectTrack1.getBars():
        #     pygame.draw.lines(surface, (255, 255, 255, 155), True, [(index*W, 300), (index*W+W, 300),
        #                                                    (index*W+W, 300+bar), (index*W, 300+bar)])
        #     index += 1
        #
        # index = 0
        # for bar in EffectTrack2.getBars():
        #     pygame.draw.lines(surface, (255, 255, 255, 155), True, [(index*W, 300), (index*W+W, 300),
        #                                                    (index*W+W, 300-bar), (index*W, 300-bar)])
        #     index += 1


class EffectDrawer:
    def __init__(self, surface, x, y, track1, track2):
        self.surface = surface
        self.x = x  # 0
        self.y = y  # (base.SCREENHEIGHT - base.NOTE_CANVAS_HEIGHT) / 2
        self.track1 = track1
        self.track2 = track2
        self.width = base.NOTE_CANVAS_WIDTH
        self.height = base.NOTE_CANVAS_HEIGHT
        self.hitList = []
        self.duration = 0.5  # 击打动效持续时间

    def AddHit(self, time_, x, y, type_):
        """
        添加一个击打
        :param time_: 击打时间
        :param x: 击打位置x
        :param y: 击打位置y
        :param type_: 击打的类型, f"{NOTE_TYPE}{EVAL}", e.g. "TapPerfect"
        :return:
        """
        self.hitList.append((time_, x, y, type_))

    def Draw(self, playTime):
        while self.hitList and self.hitList[0][0] + self.duration < playTime:
            self.hitList.pop(0)

        for time_, x, y, type_ in self.hitList:
            p = (playTime - time_) / self.duration
            p = - p * p + 2 * p  # 从0到1的二次曲线
            alpha = 255 - p * 255
            if "Tap" in type_:
                # 绘制圆形
                if "Perfect" in type_:
                    r = 40 * p + 40  # 圆的半径
                    base.TapPerfect.set_alpha(alpha)
                    TapPerfect = pygame.transform.scale(base.TapPerfect, (r * 2, r * 2))
                    self.surface.blit(TapPerfect, (x + self.x - r, y + self.y - r))
                    # pygame.draw.circle(self.surface, color, (x + self.x, y + self.y), r, 3)
            elif "Drag" in type_:
                if "Perfect" in type_:
                    r = 30 * p + 30  # 菱形的半径
                    base.DragPerfect.set_alpha(alpha)
                    DragPerfect = pygame.transform.scale(base.DragPerfect, (r * 2, r * 2))
                    self.surface.blit(DragPerfect, (x + self.x - r, y + self.y - r))


class NoteCanvas:
    # Note会出现的区域
    def __init__(self, surface, x, y, track1, track2):
        self.surface = surface
        self.x = x
        self.y = y
        self.track1 = track1
        self.track2 = track2
        self.width = base.NOTE_CANVAS_WIDTH
        self.height = base.NOTE_CANVAS_HEIGHT

    def Draw(self, playTime):
        # 绘制Note
        # Track 1, 即下方的轨道
        track1Note = list(self.track1.GetNoteByTime(playTime))
        track2Note = list(self.track2.GetNoteByTime(playTime))

        if (track1Note and track2Note and track1Note[0].hitTime < track2Note[0].hitTime) or (
                track1Note and not track2Note):
            # 下一个Note在track1打击
            note = track1Note.pop(0)
            alpha = 255 - 255 * (note.alphaTime - playTime) / (note.alphaTime - note.showTime)
            if note.type == "Tap":
                base.TapMulti.set_alpha(alpha)
                self.surface.blit(base.TapMulti,
                                  (self.x + note.x - 40, self.y + note.y - 40)
                                  )
            else:  # Drag
                base.DragMulti.set_alpha(alpha)
                self.surface.blit(base.DragMulti,
                                  (self.x + note.x - 30, self.y + note.y - 30)
                                  )
        elif (track1Note and track2Note and track1Note[0].hitTime > track2Note[0].hitTime) or (
                track2Note and not track1Note):
            # 下一个Note在track2打击
            note = track2Note.pop(0)
            alpha = 255 - 255 * (note.alphaTime - playTime) / (note.alphaTime - note.showTime)
            if note.type == "Tap":
                base.TapMulti.set_alpha(alpha)
                self.surface.blit(base.TapMulti,
                                  (self.width + self.x - note.x - 40, self.y + note.y - 40)
                                  )
            else:  # Drag
                base.DragMulti.set_alpha(alpha)
                self.surface.blit(base.DragMulti,
                                  (self.width + self.x - note.x - 30, self.y + note.y - 30)
                                  )

        elif track1Note and track2Note and track1Note[0].hitTime == track2Note[0].hitTime:
            note = track1Note.pop(0)
            alpha = 255 - 255 * (note.alphaTime - playTime) / (note.alphaTime - note.showTime)
            if note.type == "Tap":
                base.TapMulti.set_alpha(alpha)
                self.surface.blit(base.TapMulti,
                                  (self.x + note.x - 40, self.y + note.y - 40)
                                  )
            else:  # Drag
                base.DragMulti.set_alpha(alpha)
                self.surface.blit(base.DragMulti,
                                  (self.x + note.x - 30, self.y + note.y - 30)
                                  )

            note = track2Note.pop(0)
            alpha = 255 - 255 * (note.alphaTime - playTime) / (note.alphaTime - note.showTime)
            if note.type == "Tap":
                base.TapMulti.set_alpha(alpha)
                self.surface.blit(base.TapMulti,
                                  (self.width + self.x - note.x - 40, self.y + note.y - 40)
                                  )
            else:  # Drag
                base.DragMulti.set_alpha(alpha)
                self.surface.blit(base.DragMulti,
                                  (self.width + self.x - note.x - 30, self.y + note.y - 30)
                                  )

        for note in track1Note:
            alpha = 255 - 255 * (note.alphaTime - playTime) / (note.alphaTime - note.showTime)
            if note.type == "Tap":
                base.TapImage.set_alpha(alpha)
                self.surface.blit(base.TapImage,
                                  (self.x + note.x - 40, self.y + note.y - 40)
                                  )
            else:  # Drag
                base.DragImage.set_alpha(alpha)
                self.surface.blit(base.DragImage,
                                  (self.x + note.x - 30, self.y + note.y - 30)
                                  )

        # Track 2, 即上方的轨道
        for note in track2Note:
            alpha = 255 - 255 * (note.alphaTime - playTime) / (note.alphaTime - note.showTime)
            if note.type == "Tap":
                base.TapImage.set_alpha(alpha)
                self.surface.blit(base.TapImage,
                                  (self.width + self.x - note.x - 40, self.y + note.y - 40)
                                  )
            else:  # Drag
                base.DragImage.set_alpha(alpha)
                self.surface.blit(base.DragImage,
                                  (self.width + self.x - note.x - 30, self.y + note.y - 30)
                                  )


class JudgeLineCanvas:
    # 绘制判定线，包括真实判定线和虚拟判定线
    def __init__(self, surface, x, y, track1: base.Track, track2: base.Track):
        self.surface = surface
        self.x = x
        self.y = y
        self.track1 = track1
        self.track2 = track2

    def Draw(self, playTime):
        # 绘制判定线

        # Track 1, 即下方轨道
        # 先绘制真实判定线
        x = self.track1.GetPosByTime(playTime) % base.NOTE_CANVAS_WIDTH + self.x
        pygame.draw.line(self.surface, (255, 0, 0), (x, self.y + base.NOTE_CANVAS_HEIGHT / 2),
                         (x, self.y + base.NOTE_CANVAS_HEIGHT))
        # 再绘制虚拟判定线
        pygame.draw.line(self.surface, (255, 0, 0),
                         (x - base.NOTE_CANVAS_WIDTH, self.y + base.NOTE_CANVAS_HEIGHT / 2),
                         (x - base.NOTE_CANVAS_WIDTH, self.y + base.NOTE_CANVAS_HEIGHT))

        pygame.draw.line(self.surface, (255, 0, 0),
                         (x + base.NOTE_CANVAS_WIDTH, self.y + base.NOTE_CANVAS_HEIGHT / 2),
                         (x + base.NOTE_CANVAS_WIDTH, self.y + base.NOTE_CANVAS_HEIGHT))

        # Track 2, 即上方轨道
        # 先绘制真实判定线
        x = base.NOTE_CANVAS_WIDTH - self.track2.GetPosByTime(playTime) % base.NOTE_CANVAS_WIDTH + self.x
        pygame.draw.line(self.surface, (255, 0, 0), (x, self.y),
                         (x, self.y + base.NOTE_CANVAS_HEIGHT / 2))

        # 再绘制虚拟判定线
        pygame.draw.line(self.surface, (255, 0, 0),
                         (x + base.NOTE_CANVAS_WIDTH, self.y + base.NOTE_CANVAS_HEIGHT / 2),
                         (x + base.NOTE_CANVAS_WIDTH, self.y))
        pygame.draw.line(self.surface, (255, 0, 0),
                         (x - base.NOTE_CANVAS_WIDTH, self.y + base.NOTE_CANVAS_HEIGHT / 2),
                         (x - base.NOTE_CANVAS_WIDTH, self.y))


class ScoreDrawer:
    def __init__(self, surface, x, y, track1, track2):
        self.surface = surface
        self.x = x  # 0
        self.y = y  # 0
        self.track1 = track1
        self.track2 = track2
        self.width = base.NOTE_CANVAS_WIDTH
        self.height = base.NOTE_CANVAS_HEIGHT
        self.score = 0
        self.score_font = pygame.font.SysFont("arial", 30)
        self.combo_font = pygame.font.SysFont("arial", 40)
        self.noteNum = base.GetNoteNum(track1, track2)
        self.perfectNum = 0
        self.goodNum = 0
        self.combo = 0

    def AddHit(self, hitType):
        # 计算分数
        # fixme: 考虑miss & bad
        if "Perfect" in hitType:
            self.perfectNum += 1
        elif "Good" in hitType:
            self.goodNum += 1
        self.score = 1000000 * self.perfectNum / self.noteNum + 100000 * self.goodNum / self.noteNum * 0.5
        self.combo += 1

    def Draw(self, playTime):
        score = str(int(self.score)).rjust(7, "0")
        self.surface.blit(self.score_font.render(score, True, (255, 255, 255)), (base.SCREENWIDTH - 140, self.y))

        comboText = self.combo_font.render("COMBO", True, (255, 255, 255))
        self.surface.blit(comboText, (self.x + base.SCREENWIDTH / 2 - comboText.get_width() / 2, self.y))

        comboNum = self.combo_font.render(str(self.combo), True, (255, 255, 255))
        self.surface.blit(comboNum,
                          (self.x + base.SCREENWIDTH / 2 - comboNum.get_width() / 2, self.y + comboText.get_height()))


class SeparatorDrawer:
    def __init__(self, surface, x, y, track1, track2):
        self.surface = surface
        self.x = x  # 0
        self.y = y  # 0
        self.track1 = track1
        self.track2 = track2
        self.width = base.NOTE_CANVAS_WIDTH
        self.height = base.NOTE_CANVAS_HEIGHT

    def Draw(self, playTime):
        # 绘制分隔线
        pygame.draw.line(self.surface, (255, 255, 255, 155),
                         (self.x, self.y + base.SCREENHEIGHT / 2 - base.NOTE_CANVAS_HEIGHT / 2),
                         (self.x + base.SCREENWIDTH, self.y + base.SCREENHEIGHT / 2 - base.NOTE_CANVAS_HEIGHT / 2))

        pygame.draw.line(self.surface, (255, 255, 255, 155),
                         (self.x, self.y + base.SCREENHEIGHT / 2 + base.NOTE_CANVAS_HEIGHT / 2),
                         (self.x + base.SCREENWIDTH, self.y + base.SCREENHEIGHT / 2 + base.NOTE_CANVAS_HEIGHT / 2))

        pygame.draw.line(self.surface, (255, 255, 255, 155),
                         ((base.SCREENWIDTH - base.NOTE_CANVAS_WIDTH) / 2,
                          self.y + base.SCREENHEIGHT / 2 - base.NOTE_CANVAS_HEIGHT / 2),
                         ((base.SCREENWIDTH - base.NOTE_CANVAS_WIDTH) / 2,
                          self.y + base.SCREENHEIGHT / 2 + base.NOTE_CANVAS_HEIGHT / 2))

        pygame.draw.line(self.surface, (255, 255, 255, 155),
                         ((base.SCREENWIDTH + base.NOTE_CANVAS_WIDTH) / 2,
                          self.y + base.SCREENHEIGHT / 2 - base.NOTE_CANVAS_HEIGHT / 2),
                         ((base.SCREENWIDTH + base.NOTE_CANVAS_WIDTH) / 2,
                          self.y + base.SCREENHEIGHT / 2 + base.NOTE_CANVAS_HEIGHT / 2))
        # surface,
        #                                (base.SCREENWIDTH - base.NOTE_CANVAS_WIDTH) / 2,
        #                                (base.SCREENHEIGHT - base.NOTE_CANVAS_HEIGHT) / 2,
        #                                Track1, Track2)


class EvaluationDrawer:
    # 下方判定框
    def __init__(self, surface, x, y, track1, track2):
        self.surface = surface
        self.x = x  # 0
        self.y = y  # 0
        self.track1 = track1
        self.track2 = track2
        self.width = base.SCREENWIDTH
        self.height = base.SCREENHEIGHT
        self.deltaList = []
        self.blue = (50, 188, 231)
        self.green = (87, 227, 19)
        self.yellow = (218, 174, 70)
        self.arrowX = self.x + base.SCREENWIDTH / 2 - 20  # 箭头的x坐标
        self.destinationOfLastAdd = 0  # 箭头目标位置
        self.playTimeOfLastAdd = 0
        self.arrowXExp = easingFunc.EaseOutQuad(self.playTimeOfLastAdd, self.playTimeOfLastAdd + 0.5,
                                                self.arrowX, self.arrowX)

    def AddEvaluation(self, delta, playTime):
        # delta: 击打时间差
        self.deltaList.append(delta)
        self.deltaList = self.deltaList[-25:]  # 保留最近25个击打

        # 以上一次箭头的位置为起点，以目标位置为终点，构造箭头X坐标的位置
        # 更新目标位置
        evaluation = base.GetEvaluation(delta)
        if evaluation == "Bad":
            self.destinationOfLastAdd = self.x + base.SCREENWIDTH / 2 - 400 - 20
        elif evaluation == "Miss":
            self.destinationOfLastAdd = self.x + base.SCREENWIDTH / 2 + 400 - 20
        else:
            self.destinationOfLastAdd = self.x + base.SCREENWIDTH / 2 - 320 * self.deltaList[-1] / base.goodRange - 20

        # self.destinationOfLastAdd = self.x + base.SCREENWIDTH / 2 - 320 * self.deltaList[-1] / base.goodRange - 20
        self.playTimeOfLastAdd = playTime
        self.arrowXExp = easingFunc.EaseOutQuad(self.playTimeOfLastAdd, self.playTimeOfLastAdd + 0.15,
                                                self.arrowX, self.destinationOfLastAdd)

    def Draw(self, playTime):
        # 绘制
        thickness = 20
        y1 = base.SCREENHEIGHT - thickness * 2
        y2 = base.SCREENHEIGHT - thickness
        self.surface.blit(base.EvalBg, (self.x + base.SCREENWIDTH / 2 - 400 - 5, self.y + y1 - thickness))
        pygame.draw.polygon(self.surface, self.yellow,
                            [(self.x + base.SCREENWIDTH / 2 - 400, y1),
                             (self.x + base.SCREENWIDTH / 2 - 400, y2),
                             (self.x + base.SCREENWIDTH / 2 + 400, y2),
                             (self.x + base.SCREENWIDTH / 2 + 400, y1)])

        pygame.draw.polygon(self.surface, self.green,
                            [(self.x + base.SCREENWIDTH / 2 - 320, y1),
                             (self.x + base.SCREENWIDTH / 2 + 320, y1),
                             (self.x + base.SCREENWIDTH / 2 + 320, y2),
                             (self.x + base.SCREENWIDTH / 2 - 320, y2)])

        pygame.draw.polygon(self.surface, self.blue,
                            [(self.x + base.SCREENWIDTH / 2 - 160, y1),
                             (self.x + base.SCREENWIDTH / 2 + 160, y1),
                             (self.x + base.SCREENWIDTH / 2 + 160, y2),
                             (self.x + base.SCREENWIDTH / 2 - 160, y2)])
        i = 0
        for delta in self.deltaList[::-1]:
            i += 1
            evaluation = base.GetEvaluation(delta)
            alpha = 200 - i * 8
            base.EvalMark.set_alpha(alpha)
            if evaluation == "Bad":
                self.surface.blit(base.EvalMark, (self.x + base.SCREENWIDTH / 2 - 400 - 5, y1 - thickness))
            elif evaluation == "Miss":
                self.surface.blit(base.EvalMark, (self.x + base.SCREENWIDTH / 2 + 400 - 5, y1 - thickness))
            else:
                self.surface.blit(base.EvalMark,
                                  (self.x + base.SCREENWIDTH / 2 - 320 * delta / base.goodRange - 5, y1 - thickness))

        if self.deltaList:
            if playTime > self.playTimeOfLastAdd + 0.15:
                # 箭头已到达目标位置
                self.arrowX = self.destinationOfLastAdd
            else:
                self.arrowX = self.arrowXExp.Calculate(playTime)

        self.surface.blit(base.EvalArrow,
                          (self.arrowX, y1 - thickness))
