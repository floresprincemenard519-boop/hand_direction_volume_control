import cv2
import mediapipe as mp
import pyautogui

capture = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

while True:
    ret, frame = capture.read()
    
    if not ret:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        tip_index = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
        tip_thumb = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y

        if tip_index < tip_thumb:
            pyautogui.press("volumeup")
        elif tip_thumb < tip_index:
            pyautogui.press("volumedown")

    cv2.imshow("Hand Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
