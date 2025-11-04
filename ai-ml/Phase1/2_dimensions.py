import cv2 as cv

image = cv.imread("Phase1/new_python.jpeg")

if image is not None:
  (height, width, channel) = image.shape
  print(f"Height: {height}, Width: {width}, Channel: {channel}")
else:
  print("Image could not load")
  
