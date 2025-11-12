import cv2 as cv

image = cv.imread("Phase3/python.jpeg")

if image is not None:
  (h, w, c) = image.shape
  pt1 = (50, 50)
  pt2 = (250, 250)
  color = (0, 0, 255)
  thickness = 3
  center = (w // 2, h // 2)
  radius = 50
  
  cv.circle(image, center, 50, color, thickness) # image, center, radius, color, thickness
  cv.imshow("Image focusing circle", image)
  cv.waitKey(0)
  cv.destroyAllWindows()
else:
  print("Could not load image")