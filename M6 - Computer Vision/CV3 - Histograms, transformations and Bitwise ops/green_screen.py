import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

print(cv2.__version__)


PATH = "bird.jpg"
img = cv2.imshow(PATH)

def imshow(img):
    plt.figure(figsize = (10,7));
    plt.imshow(img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)
#
print(img.shape)


# green screen
green_screen = np.zeros((800,800), dtype="uint8")
print(green_screen.shape)

