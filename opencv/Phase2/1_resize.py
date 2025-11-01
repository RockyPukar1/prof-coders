import cv2 as cv

image = cv.imread("Phase2/python.jpeg")
# width, height

if image is not None:
  print("Image loaded")

  resized = cv.resize(image, (300, 300))

  cv.imshow("Original image", image)
  cv.imshow("Resized image", resized)

  cv.imwrite("Phase2/resized_output.jpeg", resized);

  cv.waitKey(0)
  cv.destroyAllWindows()
else:
  print("Could not load image")