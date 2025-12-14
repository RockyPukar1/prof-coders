import cv2 as cv
import mediapipe as mp

capture = cv.VideoCapture(0)

mp.solutions.hands
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
  (result, frame) = capture.read()

  if not result:
    print("Could not read frame")
    break

  # RGB -> Red, Green, Blue -> (255, 0, 0)
  # BGR -> (0, 0, 255)
  imgRGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
  results = hands.process(imgRGB)

  if results.multi_hand_landmarks:
    for handLms in results.multi_hand_landmarks:
      mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)
  
  cv.imshow("Live Camera", frame)
  
  if cv.waitKey(1) & 0xFF == ord("q"):
    print("Quitting...")
    break

capture.release()
cv.destroyAllWindows()