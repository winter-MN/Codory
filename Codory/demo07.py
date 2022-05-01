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
pygame.display.set_caption("Codory Demo 07")
surface = pygame.Surface((base.SCREENWIDTH, base.SCREENHEIGHT), pygame.SRCALPHA).convert_alpha()
pygame.mixer.music.load("res/VeetaCrush - Sterelogue.ogg")
pygame.mixer.music.set_volume(0.5)

background = pygame.image.load("res/VeetaCrush - Sterelogue.jpg").convert()
background = pygame.transform.scale(background, (base.SCREENWIDTH, base.SCREENHEIGHT))
background.set_alpha(100)

# EffectTrack1 = widget.EffectTrack()
# EffectTrack2 = widget.EffectTrack()

dTrack, fTrack, jTrack, kTrack = analyse.json2Event("res\Sterelogue (4ky_another).mc")

# -------------------------------------------------

Track1 = base.Track(300, 500, 600)

pc = Track1.posCalculator
pc.AddEvent(0, 299, 600)
Track1.setup1()

for key in dTrack:
    if key["event"] == 1:
        Track1.noteList.append(
            base.Tap(float(key["time"]) - 1, float(key["time"]) - 0.5, float(key["time"]), Track1, 400))
    elif key["event"] == 2:
        gap = 0.1       # 每0.4s出现一个Drag
        Track1.noteList.append(
            base.Tap(float(key["time"]) - 1, float(key["time"]) - 0.5, float(key["time"]), Track1, 400))
        for i in range(1, int((float(key["endTime"]) - float(key["time"])) / gap)+1):
            hitTime = float(key["time"]) + gap * i
            Track1.noteList.append(
                base.Drag(hitTime - 1, hitTime - 0.5, hitTime, Track1, 400))

for key in fTrack:
    if key["event"] == 1:
        Track1.noteList.append(
            base.Tap(float(key["time"]) - 1, float(key["time"]) - 0.5, float(key["time"]), Track1, 500))
    elif key["event"] == 2:
        gap = 0.1       # 每0.4s出现一个Drag
        Track1.noteList.append(
            base.Tap(float(key["time"]) - 1, float(key["time"]) - 0.5, float(key["time"]), Track1, 500))
        for i in range(1, int((float(key["endTime"]) - float(key["time"])) / gap)+1):
            hitTime = float(key["time"]) + gap * i
            Track1.noteList.append(
                base.Drag(hitTime - 1, hitTime - 0.5, hitTime, Track1, 500))

Track1.setup2()

# --------------------------------------------------

Track2 = base.Track(300, 500, 600)

pc = Track2.posCalculator
pc.AddEvent(0, 299, 600)
Track2.setup1()

for key in jTrack:
    if key["event"] == 1:
        Track2.noteList.append(
            base.Tap(float(key["time"]) - 1, float(key["time"]) - 0.5, float(key["time"]), Track1, 100))
    elif key["event"] == 2:
        gap = 0.1       # 每0.4s出现一个Drag
        Track2.noteList.append(
            base.Tap(float(key["time"]) - 1, float(key["time"]) - 0.5, float(key["time"]), Track1, 100))
        for i in range(1, int((float(key["endTime"]) - float(key["time"])) / gap)+1):
            hitTime = float(key["time"]) + gap * i
            Track2.noteList.append(
                base.Drag(hitTime - 1, hitTime - 0.5, hitTime, Track1, 100))

for key in kTrack:
    if key["event"] == 1:
        Track2.noteList.append(
            base.Tap(float(key["time"]) - 1, float(key["time"]) - 0.5, float(key["time"]), Track1, 200))
    elif key["event"] == 2:
        gap = 0.1       # 每0.4s出现一个Drag
        Track2.noteList.append(
            base.Tap(float(key["time"]) - 1, float(key["time"]) - 0.5, float(key["time"]), Track1, 200))
        for i in range(1, int((float(key["endTime"]) - float(key["time"])) / gap)+1):
            hitTime = float(key["time"]) + gap * i
            Track2.noteList.append(
                base.Drag(hitTime - 1, hitTime - 0.5, hitTime, Track1, 200))

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

startTime = time.time()
clock = pygame.time.Clock()

# print(Track2.noteList[:10])
pygame.mixer.music.play()
while True:
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
            EvaluationDrawer.AddEvaluation(random.uniform(-0.05, 0.05), beat)
        Track1.noteList.pop(0)

    while Track2.noteList and Track2.noteList[0].hitTime < beat:
        x = base.SCREENWIDTH - NoteCanvas.x - Track2.GetPosByTime(Track2.noteList[0].hitTime) % base.NOTE_CANVAS_WIDTH
        EffectTrack.AddHit(x, 2, Track2.noteList[0].type)
        EffectDrawer.AddHit(beat, x, Track2.noteList[0].y, f"{Track2.noteList[0].type}Perfect")
        ScoreDrawer.AddHit(f"{Track2.noteList[0].type}Perfect")
        if Track2.noteList and Track2.noteList[0].type == "Tap":
            EvaluationDrawer.AddEvaluation(random.uniform(-0.05, 0.05), beat)
        Track2.noteList.pop(0)
    # print(Track2.noteList)
    NoteCanvas.Draw(beat)
    screen.blit(surface, (0, 0))
    pygame.display.flip()
