import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['image.cmap'] = 'gray'


img1 = cv2.imread('../img/bokeh.jpg')
img2 = cv2.imread('../img/beach.jpg')



threshold_value = 128
threshold_type = cv2.THRESH_BINARY

threshold_types = [cv2.THRESH_BINARY, cv2.THRESH_BINARY_INV, cv2.THRESH_TOZERO, cv2.THRESH_TOZERO_INV, cv2.THRESH_TRUNC]

window_name = 'threshold'

img_copy = img2.copy()
gray_img = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)

cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)


def change_threshold_value(val):
    threshold_value = val
    ret, thresh = cv2.threshold(gray_img, threshold_value, 255, threshold_type)
    cv2.imshow(window_name, thresh)



# def change_saturation(val):
#     threshold_value = val
#     ret, thresh = cv2.threshold(gray_img, threshold_type, 255, threshold_type)
#     cv2.imshow(window_name, thresh)




cv2.createTrackbar("Threshold Value", window_name, threshold_value, 255, change_threshold_value)
# cv2.createTrackbar('Threshold Type', window_name, threshold_type, 4, change_threshold_type)


cv2.imshow(window_name, gray_img)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.waitKey(1)