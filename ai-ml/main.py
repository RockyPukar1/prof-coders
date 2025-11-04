import cv2 as cv # rename this package

# Reading image and show
image = cv.imread("python.jpeg")

if image is not None: # Check if the image is not empty
  # replace this

  cv.waitKey(0) # Wait for keyboard key to be pressed
  cv.destroyAllWindows() # Kills/Closes all the windows
else:
  print("Could not load image")

