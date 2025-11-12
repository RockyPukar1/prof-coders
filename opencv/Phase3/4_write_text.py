# image, text, origination(x, y), font, fontScale, color, thickness
import cv2 as cv

image = cv.imread("Phase3/python.jpeg")

if image is not None:
  cv.putText(image, "Hello Python Programmers", (20, 20), cv.FONT_HERSHEY_SIMPLEX, 0.3, (0, 255, 255), 2)
  cv.imshow("Adding text over image", image)
  
  cv.waitKey(0)
  cv.destroyAllWindows()
else:
  print("Could not load image")