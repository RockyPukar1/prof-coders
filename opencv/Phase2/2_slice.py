import cv2 as cv

image = cv.imread("Phase2/python.jpeg")

if image is not None:
  cropped = image[100:200, 50:150]

  cv.imshow("Original", image)
  cv.imshow("Cropped", cropped)
  cv.waitKey(0)
  cv.destroyAllWindows()
else:
  print("Could not load image")