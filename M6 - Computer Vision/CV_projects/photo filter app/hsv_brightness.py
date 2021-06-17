import numpy as np
import cv2

# Callback function, not used
def nothing(x):
    pass

# Convert BGR image to HSV image
win_img = "new"
win_img_old = "old"
# pic = cv2.imread("../img/bridge.jpg", cv2.IMREAD_UNCHANGED)
pic = cv2.imread("../img/beach.jpg", cv2.IMREAD_UNCHANGED)
pic1 = cv2.cvtColor(pic, cv2.COLOR_BGR2HSV)


# Display the original image for comparison
cv2.namedWindow(win_img_old, cv2.WINDOW_NORMAL)
cv2.imshow(win_img_old, pic)

def change_threshold_value(val):
    threshold_value = val
    ret, thresh = cv2.threshold(pic, 128, 255, cv2.THRESH_BINARY)
    cv2.imshow('threshold', thresh)

# New image window
cv2.namedWindow(win_img, cv2.WINDOW_AUTOSIZE)
#Initialize the scroll bar
cv2.createTrackbar("H",win_img, 100, 150, nothing)
cv2.createTrackbar("S",win_img, 100, 150, nothing)
cv2.createTrackbar("V",win_img, 100, 150, nothing)
cv2.createTrackbar("Threshold Value", 'threshold', 128, 255, change_threshold_value)

while True:
	# ESC press to exit
    if cv2.waitKey(10) == 27:
        print("finish adjust picture and quit")
        break
	# Read the HSV information of the current scroll bar
    h_value = float(cv2.getTrackbarPos("H",win_img)/100)
    s_value = float(cv2.getTrackbarPos("S",win_img)/100)
    v_value = float(cv2.getTrackbarPos("V",win_img)/100)
	# After splitting and reading in new data, re-synthesize the adjusted picture
    H, S, V = cv2.split(pic)
    new_pic = cv2.merge([np.uint8(H*h_value) , np.uint8(S*s_value) , np.uint8(V*v_value)])
    cv2.imshow(win_img, new_pic)

cv2.destroyAllWindows()