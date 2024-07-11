import cv2

detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img=cv2.imread('img.jpg')

# 1.3 means the image is scaled down by a factor of 1.3 at each step.
# 5 means that at least 5 overlapping rectangles are required to retain a detected face.

faces=detector.detectMultiScale(img,1.3,5)


for (x,y,w,h) in faces:                            # w-width , h-height
  # (0,255,0) ----green color  2---width
  cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)   # (x,y)---starting point  x+w---horizontal direction  y+h---vertical direction

  cv2.imwrite("Output.png",img)
  print("img loaded successfully")