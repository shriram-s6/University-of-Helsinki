#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def center(a):
    return tuple((x/2 - 0.5 for x in a.shape[0: 2]))   # note the order: (center_y, center_x)

def radial_distance(a):
    height, width = a.shape[0: 2]
    center = tuple((x/2 - 0.5 for x in a.shape[0: 2]))
    distance_arr = np.zeros((height, width))

    for index, val in np.ndenumerate(distance_arr):
        distance_arr[index] = np.linalg.norm(np.array(index) - np.array(center))
    return distance_arr

def scale(a, tmin=0.0, tmax=1.0):
    """Returns a copy of array 'a' with its values scaled to be in the range
[tmin,tmax]."""
    return (np.interp(a, (a.min(), a.max()), (tmin, tmax)))

def radial_mask(a):
    return scale(1 - radial_distance(a))

def radial_fade(a):
    height, width = a.shape[0: 2]
    mask = radial_mask(a).reshape(height, width, 1)
    fade = a * mask
    return fade

def main():
    img = plt.imread('src/painting.png')
    fig, ax = plt.subplots(3, 1)
    ax[0].imshow(img)
    ax[1].imshow(radial_mask(img))
    ax[2].imshow(radial_fade(img))
    plt.show()

if __name__ == "__main__":
    main()
