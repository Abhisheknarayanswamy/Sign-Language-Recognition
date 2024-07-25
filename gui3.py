import tkinter as tk
import subprocess
import os,sys
import cv2
from os import startfile
import tkinter.font as font
path = '\Documents\sign-language-gesture-recognition-master (1)'
sys.path.append(path)


root = tk.Tk()
root.geometry("720x500") 

bold_font = font.Font(family="Helvetica", size=16, weight="bold")
bold_label = tk.Label(root, text="Real Time Recognition", font=bold_font)
bold_label.pack(pady=10)
#text_box = tk.Text(root,height=12,width=40)
#text_box.pack()

def openInstruktion():
     
    file = open(r"C:\Users\abhis\Documents\sign-language-gesture-recognition-master (1)\result.txt").read()
    

def realtime():
    subprocess.call(["python", "real_time_prediction.py"])



execute_button = tk.Button(root, text="Camera", command=realtime, height=3, width=15)
execute_button.pack(pady=10)



root.mainloop()