import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('./images/test1.jpg',0)
ret3, th3 = cv.threshold(img, 0, 255, cv.THRESH_TOZERO+cv.THRESH_OTSU)
roi = th3[200:400,400:800]
gauss = cv.GaussianBlur(roi, (11, 11), 3)
th3[200:400,400:800]=gauss
cv.imshow('img',img)
cv.imshow('th3',th3)
cv.imshow('gauss',gauss)
cv.waitKey(0)
cv.destroyAllWindows()