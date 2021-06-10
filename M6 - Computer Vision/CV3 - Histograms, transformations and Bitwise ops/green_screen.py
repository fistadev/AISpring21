import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

print(cv2.__version__)


def imshow(img):
    plt.figure(figsize = (10,7))
    plt.imshow(img)
    plt.show()

PATH = "bird.jpg"
img = cv2.imread(PATH)
rgb_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# imshow(rgb_img)




# print(img.shape)


# green screen
green_screen = cv2.imread('img/1.jpg')
rgb_green = cv2.cvtColor(green_screen,cv2.COLOR_BGR2RGB)
print(rgb_green.shape)
# imshow(rgb_green)


# mask




# video

# video = cv2.VideoCapture(0)
#
#
# while video.isOpened():
#     check, frame = video.read()
#     if frame is not None:
#         # img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#         # img = frame
#         low_blue = np.array([110, 20, 0])
#         upper_blue = np.array([55, 255, 255])
#         mask_img = cv2.inRange(img, low_blue, upper_blue)
#         result = cv2.bitwise_and(img, img, mask=mask_img)
#         # img = frame
#         cv2.imshow("mask", mask_img)
#         cv2.imshow("original", img)
#         cv2.imshow("result", result)
#         if cv2.waitKey(30) & 0xFF == ord("q"):
#             break
#     else:
#         break
#
#
# video.release()
# cv2.destroyAllWindows()
# cv2.waitKey(1)
