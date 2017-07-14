import math

import cv2
import matplotlib.pyplot as plt
import numpy as np


def hextorgb(hexstring):
    r = int(hexstring[0:2], 16)
    g = int(hexstring[2:4], 16)
    b = int(hexstring[4:6], 16)
    return (r, g, b)


MAX_DEPTH = 15
SIGMA_ANGLE = 0.1


def length_scaling(depth):
    return math.exp(-depth/5)


def recursive_branch(image, init_length, depth, angle, start_point):
    # cv2.line(image, (0,0), (50,50), (233,233,233), 5)
    if False:
        # if (depth > MAX_DEPTH):
        return
    else:

        length = init_length * length_scaling(depth)
        length = np.random.normal(length, length/3/3)

        end_x = start_point[0] + length * math.cos(angle)
        end_y = start_point[1] - length * math.sin(angle)
        end_point = (int(end_x), int(end_y))

        # start_indx = int((depth -1)/MAX_DEPTH * len(zen_points))
        # end_indx = int(depth/MAX_DEPTH * len(zen_points))
        start_indx = int(((depth - 1) / MAX_DEPTH) ** 1 * len(zen_points))

        end_indx = int((depth / MAX_DEPTH) ** 1 * len(zen_points))

        clr = zen_points[min(np.random.randint(start_indx, end_indx),
                         len(zen_points)-1)]
        clr1, clr2, clr3 = clr.astype(np.int32)
        cv2.line(image, start_point, end_point,
                 (int(clr1), int(clr2), int(clr3)), 2, cv2.LINE_AA)

        # angle1, angle2 = (math.pi/5, math.pi/5)
        angle1, angle2 = np.random.normal(math.pi /
                                          (6 + 0.6 * depth), SIGMA_ANGLE, 2)
        angle1 = angle - abs(angle1)
        angle2 = angle + abs(angle2)

        if np.random.rand() > 0.7 * min(math.exp(1 * (depth - MAX_DEPTH)), 1):
            # if np.random.rand() < 0.9 ** (0.5 * depth):
            recursive_branch(image, init_length, depth + 1, angle1, end_point)
            recursive_branch(image, init_length, depth + 1, angle2, end_point)


if __name__ == '__main__':
    global zen_points
    zen_points = np.array([hextorgb(string)
                          for string in open('utils/zenburn_colors.txt', 'r')])
    size_tuple = (1200, 1920, 3)
    (width, height, _) = size_tuple

    img = np.full(size_tuple, hextorgb("3f3f3f"), dtype=np.uint8)
    recursive_branch(img, 200, 1, math.pi/2, (700, 1200))

    plt.imshow(img)
    plt.show()
    # plt.imsave("wallpaper.png", img)
