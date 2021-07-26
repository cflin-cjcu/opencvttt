import cv2

#開圖
img1 = cv2.imread('./images/test1.jpg',cv2.IMREAD_GRAYSCALE)

# print(img1)
#秀圖
cv2.namedWindow('test',cv2.WINDOW_NORMAL)
cv2.imshow('test',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('test.png',img1)