import cv2
import mediapipe as mp
import pyautogui

# initialize video capture and hand detection of mediapipe
capture = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)

# create a frame or the detected hand so that you can see when the mediapipe is detecting my hand.
mp_drawing = mp.solutions.drawing_utils

