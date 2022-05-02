"""
铺面游玩
"""

import analyse
import base
import pygame
import widget
import sys
import math
import time
import random

pygame.init()
pygame.mixer.init()

TITLE = "SIGMA"
MUSIC_PATH = f"res/altale/music.ogg"
BG_PATH = f"res/altale/background.png"
BEATMAP_PATH = f"res/altale/AltaleEZ.mc"

screen = pygame.display.set_mode((base.SCREENWIDTH, base.SCREENHEIGHT))
pygame.display.set_caption("Codory Demo 09")
surface = pygame.Surface((base.SCREENWIDTH, base.SCREENHEIGHT), pygame.SRCALPHA).convert_alpha()
pygame.mixer.music.load(MUSIC_PATH)
pygame.mixer.music.set_volume(0.5)

background = pygame.image.load(BG_PATH).convert()
background = pygame.transform.scale(background, (base.SCREENWIDTH, base.SCREENHEIGHT))
background.set_alpha(100)

# EffectTrack1 = widget.EffectTrack()
# EffectTrack2 = widget.EffectTrack()

Tracks = analyse.json2Event(BEATMAP_PATH)

# -------------------------------------------------

Track1 = base.Track(300, 500, 600)

pc = Track1.posCalculator
pc.AddEvent(0, 299, 600)
Track1.setup1()

n = len(Tracks) // 2
index = 0
for Track in Tracks[:n]:
    index += 1
    for key in Track:
        if key["event"] == 1:
            Track1.noteList.append(
                base.Tap(float(key["time"]) - 0.6, float(key["time"]) - 0.3, float(key["time"]), Track1,
                         base.NOTE_CANVAS_HEIGHT / 2 * (1 + index / (n + 1))))
        elif key["event"] == 2:
            gap = 0.1  # 每0.1s出现一个Drag
            Track1.noteList.append(
                base.Tap(float(key["time"]) - 0.6, float(key["time"]) - 0.3, float(key["time"]), Track1,
                         base.NOTE_CANVAS_HEIGHT / 2 * (1 + index / (n + 1))))

            for i in range(1, int((float(key["endTime"]) - float(key["time"])) / gap) + 1):
                hitTime = float(key["time"]) + gap * i
                Track1.noteList.append(
                    base.Drag(hitTime - 0.6, hitTime - 0.3, hitTime, Track1,
                              base.NOTE_CANVAS_HEIGHT / 2 * (1 + index / (n + 1))))

Track1.setup2()

# --------------------------------------------------

Track2 = base.Track(300, 500, 600)

pc = Track2.posCalculator
pc.AddEvent(10, 299, 600)
Track2.setup1()

index = 0
for Track in Tracks[n:]:
    index += 1
    for key in Track:
        if key["event"] == 1:
            Track2.noteList.append(
                base.Tap(float(key["time"]) - 0.6, float(key["time"]) - 0.3, float(key["time"]), Track1,
                         base.NOTE_CANVAS_HEIGHT / 2 * (index / (n + 1))))
        elif key["event"] == 2:
            gap = 0.1  # 每0.1s出现一个Drag
            Track2.noteList.append(
                base.Tap(float(key["time"]) - 0.6, float(key["time"]) - 0.3, float(key["time"]), Track1,
                         base.NOTE_CANVAS_HEIGHT / 2 * (index / (n + 1))))
            for i in range(1, int((float(key["endTime"]) - float(key["time"])) / gap) + 1):
                hitTime = float(key["time"]) + gap * i
                Track2.noteList.append(
                    base.Drag(hitTime - 0.6, hitTime - 0.3, hitTime, Track1,
                              base.NOTE_CANVAS_HEIGHT / 2 * (index / (n + 1))))


Track2.setup2()

# --------------------------------------------------

JudgeLineCanvas = widget.JudgeLineCanvas(surface,
                                         (base.SCREENWIDTH - base.NOTE_CANVAS_WIDTH) / 2,
                                         (base.SCREENHEIGHT - base.NOTE_CANVAS_HEIGHT) / 2,
                                         Track1, Track2)

