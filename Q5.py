import cv2
import numpy as np


image = cv2.imread('orignal_img.png')


brightness_factor = 2.5


brightened_image = cv2.addWeighted(image, brightness_factor, np.zeros_like(image), 0, 0)


cv2.imshow('Original Image', image)
cv2.imshow('Brightened Image', brightened_image)

cv2.imwrite("Brightened Image.jpg",brightened_image)


cv2.waitKey(0)
cv2.destroyAllWindows()

