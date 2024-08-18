import numpy as np
import cv2

#Neu khong tim thay file hinh thi lay mau nen
try:
    img = cv2.imread('lena.jpg', 1)     #Hinh nen
except:
    img = np.zeros([512,512,3],np.uint8)#Mau nen

img = cv2.line(img,(0,0), (255,255), (147,96,44), 10)
img = cv2.arrowedLine(img,(0,255), (255,255), (255,0,0), 10)

img = cv2.rectangle(img,(384,0), (510,128), (0,0,255), -1)

img = cv2.circle(img,(447,63), 63, (0,255,0), 3)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpenCv', (10,500), font, 4, (255,255,255), 10,cv2.LINE_AA)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()