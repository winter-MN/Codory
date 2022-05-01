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

screen = pygame.display.set_mode((base.SCREENWIDTH, base.SCREENHEIGHT))
pygame.display.set_caption("Codory Demo 08")
surface = pygame.Surface((base.SCREENWIDTH, base.SCREENHEIGHT), pygame.SRCALPHA).convert_alpha()
pygame.mixer.music.load("res/Altale.ogg")
pygame.mixer.music.set_volume(0.5)

background = pygame.image.load("res/altale.jpg").convert()
background = pygame.transform.scale(background, (base.SCREENWIDTH, base.SCREENHEIGHT))
background.set_alpha(100)

# EffectTrack1 = widget.EffectTrack()
# EffectTrack2 = widget.EffectTrack()

Tracks = analyse.json2Event(r"res\altaleEZ.mc")

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
                         base.NOTE_CANVAS_HEIGHT/2 * (1 + index / (n+1))))
        elif key["event"] == 2:
            gap = 0.1       # 每0.1s出现一个Drag
            Track1.noteList.append(
                base.Tap(float(key["time"]) - 0.6, float(key["time"]) - 0.3, float(key["time"]), Track1,
                         base.NOTE_CANVAS_HEIGHT/2 * (1 + index / (n+1))))

            for i in range(1, int((float(key["endTime"]) - float(key["time"])) / gap)+1):
                hitTime = float(key["time"]) + gap * i
                Track1.noteList.append(
                    base.Drag(hitTime - 0.6, hitTime - 0.3, hitTime, Track1,
                              base.NOTE_CANVAS_HEIGHT/2 * (1 + index / (n+1))))


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
                         base.NOTE_CANVAS_HEIGHT/2 * (index / (n+1))))
        elif key["event"] == 2:
            gap = 0.1       # 每0.1s出现一个Drag
            Track2.noteList.append(
                base.Tap(float(key["time"]) - 0.6, float(key["time"]) - 0.3, float(key["time"]), Track1,
                         base.NOTE_CANVAS_HEIGHT/2 * (index / (n+1))))
            for i in range(1, int((float(key["endTime"]) - float(key["time"])) / gap)+1):
                hitTime = float(key["time"]) + gap * i
                Track2.noteList.append(
                    base.Drag(hitTime - 0.6, hitTime - 0.3, hitTime, Track1,
                              base.NOTE_CANVAS_HEIGHT/2 * (index / (n+1))))

# for key in kTrack:
#     if key["event"] == 1:
#         Track2.noteList.append(
#             base.Tap(float(key["time"]) - 1, float(key["time"]) - 0.5, float(key["time"]), Track1, 200))
#     elif key["event"] == 2:
#         gap = 0.1       # 每0.4s出现一个Drag
#         Track2.noteList.append(
#             base.Tap(float(key["time"]) - 1, float(key["time"]) - 0.5, float(key["time"]), Track1, 200))
#         for i in range(1, int((float(key["endTime"]) - float(key["time"])) / gap)+1):
#             hitTime = float(key["time"]) + gap * i
#             Track2.noteList.append(
#                 base.Drag(hitTime - 1, hitTime - 0.5, hitTime, Track1, 200))

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

welcomed = True
inited = False
clock = pygame.time.Clock()
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
        else:
            base.WelcomeImg.set_alpha(255)
            surface.blit(base.WelcomeImg, (0, 0))
        if p > 4:
            welcomed = True
        screen.blit(surface, (0, 0))
        pygame.display.flip()
        continue

    clock.tick(120)
    beat = (time.time() - startTime)
    # print(beat)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    if beat >= 300:
        continue
    screen.fill((0, 0, 0))
    surface.fill((0, 0, 0, 255))
    surface.blit(background, (0, 0))
    JudgeLineCanvas.Draw(beat)
    # ---------------------------------------------
    EffectTrack.Draw(beat)
    EffectDrawer.Draw(beat)
    ScoreDrawer.Draw(beat)
    SeparatorLine.Draw(beat)
    EvaluationDrawer.Draw(beat)
    # ---------------------------------------------

    while Track1.noteList and Track1.noteList[0].hitTime < beat:
        x = NoteCanvas.x + Track1.GetPosByTime(Track1.noteList[0].hitTime) % base.NOTE_CANVAS_WIDTH
        EffectTrack.AddHit(x, 1, Track1.noteList[0].type)
        EffectDrawer.AddHit(beat, x, Track1.noteList[0].y, f"{Track1.noteList[0].type}Perfect")
        ScoreDrawer.AddHit(f"{Track1.noteList[0].type}Perfect")
        if Track1.noteList and Track1.noteList[0].type == "Tap":
            EvaluationDrawer.AddEvaluation(random.uniform(-0.02, 0.02), beat)
        Track1.noteList.pop(0)

    while Track2.noteList and Track2.noteList[0].hitTime < beat:
        x = base.SCREENWIDTH - NoteCanvas.x - Track2.GetPosByTime(Track2.noteList[0].hitTime) % base.NOTE_CANVAS_WIDTH
        EffectTrack.AddHit(x, 2, Track2.noteList[0].type)
        EffectDrawer.AddHit(beat, x, Track2.noteList[0].y, f"{Track2.noteList[0].type}Perfect")
        ScoreDrawer.AddHit(f"{Track2.noteList[0].type}Perfect")
        if Track2.noteList and Track2.noteList[0].type == "Tap":
            EvaluationDrawer.AddEvaluation(random.uniform(-0.02, 0.02), beat)
        Track2.noteList.pop(0)
    # print(Track2.noteList)
    NoteCanvas.Draw(beat)
    screen.blit(surface, (0, 0))
    pygame.display.flip()
