import face_recognition
import cv2   # this library is for camera
import numpy as np
import os
import pyttsx3  #this library is used for sheech module


####Code for voice alert starts here####
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
####Code for voice alert ends here####

list=[""]  #list name or id. no. to detect and speak

path = "./train/" #Declearing path for to train the model

known_names = []
known_name_encodings = []


cap = cv2.VideoCapture(0)
            
images = os.listdir(path)


for _ in images:
    image = face_recognition.load_image_file(path + _)
    image_path = path + _
    encoding = face_recognition.face_encodings(image)[0]
    known_name_encodings.append(encoding)
    known_names.append(os.path.splitext(os.path.basename(image_path))[0].capitalize())

print(known_names) #To print names in the terminal

while True:
    
    _, image = cap.read()
    
    
    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)
    


    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_name_encodings, face_encoding)
        name = ""

        face_distances = face_recognition.face_distance(known_name_encodings, face_encoding)
        best_match = np.argmin(face_distances)

        

        if matches[best_match]:
            name = known_names[best_match]
            if name in list: #Checking whether the detected person is in the list or not
                speak("criminal detected")
   
        else:
            name = "unknown"      

        #Code for showing rectangle and text after detecting face
        cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(image, (left, bottom - 25), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(image, name, (left + 6, bottom - 6), font, 0.8, (255, 255, 255), 1)
      
     
    cv2.imshow("Result", image)
    #cv2.imwrite("./output.jpg", image)      #To save output
    
    if cv2.waitKey(4) & 0xFF == ord('q'):
        break
   
cap.release()
cv2.destroyAllWindows()
