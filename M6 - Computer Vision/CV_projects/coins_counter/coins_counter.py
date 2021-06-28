import numpy as np
import cv2
import matplotlib.pyplot as plt

print(f'Numpy=={np.__version__}')
print(f'OpenCV=={cv2.__version__}')


coins = cv2.imread('img/coins.jpg', cv2.IMREAD_COLOR)
coins = cv2.cvtColor(coins,cv2.COLOR_BGR2RGB)


def imshow(img):
    plt.figure(figsize=(10, 7))
    plt.imshow(img, cmap='gray')
    plt.show()


# Convert the image to grayscale
gray_coins_original = cv2.cvtColor(coins, cv2.COLOR_RGB2GRAY)
gray_coins = gray_coins_original.copy()


# Apply some gaussian blur
blur = cv2.GaussianBlur(gray_coins, (9,9), 0)

# Apply Canny to find edges and display the image
canny = cv2.Canny(blur,50,200)


# threshold
ret, th = cv2.threshold(canny, 128, 255, cv2.THRESH_BINARY)
contours, h = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

coins_contours = coins.copy()
cv2.drawContours(coins_contours, contours, -1, (0,255,0), 2)

# area = cv2.contourArea(ctn)
# sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)

imshow(coins_contours)

print(len(coins_contours))
# imshow(gray_coins)
# imshow(gray_coins_1)
