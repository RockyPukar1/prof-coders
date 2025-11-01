import cv2 as cv

image = cv.imread("Phase2/python.jpeg")

if image is not None:
  # replace this
  flipped_horizontal = cv.flip(image, 1) # 1 means horizontal flip
  flipped_vertical = cv.flip(image, 0) # 0 means vertical flip
  flipped_both = cv.flip(image, -1) # -1 means flip in both direction

  cv.imshow("Original", image)
  cv.imshow("Flipped Horizontal", flipped_horizontal)
  cv.imshow("Flipped Vertical", flipped_vertical)
  cv.imshow("Flipped Both", flipped_both)
  
  cv.waitKey(0)
  cv.destroyAllWindows()
else:
  print("Could not load image")