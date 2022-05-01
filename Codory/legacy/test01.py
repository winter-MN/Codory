"""
测试缓动函数
"""
from matplotlib import pyplot as plt
import math

import easingFunc as ef


e = ef.Liner
e = e(0, 1, 0, 10)
xL = [i/100 for i in range(100)]
y = []
c5 = (2 * math.pi) / 4.5
for x in xL:
    y.append(e.Calculate(x))

plt.plot(xL, y)
# 显示图像
plt.show()


