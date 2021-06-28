import numpy as np
import cv2

capt_video = cv2.VideoCapture(1)

while(True):
    #capture fram by frame
    ret, frame = capt_video.read()
    big_frame = cv2.resize(frame, None, fx=4, fy=4)

    cv2.line(frame,(0,0),(150,150),(255,255,255),15)

    # Display the result frame
    cv2.imshow('frame',big_frame)
    if cv2.waitKey(30) &0xFF == ord('q'):
        break

# release capture
caqqqpt_video.release()
cv2.destroyAllWindows()
