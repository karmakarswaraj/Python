import cv2
import dlib

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load the pre-trained age and gender classification model
age_gender_model = dlib.face_recognition_model_v1("age_gender_model.dat") #PROVIDE A DATA TO TRAIN

# Initialize the camera (you may need to change the camera index)
camera = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    ret, frame = camera.read()

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    # For each detected face, estimate the age
    for (x, y, w, h) in faces:
        face_roi = gray[y:y+h, x:x+w]
        
        # Use dlib to estimate age
        face_descriptor = age_gender_model.compute_face_descriptor(frame, face_roi)
        age = int(face_descriptor[0])

        # Draw rectangles around detected faces and display age
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, f'Age: {age}', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display the frame with detected faces and estimated age
    cv2.imshow('Age Estimation', frame)

    # Exit the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the OpenCV window
camera.release()
cv2.destroyAllWindows()
