import base
from base import SpeedInstantConfig, Note
import pygame
import sys
import time


pygame.init()

screen = pygame.display.set_mode((base.SCREENWIDTH, base.SCREENHEIGHT))

# 创建一条Track
node = base.Node(500, 200)
t = base.Track(node, 1)

t.speedConfig = [SpeedInstantConfig(0, 40), SpeedInstantConfig(2, 80), SpeedInstantConfig(3, 40), SpeedInstantConfig(4, 80)]
t.noteList = [Note(5, 0), Note(6, 0), Note(7, 0), Note(8, 0), Note(9, 0), Note(10, 0), Note(11, 0)]

start = time.time()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
    screen.fill((0, 0, 0))

    pygame.draw.circle(screen, (255, 0, 0), (int(node.x), int(node.y)), 5)
    T = time.time()-start
    deltaList = t.getNotePositionByBeat(T)
    for delta in deltaList:
        pygame.draw.circle(screen, (255, 255, 255), (500, 200+delta), 10)
    pygame.draw.line(screen, (255, 0, 0), (0, 200+0), (1000, 200+0))
    pygame.draw.line(screen, (255, 0, 0), (0, 200+80), (1000, 200+80))
    pygame.draw.line(screen, (255, 0, 0), (0, 200+120), (1000, 200+120))
    pygame.draw.line(screen, (255, 0, 0), (0, 200+200), (1000, 200+200))
    pygame.draw.line(screen, (255, 0, 0), (0, 200+240), (1000, 200+240))
    pygame.draw.line(screen, (255, 0, 0), (0, 200+280), (1000, 200+280))
    pygame.display.flip()

