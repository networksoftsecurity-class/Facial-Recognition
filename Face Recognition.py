import cv2
import os
import face_recognition as fr
import numpy as np
import pygame
import ctypes
from ctypes import wintypes

imageList = []

# creates path for images
path = "images/"
myList = os.listdir(path)

# adds images from the path to a list
for img in myList:
    curImg = cv2.imread(f"{path}/{img}")
    imageList.append(curImg)

# returns a list of face encodings (info to id a face)


def findencodings(images):
    encodedlist = []

    print("Encoding images...")

    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = fr.face_encodings(img)[0]
        encodedlist.append(encode)
    return encodedlist

# creates a black window to cover up screen (this is subject to change)


def TurnOff():
    pygame.init()

    screen_size = (640, 480)

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    # puts the black screen on top of other windows
    hwnd = pygame.display.get_wm_info()['window']

    user32 = ctypes.WinDLL("user32")
    user32.SetWindowPos.restype = wintypes.HWND
    user32.SetWindowPos.argtypes = [wintypes.HWND, wintypes.HWND,
                                    wintypes.INT, wintypes.INT, wintypes.INT, wintypes.INT, wintypes.UINT]
    user32.SetWindowPos(hwnd, -1, 0, 0, 0, 0, 0x0001)

    screen.fill((0, 0, 0))

    pygame.display.flip()


# sends the image list through the encoder
encodedListKnown = findencodings(imageList)

# initializes the camera to capture faces
cap = cv2.VideoCapture(0)

while True:
    _, webcam = cap.read()
    imgResized = cv2.resize(webcam, (0, 0), None, 0.25, 0.25)
    imgResized = cv2.cvtColor(imgResized, cv2.COLOR_BGR2RGB)

    # grabs current camera frame and runs it through the encoder
    faceCurFrame = fr.face_locations(imgResized)
    encodeFaceCurFrame = fr.face_encodings(imgResized, faceCurFrame)

    # compares the current encoded camera frame and encoded list
    for encodeFace, faceLoc in zip(encodeFaceCurFrame, faceCurFrame):
        matches = fr.compare_faces(encodedListKnown, encodeFace)
        faceDis = fr.face_distance(encodedListKnown, encodeFace)

        matchIndex = np.argmin(faceDis)

        # checks for a match
        if matches[matchIndex]:
            # if there is a match, remove the black screen
            pygame.quit()
        else:
            # if there is no match, put up a black sreen
            TurnOff()

    # pressing ESC terminates the program
    key = cv2.waitKey(30) & 0xFF
    if key == 27:
        break

    cv2.imshow("webcam", webcam)
