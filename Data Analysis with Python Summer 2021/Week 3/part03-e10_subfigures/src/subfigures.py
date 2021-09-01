#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def subfigures(a):
    fig, ax = plt.subplots(1, 2)
    x1 = a[:, 0]
    y1 = a[:, 1]

    ax[0].plot(x1, y1)
    ax[1].scatter(x1, y1, c=a[:, 2], s=a[:, 3])

    plt.show()

def main():
    arr = np.array([[10, 10, 10, 10], [20, 20, 20, 20], [30, 30, 30, 30], [40, 40, 40, 40]])
    subfigures(arr)

if __name__ == "__main__":
    main()
