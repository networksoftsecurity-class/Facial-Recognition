import cv2 as cv
import numpy
import os

#load recognizer
recognize = cv.face.LBPHFaceRecognizer_create()
recognize.read('trainner/trainner.yml')
#create cascade
face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml");

webcam = cv.VideoCapture(2)

#create recognized users paired with index ids
user_list = ["", "Anna"]

#loop to capture frames
while True:
    
    _,frame = webcam.read()

    #cvt to gray
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)

    for(x,y,w,h) in faces:

        #creating rectangle to outline face
        cv.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)

        #labels and confidence index, predict() which takes portions of a face and returns the two
        name, confidence = recognize.predict(gray[y:y+h, x:x+w])

        # 0 = perfect match
        #  we use the confidence to determine what id to give and whether to lock or unlock the device
        # we will use terminal commands to lock/unlock
        if confidence < 80:
            os.popen('gnome-screensaver-command --deactivate')
            name = user_list[name]

        elif (len(faces) == 0):
            os.popen('gnome-screensaver-command --lock')
        else:
            os.popen('gnome-screensaver-command --lock')
            name = "unkown"
        
        #label our window with the id of the face detected         
        cv.putText(frame, str(name), (x, y+h), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv.imshow('frame', frame)
    
    if cv.waitKey(10) & 0xFF==ord('q'):
        break
    
webcam.release()
cv.destroyAllWindows()   
