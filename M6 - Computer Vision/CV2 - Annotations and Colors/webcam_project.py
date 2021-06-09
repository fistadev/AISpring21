import cv2
import numpy as np

# print(cv2.__version__)
# print(np.__version__)

# video

video = cv2.VideoCapture(0)


while video.isOpened():
    check, frame = video.read()
    if frame is not None:
        # img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # img = frame
        low_blue = np.array([110, 20, 0])
        upper_blue = np.array([55, 255, 255])
        mask_img = cv2.inRange(img, low_blue, upper_blue)
        result = cv2.bitwise_and(img, img, mask=mask_img)
        # img = frame
        cv2.imshow("mask", mask_img)
        cv2.imshow("original", img)
        cv2.imshow("result", result)
        if cv2.waitKey(30) & 0xFF == ord("q"):
            break
    else:
        break


video.release()
cv2.destroyAllWindows()
cv2.waitKey(1)

