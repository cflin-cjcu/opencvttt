import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('./images/test1.jpg')
img2 = cv.cvtColor(img,cv.COLOR_BGR2RGB)
plt.imshow(img2, interpolation = 'bicubic')
# plt.xticks([]), plt.yticks([]) # 隐藏 X 和 Y 轴的刻度
plt.show()
