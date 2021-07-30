from posem import PoseDetector
import cv2

cap = cv2.VideoCapture(1)
detector = PoseDetector(upBody=True)
while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False)
    if bboxInfo:
        center = bboxInfo["center"]
        cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)
    
    angle = detector.findAngle(img,12,14,16,draw=True)
    print(angle)

    cv2.imshow("Image", img)
    k=cv2.waitKey(1)
    if k==27:
        break
cv2.destroyAllWindows()    
