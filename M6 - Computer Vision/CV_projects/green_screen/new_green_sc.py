import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("img/beach.jpg")


# def imshow(img):
#     plt.figure(figsize=(10, 7))
#     plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), cmap="gray")
#     plt.show()


# webcam
video = cv2.VideoCapture(0)

while video.isOpened():
    check, frame = video.read()
    if frame is not None:
        cv2.imshow("LIVE", frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()



image = cv2.imread("img/1.jpg")

while True:

    ret, frame = video.read()

    frame = cv2.resize(frame, (640, 480))
    image = cv2.resize(image, (640, 480))

    u_green = np.array([104, 153, 70])
    l_green = np.array([30, 30, 0])

    mask = cv2.inRange(frame, l_green, u_green)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    f = frame - res
    f = np.where(f == 0, image, f)

    cv2.imshow("video", frame)
    cv2.imshow("mask", f)

    if cv2.waitKey(25) == 27:
        break

video.release()
cv2.destroyAllWindows()









