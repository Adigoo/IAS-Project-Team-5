import numpy as np
import cv2
import gdown
import pickle
 
def detect_face(img):
    try: 
        face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    except:
        url = 'https://drive.google.com/u/0/uc?id=1950zA7knjNWh7nZN_YrqxgELfe1tJOCY&export=download'
        output = 'haarcascade_frontalface_default.xml'
        gdown.download(url, output, quiet=False)
    try:
        eye_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    except:
        url = 'https://drive.google.com/u/0/uc?id=1tPcEkOA4oZ4LlE8sNy3mO2np42ETuICy&export=download'
        output = 'haarcascade_eye.xml'
        gdown.download(url, output, quiet=False)
    img = cv2.imread(img)
    print(type(img),img.shape)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.05, 3)
    if len(faces) == 0:
        print("No Face Found")
        return 0

    for (x,y,w,h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_classifier.detectMultiScale(roi_gray)
        if len(eyes) == 0:
            return 0
        
        return 1
    return 0


# img = 'g4.jpg'
# print(detect_face(img))
with open ("model.pkl","wb") as handle:
    pickle.dump(detect_face,handle)