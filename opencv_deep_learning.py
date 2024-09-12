import  cv2
import winsound
cam=cv2.VideoCapture(0)
while True:
    ret,cam1=cam.read()
    ret,cam2=cam.read()
    diff=cv2.absdiff(cam1,cam2)
    gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    ret,threshold=cv2.threshold(gray,20,255,cv2.THRESH_BINARY)
    contour,ret=cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for c in contour:
        if cv2.contourArea(c)<5000:
            continue
        winsound.Beep(100,500)
    cv2.imshow("ankit",threshold)
    if cv2.waitKey(30)==ord('a'):
        break
cam.release()
cv2.destroyAllWindows()