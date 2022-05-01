from interface import *
import beat2time
import piecewise
import pygame

pygame.init()

SCREENWIDTH = 1280
SCREENHEIGHT = 800

NOTE_CANVAS_WIDTH = 980  # note会出现的区域
NOTE_CANVAS_HEIGHT = 600  # note会出现的区域
# CVHEIGTH = 750

# 判定区间，单向区间，单位s
# 差值计算方法为 实际按下时刻 - 理论按下时刻
# perfect判定 -80ms ~ 80ms
perfectRange = 0.08
# good判定 -160ms ~ 160ms
goodRange = 0.16
# delta > 160 : bad
# delta < -160 : miss

# 无效输入判定
invalidRange = 0.4

TapImage = pygame.image.load("res\\TapImg.png")
TapFailed = pygame.image.load("res\\TapFailed.png")
TapPerfect = pygame.image.load("res\\TapPerfect.png")
TapGood = pygame.image.load("res\\TapGood.png")
TapMulti = pygame.image.load("res\\TapMulti.png")

DragImage = pygame.image.load("res\\DragImg.png")
DragFailed = pygame.image.load("res\\DragFailed.png")
DragPerfect = pygame.image.load("res\\DragPerfect.png")
DragGood = pygame.image.load("res\\DragGood.png")
DragMulti = pygame.image.load("res\\DragMulti.png")


EvalBg = pygame.image.load("res\\EvalBg.png")
EvalBg.set_alpha(100)
EvalMark = pygame.image.load("res\\EvalMark.png")
EvalMark.set_alpha(100)
EvalArrow = pygame.image.load("res\\EvalArrow.png")

WelcomeImg = pygame.image.load("res\\Welcome.png")

score = 0


class Track:
    def __init__(self, stopBeat, acc=500, initSpeed=0):
        self.posCalculator = piecewise.PosCalculator(stopBeat, acc, initSpeed)
        # 轨道透明度
        self.alpha = 255
        # 该Track上的音符列表
        # [Note(5,), Note(6), Note(7), Note(8), Note(9), Note(10), Note(11)]
        self.noteList = []

    def setup1(self):
        # 运行前准备
        self.posCalculator.Translate()

    def setup2(self):
        self.noteList.sort(key=lambda note: note.showTime)

    def GetPosByTime(self, playTime):
        return self.posCalculator.GetPos(playTime)

    def GetNoteByTime(self, playTime):
        # 只负责给出showTime <= playTime的Note，不执行删除操作
        for note in self.noteList:
            if note.showTime <= playTime:
                yield note
            else:
                break


class Note:
    def __init__(self, showTime, alphaTime, hitTime, track, y):
        # 被点击的beat
        self.showTime = ConvertToFloat(showTime)
        self.alphaTime = ConvertToFloat(alphaTime)
        self.hitTime = ConvertToFloat(hitTime)
        self.track = track
        self.y = y      # 该note在NoteCanvas上的y坐标
        self.x = self.track.GetPosByTime(self.hitTime)
        self.x %= NOTE_CANVAS_WIDTH


class Tap(Note):
    def __init__(self, showTime, alphaTime, hitTime, track, y):
        super(Tap, self).__init__(showTime, alphaTime, hitTime, track, y)
        self.type = "Tap"


class Drag(Note):
    def __init__(self, showTime, alphaTime, hitTime, track, y):
        super(Drag, self).__init__(showTime, alphaTime, hitTime, track, y)
        self.type = "Drag"


class Value:
    def __init__(self, value):
        self.value = value


class Second(Value):
    def __init__(self, value):
        super().__init__(value)
        self.type = "Second"


class Beat(Value):
    def __init__(self, value):
        super().__init__(value)
        self.type = "Beat"


def ConvertToFloat(valueObject):
    if isinstance(valueObject, Second):
        return valueObject.value
    elif isinstance(valueObject, Beat):
        return beat2time.b2t(valueObject.value)
    else:
        return valueObject


def GetNoteNum(track1, track2):
    # 获取总note数
    return len(track1.noteList) + len(track2.noteList)


def GetEvaluation(delta):
    # 判定
    # delta > 0 : 慢了
    if -perfectRange <= delta <= perfectRange:
        return "Perfect"
    elif -goodRange <= delta <= goodRange:
        return "Good"
    elif delta > goodRange:
        return "Miss"
    elif -invalidRange < delta < -goodRange:
        return "Bad"
    else:
        return "Invalid"



if __name__ == '__main__':
    Track1 = Track()  # 上部轨道
    Track2 = Track()  # 下部轨道
    # node = Node(100, 100)
    # print(Track(node, 0).getNotePositionByBeat(0))
    # print(Track(node, 0).getNotePositionByBeat(1))
    # print(Track(node, 0).getNotePositionByBeat(2))
    # print(Track(node, 0).getNotePositionByBeat(3))
    # print(Track(node, 0).getNotePositionByBeat(4))
    # print(Track(node, 0).getNotePositionByBeat(5))
    # print(Track(node, 0).getNotePositionByBeat(6))
