import cv2
import numpy as np
np.set_printoptions(threshold=np.inf)
img = cv2.imread('./shapes/slash.png')
height, width = img.shape[:2]
for item in img:
    if (item != np.array([255, 255, 255])).all():
        print(item)