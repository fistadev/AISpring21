import cv2
import numpy as np
import matplotlib.pyplot as plt


# img = cv2.imread('img/bridge.jpg')
img = cv2.imread('img/noisy.png')


def imshow(img):
    plt.figure(figsize=(10, 7))
    plt.imshow(img, cmap='gray')
    plt.show()


rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

gray = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2GRAY)

g_blur = cv2.GaussianBlur(gray, (9,9), 0)
canny = cv2.Canny(g_blur, 1, 50)
denoise = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)

img_final = cv2.cvtColor(denoise, cv2.COLOR_BGR2RGB)


imshow(img_final)
# imshow(rgb_img)

