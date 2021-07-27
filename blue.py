import cv2
import numpy as np

def nothing(x):
    pass

#開圖
img = cv2.imread('./images/test1.jpg')
cv2.namedWindow('img1')
img1 = cv2.resize(img,None,fx=1/2,fy=1/2,interpolation=cv2.INTER_CUBIC)
img2 = cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)
cv2.createTrackbar('A','img1',0,255,nothing)
cv2.createTrackbar('B','img1',0,255,nothing)

while(True):
    A = cv2.getTrackbarPos('A','img1')
    B = cv2.getTrackbarPos('B','img1')
    lower_blue = np.array([A,50,50])
    upper_blue = np.array([B,255,255])
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(img2, lower_blue, upper_blue)
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(img1,img1, mask= mask)
    #秀圖
    cv2.imshow('img1',img1)
    cv2.imshow('img2',img2)
    cv2.imshow('res',res)
    k= cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
