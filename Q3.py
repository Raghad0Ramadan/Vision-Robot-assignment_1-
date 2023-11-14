import cv2

img = cv2.imread("orignal_img.png")

# flip the image by vertically
img_v = cv2.flip(img, 0)

# flip the image by horizontally
img_h = cv2.flip(img, 1)

# rotate the image both vertically and horizontally
img_vh = cv2.flip(img, -1)

cv2.imshow("Vertical Flip", img_v)
cv2.imshow("Horizontal Flip", img_h)
cv2.imshow("Both vertical and horizontal flip", img_vh)

cv2.imwrite("vertical and horizontal flip.jpg", img_vh)
cv2.imwrite("Vertical Flip.jpg", img_v)
cv2.imwrite("Horizontal Flip.jpg", img_h)

cv2.waitKey(0)
cv2.destroyAllWindows()