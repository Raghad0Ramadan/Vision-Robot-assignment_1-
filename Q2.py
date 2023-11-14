import cv2
import numpy as np
img = cv2.imread("orignal_img.png")

# way(wihte)
gray = cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)
num,thrshold2 = cv2.threshold(gray,50,255,cv2.THRESH_BINARY)

#way 2(black)
thrshold = np.zeros(gray.shape)
for i in range (gray.shape[0]):
    for j in range (gray.shape[1]):
        if gray [i,j] <200 :
            thrshold[i,j]=0
        else:
            thrshold[i,j]=255

cv2.imshow("gray",gray)
cv2.imshow("Black",thrshold)
cv2.imshow("white",thrshold2)
cv2.imwrite("black_thrshold.jpg", thrshold)
cv2.imwrite("white_thrshold.jpg", thrshold2)




cv2.waitKey(0)
cv2.destroyAllWindows()
