import numpy as np
import cv2
import matplotlib.pyplot as plt

# print(f'Numpy=={np.__version__}')
# print(f'OpenCV=={cv2.__version__}')



candy = cv2.imread('img/candy_1.jpg', cv2.IMREAD_COLOR)
candy = cv2.cvtColor(candy, cv2.COLOR_BGR2RGB)
candy_hsv = cv2.cvtColor(candy, cv2.COLOR_RGB2HSV)


def imshow(img):
    plt.figure(figsize=(10, 7))
    plt.imshow(img, cmap='gray')
    plt.show()


# Convert the image to grayscale
gray_candy_original = cv2.cvtColor(candy, cv2.COLOR_RGB2GRAY)
gray_candy = gray_candy_original.copy()


# Apply some gaussian blur
blur = cv2.GaussianBlur(gray_candy, (9, 9), 1)

# Apply Canny to find edges and display the image
canny = cv2.Canny(blur,150,220)


# threshold
ret, th = cv2.threshold(canny, 128, 255, cv2.THRESH_BINARY)
contours, h = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

candy_contours = candy.copy()
cv2.drawContours(candy_contours, contours, -1, (255, 0, 255), 3)

# area = cv2.contourArea(ctn)
# sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)

imshow(candy_contours)

# couting
sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)

print(f'# Candy Counter: {len(sorted_contours)}')
# imshow(canny)




# # count colors
# img = candy
#
# rows, cols, bands = img.shape
# X = img.reshape(rows*cols, bands)
#
# kmeans = KMeans(n_clusters=7, random_state=42).fit(X)
# labels = kmeans.labels_.reshape(rows, cols)
#
# for i in np.unique(labels):
#     blobs = np.int_(morphology.binary_opening(labels == i))
#     color = np.around(kmeans.cluster_centers_[i])
#     count = len(np.unique(measure.label(blobs))) - 1
#     print('Color: {}  >>  Objects: {}'.format(color, count))









prob = round(int(1/6*100),4)
# print(f'Probability of each color: {prob} %')
# num_prob = float(sorted_contours) * prob
# print(f'# probability of each color: {num_prob}')





#show the image
# cv.namedWindow('Contours',cv.WINDOW_NORMAL)
# # cv.namedWindow('Thresh',cv.WINDOW_NORMAL)
# cv.imshow('Contours', img)
# # cv.imshow('Thresh', thresh)
# if cv.waitKey(0):
#     cv.destroyAllWindows()



# range of colors

# Red color
low_red = np.array([165, 155, 84])
high_red = np.array([179, 255, 255])
# Threshold the HSV image to get only red colors
red_mask = cv2.inRange(candy_hsv, low_red, high_red)
red = cv2.bitwise_and(low_red, high_red, mask=red_mask)


# Blue color
low_blue = np.array([100, 50, 50])
high_blue = np.array([126, 255, 255])
# Threshold the HSV image to get only blue colors
blue_mask = cv2.inRange(candy_hsv, low_blue, high_blue)
blue = cv2.bitwise_and(low_blue, high_blue, mask=blue_mask)


# Green color
low_green = np.array([45, 50, 72])
high_green = np.array([70,255,255])
# Threshold the HSV image to get only green colors
green_mask = cv2.inRange(candy_hsv, low_green, high_green)
green = cv2.bitwise_and(low_green, high_green, mask=green_mask)


# Yellow color
low_yellow = np.array([26, 50, 72])
high_yellow = np.array([32,255,255])
# Threshold the HSV image to get only yellow colors
yellow_mask = cv2.inRange(candy_hsv, low_yellow, high_yellow)
yellow = cv2.bitwise_and(low_yellow, high_yellow, mask=yellow_mask)


# Orange color
low_orange = np.array([15, 50, 72])
high_orange = np.array([25,255,255])
# Threshold the HSV image to get only orange colors
orange_mask = cv2.inRange(candy_hsv, low_orange, high_orange)
# orange = cv2.bitwise_and(low_orange, high_orange, mask=orange_mask)


# Brown color
low_brown = np.array([96, 58, 52])
high_brown = np.array([61,43,39])
# Threshold the HSV image to get only brown colors
brown_mask = cv2.inRange(candy_hsv, low_brown, high_brown)
# brown = cv2.bitwise_and(low_brown, high_brown, mask=brown_mask)



print(f'# red: {len(red)}')
print(f'# blue: {len(blue)}')
print(f'# green: {len(green)}')
print(f'# yellow: {len(yellow)}')
print(f'# orange: {len(orange)}')
print(f'# brown: {len(brown)}')
