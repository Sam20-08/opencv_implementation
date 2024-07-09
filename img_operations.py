import cv2

# Reading the image
image=cv2.imread('images.jpeg')

# Getting the width and height of image

print("The width of the image is : ",image.shape[1])
print("The height of the image is : ",image.shape[0])

# Resizing the mage
resized=cv2.resize(image,(500,300))

if image is None:
  print(f"Unable to load the image {image}")
else:
  cv2.imshow('real_image',image)
  cv2.imshow('resized_image',resized)

  # To rotate the image

  width=image.shape[1]
  height=image.shape[0]
  
  rotation_matrix=cv2.getRotationMatrix2D((width//2,height//2),45,1)   # 45 degree and 1--- anticlockwise direction
  rotated_image=cv2.warpAffine(image,rotation_matrix,(width,width))
  cv2.imshow('Rotated Image',rotated_image)

  #TO flip the image

  flipped_img=cv2.flip(image,0)  # 0 for vertical flip and 1 for horizontal flip
  cv2.imshow('flipped image',flipped_img)


  cv2.waitKey(0)
  cv2.destroyAllWindows()

