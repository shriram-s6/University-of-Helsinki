#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def to_grayscale(img):
    multipliers = [0.2126, 0.7152, 0.0722]
    grey_scaled = np.sum(multipliers * img, axis=2)
    return grey_scaled

def to_red(img):
    multipliers = [1, 0, 0]
    return img * multipliers

def to_green(img):
    multipliers = [0, 1, 0]
    return img * multipliers

def to_blue(img):
    multipliers = [0, 0, 1]
    return img * multipliers

def main():
    paint = plt.imread('src/painting.png')
    fig, ax = plt.subplots(3, 1)
    ax[0].imshow(to_red(paint))
    ax[1].imshow(to_green(paint))
    ax[2].imshow(to_blue(paint))
    plt.show()

    grey_scaled = to_grayscale(paint)
    plt.imshow(grey_scaled)
    plt.gray()
    plt.show()

if __name__ == "__main__":
    main()
