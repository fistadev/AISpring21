import cv2
import matplotlib.pyplot as plt

img = cv2.imread('img/night_1.jpg')
img2 = cv2.imread('img/beach.jpg')


def imshow(img):
    plt.figure(figsize=(10,7))
    plt.imshow(img, cmap='gray')
    plt.show()


rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

gray = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2GRAY)
_, thres_img = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
edges = cv2.Canny(thres_img,128,255)
_, edges_inv = cv2.threshold(edges, 128, 255, cv2.THRESH_BINARY_INV)


# print(edges_inv.shape)

# imshow(rgb_img)
# imshow(gray)
# imshow(thres_img)
imshow(edges_inv)