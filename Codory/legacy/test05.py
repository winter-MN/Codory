import piecewise as pw
import matplotlib.pyplot as plt
from scipy.integrate import quad
import sys


x = [i / 100 for i in range(-100, 20001)]
stopBeat = 200
pc = pw.PosCalculator(stopBeat)
pc.AddEvent(0, 0, 30)
pc.AddEvent(0, 40, 40)
pc.AddEvent(1, 90, 120)
pc.AddEvent(2, 150, 200)
pc.AddEvent(28, 170, 20)

pc.Translate()

print('')
print(pc.GetPos(150.0))
print(pc.functionList)
acc = 500       # 一beat被分为acc份

d = 1 / acc
y_= []
y = []
x_ = []
for i in range(0, stopBeat*acc+1):
    X = round(i * d, 4)
    sys.stdout.write(f"\r{X.__round__()} / {stopBeat}")
    y_ .append(pc.GetPos(X))
    y.append(pc._GetPos(X))
    x_.append(X)

# print(quad(pc.GetPos, 50, 200)[0])
# print('')
# print(total)
# print(quad(pc._GetPos, 0, 150)[0])
# y = [pc.GetPos(i) for i in x]
#
plt.grid(True)
# plt.plot(x_, y_)
plt.plot(x_, y)
plt.show()
