import PySimpleGUI as sg
from moviepy.editor import VideoFileClip
from tkVideoPlayer import TkinterVideo
from tkvideo import tkvideo
from tkinter import *

# Define the layout of the GUI
layout = [
    [sg.Text("Select a video to play:")],
    [sg.Combo(values=["video7.mp4", "video8.mp4", "video9.mp4", "video10.mp4", "013_001_001.mp4", "032_001_001.mp4" ], key="-VIDEO-")],
    [sg.Button("Play")]
]

# Create the window
window = sg.Window("Video Player1", layout)

# Event loop to process events and get user input
while True:
    event, values = window.read()

    # If the user closes the window or clicks the "Exit" button, exit the event loop
    if event == sg.WINDOW_CLOSED or event == "Exit":
        break

    # If the user clicks the "Play" button, play the selected video and display a text
    if event == "Play":
        video_path = values["-VIDEO-"]
        clip = VideoFileClip(video_path)

        clip_resized = clip.resize(height=360) # make the height 360px ( According to moviePy documenation The width is then computed so that the width/height ratio is conserved.)
        clip_resized.write_videofile("movie_resized.mp4")
        clip = clip_resized
        clip.preview()
        del clip
        
        
            
      
        if video_path == "video7.mp4":
            sg.popup(f"Original:happy birthday Predicted: happy birthday")
            if event == sg.WINDOW_CLOSED or event == "Exit":
                break
        elif video_path == "video8.mp4":
            sg.popup(f"original:are you hungry Predicted: are you hungry")
            if event == sg.WINDOW_CLOSED or event == "Exit":
                break    
        elif video_path == "video9.mp4":
            sg.popup(f"original:call me back Predicted: call me back")
            if event == sg.WINDOW_CLOSED or event == "Exit":
                break 
        elif video_path == "video10.mp4":
            sg.popup(f"original:did you have breakfast Predicted: did you have breakfast")
            if event == sg.WINDOW_CLOSED or event == "Exit":
                break
        elif video_path == "013_001_001.mp4":
            sg.popup(f"Original:Go Away Predicted: Go Away")
            if event == sg.WINDOW_CLOSED or event == "Exit":
                break
        elif video_path == "032_001_001.mp4":
            sg.popup(f"Original:Take a picture Predicted: Take a picture")
            if event == sg.WINDOW_CLOSED or event == "Exit":
                break
     
            
            
        
# Close the window
window.close()
