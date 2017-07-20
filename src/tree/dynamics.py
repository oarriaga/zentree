import math
import cv2
import numpy as np

from utils.colors import get_zenburn_colors


def length_scaling(depth):
    return math.exp(-depth/5)


def recursive_branch(image, initial_length, depth, angle,
                     start_point, zen_colors=None,
                     MAX_DEPTH=15, SIGMA_ANGLE=0.1):

    if zen_colors is None:
        zen_colors = get_zenburn_colors()

    length = initial_length * length_scaling(depth)
    length = np.random.normal(length, length/9)

    end_x = int(start_point[0] + length * math.cos(angle))
    end_y = int(start_point[1] - length * math.sin(angle))
    end_point = (end_x, end_y)

    start_index = int(((depth - 1) / MAX_DEPTH) * len(zen_colors))
    end_index = int((depth / MAX_DEPTH) * len(zen_colors))

    colors = zen_colors[min(np.random.randint(start_index, end_index),
                        len(zen_colors) - 1)]
    color1, color2, color3 = colors.astype(np.int32)
    cv2.line(image, start_point, end_point,
             (int(color1), int(color2), int(color3)), 2, cv2.LINE_AA)

    angle1, angle2 = np.random.normal(math.pi /
                                      (6.6 + 0.6 * depth), SIGMA_ANGLE, 2)
    angle1 = angle - abs(angle1)
    angle2 = angle + abs(angle2)

    if np.random.rand() > 0.7 * min(math.exp(1 * (depth - MAX_DEPTH)), 1):
        # randomize the number of branches
        recursive_branch(image, initial_length, depth + 1,
                         angle1, end_point, zen_colors)
        recursive_branch(image, initial_length, depth + 1,
                         angle2, end_point, zen_colors)
