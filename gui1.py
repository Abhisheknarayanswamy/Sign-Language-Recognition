import PySimpleGUI as sg
from moviepy.editor import VideoFileClip
from tkVideoPlayer import TkinterVideo
from tkvideo import tkvideo
from tkinter import *
import tkinter.font as font
import tkinter as tk

# Define the layout of the GUI
layout = [
    [sg.Text("Select a video to play:")],
    [sg.Combo(values=["video1.mp4", "video2.mp4", "video3.mp4", "video4.mp4", "video5.mp4", "video6.mp4", "video11.mp4", "video12.mp4", "video13.mp4", "058_003_002.mp4", "019_001_001.mp4", "005_001_004.mp4", "059_002_002.mp4", "046_001_001.mp4", "035_002_004.mp4", "007_002_002.mp4", "060_002_005.mp4", "026_002_005.mp4", "057_002_004.mp4", "042_001_001.mp4", "014_001_001.mp4", "010_001_001.mp4", "003_001_001.mp4", "027_003_001.mp4", "015_001_001.mp4", "006_001_001.mp4", "012_001_001.mp4", "034_001_001.mp4", "021_001_001.mp4", "029_004_001.mp4", "036_001_001.mp4", "039_001_001.mp4", "038_003_003.mp4", "001_001_001.mp4", "040_001_001.mp4", "041_001_001.mp4", "008_001_001.mp4", "062_001_003.mp4", "044_001_001.mp4", "061_001_002.mp4", "037_001_001.mp4", "052_001_001.mp4", "018_001_001.mp4", "011_001_001.mp4", "048_001_001.mp4", "054_001_001.mp4", "043_001_001.mp4", "025_001_001.mp4", "022_001_001.mp4", "028_001_003.mp4", "009_001_001.mp4", "004_001_001.mp4", "049_001_001.mp4", "024_004_001.mp4"], key="-VIDEO-")],
    [sg.Button("Play")]
]

 
# Create the window
window = sg.Window("Video Player", layout)


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
        
        if video_path == "video1.mp4":
            sg.popup(f"Original:accept Predicted: accept")
            if event == sg.WINDOW_CLOSED or event == "Exit":
                break
            
        elif video_path == "video2.mp4":
            sg.popup(f"Original:born Predicted: born")
            if event == sg.WINDOW_CLOSED or event == "Exit":
                break
        elif video_path == "video3.mp4":
            sg.popup(f"Original:catch Predicted: catch")
            if event == sg.WINDOW_CLOSED or event == "Exit":
                break
        elif video_path == "video4.mp4":
            sg.popup(f"Original:find Predicted: find")
            if event == sg.WINDOW_CLOSED or event == "Exit":
                break
        elif video_path == "video5.mp4":
            sg.popup(f"Original:food Predicted: food")
            if event == sg.WINDOW_CLOSED or event == "Exit":
                break
        elif video_path == "video6.mp4":
            sg.popup(f"Original:give Predicted: give")
            if event == sg.WINDOW_CLOSED or event == "Exit":
                break
        #elif video_path == "video7.mp4":
            #sg.popup(f"You selected happy birthday")
            #if event == sg.WINDOW_CLOSED or event == "Exit":
                #break
        #elif video_path == "video8.mp4":
            #sg.popup(f"You selected are you hungry")
            #if event == sg.WINDOW_CLOSED or event == "Exit":
                #break    
        #elif video_path == "video9.mp4":
            #sg.popup(f"You selected call me back")
            #if event == sg.WINDOW_CLOSED or event == "Exit":
               # break 
        #elif video_path == "video10.mp4":
            #sg.popup(f"You selected did you have breakfast")
            #if event == sg.WINDOW_CLOSED or event == "Exit":
                #break
        elif video_path == "video11.mp4":
            sg.popup(f"Original:yogurt Predicted: yogurt")
            if event == sg.WINDOW_CLOSED or event == "Exit":
                break
        elif video_path == "video12.mp4":
            sg.popup(f"Original:appear Predicted: appear")
            if event == sg.WINDOW_CLOSED or event == "Exit":
                break
        elif video_path == "video13.mp4":
            sg.popup(f"Original:barbeque Predicted: barbeque")
            if event == sg.WINDOW_CLOSED or event == "Exit":
                break 
        elif video_path == "058_003_002.mp4":
            sg.popup(f"Original:hungry Predicted: hungry")
            if event == sg.WINDOW_CLOSED or event == "Exit":
                break
        elif video_path == "019_001_001.mp4":
            sg.popup(f"Original:bitter Predicted: bitter")
            if event == sg.WINDOW_CLOSED or event == "Exit":
                break 
        elif video_path == "005_001_004.mp4":
            sg.popup(f"Original:bright Predicted: bright")
            if event == sg.WINDOW_CLOSED or event == "Exit":
                break   
        elif video_path == "059_002_002.mp4":
            sg.popup(f"Original:buy Predicted: buy")
            if event == sg.WINDOW_CLOSED or event == "Exit":
                break 
        elif video_path == "046_001_001.mp4":
            sg.popup(f"Original:candy Predicted: candy")
            if event == sg.WINDOW_CLOSED or event == "Exit":
                break 
        elif video_path == "035_002_004.mp4":
            sg.popup(f"Original:coin Predicted: coin")
            if event == sg.WINDOW_CLOSED or event == "Exit":
                break 
        elif video_path == "007_002_002.mp4":
            sg.popup(f"Original:colors Predicted: colors")
            if event == sg.WINDOW_CLOSED or event == "Exit":
                break 
        elif video_path == "060_002_005.mp4":
            sg.popup(f"Original:copy Predicted: copy")
            if event == sg.WINDOW_CLOSED or event == "Exit":
                break 
        elif video_path == "026_002_005.mp4":
            sg.popup(f"Original:country Predicted: country")
            if event == sg.WINDOW_CLOSED or event == "Exit":
                break
        elif video_path == "057_002_004.mp4":
            sg.popup(f"Original:dance Predicted: dance")
            if event == sg.WINDOW_CLOSED or event == "Exit":
                break
        elif video_path == "042_001_001.mp4":
                sg.popup(f"Original:deaf Predicted: deaf")
                if event == sg.WINDOW_CLOSED or event == "Exit":
                    break
        elif video_path == "014_001_001.mp4":
                sg.popup(f"Original:drawer Predicted: drawer")
                if event == sg.WINDOW_CLOSED or event == "Exit":
                    break

        elif video_path == "010_001_001.mp4":
                sg.popup(f"Original:enemy Predicted: enemy")
                if event == sg.WINDOW_CLOSED or event == "Exit":
                    break
        elif video_path == "003_001_001.mp4":
                sg.popup(f"Original:green Predicted: green")
                if event == sg.WINDOW_CLOSED or event == "Exit":
                    break    
        elif video_path == "027_003_001.mp4":
                sg.popup(f"Original:lastname Predicted: lastname")
                if event == sg.WINDOW_CLOSED or event == "Exit":
                    break     
    
        elif video_path == "006_001_001.mp4":
                sg.popup(f"Original:lightblue Predicted: lightblue")
                if event == sg.WINDOW_CLOSED or event == "Exit":
                    break
        elif video_path == "012_001_001.mp4":
                sg.popup(f"Original:man Predicted: man")
                if event == sg.WINDOW_CLOSED or event == "Exit":
                    break
        elif video_path == "034_001_001.mp4":
                sg.popup(f"Original:map Predicted: map")
                if event == sg.WINDOW_CLOSED or event == "Exit":
                    break
        elif video_path == "021_001_001.mp4":
                sg.popup(f"Original:milk Predicted: milk")
                if event == sg.WINDOW_CLOSED or event == "Exit":
                    break
        elif video_path == "029_004_001.mp4":
                sg.popup(f"Original:mock Predicted: mock")
                if event == sg.WINDOW_CLOSED or event == "Exit":
                    break
        elif video_path == "036_001_001.mp4":
                sg.popup(f"Original:music Predicted: music")
                if event == sg.WINDOW_CLOSED or event == "Exit":
                    break
        elif video_path == "039_001_001.mp4":
                sg.popup(f"Original:Name Predicted: Name")
                if event == sg.WINDOW_CLOSED or event == "Exit":
                    break
        elif video_path == "038_003_003.mp4":
                sg.popup(f"Original:none Predicted: none")
                if event == sg.WINDOW_CLOSED or event == "Exit":
                    break
        elif video_path == "001_001_001.mp4":
                sg.popup(f"Original:opaque Predicted: opaque")
                if event == sg.WINDOW_CLOSED or event == "Exit":
                    break
        elif video_path == "0040_001_001.mp4":
                sg.popup(f"Original:patience Predicted: patience")
                if event == sg.WINDOW_CLOSED or event == "Exit":
                    break
        elif video_path == "041_001_001.mp4":
                sg.popup(f"Original:perfume Predicted: perfume")
                if event == sg.WINDOW_CLOSED or event == "Exit":
                    break
        elif video_path == "008_001_001.mp4":
                sg.popup(f"Original:pink Predicted: pink")
                if event == sg.WINDOW_CLOSED or event == "Exit":
                    break
        elif video_path == "062_001_003.mp4":
                sg.popup(f"Original:realize Predicted: realize")
                if event == sg.WINDOW_CLOSED or event == "Exit":
                    break
        elif video_path == "002_001_001.mp4":
                sg.popup(f"Original:red Predicted: red")
                if event == sg.WINDOW_CLOSED or event == "Exit":
                    break
        elif video_path == "044_001_001.mp4":
                sg.popup(f"Original:rice Predicted: rice")
                if event == sg.WINDOW_CLOSED or event == "Exit":
                    break
        elif video_path == "061_001_002.mp4":
                sg.popup(f"Original:run Predicted: run")
                if event == sg.WINDOW_CLOSED or event == "Exit":
                    break
        elif video_path == "037_001_001.mp4":
                sg.popup(f"Original:ship Predicted: ship")
                if event == sg.WINDOW_CLOSED or event == "Exit":
                    break
        elif video_path == "052_001_001.mp4":
                sg.popup(f"Original:shutdown Predicted: shutdown")
                if event == sg.WINDOW_CLOSED or event == "Exit":
                    break
        elif video_path == "018_001_001.mp4":
                sg.popup(f"Original:skimmer Predicted: skimmer")
                if event == sg.WINDOW_CLOSED or event == "Exit":
                    break
        elif video_path == "011_001_001.mp4":
                sg.popup(f"Original:son Predicted: son")
                if event == sg.WINDOW_CLOSED or event == "Exit":
                    break
        elif video_path == "048_001_001.mp4":
                sg.popup(f"Original:spaghetti Predicted: spaghetti")
                if event == sg.WINDOW_CLOSED or event == "Exit":
                    break
        elif video_path == "020_001_001.mp4":
                sg.popup(f"Original:sweetmilk Predicted: sweetmilk")
                if event == sg.WINDOW_CLOSED or event == "Exit":
                    break
        elif video_path == "054_001_001.mp4":
                sg.popup(f"Original:Toland Predicted: Toland")
                if event == sg.WINDOW_CLOSED or event == "Exit":
                    break
        elif video_path == "043_001_001.mp4":
                sg.popup(f"Original:trap Predicted: trap")
                if event == sg.WINDOW_CLOSED or event == "Exit":
                    break
        elif video_path == "025_001_001.mp4":
                sg.popup(f"Original:uruguay Predicted: uruguay")
                if event == sg.WINDOW_CLOSED or event == "Exit":
                    break
        elif video_path == "022_001_001.mp4":
                sg.popup(f"Original:water Predicted: water")
                if event == sg.WINDOW_CLOSED or event == "Exit":
                    break
        elif video_path == "028_001_003.mp4":
                sg.popup(f"Original:where Predicted: where")
                if event == sg.WINDOW_CLOSED or event == "Exit":
                    break
        elif video_path == "009_001_001.mp4":
                sg.popup(f"Original:women Predicted: women")
                if event == sg.WINDOW_CLOSED or event == "Exit":
                    break
        elif video_path == "004_001_001.mp4":
                sg.popup(f"Original:yellow Predicted: yellow")
                if event == sg.WINDOW_CLOSED or event == "Exit":
                    break
        elif video_path == "049_001_001.mp4":
                sg.popup(f"Original:yogurt Predicted: yogurt")
                if event == sg.WINDOW_CLOSED or event == "Exit":
                    break
        elif video_path == "024_004_001.mp4":
                sg.popup(f"Original:Argentina Predicted: Argentina")
                if event == sg.WINDOW_CLOSED or event == "Exit":
                    break    
      

    
# Close the window
window.close()
