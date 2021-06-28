import numpy as np
import cv2

img3 = cv2.imread('img/beach.jpg')

lower_1 = np.array([10, 0, 10])
upper_1 = np.array([50, 255, 255])
lower_2 = np.array([200, 0, 10])
upper_2 = np.array([20, 255, 255])

vc = cv2.VideoCapture(0)
if vc.isOpened():
    response, frame = vc.read()

else:
    response = False
i = 0
while response:
    response, frame = vc.read()
    hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask_red0 = cv2.inRange(hsv_img, lower_1, upper_1)
    mask_red1 = cv2.inRange(hsv_img, lower_2, upper_2)
    mask = mask_red0 + mask_red1

    img3_resized = cv2.resize(img3, (frame.shape[1], frame.shape[0]), interpolation=cv2.INTER_AREA)

    frame[mask == 255] = img3_resized[mask == 255]
    cv2.imshow('Live', frame)

    key = cv2.waitKey(1)
    if cv2.waitKey(25) == 27: # EXIT
        break

cv.destroyAllWindows()
vc.release()