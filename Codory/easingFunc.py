"""
30种曲线缓动函数
more detail about easing function at https://easings.net/en
"""
import math


class Func:
    """
    缓动函数的超类
    """

    def __init__(self, startBeat, endBeat, origin, target):
        """
        :param startBeat: 缓动开始的时刻
        :param endBeat: 缓动结束的时刻
        :param origin: 缓动前原始值
        :param target: 完成缓动后目标值
        :return:
        """
        self.target = target
        self.origin = origin
        self.endBeat = endBeat
        self.startBeat = startBeat
        self.k = target - origin  # 纵向扩大函数的值域
        self.liner = False          # 代表这是非线性的缓动函数

    def Calculate(self, beat):
        """
        计算beat时刻 缓动项 的值
        :param beat: 当前时刻
        :return: double
        """

    def __repr__(self):
        return f"<Func / {self.startBeat}, {self.endBeat}, {self.origin}, {self.target}>"


class Liner(Func):
    def __init__(self, startBeat, endBeat, origin, target):
        super().__init__(startBeat, endBeat, origin, target)
        self.liner = True

    def Calculate(self, beat):
        if beat < self.endBeat:
            x = (beat - self.startBeat) / (self.endBeat - self.startBeat)
            # print(self.endBeat, self.startBeat, x)
            return x * self.k + self.origin
        else:
            return self.target


class EaseInSine(Func):
    def __init__(self, startBeat, endBeat, origin, target):
        super().__init__(startBeat, endBeat, origin, target)

    def Calculate(self, beat):
        if beat < self.endBeat:
            x = (beat - self.startBeat) / (self.endBeat - self.startBeat)
            # print(beat, self.startBeat, self.endBeat, self.origin)
            return (1 - math.cos((x * math.pi) / 2)) * self.k + self.origin
        else:
            return self.target


class EaseOutSine(Func):
    def __init__(self, startBeat, endBeat, origin, target):
        super().__init__(startBeat, endBeat, origin, target)

    def Calculate(self, beat):
        if beat < self.endBeat:
            x = (beat - self.startBeat) / (self.endBeat - self.startBeat)
            return math.sin((x * math.pi) / 2) * self.k + self.origin
        else:
            return self.target


class EaseInOutSine(Func):
    def __init__(self, startBeat, endBeat, origin, target):
        super().__init__(startBeat, endBeat, origin, target)

    def Calculate(self, beat):
        if beat < self.endBeat:
            x = (beat - self.startBeat) / (self.endBeat - self.startBeat)
            return -(math.cos(math.pi * x) - 1) / 2 * self.k + self.origin
        else:
            return self.target


class EaseInQuad(Func):
    def __init__(self, startBeat, endBeat, origin, target):
        super().__init__(startBeat, endBeat, origin, target)

    def Calculate(self, beat):
        if beat < self.endBeat:
            x = (beat - self.startBeat) / (self.endBeat - self.startBeat)
            return x * x * self.k + self.origin
        else:
            return self.target


class EaseOutQuad(Func):
    def __init__(self, startBeat, endBeat, origin, target):
        super().__init__(startBeat, endBeat, origin, target)

    def Calculate(self, beat):
        if beat < self.endBeat:
            x = (beat - self.startBeat) / (self.endBeat - self.startBeat)
            return (1 - (1 - x) * (1 - x)) * self.k + self.origin
        else:
            return self.target


class EaseInOutQuad(Func):
    def __init__(self, startBeat, endBeat, origin, target):
        super().__init__(startBeat, endBeat, origin, target)

    def Calculate(self, beat):
        if beat < self.endBeat:
            x = (beat - self.startBeat) / (self.endBeat - self.startBeat)
            return (2 * x * x if x < 0.5 else 1 - math.pow(-2 * x + 2, 2) / 2) * self.k + self.origin
        else:
            return self.target


class EaseInCubic(Func):
    def __init__(self, startBeat, endBeat, origin, target):
        super().__init__(startBeat, endBeat, origin, target)

    def Calculate(self, beat):
        if beat < self.endBeat:
            x = (beat - self.startBeat) / (self.endBeat - self.startBeat)
            return x * x * x * self.k + self.origin
        else:
            return self.target


