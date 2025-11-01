import cv2 as cv

image = cv.imread("Phase1/python.jpeg")

if image is not None:
  (h, w, c) = image.shape
  print(f"Image Loaded:\nHeight: {h}\nWidth: {w}\nChannels: {c}")
else:
  print("Could not load image")