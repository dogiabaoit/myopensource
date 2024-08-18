import cv2  #pip install opencv-python
            #https://github.com/opencv
            #Nho import opencv-python package trong File/Setting:Project>Interpreter

cap = cv2.VideoCapture(0);                  #docs.opencv.org
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))
print(cap.isOpened())

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        #GHI LAI PHIM
        out.write(frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BG2GRAY)
        #cv2.imshow('frame', frame)
        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
