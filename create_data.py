import cv2 as cv
import numpy
import os

#create a video capture object
webcam = cv.VideoCapture(2);

#cascadeClassifier class's instance for obj detection
detect = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

#capture images from webcam + assign a label which will be saved in our data_set
label = input('id: ');
count = 0

#set the path to where it will save 
path_name = os.path.join("data_set/User." + label + "." + str(count) + ".jpg")


#loop to capture images
while count < 50:
    
    _,frame = webcam.read()

    #convert BGR to grayscale since its easier to read faces using grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    #segreagte images through brightness of pixel (black/gray/white)
    #detect the face in the img using CascadeClassifier (comes with opencv)
    #gray: input img, 1.3: img size reduced at each scale (inc likelihood of finding matching features)
    #5: how many neighbors, quality of detected faces
    faces = detect.detectMultiScale(gray,1.3,5)

    #when faces are found, return positions of face as a rectangle x/y: corner w/h: width n height
    for(x,y,w,h) in faces:

        #increment count
        count += 1

        #create rectangle to outline face
        cv.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)

        #save the frame captured in path name
        cv.imwrite("data_set/" + label + '.' + str(count) + ".jpg", gray[y:y+h, x:x+w])

        #creates a window and displays our webcam
        cv.imshow('frame', frame)

        #delay 50ms 
        if cv.waitKey(50):
            break

        elif count > 50:
            break
webcam.release()
cv.destroyAllWindows()
