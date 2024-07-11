import cv2

detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

live_detect=cv2.VideoCapture(0)  # Used to capture the live video

# Infinite Loop

while True:
  ret,img=live_detect.read()

  # convert to grey scale img
  grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

  # detect Face
  faces=detector.detectMultiScale(img,1.3,5)
  # drawing rectangle
  for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)   # (0,255,0) ----green color  2---width
    cv2.imshow('img',img)

    quit=cv2.waitKey(100) & 0xff

    if quit==27:
      break
live_detect.release()

