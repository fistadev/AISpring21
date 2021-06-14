import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

print(cv2.__version__)


def imshow(img):
    plt.figure(figsize=(10, 7))
    plt.imshow(img)
    plt.show()


PATH = "img/beach.jpg"
img = cv2.imread(PATH, 1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
print(img.shape)
# imshow(rgb_img)


# green screen
green_screen = cv2.imread("img/1.jpg", 1)
rgb_green = cv2.cvtColor(green_screen, cv2.COLOR_BGR2HSV)
print(rgb_green.shape)
# imshow(rgb_green)


green_screen_copy = np.copy(rgb_green)
image_copy = cv2.cvtColor(green_screen_copy, cv2.COLOR_BGR2RGB)
# imshow(green_screen_copy)


# defining the color threshold
lower_green = np.array([55, 50, 72])  ##[R value, G value, B value]
upper_green = np.array([65, 255, 255])

# Create a mask
mask = cv2.inRange(green_screen_copy, lower_green, upper_green)
# plt.imshow(mask, cmap='gray')
# plt.show()

# make image over mask
masked_image = np.copy(green_screen_copy)
masked_image[mask != 0] = [0, 0, 0]
# imshow(masked_image)

# convert mask to RGB
masked_image = cv2.cvtColor(masked_image, cv2.COLOR_HSV2RGB)

# Mask and Add Background Image
background_image = cv2.imread(PATH)
background_image = cv2.cvtColor(background_image, cv2.COLOR_BGR2RGB)

crop_background = background_image[0:650, 0:1100]

crop_background[mask == 0] = [0, 0, 0]

# imshow(crop_background)

# print(masked_image.shape)
# print(background_image.shape)

# final image
# Only works if both images are the same shape
# final_image = masked_image + background_image
# final_image = background_image + masked_image
# final_image = crop_background + masked_image
final_image = masked_image + crop_background
imshow(final_image)


# # videoq
#
# video = cv2.VideoCapture(0)
#
#
# while video.isOpened():
#     check, frame = video.read()
#     if frame is not None:
#         # img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         # img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#         img = frame
#         low_blue = np.array([110, 20, 0])
#         upper_blue = np.array([55, 255, 255])
#         mask_img = cv2.inRange(img, low_blue, upper_blue)
#         result = cv2.bitwise_and(img, img, mask=mask_img)
#         # img = frame
#         # cv2.imshow("mask", mask_img)
#         # cv2.imshow("original", img)
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