class EaseOutCubic(Func):
    def __init__(self, startBeat, endBeat, origin, target):
        super().__init__(startBeat, endBeat, origin, target)

    def Calculate(self, beat):
        if beat < self.endBeat:
            x = (beat - self.startBeat) / (self.endBeat - self.startBeat)
            return (1 - math.pow(1 - x, 3)) * self.k + self.origin
        else:
            return self.target


class EaseInOutCubic(Func):
    def __init__(self, startBeat, endBeat, origin, target):
        super().__init__(startBeat, endBeat, origin, target)

    def Calculate(self, beat):
        if beat < self.endBeat:
            x = (beat - self.startBeat) / (self.endBeat - self.startBeat)
            return (4 * x * x * x if x < 0.5 else 1 - math.pow(-2 * x + 2, 3) / 2) * self.k + self.origin
        else:
            return self.target


class EaseInQuart(Func):
    def __init__(self, startBeat, endBeat, origin, target):
        super().__init__(startBeat, endBeat, origin, target)

    def Calculate(self, beat):
        if beat < self.endBeat:
            x = (beat - self.startBeat) / (self.endBeat - self.startBeat)
            return (x * x * x * x) * self.k + self.origin
        else:
            return self.target


class EaseOutQuart(Func):
    def __init__(self, startBeat, endBeat, origin, target):
        super().__init__(startBeat, endBeat, origin, target)

    def Calculate(self, beat):
        if beat < self.endBeat:
            x = (beat - self.startBeat) / (self.endBeat - self.startBeat)
            return (1 - math.pow(1 - x, 4)) * self.k + self.origin
        else:
            return self.target


class EaseInOutQuart(Func):
    def __init__(self, startBeat, endBeat, origin, target):
        super().__init__(startBeat, endBeat, origin, target)

    def Calculate(self, beat):
        if beat < self.endBeat:
            x = (beat - self.startBeat) / (self.endBeat - self.startBeat)
            return (8 * x * x * x * x if x < 0.5 else 1 - math.pow(-2 * x + 2, 4) / 2) * self.k + self.origin
        else:
            return self.target


class EaseInQuint(Func):
    def __init__(self, startBeat, endBeat, origin, target):
        super().__init__(startBeat, endBeat, origin, target)

    def Calculate(self, beat):
        if beat < self.endBeat:
            x = (beat - self.startBeat) / (self.endBeat - self.startBeat)
            return (x * x * x * x * x) * self.k + self.origin
        else:
            return self.target


class EaseOutQuint(Func):
    def __init__(self, startBeat, endBeat, origin, target):
        super().__init__(startBeat, endBeat, origin, target)

    def Calculate(self, beat):
        if beat < self.endBeat:
            x = (beat - self.startBeat) / (self.endBeat - self.startBeat)
            return (1 - math.pow(1 - x, 5)) * self.k + self.origin
        else:
            return self.target


class EaseInOutQuint(Func):
    def __init__(self, startBeat, endBeat, origin, target):
        super().__init__(startBeat, endBeat, origin, target)

    def Calculate(self, beat):
        if beat < self.endBeat:
            x = (beat - self.startBeat) / (self.endBeat - self.startBeat)
            return (16 * x * x * x * x * x if x < 0.5 else 1 - math.pow(-2 * x + 2, 5) / 2) * self.k + self.origin
        else:
            return self.target


class EaseInExpo(Func):
    def __init__(self, startBeat, endBeat, origin, target):
        super().__init__(startBeat, endBeat, origin, target)

    def Calculate(self, beat):
        if beat < self.endBeat:
            x = (beat - self.startBeat) / (self.endBeat - self.startBeat)
            return (0 if x == 0 else math.pow(2, 10 * x - 10)) * self.k + self.origin
        else:
            return self.target


class EaseOutExpo(Func):
    def __init__(self, startBeat, endBeat, origin, target):
        super().__init__(startBeat, endBeat, origin, target)

    def Calculate(self, beat):
        if beat < self.endBeat:
            x = (beat - self.startBeat) / (self.endBeat - self.startBeat)
            return (1 if x == 1 else 1 - math.pow(2, -10 * x)) * self.k + self.origin
        else:
            return self.target


class EaseInOutExpo(Func):
    def __init__(self, startBeat, endBeat, origin, target):
        super().__init__(startBeat, endBeat, origin, target)

    def Calculate(self, beat):
        if beat < self.endBeat:
            x = (beat - self.startBeat) / (self.endBeat - self.startBeat)
            return (0 if x == 0 else 1 if x == 1 else math.pow(2, 20 * x - 10) / 2 if x < 0.5 else \
                (2 - pow(2, -20 * x + 10)) / 2) * self.k + self.origin
        else:
            return self.target


