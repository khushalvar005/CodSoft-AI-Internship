import cv2
import os

# Load the pre-trained Haar Cascade face detection model
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

if face_cascade.empty():
    print("Error: Could not load the face detection model.")
    exit()
    

def detect_faces(image_path):
    # Check if the image exists
    if not os.path.exists(image_path):
        print("Error: Image file not found!")
        return

    # Read the image
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Could not read the image.")
        return

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(
            image,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        cv2.putText(
            image,
            "Face Detected",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

    print("Number of faces detected:", len(faces))

    # Display the result
    cv2.imshow("Face Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the output image
    cv2.imwrite("detected_faces.jpg", image)
    print("Output saved as detected_faces.jpg")


def detect_faces_video():
    # Open the default webcam
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Error: Could not access the webcam.")
        return

    print("Starting webcam face detection...")
    print("Press 'q' to quit.")

    while True:
        success, frame = camera.read()

        if not success:
            print("Error: Could not read video frame.")
            break

        # Convert frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        # Draw rectangles around faces
        for (x, y, w, h) in faces:
            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                "Face Detected",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

        cv2.putText(
            frame,
            f"Faces: {len(faces)}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )

        cv2.imshow("Real-Time Face Detection", frame)

        # Press q to quit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()


# Main program
while True:
    print("\n===== AI FACE DETECTION SYSTEM =====")
    print("1. Detect faces in an image")
    print("2. Detect faces using webcam")
    print("3. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        image_path = input("Enter the image path: ").strip()
        detect_faces(image_path)

    elif choice == "2":
        detect_faces_video()

    elif choice == "3":
        print("Thank you for using the Face Detection System!")
        break

    else:
        print("Invalid choice. Please select 1, 2, or 3.")