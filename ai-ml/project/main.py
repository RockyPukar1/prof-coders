import cv2
import mediapipe as mp

# Load glasses PNG (must have transparency)
glasses = cv2.imread("project/glasses.png", cv2.IMREAD_UNCHANGED)
print("Shape:", glasses.shape)
print("Top-left pixel:", glasses[0,0])

# Mediapipe face mesh
mp_face = mp.solutions.face_mesh
face_mesh = mp_face.FaceMesh(static_image_mode=False,
                             max_num_faces=1,
                             refine_landmarks=True,
                             min_detection_confidence=0.5,
                             min_tracking_confidence=0.5)

def overlay_transparent(background, overlay, x, y, w, h):
    overlay_resized = cv2.resize(overlay, (w, h))

    if overlay_resized.shape[2] < 4:
        raise ValueError("Overlay image must have alpha channel (RGBA)")

    b,g,r,a = cv2.split(overlay_resized)
    overlay_rgb = cv2.merge((b,g,r))
    mask = a / 255.0

    bh, bw = background.shape[:2]
    oh, ow = overlay_rgb.shape[:2]

    # Check boundaries
    if x < 0: x = 0
    if y < 0: y = 0
    if x+ow > bw: ow = bw - x
    if y+oh > bh: oh = bh - y
    if ow <= 0 or oh <= 0:
        return background

    alpha = mask[0:oh, 0:ow]
    for c in range(3):
        background[y:y+oh, x:x+ow, c] = (
            overlay_rgb[0:oh, 0:ow, c] * alpha +
            background[y:y+oh, x:x+ow, c] * (1 - alpha)
        )
    return background

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:
        print("Face detected")
        lm = results.multi_face_landmarks[0].landmark

        # Eye landmarks (these give good glasses placement)
        left_eye_outer = lm[33]
        right_eye_outer = lm[263]

        # Convert to pixel coords
        x1 = int(left_eye_outer.x * w)
        y1 = int(left_eye_outer.y * h)
        x2 = int(right_eye_outer.x * w)
        y2 = int(right_eye_outer.y * h)

        # Calculate glasses width
        glasses_width = int(abs(x2 - x1) * 1.8)
        glasses_height = int(glasses_width * glasses.shape[0] / glasses.shape[1])

        # Position: centered between eyes
        center_x = int((x1 + x2) / 2)
        center_y = int((y1 + y2) / 2)

        top_left_x = center_x - glasses_width // 2
        top_left_y = center_y - glasses_height // 2

        # Bounds check
        if top_left_x > 0 and top_left_y > 0:
            print("Overlaying glasses")
            try:
                frame = overlay_transparent(
                    frame, glasses,
                    top_left_x, top_left_y,
                    glasses_width, glasses_height
                )
            except:
                pass

    cv2.imshow("Virtual Glasses", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
