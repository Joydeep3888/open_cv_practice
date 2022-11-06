import numpy as np
import cv2

images=np.zeros((512,512,3), dtype=int)
###function##
def draw_circle(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(images,(x,y),100,(0,255,0),-1)

cv2.namedWindow(winname='mydraw')
cv2.setMouseCallback('mydraw',draw_circle)

##showingImage###
image=np.zeros((512,512,3),np.int)
while True:
    cv2.imshow('mydraw',images)
    
    if cv2.waitKey(20) & 0xFF==27:
        break
cv2.destroyAllWindows()