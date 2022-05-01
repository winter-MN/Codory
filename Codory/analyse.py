import json
import beat2time
from decimal import Decimal


ENCODING = "utf-8"


def json2Event(path):
    col2EventDict = {}
    C0EventDict = []
    C1EventDict = []
    C2EventDict = []
    C3EventDict = []
    C4EventDict = []
    C5EventDict = []

    with open(path, 'r', encoding=ENCODING) as f:
        beatmap = json.load(f)

    title = beatmap['meta']['song']['title']
    # BPM = beatmap['time'][0]['bpm']
    notes = beatmap['note'][:-1]
    if 'offset' in beatmap['note'][-1]:
        offset = beatmap['note'][-1]['offset']
    else:
        offset = 0

    beat2time.load(beatmap['time'])

    print('Analysing %s...' % title)

    for note in notes:
        beat = note['beat']
        column = note['column']
        # time = (60 / BPM) * beat[0] + (beat[1] / beat[2]) * (60 / BPM) - offset / 1000
        time = beat2time.b2t(beat[0] + (beat[1] / beat[2])) - Decimal(str(offset)) / 1000
        if 'endbeat' in note:
            endBeat = note['endbeat']
            # endTime = (60 / BPM) * endBeat[0] + (endBeat[1] / endBeat[2]) * (60 / BPM) - offset / 1000
            endTime = beat2time.b2t(endBeat[0] + (endBeat[1] / endBeat[2])) - Decimal(str(offset)) / 1000
            d_ = col2EventDict.get(column, [])
            d_.append({'time': time, 'event': 2, 'endTime': endTime})
            col2EventDict[column] = d_
            # if column == 0:
            #     C0EventDict.append()
            # elif column == 1:
            #     C1EventDict.append({'time': time, 'event': 2, 'endTime': endTime})
            # elif column == 2:
            #     C2EventDict.append({'time': time, 'event': 2, 'endTime': endTime})
            # else:
            #     C3EventDict.append({'time': time, 'event': 2, 'endTime': endTime})
        else:
            d_ = col2EventDict.get(column, [])
            d_.append({'time': time, 'event': 1})
            col2EventDict[column] = d_
            # if column == 0:
            #     C0EventDict.append({'time': time, 'event': 1})
            # elif column == 1:
            #     C1EventDict.append({'time': time, 'event': 1})
            # elif column == 2:
            #     C2EventDict.append({'time': time, 'event': 1})
            # else:
            #     C3EventDict.append({'time': time, 'event': 1})

    print(tuple(col2EventDict.values()))
    return tuple(col2EventDict.values())


if __name__ == '__main__':
    print(json2Event('beatmap.json'))