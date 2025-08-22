import cv2

# Load Haarcascade Properly:-
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Read the Input Image:-
image = cv2.imread(
    r"d:\Learning Python\02_Day2_Application_of_Python\Face_Recognition\1.jpg"
)

# Check If Image Loaded Successfully:-
if image is None:
    print("Error: Image not found!")
    exit()

# Resize The Image:-
img = cv2.resize(image, None, fx=0.3, fy=0.3)

# Convert To Grayscale:-
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect Faces
faces = face_cascade.detectMultiScale(imgGray, 1.2, 5)

# Draw Rectangle Around Faces:-
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Show Output:-
cv2.imshow("img", img)
cv2.waitKey()
cv2.destroyAllWindows()