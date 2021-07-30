from cvzone.FaceMeshModule import FaceMeshDetector
import cv2

cap = cv2.VideoCapture(1)
detector = FaceMeshDetector(maxFaces=2)
while True:
    success, img = cap.read()
    img, faces = detector.findFaceMesh(img)
    if faces:
        cv2.line(img,(faces[0][147][0],faces[0][147][1]),(faces[0][440][0],faces[0][440][1]),(0,0,255),10)
    cv2.imshow("Image", img)
    k=cv2.waitKey(1)
    if k==27:
        break
cv2.destroyAllWindows()