import cv2 as cv # rename this package

# Reading image and show
image = cv.imread("python.jpeg")

if image is not None: # Check if the image is not empty
  (h, w, c) = image.shape
  center = (w // 2, h / 2) # width, height
  Matrix = cv.getRotationMatrix2D(center, -270, 1.0) # center, angle, scaling
  rotated = cv.warpAffine(image, Matrix, (w, h)) # image, transformation function, (width, height)

  cv.imshow("Original", image)
  cv.imshow("Rotated", rotated)
  cv.waitKey(0) # Wait for keyboard key to be pressed
  cv.destroyAllWindows() # Kills/Closes all the windows
else:
  print("Could not load image")

