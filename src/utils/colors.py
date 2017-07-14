import numpy as np


def hex_to_rgb(hexstring):
    r = int(hexstring[0:2], 16)
    g = int(hexstring[2:4], 16)
    b = int(hexstring[4:6], 16)
    return (r, g, b)


def get_zenburn_colors(color_file_path='utils/zenburn_colors.txt'):
    zenburn_colors = [hex_to_rgb(string)
                      for string in open(color_file_path, 'r')]
    return np.array(zenburn_colors)
