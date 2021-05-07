import math
import random
from matplotlib import pyplot as plt

def circleDraw(N, p):
    angleList = [2 * math.pi / N * i for i in range(N)]
    xList = list(map(math.cos, angleList))
    yList = list(map(math.sin, angleList))
    plt.scatter(xList, yList, s=0.05, c='black')

    for i in range(N):
        for j in range(N):
            if i!= j:
                if random.random() < p:
                    plt.plot([xList[i], xList[j]], [yList[i], yList[j]], c='b')
    plt.show()

if __name__ == '__main__':
    circleDraw(1000, 0.0002)