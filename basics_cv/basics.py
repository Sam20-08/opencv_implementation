
# Importing the cv Library
import cv2

# Reading the image (imread will read the image  and return numpy array for the image)
image_path="img1.jpeg"

image=cv2.imread(image_path)

# Resizing The image

resized_image=cv2.resize(image,(400,350))

#check the image loaded successfully

if image is None:

  print(f"There is an error loading the {image_path}")

else:
  cv2.imshow('Hello CV',image)

  # display the resized image

  cv2.imshow("Hello opencv", resized_image)

  # Wait for key event and close the window
  cv2.waitKey(0)
  cv2.destroyAllWindows()