#interactive drawing

import cv2

#call back function

def draw_circle(event,x,y,flags,param):
    
    global left_clicked,pt1
    
    if event==cv2.EVENT_LBUTTONDOWN:
        pt1=(x,y)
        left_clicked=False
        
    if event==cv2.EVENT_LBUTTONUP:
        left_clicked=True
          
            
#global variable

pt1=(0,0)

left_clicked=False

#connect to call back

capture=cv2.VideoCapture(0)
cv2.namedWindow('Test')
cv2.setMouseCallback('Test',draw_circle)


while True: 
    ret,frame=capture.read()
    
    #drawing based on global variable
    if left_clicked:
        cv2.circle(frame,center=pt1,radius=50,color=(0,0,255), thickness=5)
     
    cv2.imshow('Test',frame)
    
    if cv2.waitKey(10) & 0xFF==ord('q'):
        break
    
capture.release()
cv2.destroyAllWindows()
    
    
    
    
    
