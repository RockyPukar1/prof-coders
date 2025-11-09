import cv2 as cv

image = cv.imread("Phase3/python.jpeg")

if image is not None:
  pt1 = (50, 100) # (x, y)
  pt2 = (300, 100) # (x, y)
  color = (255, 0, 0) # (Blue, Green, Red)
  thickness = 4
  
  cv.line(image, pt1, pt2, color, thickness) # image, starting point, end point, color, thickness
  
  cv.imshow("Line Drawing", image)
  cv.waitKey(0)
  cv.destroyAllWindows()
else:
  print("Could not load image")