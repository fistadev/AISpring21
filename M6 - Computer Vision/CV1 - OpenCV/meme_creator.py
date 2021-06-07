import cv2
import numpy as np
import matplotlib.pyplot as plt

print(cv2.__version__)


img = cv2.imread("annotations.jpg")

# print(img)

# print(type(img))


# cv2.imshow("My image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.waitKey(1)

cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(20, 10))
plt.imshow(img)