class EaseInCirc(Func):
    def __init__(self, startBeat, endBeat, origin, target):
        super().__init__(startBeat, endBeat, origin, target)

    def Calculate(self, beat):
        if beat < self.endBeat:
            x = (beat - self.startBeat) / (self.endBeat - self.startBeat)
            return (1 - math.sqrt(1 - math.pow(x, 2))) * self.k + self.origin
        else:
            return self.target


class EaseOutCirc(Func):
    def __init__(self, startBeat, endBeat, origin, target):
        super().__init__(startBeat, endBeat, origin, target)

    def Calculate(self, beat):
        if beat < self.endBeat:
            x = (beat - self.startBeat) / (self.endBeat - self.startBeat)
            return (math.sqrt(1 - math.pow(x - 1, 2))) * self.k + self.origin
        else:
            return self.target


class EaseInOutCirc(Func):
    def __init__(self, startBeat, endBeat, origin, target):
        super().__init__(startBeat, endBeat, origin, target)

    def Calculate(self, beat):
        if beat < self.endBeat:
            x = (beat - self.startBeat) / (self.endBeat - self.startBeat)
            return ((1 - math.sqrt(1 - math.pow(2 * x, 2))) / 2 if x < 0.5 else (math.sqrt(
                1 - math.pow(-2 * x + 2, 2)) + 1) / 2) * self.k + self.origin
        else:
            return self.target


class EaseInBack(Func):
    c1 = 1.70158
    c3 = c1 + 1

    def __init__(self, startBeat, endBeat, origin, target):
        super().__init__(startBeat, endBeat, origin, target)

    def Calculate(self, beat):
        if beat < self.endBeat:
            x = (beat - self.startBeat) / (self.endBeat - self.startBeat)
            return (EaseInBack.c3 * x * x * x - EaseInBack.c1 * x * x) * self.k + self.origin
        else:
            return self.target


class EaseOutBack(Func):
    c1 = 1.70158
    c3 = c1 + 1

    def __init__(self, startBeat, endBeat, origin, target):
        super().__init__(startBeat, endBeat, origin, target)

    def Calculate(self, beat):
        if beat < self.endBeat:
            x = (beat - self.startBeat) / (self.endBeat - self.startBeat)
            return (1 + EaseOutBack.c3 * math.pow(x - 1, 3) + EaseOutBack.c1 * math.pow(x - 1,
                                                                                        2)) * self.k + self.origin
        else:
            return self.target


class EaseInOutBack(Func):
    c1 = 1.70158
    c2 = c1 * 1.525

    def __init__(self, startBeat, endBeat, origin, target):
        super().__init__(startBeat, endBeat, origin, target)

    def Calculate(self, beat):
        if beat < self.endBeat:
            x = (beat - self.startBeat) / (self.endBeat - self.startBeat)
            return ((math.pow(2 * x, 2) * ((EaseInOutBack.c2 + 1) * 2 * x - EaseInOutBack.c2)) / 2 if x < 0.5 \
                        else (math.pow(2 * x - 2, 2) * (
                    (EaseInOutBack.c2 + 1) * (x * 2 - 2) + EaseInOutBack.c2) + 2) / 2) * \
                   self.k + self.origin
        else:
            return self.target


class EaseInElastic(Func):
    c4 = (2 * math.pi) / 3

    def __init__(self, startBeat, endBeat, origin, target):
        super().__init__(startBeat, endBeat, origin, target)

    def Calculate(self, beat):
        if beat < self.endBeat:
            x = (beat - self.startBeat) / (self.endBeat - self.startBeat)
            # x == 0  ? 0  : x == 1  ? 1  : -math.pow(2, 10 * x - 10) * math.sin((x * 10 - 10.75) * c4)
            return (0 if x == 0 else 1 if x == 1 else \
                -math.pow(2, 10 * x - 10) * math.sin((x * 10 - 10.75) * EaseInElastic.c4)) * self.k + self.origin
        else:
            return self.target


