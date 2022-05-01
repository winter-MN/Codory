import base
import pygame
import pygame.gfxdraw
import sys
import math
import time


pygame.init()
screen = pygame.display.set_mode((800, 600), )
surface = pygame.Surface((800, 600), pygame.SRCALPHA)


base.Track1.noteList = [base.Note(5, 0), base.Note(6, 0), base.Note(7, 0), base.Note(8, 0),
                                           base.Note(9, 0), base.Note(10, 0), base.Note(11, 0)]

base.Track1.speedConfig = [base.SpeedInstantConfig(0, 80), base.SpeedInstantConfig(2, 160),
                                              base.SpeedInstantConfig(3, 80), base.SpeedInstantConfig(4, 160)]


def DrawNote(centerX, centerY, a, angle, alpha):
    """
    绘制正方形音符
    :param centerX: 对角线交点x坐标
    :param centerY:
    :param a: 边长
    :param angle: 图形绕中心旋转角
    :param alpha: 透明度
    :return:
    """
    angle += 45
    pygame.draw.lines(surface, (255, 255, 255, alpha), True, [
        (centerX + a / 2 * math.cos(math.radians(angle)), centerY - a / 2 * math.sin(math.radians(angle))),
        (centerX + a / 2 * math.cos(math.radians(angle+90)), centerY - a / 2 * math.sin(math.radians(angle+90))),
        (centerX + a / 2 * math.cos(math.radians(angle+180)), centerY - a / 2 * math.sin(math.radians(angle+180))),
        (centerX + a / 2 * math.cos(math.radians(angle+270)), centerY - a / 2 * math.sin(math.radians(angle+270)))
    ], 3
                             )



startTime = time.time()
while True:
    beat = time.time() - startTime
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
    # screen.fill((0, 0, 0))
    surface.fill((0, 0, 0, 255))
    notePositionList = base.Track1.getNotePositionByBeat(0)
    for notePosition in notePositionList:
        print(notePosition)
        x = notePosition % base.SCREENWIDTH
        y = 450
        DrawNote(x, y, 40, 0, base.Track1.alpha)
    screen.blit(surface, (0, 0))
    pygame.display.flip()

