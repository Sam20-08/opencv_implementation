import cv2

#cv2.threashold is only for greyscale image


img=cv2.imread('img1.jpg')

_,th1=cv2.threshold(img,50,255,cv2.THRESH_BINARY)
#127 - (2nd parameter is threshold parameter)
#max_value (255)

_,th2=cv2.threshold(img,120,255,cv2.THRESH_BINARY_INV) # It is the inverse of the th1

_,th3=cv2.threshold(img,200,255,cv2.THRESH_TRUNC) # after the 200 pixel it will be same

_,th4=cv2.threshold(img,200,255,cv2.THRESH_TOZERO) # if the value of pixel is less than 200 make it 0(BLACK) else keep it as it is 

_,th5=cv2.threshold(img,200,255,cv2.THRESH_TOZERO_INV)

cv2.imshow('output',img)
cv2.imshow("th1",th1)
cv2.imshow("th2",th2)
cv2.imshow("th3",th3)
cv2.imshow("th4",th4)
cv2.imshow("th5",th5)

cv2.waitKey(0)
cv2.destroyAllWindows()
