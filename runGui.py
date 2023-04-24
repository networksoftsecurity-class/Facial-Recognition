import sys
import os
from tkinter import *

window = Tk()

window.title("Facial Authentication")
window.geometry('550x200')

def run():
    os.system('python3 create_data.py')
    
btn = Button(window, text="Create", bg="black", fg="white", command=run)
btn.grid(column=0, row=0)

def run2():
    os.system('python3 train_recognizer.py')
btn2 = Button(window, text="Train", bg="black", fg="white", command=run2)
btn2.grid(column=10, row=0)

def run3():
    os.system('python3 recognizer.py')
btn2 = Button(window, text="Authenticate", bg="black", fg="white", command=run3)
btn2.grid(column=20, row=0)

window.mainloop()
