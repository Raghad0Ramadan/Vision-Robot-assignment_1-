import cv2
import numpy as np


img = cv2.imread('orignal_img.png')
print(img.shape)

# Define the shapes
circle_mask = np.zeros_like(img)
triangle_mask = np.zeros_like(img)
square_mask = np.zeros_like(img)

# Create a circle
cv2.circle(circle_mask, (200,200), 100, (255, 255, 255), thickness=-1)

# Create a triangle
pts = np.array([[150, 200], [300, 150], [200, 200]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.fillPoly(triangle_mask, [pts], (255, 255, 255))

# Create a square
cv2.rectangle(square_mask, (100, 100), (200, 200), (255, 255, 255), thickness=-1)

# Apply masks to the original image
circle_img = cv2.bitwise_and(img, circle_mask)
triangle_img = cv2.bitwise_and(img, triangle_mask)
square_img = cv2.bitwise_and(img, square_mask)

# Display the results
cv2.imshow('Circle Result', circle_img)
cv2.imshow('Triangle Result', triangle_img)
cv2.imshow('Square Result', square_img)
cv2.imwrite("Square Result.jpg", square_img)
cv2.imwrite("Circle Result.jpg", circle_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

