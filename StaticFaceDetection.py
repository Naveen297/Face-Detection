import cv2

def detect_faces(image_path):
    # Load the pre-trained Haar Cascade model for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Read the image
    img = cv2.imread(image_path)
    # Convert the image to grayscale (required for face detection)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5)

    # Draw rectangles around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display the image with detected faces
    cv2.imshow('Face Detected', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Replace 'path_to_your_image.jpg' with the path to the image you want to process
image_path = 'Images\img4.jpg'
detect_faces(image_path)
