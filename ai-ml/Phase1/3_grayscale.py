import cv2 as cv

image = cv.imread("Phase1/new_python.jpeg")

if image is not None:
  print(cv.COLOR_BGR2GRAY)
  gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

  cv.imshow("Grayscale Phase 1", gray_image)

  cv.waitKey(0)
  cv.destroyAllWindows()

  cv.imwrite("Phase1/gray_python.jpeg", gray_image)
else:
  print("Image not loaded")