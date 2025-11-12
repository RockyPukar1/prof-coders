import cv2 as cv # rename this package

# Reading image and show
image = cv.imread("python.jpeg")

if image is not None: # Check if the image is not empty
  flipped_horizontal = cv.flip(image, 1) # 1 means horizontal
  flipped_vertical = cv.flip(image, 0) # 0 means vertical
  flipped_both = cv.flip(image, -1) # -1 mean flip in both direction

  cv.imshow("Original Image", image)
  cv.imshow("Horizontal Image", flipped_horizontal)
  cv.imshow("Vertical Image", flipped_vertical)
  cv.imshow("Flipped Both Image", flipped_both)

  cv.imwrite("Phase2/flipped_both.jpeg", flipped_both)

  cv.waitKey(0) # Wait for keyboard key to be presse
  cv.destroyAllWindows() # Kills/Closes all the windows
else:
  print("Could not load image")

