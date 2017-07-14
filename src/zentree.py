import math

import matplotlib.pyplot as plt

from utils.colors import create_background
from tree.dynamics import recursive_branch

image_size = (1200, 1920, 3)
image = create_background(image_size, '3f3f3f')
recursive_branch(image, 200, 1, math.pi/2, (700, 1200))

plt.imshow(image)
plt.show()
# plt.imsave("wallpaper.png", img)
