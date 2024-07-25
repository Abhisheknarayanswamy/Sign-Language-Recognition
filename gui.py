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
root.configure(bg="light grey")
root.attributes('-alpha',1.0)
#root.wm_attributes("-topmost", True)
#root.wm_attributes("-disabled", True)
#root.wm_attributes("-transparentcolor", "white")


bold_font = font.Font(family="Helvetica", size=16, weight="bold")
bold_label = tk.Label(root, text="SIGN LANGUAGE RECOGNITION", font=bold_font)
bold_label.pack(pady=10)
#text_box = tk.Text(root,height=12,width=40)
#text_box.pack()

def openInstruktion():
     
    file = open(r"C:\Users\abhis\Documents\sign-language-gesture-recognition-master (1)\result.txt").read()
    text_box.insert(0.0, file)

def realtime():
    subprocess.call(["python", "gui3.py"])

def gui():
    subprocess.call(["python", "gui1.py"])

def gu():
    subprocess.call(["python", "gui2.py"])

#execute_button = tk.Button(root, text="Words/Sentence", command=openInstruktion, height=3, width=15)
#execute_button.pack(pady=10)

btn = tk.Button(root, text="REAL TIME PREDICTION",command=realtime, height=3, width=20, bg='#4681f4')
btn.pack(pady=10)

btn1 = tk.Button(root, text="WORDS", command=gui, height=3, width=20, bg='#5dbea3')
btn1.pack(pady=10)

btn2 = tk.Button(root, text="SENTENCES", command=gu, height=3, width=20, bg='#a881af')
btn2.pack(pady=10)

root.mainloop()