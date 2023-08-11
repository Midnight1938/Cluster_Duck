import cv2
import mediapipe as mp

# Define the MediaPipe hands model and a drawing utility function
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Define the smiley emoji image
smiley = cv2.imread('smiley.png')

# Load the webcam and start processing frames
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        # Read a frame from the webcam
        success, image = cap.read()
        if not success:
            break

        # Flip the image horizontally for a mirror effect
        image = cv2.flip(image, 1)

        # Convert the image to RGB and process it with MediaPipe
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image_rgb)

        # Draw landmarks on the hand in the image
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Get the coordinates of the index finger tip
                index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                x, y = int(index_finger_tip.x * image.shape[1]), int(index_finger_tip.y * image.shape[0])

                # Display the smiley emoji on the index finger tip
                emoji_height, emoji_width = smiley.shape[:2]
                y -= emoji_height
                x -= int(emoji_width / 2)
                image[y:y+emoji_height, x:x+emoji_width] = smiley

        # Display the image with the smiley emoji
        cv2.imshow('Smiley on Index Finger', image)
        if cv2.waitKey(5) & 0xFF == 27:
            break

# Release resources
cap.release()
cv2.destroyAllWindows()
