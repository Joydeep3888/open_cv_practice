#interactive drawing

import cv2

#call back function

def draw_rectangle(event,x,y,flags,param):
    
    global top_left_clicked,b_right_clicked,pt1,pt2
    
    if event==cv2.EVENT_LBUTTONDOWN:
        
        #reset the rectangle
        if top_left_clicked & b_right_clicked:
            pt1=(0,0)
            pt2=(0,0)
            top_left_clicked=False
            b_right_clicked=False
        
        if top_left_clicked==False:
            pt1=(x,y)
            top_left_clicked=True
        
        elif b_right_clicked==False: 
            pt2=(x,y)
            b_right_clicked=True
            
            
#global variable

pt1=(0,0)
pt2=(0,0)

top_left_clicked=False
b_right_clicked=False

#connect to call back

capture=cv2.VideoCapture(0)
cv2.namedWindow('Test')
cv2.setMouseCallback('Test',draw_rectangle)


while True: 
    ret,frame=capture.read()
    
    #drawing based on global variable
    if top_left_clicked:
        cv2.circle(frame,center=pt1,radius=1,color=(0,0,255), thickness=-1)
    
    if top_left_clicked & b_right_clicked:
        cv2.rectangle(frame, pt1,pt2,(0,0,255),4)
     
    cv2.imshow('Test',frame)
    
    if cv2.waitKey(10) & 0xFF==ord('q'):
        break
    
capture.release()
cv2.destroyAllWindows()
    
    
    
    
    
