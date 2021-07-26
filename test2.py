import numpy as np
import cv2 as cv

img = cv.imread('./images/test1.jpg',0)
cv.imshow('image',img)
k = cv.waitKey(0)
if k == 27: # ESC 退出
    cv.destroyAllWindows()
elif k == ord('s'): # 's' 保存退出
    cv.imwrite('messigray.png',img)
    cv.destroyAllWindows()
