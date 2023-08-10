import cv2
def detect_smiles(image_path):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in faces:
        roi_gray = gray_image[y:y + h, x:x + w]
        smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.8, minNeighbors=20)
        for (ex, ey, ew, eh) in smiles:
            cv2.rectangle(image[y:y + h, x:x + w], (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 2)
    cv2.imshow('Smile Detection', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == "__main__":
    image_path = 'C:\\Users\\91984\\Pictures\\Screenshots\\Screenshot 2023-08-10 084737.png'
    detect_smiles(image_path)
