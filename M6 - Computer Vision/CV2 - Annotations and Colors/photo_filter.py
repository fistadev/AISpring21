import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

print(cv2.__version__)


img = cv2.imshow("bokeh.jpg", 0)

# print(img.shape)

# cv2.imshow("Image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.waitKey(1)

print(type(img))


def imshow(img):
    plt.figure(figsize=(10, 7))
    plt.imshow(img, cmap="gray")


print(img.shape)

# convert ot RGB
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# print(type(rgb_img))

# split
B = rgb_img[:, :, 0]
G = rgb_img[:, :, 1]
R = rgb_img[:, :, 2]

# black
k = np.zeros(rgb_img.shape[:2], dtype="uint8")

# white
w = np.zeros(rgb_img.shape[:2], dtype="uint8")
w[:, :] = [255]

# red
red = cv2.merge([R, k, k])

# blue
blue = cv2.merge([k, k, B])

# green
green = cv2.merge([k, G, k])

# mask


# filter
opacity = 0.25
img_2w = cv2.addWeighted(green, opacity, rgb_img, 1 - opacity, 0)

imshow(img_2w)


# upload

# fileitem = form['filename']

# # check if the file has been uploaded
# if fileitem.filename:
#     # strip the leading path from the file name
#     fn = os.path.basename(fileitem.filename)

#    # open read and write the file into the server
#     open(fn, 'wb').write(fileitem.file.read())
