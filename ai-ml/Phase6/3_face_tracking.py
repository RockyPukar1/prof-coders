import cv2 as cv
import mediapipe as mp

cap = cv.VideoCapture(0)

mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh()

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
                frame,
                faceLms,
                connections=mpFaceMesh.FACEMESH_TESSELATION,
            )

    cv.imshow("Face Mesh", frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
