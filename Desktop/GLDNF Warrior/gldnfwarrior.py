import PySimpleGUI as sg
#import pysimplesql as ss
#import logging
import os
from PIL import Image, ImageTk
import io

sg.theme('DarkAmber') 


file_types = [("JPEG (*.jpg)", "*.jpg"),
              ("PNG (*.png)", "*.png"),
              ("GIF (*.gif)", "*.gif"),
              ("All files (*.*)", "*.*")]



def main():
    layout = [
        [sg.Image(key="-IMAGE-")],
        [
            sg.Text("Choose Your Warrior"),
            sg.Input(size=(25, 1), key="-FILE-"),
            sg.FileBrowse(file_types=file_types),
            sg.Button("Load Warrior"),
        ],
    ]
    window = sg.Window("GLDNF WARRIOR APP", layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "Load Warrior":
            filename = values["-FILE-"]
            if os.path.exists(filename):
                image = Image.open(values["-FILE-"])
                image.thumbnail((800, 800))
                bio = io.BytesIO()
                image.save(bio, format="PNG")
                window["-IMAGE-"].update(data=bio.getvalue())
    window.close()
if __name__ == "__main__":
    main()