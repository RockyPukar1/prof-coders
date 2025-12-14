import cv2 as cv
import mediapipe as mp
import time

cap = cv.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
pTime = 0 # previous time
cTime = 0 # current time

while True:
  result, frame = cap.read()
  
  if not result:
    print("Could not read frame")
    break
  
  (h, w, c) = frame.shape

  imgRGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
  results = hands.process(imgRGB)

  if results.multi_hand_landmarks:
    for handLms in results.multi_hand_landmarks:
      for id, lm in enumerate(handLms.landmark):
        (cx, cy) = (int(lm.x * w), int(lm.y * h))
        if id % 4 == 0:
          cv.circle(frame, (cx, cy), 7, (255, 0, 255), cv.FILLED)
        
      mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)

  cTime = time.time()
  fps = 1/(cTime - pTime)
  pTime = cTime

  cv.putText(frame, str(int(fps)), (10, 70), cv.FONT_HERSHEY_DUPLEX, 3, (255, 0, 255), 3)
  cv.imshow("Image", frame)

  if cv.waitKey(1) & 0xFF == ord("q"):
    break

cap.release() # close camera
cv.destroyAllWindows()