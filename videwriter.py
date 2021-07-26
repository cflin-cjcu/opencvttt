import numpy as np
import cv2 as cv
cap = cv.VideoCapture(1)
# 声明编码器和创建 VideoWrite 对象
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('../output.avi',fourcc, 20.0, (640,480))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        
        frame = cv.flip(frame,1)
        # 写入已经翻转好的帧
        out.write(frame)
        cv.imshow('frame',frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
# 释放已经完成的工作
cap.release()
out.release()
cv.destroyAllWindows()
