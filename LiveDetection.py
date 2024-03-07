import cv2
import os
from datetime import datetime

def detect_faces_live():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Start video capture from the webcam
    cap = cv2.VideoCapture(0)  # 0 is usually the default ID for the built-in webcam
    print("1. To capture & save the image press `c` key\n2. To quit press `q` key.\n")
    
    while True:
        # Read frames from the webcam
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break
        
        # Convert the video frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
        
        # Draw rectangles around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        # Display the frame with detected faces
        cv2.imshow('Face Detection', frame)
        
        # Wait for key press
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            # Quit if 'q' is pressed
            break
        elif key == ord('c'):
            # Ensure the 'captured_images' directory exists
            if not os.path.exists('captured_images'):
                os.makedirs('captured_images')
            
            # Capture and save the image if 'c' is pressed
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            image_path = os.path.join('captured_images', f'capture_{timestamp}.jpg')
            cv2.imwrite(image_path, frame)
            print(f"Image saved as {image_path}")
    
    # Release the VideoCapture object and close display windows
    cap.release()
    cv2.destroyAllWindows()

detect_faces_live()
