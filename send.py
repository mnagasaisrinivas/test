import cv2
import requests
import numpy as np

# Configuration
api_url = 'https://5000-01j4k3cgnem1a8kxf0mmxkpyw2.cloudspaces.litng.ai/upload_video'  # Replace with the actual API endpoint

# Open video capture
cap = cv2.VideoCapture(0)  # 0 for default webcam

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break

    # Encode the frame
    encoded, buffer = cv2.imencode('.jpg', frame)
    frame_data = buffer.tobytes()

    # Send the frame data to the server via POST request
    response = requests.post(api_url, files={'frame': frame_data})

    if response.status_code != 200:
        print("Failed to send frame")

    # Optional: Display the frame locally
    cv2.imshow('Sending Video', frame)

    # Break loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