class EaseOutElastic(Func):
    c4 = (2 * math.pi) / 3

    def __init__(self, startBeat, endBeat, origin, target):
        super().__init__(startBeat, endBeat, origin, target)

    def Calculate(self, beat):
        if beat < self.endBeat:
            x = (beat - self.startBeat) / (self.endBeat - self.startBeat)
            # x == 0  ? 0  : x == 1  ? 1  : math.pow(2, -10 * x) * math.sin((x * 10 - 0.75) * c4) + 1
            return (0 if x == 0 else 1 if x == 1 else math.pow(2, -10 * x) * math.sin(
                (x * 10 - 0.75) * EaseOutElastic.c4) + 1) * self.k + self.origin
        else:
            return self.target


class EaseInOutElastic(Func):
    c5 = (2 * math.pi) / 4.5

    def __init__(self, startBeat, endBeat, origin, target):
        super().__init__(startBeat, endBeat, origin, target)

    def Calculate(self, beat):
        if beat < self.endBeat:
            x = (beat - self.startBeat) / (self.endBeat - self.startBeat)
            return (0 if x == 0 else 1 if x == 1 else
            -(math.pow(2, 20 * x - 10) * math.sin((20 * x - 11.125) * EaseInOutElastic.c5)) / 2 if x < 0.5 else
            (math.pow(2, -20 * x + 10) * math.sin((20 * x - 11.125) * EaseInOutElastic.c5)) / 2 + 1) * \
                   self.k + self.origin
        else:
            return self.target


def _easeOutBounce(x):
    if x < 1 / EaseOutBounce.d1:
        return EaseOutBounce.n1 * x * x
    elif x < 2 / EaseOutBounce.d1:
        x -= 1.5 / EaseOutBounce.d1
        return EaseOutBounce.n1 * x * x + 0.75
    elif x < 2.5 / EaseOutBounce.d1:
        x -= 2.25 / EaseOutBounce.d1
        return EaseOutBounce.n1 * x * x + 0.9375
    else:
        x -= 2.625 / EaseOutBounce.d1
        return EaseOutBounce.n1 * x * x + 0.984375


class EaseInBounce(Func):
    def __init__(self, startBeat, endBeat, origin, target):
        super().__init__(startBeat, endBeat, origin, target)

    def Calculate(self, beat):
        if beat < self.endBeat:
            x = (beat - self.startBeat) / (self.endBeat - self.startBeat)
            return (1 - _easeOutBounce(1 - x)) * self.k + self.origin
        else:
            return self.target


class EaseOutBounce(Func):
    n1 = 7.5625
    d1 = 2.75

    def __init__(self, startBeat, endBeat, origin, target):
        super().__init__(startBeat, endBeat, origin, target)

    def Calculate(self, beat):
        if beat < self.endBeat:
            x = (beat - self.startBeat) / (self.endBeat - self.startBeat)
            return (_easeOutBounce(x)) * self.k + self.origin
        else:
            return self.target


class EaseInOutBounce(Func):
    def __init__(self, startBeat, endBeat, origin, target):
        super().__init__(startBeat, endBeat, origin, target)

    def Calculate(self, beat):
        if beat < self.endBeat:
            x = (beat - self.startBeat) / (self.endBeat - self.startBeat)
            return ((1 - _easeOutBounce(1 - 2 * x)) / 2 if x < 0.5 else (1 + _easeOutBounce(2 * x - 1)) / 2) * \
                   self.k + self.origin
        else:
            return self.target


code2FuncDict = {0: Liner,
                 1: EaseInSine, 2: EaseOutSine, 3: EaseInOutSine, 4: EaseInQuad,
                 5: EaseOutQuad, 6: EaseInOutQuad, 7: EaseInCubic, 8: EaseOutCubic, 9: EaseInOutCubic, 10: EaseInQuart,
                 11: EaseOutQuart, 12: EaseInOutQuart, 13: EaseInQuint, 14: EaseOutQuint, 15: EaseInOutQuint,
                 16: EaseInExpo, 17: EaseOutExpo, 18: EaseInOutExpo, 19: EaseInCirc, 20: EaseOutCirc,
                 21: EaseInOutCirc, 22: EaseInBack, 23: EaseOutBack, 24: EaseInOutBack, 25: EaseInElastic,
                 26: EaseOutElastic, 27: EaseInOutElastic, 28: EaseInBounce, 29: EaseOutBounce, 30: EaseInOutBounce, }
