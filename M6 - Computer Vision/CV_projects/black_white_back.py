import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# print(cv2.__version__)


def imshow(img):
    plt.figure(figsize=(10, 7))
    plt.imshow(img)
    plt.show()


PATH = "img/bokeh.jpg"
img = cv2.imread(PATH)
# rgb_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# imshow(rgb_img)


# print(img.shape)
#
# print(type(img))


# print(type(rgb_img))

# split
B = hsv_img[:, :, 0]
G = hsv_img[:, :, 1]
R = hsv_img[:, :, 2]

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
opacity = 0.35
img_2w = cv2.addWeighted(k, opacity, rgb_img, 1 - opacity, 0)
img_2w_k = cv2.addWeighted(img_2w, opacity, rgb_img, 1 - opacity, 0)


imshow(img_2w_k)


# upload

# fileitem = form['filename']

# # check if the file has been uploaded
# if fileitem.filename:
#     # strip the leading path from the file name
#     fn = os.path.basename(fileitem.filename)

#    # open read and write the file into the server
#     open(fn, 'wb').write(fileitem.file.read())
