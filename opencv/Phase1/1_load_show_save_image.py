import cv2 as cv
image = cv.imread("Phase1/python.jpeg") # load and read the image

if image is not None:
  cv.imshow("Image showing", image) # open the window to show image
  cv.waitKey(0) # wait for a key to be pressed
  cv.destroyAllWindows() # close the window

  # Save new image
  success = cv.imwrite("Phase1/new_python.jpeg", image)
  if success:
    print("Image saved successfully as 'new_python.jpeg'")
  else:
    print("Failed to save image")
else:
  print("Could not load image")
