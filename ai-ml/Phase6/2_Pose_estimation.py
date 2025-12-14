import cv2 as cv
import mediapipe as mp

cap = cv.VideoCapture(0)
mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

while True:
  (result, frame) = cap.read()

  if not result:
    print("Could not read frame")
    break

  imgRGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
  results = pose.process(imgRGB)

  if results.pose_landmarks:
    mpDraw.draw_landmarks(frame, results.pose_landmarks, mpPose.POSE_CONNECTIONS)

  cv.imshow("Live camera", frame)
  
  if cv.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv.destroyAllWindows()