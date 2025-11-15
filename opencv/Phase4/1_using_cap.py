import cv2 as cv

cap = cv.VideoCapture(0)

while True:
  (ret, frame) = cap.read() # ret=True/False frame=image

  if not ret:
    print("Could not read frame")
    break

  cv.imshow("Webcam Feed", frame)

  if cv.waitKey(1) & 0xFF == ord("q"):
    print("Quitting....")
    break

cap.release() # close camera
cv.destroyAllWindows()