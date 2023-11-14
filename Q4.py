import cv2
import numpy as np


image = cv2.imread("orignal_img.png")
filterd_image_1= np.zeros(image.shape)
filterd_image_1 = cv2.Laplacian(image,-1,filterd_image_1)


print(filterd_image_1.shape)
cv2.imshow("image",image)
cv2.imshow("filterd_image",filterd_image_1)
cv2.imwrite("Laplacian.jpg", filterd_image_1)

cv2.waitKey(0)
cv2.destroyAllWindows()