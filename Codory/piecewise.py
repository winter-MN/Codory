import easingFunc
import hashlib
import sys
import os


class PosCalculator:
    # 根据速度计算出每beat的位置
    def __init__(self, stopBeat, acc=500, initSpeed=0):
        self.acc = acc
        self.eventList = []
        self.functionList = []
        # 设置起始速度
        self.AddEvent(0, 0, initSpeed)

        # 停止时间
        self.stopBeat = stopBeat
        self.AddEvent(stopBeat, stopBeat, 0)

        self.cacheName = "PosCache{}.txt"
        self.beat2posDict = {}

    def AddEvent(self, mode, startBeat, target):
        self.eventList.append((mode, startBeat, target))

    def Translate(self):
        # 将eventList中的事件按照startBeat排序
        self.eventList.sort(key=lambda x: x[1])

        # 将eventList中的事件转换至functionList
        index = 0
        event = self.eventList[0]
        self.functionList.append(easingFunc.code2FuncDict[event[0]](0, self.eventList[index+1][1], event[2], event[2]))
        index += 1
        # print("eventList:", self.eventList)
        for event in self.eventList[1:-1]:
            self.functionList.append(easingFunc.code2FuncDict[event[0]](event[1], self.eventList[index+1][1],
                                                                        self.eventList[index-1][2], event[2]))
            index += 1

        # 检验本地缓存是否有效
        cacheHash = hashlib.md5(str(self.eventList).encode('utf-8')).hexdigest()
        print(cacheHash)
        # 若有效，则直接读取
        if os.path.exists(self.cacheName.format(cacheHash)):
            with open(self.cacheName.format(cacheHash), 'r') as f:
                self.beat2posDict = {}
                for line in f.readlines():
                    line = line.strip()
                    beat, pos = line.split(',')
                    self.beat2posDict[float(beat)] = float(pos)
            return

        # 求出各beat时的位置
        acc = float(self.acc)  # 一beat被分为acc份
        d = 1 / float(acc)
        total = float(0)
        # 生成一个beat到位置的映射, 并保存缓存至本地
        with open(self.cacheName.format(cacheHash), "w") as f:
            f.write(f"0,0\n")
            self.beat2posDict[0] = float(0)
            for i in range(1, self.stopBeat * self.acc + 1):
                X = i * d
                # sys.stdout.write(f"\rTranslate {X.__round__()} / {self.stopBeat} ")
                total += (float(self._GetPos(X-d/2)) + float(self._GetPos(X + d/2))) * d / 2
                f.write(f"{round(float(X), 4)},{float(total)}\n")
                self.beat2posDict[round(float(X), 4)] = float(total)

    def _GetPos(self, beat, delete=False):
        # 若delete == True, 删去过时的function
        # print(self.functionList[0].endBeat, beat)
        while self.functionList[0].endBeat < beat and delete:
            self.functionList.pop(0)
        # print(beat)
        # print(self.functionList)
        if beat <= 0:
            return 0
        if beat >= self.stopBeat:
            return self.functionList[-1].target
        for func in self.functionList:
            if func.startBeat <= beat <= func.endBeat:
                if not func.liner:
                    beat = float(beat)
                return func.Calculate(beat)

    def GetPos(self, beat):
        return self.beat2posDict[round(beat*self.acc // 1 * (1/self.acc), 4)]





