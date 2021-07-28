import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./images/test1.jpg')

lower = cv2.pyrDown(img)
lower1 = cv2.pyrDown(lower)
higher = cv2.pyrUp(lower1)
higher1 = cv2.pyrUp(higher)
laplace = cv2.subtract(img, higher1)
print(img.shape,higher1.shape)
plt.subplot(121), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('Src')
plt.subplot(122), plt.imshow(cv2.cvtColor(laplace, cv2.COLOR_BGR2RGB)), plt.title('Laplace')
plt.show()