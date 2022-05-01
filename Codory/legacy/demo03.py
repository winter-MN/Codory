import numpy as np
import math
import matplotlib.pyplot as plt


T = [i/1000 for i in range(1, 1001)]
b = []
for t in T:
    if t < 0.2:
        b.append((-25*t*t+10*t))
    else:
        b.append(math.cos(math.pi*5/8*t-math.pi/8))

plt.plot(T, b)
plt.show()