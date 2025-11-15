import cv2 as cv

camera = cv.VideoCapture(0)

frame_width = int(camera.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv.CAP_PROP_FRAME_HEIGHT))

codec = cv.VideoWriter.fourcc(*"XVID")
recorder = cv.VideoWriter("my_video.mp4", codec, 20, (frame_width, frame_height)) # file name, fourcc, fps, frameSize(frame_width, frame_height)

while True:
  (success, frame) = camera.read()

  if not success:
    break

  recorder.write(frame)
  cv.imshow("Recording live", frame)

  if cv.waitKey(1) & 0xFF == ord("q"):
    break

camera.release()
recorder.release()
cv.destroyAllWindows()