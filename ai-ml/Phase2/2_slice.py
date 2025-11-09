import cv2 as cv # rename this package

# Reading image and show
image = cv.imread("python.jpeg")

if image is not None: # Check if the image is not empty
  (h, w, c) = image.shape
  print(h, w)
  cropped = image[20:100, 30:300] # height, width

  cv.imshow("Original Image", image)
  cv.imshow("Cropped Image", cropped)

  cv.imwrite("Phase2/cropped_python.jpeg", cropped)

  cv.waitKey(0) # Wait for keyboard key to be pressed
  cv.destroyAllWindows() # Kills/Closes all the windows
else:
  print("Could not load image")

