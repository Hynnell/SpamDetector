'''
Author: Lucas Hyatt
Last Modified: 2/8/20
'''


'''======================================Imports=========================================='''
import tkinter as tk
from tkinter import filedialog, Text, messagebox
import tkinter.ttk as ttk
import tkinter.font
import os
import sys
from datetime import datetime


'''======================================Functions=========================================='''

def print_in_window(text):
    label = tk.Label(root, text=text, bg='#0486ff')
    label.place(relx = .3, rely = .4)

def input_file():
    filename = filedialog.askopenfilename(initialdir="./..", title="Select File")
    print_in_window("This is where spam info will go.")

def exitProgram():
    root.destroy()


'''======================================GUI=========================================='''

'''
Color Scheme:

red = #ff0443
blue = #0486ff
yellow = #ffde04
'''

#Creating a root and initializing attributes (foundation for GUI)
root = tk.Tk() #Establishes structure for app window
root.geometry('500x500')
root.resizable(False, False)
root.title("Cold Call System")
root.attributes("-topmost", True)  # open window in front
root.protocol("WM_DELETE_WINDOW", exitProgram)  # calls closeWindow() if user clicks red 'x'

#Initializing pane to attach buttons and label to
pane = tk.Frame(root, width = 500, height = 500, bg = '#0486ff', bd=30)
pane.pack(fill = tk.BOTH, expand = True)

#Initializing font for the buttons.
button_font = tkinter.font.Font(family="Helvetica",size=20,weight="bold")
label_font = tkinter.font.Font(family="Helvetica",size=25,weight="bold")

#Progress bar will show how many student out of the roster have been chosen.
'''progress = ttk.Progressbar(pane, orient=tk.HORIZONTAL, length=496)
progress['value'] = 25
progress.pack(side=tk.BOTTOM)'''

#Label for the HOME MENU
label = tk.Label(pane, text="Welcome to Spam Detector 3000", bg='#0486ff')
label['font'] = label_font
label.place(relx = .5, rely = .05, anchor = tk.CENTER)

#Button for the user view
input_data = tk.Button(pane, padx=3, width=15, text="Input Data", highlightbackground='#0486ff', command=input_file)
input_data['font'] = button_font
input_data.place(relx = .1, rely = .15)

#Button for inputting a roster
detect_spam = tk.Button(pane, padx=3, width=15, text="Scan Spam", highlightbackground='#0486ff')
detect_spam['font'] = button_font
detect_spam.place(relx = .5, rely = .15)

#Button for exiting and closing the program (all windows)
exit_menu = tk.Button(pane, width=10, text="Exit", highlightbackground='#0486ff', fg='red', command=exitProgram)
exit_menu['font'] = button_font
exit_menu.place(relx = .5, rely = .95, anchor = tk.CENTER)

# Main Loop
root.update()
root.attributes("-topmost", False)  # allow window to go behind other windows
root.mainloop()
exit()

'''
Sources: 
https://stackoverflow.com/questions/31128780/tkinter-how-to-make-a-button-center-itself
https://www.geeksforgeeks.org/python-pack-method-in-tkinter/
https://www.youtube.com/watch?v=u4ykDbciXa8&feature=youtu.be
https://www.youtube.com/watch?v=qC3FYdpJI5Y&feature=youtu.be
https://stackoverflow.com/questions/110923/how-do-i-close-a-tkinter-window
https://www.tutorialspoint.com/python/tk_place.htm
https://datatofish.com/message-box-python/
'''














