"""
铺面AUTO演示
"""
import analyse
import base
import pygame
import widget
import sys
import math
import time

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Codory Demo 06")
surface = pygame.Surface((800, 600), pygame.SRCALPHA)
pygame.mixer.music.load("res/VeetaCrush - Sterelogue.ogg")
pygame.mixer.music.set_volume(0.5)

background = pygame.image.load("res/VeetaCrush - Sterelogue.jpg").convert()
background = pygame.transform.scale(background, (800, 600))
background.set_alpha(100)

noteImg = pygame.image.load("res\\noteImg.png")
noteFailImg = pygame.image.load("res\\noteFailed.png")

EffectTrack1 = widget.EffectTrack()
EffectTrack2 = widget.EffectTrack()

dTrack, fTrack, jTrack, kTrack = analyse.json2Event("res\Sterelogue (4ky_another).mc")

Track1 = widget.Track(300, 500, 600)
for key in dTrack:
    if key["event"] == 1:
        Track1.noteList.append(widget.Note(400, float(key["time"])))

for key in fTrack:
    if key["event"] == 1:
        Track1.noteList.append(widget.Note(500, float(key["time"])))

pc = Track1.posCalculator
pc.AddEvent(0, 299, 600)
Track1.setup()

Track2 = widget.Track(300, 500, 600)
for key in jTrack:
    if key["event"] == 1:
        Track2.noteList.append(widget.Note(100, float(key["time"])))

for key in kTrack:
    if key["event"] == 1:
        Track2.noteList.append(widget.Note(200, float(key["time"])))
# Track2.noteList.append(widget.Note(150, 1.6))
# Track2.noteList.append(widget.Note(200, 2.4))
# Track2.noteList.append(widget.Note(200, 3.1))
# Track2.noteList.append(widget.Note(100, 3.5))
# Track2.noteList.append(widget.Note(150, 4))
# Track2.noteList.append(widget.Note(100, 5.5))
# Track2.noteList.append(widget.Note(150, 6.2))
# Track2.noteList.append(widget.Note(150, 6.7))
# Track2.noteList.append(widget.Note(200, 7))
# Track2.noteList.append(widget.Note(250, 8.5))
# Track2.noteList.append(widget.Note(250, 9.5))
# Track2.noteList.append(widget.Note(250, 10))
# Track2.noteList.append(widget.Note(200, 11.5))
# Track2.noteList.append(widget.Note(150, 11))
# Track2.noteList.append(widget.Note(100, 12.5))
# Track2.noteList.append(widget.Note(100, 12))
# Track2.noteList.append(widget.Note(200, 13.5))
# Track2.noteList.append(widget.Note(250, 14))
pc = Track2.posCalculator
pc.AddEvent(0, 299, 600)
Track2.setup()

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
        if event.type == pygame.KEYDOWN:
            if event.unicode.upper() in "SDF":
                EffectTrack1.AddHit(Track1.getPositionByBeat(beat) % 800)
            elif event.unicode.upper() in "JKL":
                EffectTrack2.AddHit(800 - Track2.getPositionByBeat(beat) % 800)
    if beat >= 300:
        continue
    screen.fill((0, 0, 0))
    surface.fill((0, 0, 0, 255))
    surface.blit(background, (0, 0))
    pygame.draw.line(surface, (255, 0, 0), (Track1.getPositionByBeat(beat) % 800, 300),
                     (Track1.getPositionByBeat(beat) % 800, 600))
    pygame.draw.line(surface, (255, 0, 0), (800 - Track2.getPositionByBeat(beat) % 800, 300),
                     (800 - Track2.getPositionByBeat(beat) % 800, 0))

    index = 0
    W = widget.EffectTrack.W

    for bar in EffectTrack1.getBars():
        pygame.draw.lines(surface, (255, 255, 255, 155), True, [(index * W, 300), (index * W + W, 300),
                                                                (index * W + W, 300 + bar), (index * W, 300 + bar)])
        index += 1

    index = 0
    for bar in EffectTrack2.getBars():
        pygame.draw.lines(surface, (255, 255, 255, 155), True, [(index * W, 300), (index * W + W, 300),
                                                                (index * W + W, 300 - bar), (index * W, 300 - bar)])
        index += 1

    for note in Track1.noteList:
        #
        if note.showBeat <= beat and note.hitBeat >= beat:
            pos = Track1.getPositionByBeat(note.hitBeat) % 800
            alpha = 255 - 255 * (note.hitBeat - beat) / (note.hitBeat - note.showBeat)
            if alpha > 255:
                alpha = 255
            noteImg.set_alpha(alpha)
            surface.blit(noteImg, (pos - 40, note.y - 40))
            # pygame.draw.circle(surface, (255, 255, 255, alpha), (pos, note.y), 30)
            # pygame.draw.circle(surface, (100, 100, 100, 255-alpha), (pos, note.y), 8)

    while Track1.noteList and Track1.noteList[0].hitBeat < beat:
        EffectTrack1.AddHit(Track1.getPositionByBeat(Track1.noteList[0].hitBeat) % 800)
        Track1.noteList.pop(0)

    for note in Track2.noteList:
        # print(note.showBeat, beat, note.hitBeat)
        if note.showBeat <= beat and note.hitBeat >= beat:
            pos = Track2.getPositionByBeat(note.hitBeat) % 800
            alpha = 255 - 255 * (note.hitBeat - beat) / (note.hitBeat - note.showBeat)
            if alpha > 255:
                alpha = 255
            noteImg.set_alpha(alpha)
            surface.blit(noteImg, (800 - pos - 40, note.y - 40))
            # pygame.draw.circle(surface, (255, 255, 255, alpha), (800 - pos, note.y), 30)
            # pygame.draw.circle(surface, (100, 100, 100, 255-alpha), (800 - pos, note.y), 8)
    # print(beat, Track2.noteList[:10])
    while Track2.noteList and Track2.noteList[0].hitBeat < beat:
        EffectTrack2.AddHit(800 - Track2.getPositionByBeat(Track2.noteList[0].hitBeat) % 800)
        Track2.noteList.pop(0)
    # print(Track2.noteList)
    screen.blit(surface, (0, 0))
    pygame.display.flip()
