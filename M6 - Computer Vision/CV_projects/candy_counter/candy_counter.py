import numpy as np
import cv2
import matplotlib.pyplot as plt
from skimage import io, morphology, measure
from sklearn.cluster import KMeans

# print(f'Numpy=={np.__version__}')
# print(f'OpenCV=={cv2.__version__}')



candy = cv2.imread('img/candy.jpg', cv2.IMREAD_COLOR)
candy = cv2.cvtColor(candy, cv2.COLOR_BGR2RGB)


def imshow(img):
    plt.figure(figsize=(10, 7))
    plt.imshow(img, cmap='gray')
    plt.show()


# Convert the image to grayscale
gray_candy_original = cv2.cvtColor(candy, cv2.COLOR_RGB2GRAY)
gray_candy = gray_candy_original.copy()


# Apply some gaussian blur
blur = cv2.GaussianBlur(gray_candy, (9, 9), 0)

# Apply Canny to find edges and display the image
canny = cv2.Canny(blur,50,200)


# threshold
ret, th = cv2.threshold(canny, 128, 255, cv2.THRESH_BINARY)
contours, h = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

candy_contours = candy.copy()
cv2.drawContours(candy_contours, contours, -1, (0, 255, 0), 4)

# area = cv2.contourArea(ctn)
# sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)

imshow(candy_contours)

# couting
sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)

print(f'# Candy Counter: {len(sorted_contours)}')
# imshow(gray_coins)
# imshow(gray_coins_1)

img = candy

# count colors
rows, cols, bands = img.shape
X = img.reshape(rows*cols, bands)

kmeans = KMeans(n_clusters=7, random_state=42).fit(X)
labels = kmeans.labels_.reshape(rows, cols)

for i in np.unique(labels):
    blobs = np.int_(morphology.binary_opening(labels == i))
    color = np.around(kmeans.cluster_centers_[i])
    count = len(np.unique(measure.label(blobs))) - 1
    print('Color: {}  >>  Objects: {}'.format(color, count))

# Create a dictionary of color names and RGB values
color_dict = {
    'blue': (47,159,215),
    'green': (49,172,85),
    'red': (177,18,36),
    'brown': (96,58,52),
    'yellow': (255,242,0),
    'orange': (242,111,34),
          }

blue = []
green = []
red = []
brown = []
yellow = []
orange = []
white = []

# count = []
for i in labels:
    if i == (51,139,209):
        # count += 1
        blue += 1
    elif i == (66,161,48):
        # count += 1
        green += 1
    elif i == (215,73,55):
        # count += 1
        red += 1
    elif i == (72,37,38):
        # count += 1
        brown += 1
    elif i == (230,188,21):
        # count += 1
        yellow += 1
    elif i == (234,91,69):
        # count += 1
        orange += 1
    # else:
    #     white += 1

prob = round(int(1/len(color_dict)*100),4)
# num_prob = float(sorted_contours) * prob
print(f'Probability of each color: {prob} %')
# print(f'# probability of each color: {num_prob}')


# print(f'# colors: {count}')

print(f'# blue: {blue}')
print(f'# green: {green}')
print(f'# red: {red}')
print(f'# brown: {brown}')
print(f'# yellow: {yellow}')
print(f'# orange: {orange}')
# print(f'# white: {white}')

#show the image
# cv.namedWindow('Contours',cv.WINDOW_NORMAL)
# # cv.namedWindow('Thresh',cv.WINDOW_NORMAL)
# cv.imshow('Contours', img)
# # cv.imshow('Thresh', thresh)
# if cv.waitKey(0):
#     cv.destroyAllWindows()