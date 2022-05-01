import base
import pygame
import widget
import sys
import math
import time


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Codory Test 04")
surface = pygame.Surface((800, 600), pygame.SRCALPHA)

background = pygame.image.load("SIGMA.png").convert()
background.set_alpha(100)


EffectTrack1 = widget.EffectTrack()
EffectTrack2 = widget.EffectTrack()

Track1 = widget.Track(30, 500, 200)
Track1.noteList.append(widget.Note(450, 1))
Track1.noteList.append(widget.Note(500, 2))
Track1.noteList.append(widget.Note(500, 3))
Track1.noteList.append(widget.Note(400, 3))
Track1.noteList.append(widget.Note(450, 4))
Track1.noteList.append(widget.Note(400, 5))
Track1.noteList.append(widget.Note(450, 6))
Track1.noteList.append(widget.Note(350, 6))
Track1.noteList.append(widget.Note(400, 7))
Track1.noteList.append(widget.Note(400, 8))
Track1.noteList.append(widget.Note(350, 9))
Track1.noteList.append(widget.Note(350, 10))
Track1.noteList.append(widget.Note(400, 11))
Track1.noteList.append(widget.Note(450, 11))
Track1.noteList.append(widget.Note(450, 12))
Track1.noteList.append(widget.Note(350, 12))
Track1.noteList.append(widget.Note(500, 13))
Track1.noteList.append(widget.Note(450, 14))

pc = Track1.posCalculator
pc.AddEvent(0, 2, 300)
pc.AddEvent(2, 5, 100)
pc.AddEvent(28, 10, 400)
Track1.setup()

Track2 = widget.Track(30, 500, 300)
Track2.noteList.append(widget.Note(150, 1.6))
Track2.noteList.append(widget.Note(200, 2.4))
Track2.noteList.append(widget.Note(200, 3.1))
Track2.noteList.append(widget.Note(100, 3.5))
Track2.noteList.append(widget.Note(150, 4))
Track2.noteList.append(widget.Note(100, 5.5))
Track2.noteList.append(widget.Note(150, 6.2))
Track2.noteList.append(widget.Note(150, 6.7))
Track2.noteList.append(widget.Note(200, 7))
Track2.noteList.append(widget.Note(250, 8.5))
Track2.noteList.append(widget.Note(250, 9.5))
Track2.noteList.append(widget.Note(250, 10))
Track2.noteList.append(widget.Note(200, 11.5))
Track2.noteList.append(widget.Note(150, 11))
Track2.noteList.append(widget.Note(100, 12.5))
Track2.noteList.append(widget.Note(100, 12))
Track2.noteList.append(widget.Note(200, 13.5))
Track2.noteList.append(widget.Note(250, 14))
pc = Track2.posCalculator
pc.AddEvent(0, 3, 300)
pc.AddEvent(2, 6, 100)
pc.AddEvent(6, 9, 600)
pc.AddEvent(14, 12, 200)
Track2.setup()

startTime = time.time()
clock = pygame.time.Clock()
while True:
    clock.tick(120)
    beat = (time.time() - startTime) * 100 / 60
    # print(beat)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if event.type == pygame.KEYDOWN:
            if event.unicode.upper() in "SDF":
                EffectTrack1.AddHit(Track1.getPositionByBeat(beat)%800)
            elif event.unicode.upper() in "JKL":
                EffectTrack2.AddHit(800- Track2.getPositionByBeat(beat) % 800)
    if beat >= 30:
        continue
    screen.fill((0, 0, 0))
    surface.fill((0, 0, 0, 255))
    surface.blit(background, (0, 0))
    pygame.draw.line(surface, (255, 0, 0), (Track1.getPositionByBeat(beat)%800, 300), (Track1.getPositionByBeat(beat)%800, 600))
    pygame.draw.line(surface, (255, 0, 0), (800-Track2.getPositionByBeat(beat)%800, 300), (800-Track2.getPositionByBeat(beat)%800, 0))

    index = 0
    W = widget.EffectTrack.W

    for bar in EffectTrack1.getBars():
        pygame.draw.lines(surface, (255, 255, 255, 155), True, [(index*W, 300), (index*W+W, 300),
                                                       (index*W+W, 300+bar), (index*W, 300+bar)])
        index += 1

    index = 0
    for bar in EffectTrack2.getBars():
        pygame.draw.lines(surface, (255, 255, 255, 155), True, [(index*W, 300), (index*W+W, 300),
                                                       (index*W+W, 300-bar), (index*W, 300-bar)])
        index += 1

    for note in Track1.noteList:
        #
        if note.showBeat <= beat and note.hitBeat >= beat:
            pos = Track1.getPositionByBeat(note.hitBeat) % 800
            alpha = 255 - 255 * (note.hitBeat - beat) / (note.hitBeat - note.showBeat)
            if alpha > 255:
                alpha = 255
            pygame.draw.circle(surface, (255, 255, 255, alpha), (pos, note.y), 20)
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
            pygame.draw.circle(surface, (255, 255, 255, alpha), (800 - pos, note.y), 20)
    while Track2.noteList and Track2.noteList[0].hitBeat < beat:
        EffectTrack2.AddHit(800 - Track2.getPositionByBeat(Track2.noteList[0].hitBeat) % 800)
        Track2.noteList.pop(0)
    screen.blit(surface, (0, 0))
    pygame.display.flip()

