import cv2
import mediapipe as mp
import pyautogui

# initialize video capture and hand detection of mediapipe
capture = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)

# create a frame for the detected hand so that you can see when the mediapipe is detecting my hand.
mp_drawing = mp.solutions.drawing_utils

# a loop where each frame can be processed and edited. this needed by mediapipe.
while True:
    ret, frame = capture.read()
    if not ret:
        break

    # convert each frame to RGB because mediapipe needs and only works with rgb frames.
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # finally process the frame using mediapipe
    results = hands.process(frame_rgb)

    # if there is a hand detected we can use the landmarks in the hand to control the volume of the computer.
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # This will be the code for what controls the volume and in this code i'll use the index to control and the thumb as the base.
        # but first we have to identify the landmarks of my index and tumb.
        tip_index = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
        tip_thumb = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y

        # the step is to make the logic (what does these landmarks mean)
        # if tip_index.y < tip_thumb.y:
        #     hand_direction = "up"
        # elif tip_thumb.y < tip_index.y:
        #     hand_direction = "down"
        # else:
        #     hand_direction = "else"
 
        # # next thing to do is to now attach commands to the direction of my finger.
        # if hand_direction == "up":
        #     pyautogui.press("volumeup")
        # elif hand_direction == "down":
        #     pyautogui.press("volumedown")

        if tip_index < tip_thumb:
            pyautogui.press("volumeup")
        elif tip_thumb < tip_index:
            pyautogui.press("volumedown")

        # to show the frame so that the hand tracking is shown.
    cv2.imshow("Hand Tracking", frame)

    # this is for exiting the loop and add clean up code
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
# errorrrr about the mediapipe solved 
# another error about .y no attribute P.S. Solved i removed the .y it isnt needed.