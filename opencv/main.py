import cv2 as cv

image = cv.imread("Phase_/python.jpeg")

if image is not None:
  # replace this

  cv.waitKey(0)
  cv.destroyAllWindows()
else:
  print("Could not load image")