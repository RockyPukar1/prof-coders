import cv2 as cv

camera = cv.VideoCapture("my_video.mp4")

while True:
  (result, frame) = camera.read()

  if not result:
    print("Could not read frame")
    break

  cv.imshow("Webcam", frame)
  
  print(ord("q"))
  if cv.waitKey(1) & 0xFF == ord("q"):
    print("Quitting....")
    break

camera.release()
cv.destroyAllWindows()