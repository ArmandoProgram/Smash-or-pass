import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('mapache.jpg')
cv2.imshow('mapache.jpg', img)

color = ('b','g','r')

for i, c in enumerate(color):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color = c)
    plt.xlim([0,256])

plt.show()
