import cv2 as cv

# Reading image and show
image = cv.imread("python.jpeg")

if image is not None:
  cv.imshow("Python Image", image) # window_name, image

  cv.waitKey(0)
  cv.destroyAllWindows()

  success = cv.imwrite("Phase1/new_python.jpeg", image) # location and name of new image, image
  if success:
    print("Image saved successfully as 'new_python.jpeg'")
  else:
    print("Failed to save image")
else:
  print("Could not load image")

