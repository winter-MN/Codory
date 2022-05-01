from decimal import Decimal

time = []
k = [0]


def load(time_):
    global time, k
    time = time_
    k = [Decimal(str(0))]
    # 一次函数的常值
    index = 1
    # for i in range(len(time[1:])):
    #     nowBeat = time[index]['beat'][0] + time[index]['beat'][1] / time[index]['beat'][2]
    #     lastBeat = time[index - 1]['beat'][0] + time[index - 1]['beat'][1] / time[index - 1]['beat'][2]
    #     k.append((nowBeat - lastBeat) / time[index - 1]['bpm'] * 60 + k[index - 1])
    #     # print((nowBeat - lastBeat) / time[index-1]['bpm']*60)
    #     index += 1

    for i in range(len(time[1:])):
        nowBeat = Decimal(str(time[index]['beat'][0])) + \
                  Decimal(str(time[index]['beat'][1])) / Decimal(str(time[index]['beat'][2]))
        lastBeat = Decimal(str(time[index - 1]['beat'][0])) + \
                   Decimal(str(time[index - 1]['beat'][1])) / Decimal(str(time[index - 1]['beat'][2]))
        k.append((nowBeat - lastBeat) / Decimal(str(time[index - 1]['bpm'])) * 60 + k[index - 1])
        # print((nowBeat - lastBeat) / time[index-1]['bpm']*60)
        index += 1
    # print('b2t function coef list:', k)


def b2t(beat):
    index = 1
    nowBeat = 0
    lastBeat = 0
    for _ in range(len(time[1:])):
        nowBeat = Decimal(str(time[index]['beat'][0])) + \
                  Decimal(str(time[index]['beat'][1])) / Decimal(str(time[index]['beat'][2]))
        lastBeat = Decimal(str(time[index - 1]['beat'][0])) + \
                   Decimal(str(time[index - 1]['beat'][1])) / Decimal(str(time[index - 1]['beat'][2]))

        if lastBeat <= beat < nowBeat:
            break
        index += 1
    if index == len(time):
        return k[index - 1] + (Decimal(str(beat)) - nowBeat) / Decimal(str(time[index - 1]['bpm'])) * 60
    else:
        return k[index - 1] + (Decimal(str(beat)) - lastBeat) / Decimal(str(time[index - 1]['bpm'])) * 60


if __name__ == '__main__':
    # load([
    #     {
    #         "beat": [0, 0, 1],
    #         "bpm": 180.0
    #     },
    #     {
    #         "beat": [189, 0, 4],
    #         "bpm": 90.0
    #     },
    #     {
    #         "beat": [190, 2, 4],
    #         "bpm": 180.0
    #     },
    #     {
    #         "beat": [222, 2, 4],
    #         "bpm": 90.0
    #     },
    #     {
    #         "beat": [223, 0, 4],
    #         "bpm": 180.0
    #     },
    #     {
    #         "beat": [284, 5, 8],
    #         "bpm": 90.0
    #     },
    #     {
    #         "beat": [284, 6, 8],
    #         "bpm": 180.0
    #     },
    #     {
    #         "beat": [285, 0, 8],
    #         "bpm": 90.0
    #     },
    #     {
    #         "beat": [285, 1, 8],
    #         "bpm": 180.0
    #     },
    #     {
    #         "beat": [285, 3, 8],
    #         "bpm": 90.0
    #     },
    #     {
    #         "beat": [285, 4, 8],
    #         "bpm": 180.0
    #     },
    #     {
    #         "beat": [285, 6, 8],
    #         "bpm": 90.0
    #     },
    #     {
    #         "beat": [285, 7, 8],
    #         "bpm": 180.0
    #     },
    #     {
    #         "beat": [286, 1, 8],
    #         "bpm": 90.0
    #     },
    #     {
    #         "beat": [286, 2, 8],
    #         "bpm": 180.0
    #     },
    #     {
    #         "beat": [378, 3, 8],
    #         "bpm": 90.0
    #     },
    #     {
    #         "beat": [378, 5, 8],
    #         "bpm": 180.0
    #     },
    #     {
    #         "beat": [378, 7, 8],
    #         "bpm": 90.0
    #     },
    #     {
    #         "beat": [379, 1, 8],
    #         "bpm": 180.0
    #     },
    #     {
    #         "beat": [379, 3, 8],
    #         "bpm": 90.0
    #     },
    #     {
    #         "beat": [379, 4, 8],
    #         "bpm": 180.0
    #     },
    #     {
    #         "beat": [379, 6, 8],
    #         "bpm": 90.0
    #     },
    #     {
    #         "beat": [380, 0, 8],
    #         "bpm": 180.0
    #     },
    #     {
    #         "beat": [380, 2, 8],
    #         "bpm": 90.0
    #     },
    #     {
    #         "beat": [380, 4, 8],
    #         "bpm": 180.0
    #     }
    # ])
    load(
        [
            {
                "beat": [0, 0, 1],
                "bpm": 60.0
            },
            {
                "beat": [60, 0, 1],
                "bpm": 30
            },
            {
                "beat": [90, 0, 1],
                "bpm": 60
            },
        ]
    )
    print(b2t(5))
    print(b2t(61))
