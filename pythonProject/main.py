import cv2

# Test the first camera index
cap = cv2.VideoCapture(0)  # Change to 1, 2, etc., if 0 doesn't work

if not cap.isOpened():
    print("Unable to access the camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break
    cv2.imshow('Webcam', frame)
    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

cap.release()
cv2.destroyAllWindows()
