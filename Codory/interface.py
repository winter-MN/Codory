from easingFunc import code2FuncDict


class IChangeableAlpha:
    def __init__(self):
        self.eventList = []
        self.easingFuncList = []

    def AddEvent(self, startBeat, endBeat, target, mode):
        self.eventList.append([startBeat, endBeat, target, code2FuncDict[mode]])

    def Translate(self):
        # 运行前需执行本方法，将self.eventList 翻译为self.easingFuncList
        idx = 0
        for event in self.eventList:
            if len(self.easingFuncList) == 0:
                # 添加第一个缓动函数，将alpha设为255
                # .__init__(self, startBeat, endBeat, origin, target)
                self.easingFuncList.append(event[3](event[0], event[1], 255, event[2]))
            else:
                self.easingFuncList.append(event[3](event[0], event[1], self.eventList[idx-1][2], event[2]))
            idx += 1

    def getAlpha(self, beat):
        # 先删去过时缓动函数对象
        outOfDateEasingFuncList = []
        for easingFunc in self.easingFuncList:
            if easingFunc.startBeat < beat:
                outOfDateEasingFuncList.append(easingFunc)
            elif easingFunc.startBeat > beat:
                break

        for easingFunc in outOfDateEasingFuncList:
            self.easingFuncList.remove(easingFunc)

        # 删去了所有过时的缓动函数对象，则self.easingFuncList[0]就是所需的缓动函数对象
        return self.easingFuncList[0].Calculate(beat)


class IChangeableLength:
    def __init__(self):
        self.eventList = []
        self.easingFuncList = []

    def AddEvent(self, startBeat, endBeat, target, mode):
        self.eventList.append([startBeat, endBeat, target, code2FuncDict[mode]])

    def Translate(self):
        # 运行前需执行本方法，将self.eventList 翻译为self.easingFuncList
        idx = 0
        for event in self.eventList:
            if len(self.easingFuncList) == 0:
                # 添加第一个缓动函数，将length设为0
                # .__init__(self, startBeat, endBeat, origin, target)
                self.easingFuncList.append(event[3](event[0], event[1], 0, event[2]))
            else:
                self.easingFuncList.append(event[3](event[0], event[1], self.eventList[idx-1][2], event[2]))
            idx += 1

    def getLength(self, beat):
        # 先删去过时缓动函数对象
        outOfDateEasingFuncList = []
        for easingFunc in self.easingFuncList:
            if easingFunc.startBeat < beat:
                outOfDateEasingFuncList.append(easingFunc)
            elif easingFunc.startBeat > beat:
                break

        for easingFunc in outOfDateEasingFuncList:
            self.easingFuncList.remove(easingFunc)

        # 删去了所有过时的缓动函数对象，则self.easingFuncList[0]就是所需的缓动函数对象
        return self.easingFuncList[0].Calculate(beat)


class IChangeableAngle:
    def __init__(self):
        self.eventList = []
        self.easingFuncList = []

    def AddEvent(self, startBeat, endBeat, target, mode):
        self.eventList.append([startBeat, endBeat, target, code2FuncDict[mode]])

    def Translate(self):
        # 运行前需执行本方法，将self.eventList 翻译为self.easingFuncList
        idx = 0
        for event in self.eventList:
            if len(self.easingFuncList) == 0:
                # 添加第一个缓动函数，将angle设为0
                # .__init__(self, startBeat, endBeat, origin, target)
                self.easingFuncList.append(event[3](event[0], event[1], 0, event[2]))
            else:
                self.easingFuncList.append(event[3](event[0], event[1], self.eventList[idx-1][2], event[2]))
            idx += 1

    def getAngle(self, beat):
        # 先删去过时缓动函数对象
        outOfDateEasingFuncList = []
        for easingFunc in self.easingFuncList:
            if easingFunc.startBeat < beat:
                outOfDateEasingFuncList.append(easingFunc)
            elif easingFunc.startBeat > beat:
                break

        for easingFunc in outOfDateEasingFuncList:
            self.easingFuncList.remove(easingFunc)

        # 删去了所有过时的缓动函数对象，则self.easingFuncList[0]就是所需的缓动函数对象
        return self.easingFuncList[0].Calculate(beat)
