import mediapipe as mp
import cv2
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
def detect_gesture(frame):
    # Convert frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            thumb_tip = hand_landmarks.landmark[4]
            index_tip = hand_landmarks.landmark[8]
            middle_tip = hand_landmarks.landmark[12]
            ring_tip = hand_landmarks.landmark[16]
            pinky_tip = hand_landmarks.landmark[20]
            # Example gestures
            if index_tip.y < middle_tip.y < ring_tip.y < pinky_tip.y:
                return "U"  # Rotate up
            elif thumb_tip.y > index_tip.y > middle_tip.y > ring_tip.y > pinky_tip.y:
                return "D"  # Rotate down
            elif thumb_tip.x < index_tip.x and middle_tip.x < ring_tip.x:
                return "R"  # Rotate right
            elif thumb_tip.x > index_tip.x and middle_tip.x > ring_tip.x:
                return "L"  # Rotate left
    return None