NoteCanvas = widget.NoteCanvas(surface,
                               (base.SCREENWIDTH - base.NOTE_CANVAS_WIDTH) / 2,
                               (base.SCREENHEIGHT - base.NOTE_CANVAS_HEIGHT) / 2,
                               Track1, Track2)

EffectTrack = widget.EffectTrack(surface,
                                 0,
                                 0,
                                 Track1, Track2)

EffectDrawer = widget.EffectDrawer(surface,
                                   0,
                                   (base.SCREENHEIGHT - base.NOTE_CANVAS_HEIGHT) / 2,
                                   Track1, Track2)

ScoreDrawer = widget.ScoreDrawer(surface,
                                 0,
                                 0,
                                 Track1, Track2)

SeparatorLine = widget.SeparatorDrawer(surface,
                                       0,
                                       0,
                                       Track1, Track2)

EvaluationDrawer = widget.EvaluationDrawer(surface,
                                           0,
                                           0,
                                           Track1, Track2)

KeyboardInfo = base.KeyboardInfo()

welcomed = False
inited = False
clock = pygame.time.Clock()
titleFont = pygame.font.SysFont("simHei", 30)
startTime = time.time()

while True:
    if welcomed and not inited:
        inited = True
        startTime = time.time()
        pygame.mixer.music.play()
    if not welcomed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        screen.fill((0, 0, 0))
        surface.fill((0, 0, 0, 255))
        p = time.time() - startTime
        if 0 < p < 1:
            base.WelcomeImg.set_alpha(int(p * 255))
            surface.blit(base.WelcomeImg, (0, 0))
        elif 3 < p < 4:
            base.WelcomeImg.set_alpha(int((4 - p) * 255))
            surface.blit(base.WelcomeImg, (0, 0))
        elif 1 <= p <= 3:
            base.WelcomeImg.set_alpha(255)
            surface.blit(base.WelcomeImg, (0, 0))
        elif 4 < p < 5:
            base.Welcome2Img.set_alpha(int((p-4) * 255))
            surface.blit(base.Welcome2Img, (0, 0))
        elif 7 < p < 8:
            base.Welcome2Img.set_alpha(int((4 - (p-4)) * 255))
            surface.blit(base.Welcome2Img, (0, 0))
        else:
            base.Welcome2Img.set_alpha(255)
            surface.blit(base.Welcome2Img, (0, 0))
        if p > 8:
            welcomed = True
        screen.blit(surface, (0, 0))
        pygame.display.flip()
        continue

    clock.tick(60)
    playTime = (time.time() - startTime)

    # 获取键盘上有效按键按下了几个
    # 按下一个按键只能判定一个Drag
    keyPressedNum = KeyboardInfo.GetPressedNum()

    track1Note = list(Track1.GetNoteByTime(playTime))
    track2Note = list(Track2.GetNoteByTime(playTime))
    # 找到下一个要被打击的Note
    notes = track1Note + track2Note
    notes.sort(key=lambda x: x.hitTime)

    for note in notes:
        # 计算出Note的显示位置
        if note in track1Note:
            x = NoteCanvas.x + Track1.GetPosByTime(note.hitTime) % base.NOTE_CANVAS_WIDTH
        else:
            x = base.SCREENWIDTH - NoteCanvas.x - Track2.GetPosByTime(
                note.hitTime) % base.NOTE_CANVAS_WIDTH
        delta = playTime - note.hitTime
        if note.type == "Drag":
            evaluation = base.GetEvaluation(delta)
            if evaluation == "Miss":
                if note in track1Note:
                    Track1.noteList.remove(note)
                else:
                    Track2.noteList.remove(note)
                EffectDrawer.AddHit(playTime, x, note.y, f"Drag{evaluation}")
                ScoreDrawer.AddHit(f"Drag{evaluation}")

            elif note.hitTime < playTime and keyPressedNum > 0:  # 已经可以进行判定
                # 此处的 evaluation 不会出现 Invalid
                if note in track1Note:
                    Track1.noteList.remove(note)
                else:
                    Track2.noteList.remove(note)
                EffectDrawer.AddHit(playTime, x, note.y, f"Drag{evaluation}")
                EffectTrack.AddHit(x, 1 if note in track1Note else 2, "Drag")
                ScoreDrawer.AddHit(f"Drag{evaluation}")
                keyPressedNum -= 1

        elif note.type == "Tap":
            # 判定Miss
            if base.GetEvaluation(delta) == "Miss":
                if note in track1Note:
                    Track1.noteList.remove(note)
                else:
                    Track2.noteList.remove(note)
                EffectDrawer.AddHit(playTime, x, note.y, f"TapMiss")
                ScoreDrawer.AddHit(f"TapMiss")
                EvaluationDrawer.AddEvaluation(delta, playTime)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type in [pygame.KEYDOWN, pygame.KEYUP]:
            KeyboardInfo.RespondEvent(event)
            if event.type == pygame.KEYDOWN:
                # 进行Tap的Perfect/Good/Bad/Invalid判定
                if event.unicode.upper() in base.KEY_MAP:
                    track1Note = list(Track1.GetNoteByTime(playTime))
                    track2Note = list(Track2.GetNoteByTime(playTime))
                    # 找到下一个要被打击的Note
                    notes = track1Note + track2Note
                    notes.sort(key=lambda x: abs(x.hitTime - playTime))
                    while notes and notes[0].type == "Drag":
                        notes.pop(0)
                        continue

                    if notes:  # 只有出现在屏幕上的Note会被判定
                        note = notes[0]
                        if note in track1Note:
                            x = NoteCanvas.x + Track1.GetPosByTime(note.hitTime) % base.NOTE_CANVAS_WIDTH
                        else:
                            x = base.SCREENWIDTH - NoteCanvas.x - Track2.GetPosByTime(
                                note.hitTime) % base.NOTE_CANVAS_WIDTH
                        hitTimeOfNextNote = note.hitTime
                        delta = playTime - hitTimeOfNextNote
                        evaluation = base.GetEvaluation(delta)
                        # 此处的 evaluation 只会出现 Perfect/Good/Bad/Invalid 四种类型
                        if evaluation == "Invalid":
                            continue
                        else:
                            # 成功被判定，则该Note已被击打，应从NoteList中移除
                            if note in track1Note:
                                Track1.noteList.remove(note)
                            else:
                                Track2.noteList.remove(note)
                            EffectDrawer.AddHit(playTime, x, note.y, f"Tap{evaluation}")
                            EffectTrack.AddHit(x, 1 if note in track1Note else 2, "Tap")
                            ScoreDrawer.AddHit(f"Tap{evaluation}")
                            EvaluationDrawer.AddEvaluation(delta, playTime)

    if playTime >= 300:
        continue
    screen.fill((0, 0, 0))
    surface.fill((0, 0, 0, 255))
    surface.blit(background, (0, 0))
    JudgeLineCanvas.Draw(playTime)
    # ---------------------------------------------
    # 绘制标题与fps
    surface.blit(titleFont.render(TITLE, True, (255, 255, 255)), (0, 0))
    surface.blit(titleFont.render(f"fps:{int(clock.get_fps())}", True, (255, 255, 255)), (0, 30))
    # ---------------------------------------------
    EffectTrack.Draw(playTime)
    EffectDrawer.Draw(playTime)
    ScoreDrawer.Draw(playTime)
    SeparatorLine.Draw(playTime)
    EvaluationDrawer.Draw(playTime)
    NoteCanvas.Draw(playTime)
    # ---------------------------------------------

    # print(Track2.noteList)

    screen.blit(surface, (0, 0))
    pygame.display.flip()
