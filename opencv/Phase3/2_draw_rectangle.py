import cv2 as cv

image = cv.imread("Phase_/python.jpeg")

if image is not None:
  pt1 = (50, 50)
  pt2 = (250, 250)
  color = (0, 0, 255)
  thickness = 3
  
  cv.rectangle(image, pt1, pt2, color, thickness)
  cv.imshow("Image focusing rectangle", image)
  cv.waitKey(0)
  cv.destroyAllWindows()
else:
  print("Could not load image")