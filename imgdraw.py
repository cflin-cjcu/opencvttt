import cv2
import numpy as np

#開圖
img1 = cv2.imread('./images/test1.jpg')

print(len(img1),len(img1[0]))
print(img1.shape)
cv2.line(img1,(200,100),(200,200),(0,0,255),5)
cv2.rectangle(img1,(100,50),(250,300),(255,0,0),-1)
cv2.circle(img1,(300,300),100,(0,255,0),-1)
cv2.putText(img1,'hello world',(600,100),1,5,(255,255,0))

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img1,[pts],True,(0,255,255))


#秀圖
cv2.namedWindow('test',cv2.WINDOW_AUTOSIZE)
cv2.imshow('test',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('test.png',img1)