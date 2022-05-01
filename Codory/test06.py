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


dTrack, fTrack, jTrack, kTrack = analyse.json2Event("res\Sterelogue (4ky_another).mc")

Track1 = base.Track(300, 500, 600)

pc = Track1.posCalculator
pc.AddEvent(0, 299, 600)
Track1.setup()

for key in dTrack:
    if key["event"] == 1:
        Track1.noteList.append(base.Note(float(key["time"]), float(key["time"])-0.5, float(key["time"])-1, Track1, 400))

print(list(Track1.GetNoteByTime(10)))

