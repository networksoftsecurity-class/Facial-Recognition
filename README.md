# Facial-Recognition
This is a face authentication program that can run on Ubuntu.

You can clone our repository here: 
https://github.com/networksoftsecurity-class/Facial-Recognition

Or see attached zip filed.

Whats included:
data_set/ <- directory
LBPH_model/ <- directory
haarcascade_frontalface_default.xml
create_data.py
train_recognizer.py
recognizer.py
runGui.py

Required:
webcam

Install to run (terminal): 
Video4Linux:

	#install
		sudo apt get install v4l-utils
python3:

	# check if already installed:
		python --version

	# update repository
		sudo apt update

	# deadsnakes PPA to install python
		sudo awordpt-get install software-properties-common
		sudo add-apt-repository ppa:deadsnakes/ppa
		sudo apt-get update

	# install python3
		sudo apt-get install python3.8
	
pip3: 

	# update repository
		sudo apt update

	# install pip
		sudo apt install python3-pip

	# verify install
	pip3 --version

opencv:

	# install opencv
		sudo apt install python3-opencv

	# Required dependencies
		sudo apt install build-essential cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev

numpy:

	# install 
		sudo apt-get install python3-numpy
pillow
	# install
		sudo pip3 install Pillow

tkinter
	# install
		sudo apt install python3-tk

Now to run our program all you need to run is the runGUI.py file.

First in the terminal we need to check which webcam our device is using
In our terminal type:
v4l2-ctl --list-devices

This should output something similar to:
Integrated Camera (usb-0000:00:1a.0-1.6):
        /dev/video0
You need to note the first video being used, default will be "video0"
but if its another we need to change the code in the create_data.py and recognizer.py files.
The line that reads "webcam = cv.VideoCapture(0);"

Open the terminal to where the directory is located.
cd /Facial-Recognition

Now run by typing this in the terminal
python3 runGUI.py

This opens a simple GUI.
Start with "Create" - will display a webcam that begins to capture images, creating our data set.
Second is "Train" - wait a moment will our model is being trained with the created data_set.
Final is "Authenticate" - which will unlock/lock the device if the face is recognized. 
