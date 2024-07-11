
import numpy as np
import cv2

# Load image
img = cv2.imread('dog.jpg')

# 7.blank images

img=np.zeros([512,512,3],np.uint8)
#[512,512,3]---size of the window

# 1.Draw a line on the image
img = cv2.line(img, (0,0), (255,255), (147, 96, 44), 10) 

# (0,0)---starting pointof the line
# (255,255)---ending point of the line
# (147,96,44)---color of the line
# 10---thickness of the line

# 2.Draw the arrowline
img = cv2.arrowedLine(img, (0,255), (255,255), (255, 0, 0), 5)

#(0,255)---x-origin
#(255,255)--starting point
#(255,0,0)--ending point
#(255, 0, 0)---color
#5--width

# 3.Drawing the rectangle
img=cv2.rectangle(img,(384,0),(510,128),(0,0,255),10)

#(384,0)---top left point
#(510,128)--botton right point
#10---width
#(0,0,255)--color

# 4.Circle

img=cv2.circle(img,(447,63),63,(0,255,0),-1)

#(600,80)--points
#63--radius
#(0,255,0)---rgb
#-1---thickness (fullings inside the circle)

# 5.TO put text on the image
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpenCv', (10, 500), font, 4, (0, 255, 255), 10)

#'OpenCv'--text to put on the image
#4--font scale
#(0, 255, 255)--color of the font

# 6.Ellipse

#cv2.ellipse(img,center_coordinates,axeslength,angle,startangle,endangle,color,thickness)
img=cv2.ellipse(img,(256,256),(100,50),0,0,180,(0, 255, 255),-1)

#axeslength---length of the ecllipse



cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
