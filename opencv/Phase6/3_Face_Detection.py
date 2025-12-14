import cv2 as cv
import mediapipe as mp

cap = cv.VideoCapture(0)

mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(
  static_image_mode=False,
  max_num_faces=1,
  refine_landmarks=True,
  min_detection_confidence=0.5,
  min_tracking_confidence=0.5
)

mpDraw = mp.solutions.drawing_utils
drawSpec = mpDraw.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1)

while True:
  success, frame = cap.read()
  if not success:
    break

  imgRGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
  results = faceMesh.process(imgRGB)

  if results.multi_face_landmarks:
    for faceLms in results.multi_face_landmarks:
      mpDraw.draw_landmarks(
        image=frame,
        landmark_list=faceLms,
        connections=mpFaceMesh.FACEMESH_TESSELATION,
        landmark_drawing_spec=drawSpec,
        connection_drawing_spec=drawSpec
      )

  cv.imshow("Face Mesh", frame)

  if cv.waitKey(1) & 0xFF == ord('q'):
      break

cap.release()
cv.destroyAllWindows()
