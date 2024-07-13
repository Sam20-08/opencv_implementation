#Adaptive thresholding is used in case of colored image 
# It is used when normal threshold fails

import cv2
img=cv2.imread('soduku.png',cv2.IMREAD_GRAYSCALE)

_,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

# Mean makes bold than gaussian

th3=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)


cv2.imshow('IMAGE',img)
cv2.imshow("th1",th1)
cv2.imshow('th2',th2)
cv2.imshow('th3',th3)


cv2.waitKey(0)
cv2.destroyAllWindows()