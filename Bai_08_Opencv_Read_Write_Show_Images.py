import cv2  #pip install opencv-python
            #https://github.com/opencv
            #Nho import opencv-python package trong File/Setting:Project>Interpreter
#print(cv2.__version__)

#READ
img = cv2.imread('lena.jpg', 1)       # -1: Load image as such including alpha chanel; 1: Loads a color image; 0: Loads image in grayscale mode

#SHOW
cv2.imshow('image',img)
k = cv2.waitKey(0) & 0xFF             #Thoi gian cho nhan phim hoac nhan vao color tren hinh nhu ma colorr cai dat

if k==27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    #WRITE
    cv2.imwrite('lena_copy.jpg',img)
    cv2.destroyAllWindows()

