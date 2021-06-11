import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

print('OpenCV: ', cv2.__version__)


# upload

# fileitem = form['filename']

# # check if the file has been uploaded
# if fileitem.filename:
#     # strip the leading path from the file name
#     fn = os.path.basename(fileitem.filename)

#    # open read and write the file into the server
#     open(fn, 'wb').write(fileitem.file.read())


def imshow(img):
    plt.figure(figsize=(10, 7))
    plt.imshow(img, cmap='gray')
    plt.show()


PATH = "img/beach.jpg"
img = cv2.imread(PATH)
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# imshow(rgb_img)


print('img.shape:', img.shape)

print(type(img))


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

# red filter
red = cv2.merge([R, k, k])

# blue filter
blue = cv2.merge([k, k, B])

# green filter
green = cv2.merge([k, G, k])

# mask


# Dark
pixel_values = np.ones(img.shape, dtype='uint8') * 50
darker_img = cv2.add(img, pixel_values)

# Bright
pixel_values = np.ones(img.shape, dtype='uint8') * 200
bright_img = cv2.add(img, pixel_values)



# red filter
opacity = 0.95
img_2w = cv2.addWeighted(red, opacity, rgb_img, 1 - opacity, 0)
img_2w_red = cv2.addWeighted(img_2w, opacity, rgb_img, 1 - opacity, 0)


# green filter
opacity = 0.35
img_2w = cv2.addWeighted(green, opacity, rgb_img, 1 - opacity, 0)
img_2w_green = cv2.addWeighted(img_2w, opacity, rgb_img, 1 - opacity, 0)


# blue filter
opacity = 0.35
img_2w = cv2.addWeighted(blue, opacity, rgb_img, 1 - opacity, 0)
img_2w_blue = cv2.addWeighted(img_2w, opacity, rgb_img, 1 - opacity, 0)


# sharpen red
kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
img_sharp_red = cv2.filter2D(img_2w_red, -1, kernel)

# sharpen green
kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
img_sharp_green = cv2.filter2D(img_2w_green, -1, kernel)

# sharpen blue
kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
img_sharp_blue = cv2.filter2D(img_2w_blue, -1, kernel)

# black&white
kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
img_bw = cv2.filter2D(gray, -1, kernel)



# 2nd layer
opacity_final = 0.2
img_final = cv2.addWeighted(img_sharp_red, opacity_final, img_2w_green, 1 - opacity_final, 0)


# imshow(img_2w_red)
# imshow(img_2w_green)
# imshow(img_2w_blue)
# imshow(img_sharp)
# imshow(img_final)
imshow(img_bw)
# imshow(rgb_img)
# imshow(red)
# imshow(blue)
# imshow(green)
# imshow(darker_img)
# imshow(bright_img)

