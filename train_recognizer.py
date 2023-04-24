import cv2 as cv
import os
import numpy
from PIL import Image

#initialize recognizer n face detector
#recoginiton method: LPPH = histograms of local binary patterns
recognize = cv.face.LBPHFaceRecognizer_create()
detect = cv.CascadeClassifier("haarcascade_frontalface_default.xml");

#load in the images from our created set
def getData(path):
    
    #create an empty list to save img n id data
    face_list=[]
    label_list=[]

    #load the imgs
    #get path
    img_path = [os.path.join('data_set', f) for f in os.listdir('data_set')]

    for img in img_path:
        #cvt to graxy
        gray_image = Image.open(img).convert('L')

        #cvt to numpy array
        numpy_image = numpy.array(gray_image, 'uint8')

        #get label (id)
        label = int(os.path.split(img)[-1].split(".")[0])
        #print(name)
        
        #extract face from images
        data_face = detect.detectMultiScale(numpy_image)

        for(x,y,w,h) in data_face:
            face_list.append(numpy_image[y:y+h, x:x+w])
            label_list.append(label)
                   
    return face_list, label_list

faces, names = getData('data_set')

#train with these two lists
recognize.train(faces, numpy.array(names))

#generate a file containing histograms and labels
recognize.save('LBPH_model/model.yml')
