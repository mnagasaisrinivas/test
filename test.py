import cv2
import socket
import struct
import pickle

# Set up UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address
server_address = ('10.192.12.202', 4264)

# Open video capture
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    # Encode frame
    _, buffer = cv2.imencode('.jpg', frame)
    frame_data = pickle.dumps(buffer)

    # Send frame to server
    client_socket.sendto(frame_data, server_address)

    # Receive processed frame from server
    data, _ = client_socket.recvfrom(65536)
    processed_frame_data = pickle.loads(data)

    processed_frame = cv2.imdecode(processed_frame_data, cv2.IMREAD_COLOR)

    # Display the processed frame
    cv2.imshow('Processed Video', processed_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
