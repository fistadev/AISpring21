import cv2
import matplotlib.pyplot as plt

img = cv2.imread("img/beach.jpg")


def imshow(img):
    plt.figure(figsize=(10, 7))
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), cmap="gray")
    plt.show()


def sketch(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    g_blur = cv2.GaussianBlur(gray, (7, 7), 0)
    # _, thres_img = cv2.threshold(g_blur, 128, 255, cv2.THRESH_BINARY)
    edges = cv2.Canny(g_blur, 1, 80)
    _, edges_inv = cv2.threshold(edges, 150, 255, cv2.THRESH_BINARY_INV)
    return edges_inv



# imshow(sketch(img))




imshow(img)


# imshow(gray)
# imshow(thres_img)
# plt.show()