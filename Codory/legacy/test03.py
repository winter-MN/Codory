import base


base.Track1.noteList = [base.Note(5, 0), base.Note(6, 0), base.Note(7, 0), base.Note(8, 0),
                                           base.Note(9, 0), base.Note(10, 0), base.Note(11, 0)]

base.Track1.speedConfig = [base.SpeedInstantConfig(0, 80), base.SpeedInstantConfig(2, 160),
                                              base.SpeedInstantConfig(3, 80), base.SpeedInstantConfig(4, 160)]

print(base.Track1.getNotePositionByBeat(0))