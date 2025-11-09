import cv2 as cv # rename this package

# Reading image and show
image = cv.imread("python.jpeg")

if image is not None: # Check if the image is not empty
  (h, w, c) = image.shape
  size = (round(w * 0.5), round(h * 0.5)) # dimensions must be in pixel(integer)
  print(size)
  resized = cv.resize(image, size) # (image, (width, height))

  cv.imwrite("Phase2/resized_python.jpeg", resized)

  cv.imshow("Original Image", image)
  cv.imshow("Resized Image", resized)

  cv.waitKey(0) # Wait for keyboard key to be pressed
  cv.destroyAllWindows() # Kills/Closes all the windows
else:
  print("Could not load image")

