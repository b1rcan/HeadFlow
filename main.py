import cv2
import mediapipe as mp
import pyautogui
import time

 
DEADZONE = 3.2
STOP_THRESHOLD = 1.2
SENSITIVITY = 4.0
SMOOTHING_X = 0.1
SMOOTHING_Y = 0.1

pyautogui.FAILSAFE = False

 
EYE_CLOSED = 0.20
CLICK_FRAMES = 2
HOLD_FRAMES = 8

left_counter = 0
right_counter = 0
left_holding = False
click_lock = False

# ====================
# BAŞLANGIÇ KALİBRASYON
# ====================
CALIBRATION_TIME = 2.0
calibration_start = time.time()
calibrated = False
yaw_samples = []
pitch_samples = []

# ====================
# MEDIAPIPE
# ====================
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    refine_landmarks=True
)

cap = cv2.VideoCapture(0)

neutral_yaw = None
neutral_pitch = None
smooth_x = 0.0
smooth_y = 0.0
prev_dyaw = 0.0
prev_dpitch = 0.0

# ====================
# YARDIMCI FONKSİYON
# ====================
def eye_ear(landmarks, ids):
    eye = [landmarks.landmark[i] for i in ids]
    h = abs(eye[0].x - eye[3].x)
    v = (abs(eye[1].y - eye[5].y) + abs(eye[2].y - eye[4].y)) / 2
    return v / h

LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]

# ====================
# ANA DÖNGÜ
# ====================
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:
        lm = results.multi_face_landmarks[0]

        nose = lm.landmark[1]
        yaw = (nose.x - 0.5) * 100
        pitch = (nose.y - 0.5) * 100

        # --------------------
        # BAŞLANGIÇ KALİBRASYON
        # --------------------
        if not calibrated:
            yaw_samples.append(yaw)
            pitch_samples.append(pitch)

            cv2.putText(
                frame,
                "Hold your natural posture...",
                (30, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 255),
                2
            )

            if time.time() - calibration_start >= CALIBRATION_TIME:
                neutral_yaw = sum(yaw_samples) / len(yaw_samples)
                neutral_pitch = sum(pitch_samples) / len(pitch_samples)
                calibrated = True

            cv2.imshow("HeadFlow", frame)
            if cv2.waitKey(1) & 0xFF == 27:
                break
            continue

        # --------------------
        # KAFA → MOUSE
        # --------------------
        dyaw = yaw - neutral_yaw
        dpitch = pitch - neutral_pitch

        move_x = 0.0
        move_y = 0.0

        if abs(dyaw) > DEADZONE:
            move_x = dyaw * SENSITIVITY
        if abs(dpitch) > DEADZONE:
            move_y = dpitch * SENSITIVITY

        # YÖN DEĞİŞİMİ → ANINDA DUR
        if dyaw * prev_dyaw < 0:
            smooth_x = 0.0
        if dpitch * prev_dpitch < 0:
            smooth_y = 0.0

         
        if abs(dyaw) < STOP_THRESHOLD:
            smooth_x = 0.0
        else:
            smooth_x = smooth_x * SMOOTHING_X + move_x * (1 - SMOOTHING_X)

        if abs(dpitch) < STOP_THRESHOLD:
            smooth_y = 0.0
        else:
            smooth_y = smooth_y * SMOOTHING_Y + move_y * (1 - SMOOTHING_Y)

        if abs(smooth_x) > 0.1 or abs(smooth_y) > 0.1:
            pyautogui.moveRel(smooth_x, smooth_y, duration=0)

        prev_dyaw = dyaw
        prev_dpitch = dpitch

        # --------------------
        # BLINK → CLICK
        # --------------------
        left_ear = eye_ear(lm, LEFT_EYE)
        right_ear = eye_ear(lm, RIGHT_EYE)

        left_closed = left_ear < EYE_CLOSED
        right_closed = right_ear < EYE_CLOSED

        if left_closed and right_closed:
            left_counter = 0
            right_counter = 0
            click_lock = True
        else:
            if left_closed:
                left_counter += 1
                if left_counter >= HOLD_FRAMES and not left_holding:
                    pyautogui.mouseDown()
                    left_holding = True
                    click_lock = True
            else:
                if left_holding:
                    pyautogui.mouseUp()
                    left_holding = False
                elif CLICK_FRAMES <= left_counter < HOLD_FRAMES and not click_lock:
                    pyautogui.click(button="left")
                left_counter = 0

            if right_closed:
                right_counter += 1
            else:
                if CLICK_FRAMES <= right_counter < HOLD_FRAMES and not click_lock:
                    pyautogui.click(button="right")
                right_counter = 0

        if not left_closed and not right_closed:
            click_lock = False

    # --------------------
    # KLAVYE (RECENTER)
    # --------------------
    key = cv2.waitKey(1) & 0xFF

    if key == 32:  # SPACE
        neutral_yaw = yaw
        neutral_pitch = pitch
        smooth_x = 0.0
        smooth_y = 0.0

    if key == 27:
        break

    cv2.imshow("HeadFlow", frame)

cap.release()
cv2.destroyAllWindows()
