import cv2 as cv

image = cv.imread("Phase2/python.jpeg")

if image is not None:
  (h, w) = image.shape[:2]

  center = (w // 2, h // 2)

  Matrix = cv.getRotationMatrix2D(center, 90, 1.0) # anticlockwise rotation
  rotated = cv.warpAffine(image, Matrix, (w, h)) # image, transformation function, (width, height)
  cv.imshow("Original", image)
  cv.imshow("Rotated 90 degrees", rotated)
  
  cv.waitKey(0)
  cv.destroyAllWindows()
else:
  print("Could not load image")