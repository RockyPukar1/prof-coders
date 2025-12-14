import cv2 as cv
import mediapipe as mp
import time

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()
pTime = 0 # previous time
cTime = 0 # current time

cap = cv.VideoCapture(0)

while True:
  result, frame = cap.read()

  if not result:
    print("Could not read frame")
    break
  
  imgRGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
  results = pose.process(imgRGB)

  if results.pose_landmarks:
    mpDraw.draw_landmarks(frame, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
    for (id, lm) in enumerate(results.pose_landmarks.landmark):
      (h, w, c) = frame.shape
      (cx, cy) = int(lm.x * w), int(lm.y * h)
  

  cTime = time.time()
  fps = 1/(cTime - pTime)
  pTime = cTime

  cv.putText(frame, str(int(fps)), (10, 70), cv.FONT_HERSHEY_DUPLEX, 3, (255, 0, 255), 3)
  cv.imshow("Image", frame)
  
  if cv.waitKey(1) & 0xFF == ord("q"):
    break

cap.release() # close camera
cv.destroyAllWindows()