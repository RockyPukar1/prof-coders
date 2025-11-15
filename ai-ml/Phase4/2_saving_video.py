import cv2 as cv

camera = cv.VideoCapture(0)

frame_width = int(camera.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv.CAP_PROP_FRAME_HEIGHT))

frame_size = (frame_width, frame_height)

codec = cv.VideoWriter.fourcc(*"XVID")

recorder = cv.VideoWriter("my_video.mp4", codec, 20, frame_size) # filename, fourcc, fps(frame per image), frameSize(frame_width, frame_height)

while True:
  (result, frame) = camera.read()

  if not result:
    print("Could not load frame")
    break

  recorder.write(frame)
  cv.imshow("Recording live", frame)

  if cv.waitKey(1) & 0xFF == ord("q"):
    print("Quitting....")
    break

camera.release()
