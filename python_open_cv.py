import cv2
images=np.zeros((512,512,3), dtype=int)
class image_class:
    
    def __init__(self,path):
        self.path=path
        
    def reading_images_CV(self):
        img=cv2.imread(self.path)
        while True: 
            cv2.imshow('BeyondtheUniverse',img)
            if cv2.waitKey(1) & 0xFF ==27:
                break
        cv2.destroyAllWindows()

        
x=image_class(r'C:\Users\hp\OneDrive\Desktop\Blog Pictures\Beyond the Universe Ending Explained-1.jpg')
x.reading_images_CV()