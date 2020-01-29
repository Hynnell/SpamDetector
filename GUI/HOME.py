#Author: Lucas Hyatt

import tkinter as tk
from tkinter import filedialog, Text
import tkinter.font
import GUI

root = tk.Tk() #Establishes structure for app window
# root.geometry("300x300")
root.resizable(False, False)
root.title("Cold Call System")
# root.attributes("-topmost", True)   # open window in front

'''
Color Scheme:

red = #ff0443
blue = #0486ff
yellow = #ffde04
'''

def inputFile():
    filename = filedialog.askopenfilename(initialdir="./..", title="Select File")

    #This is where we insert the rest of I/O for the

def exitProgram():
    root.destroy()

pane = tk.Frame(root, bg = '#0486ff', bd=30)
pane.pack(fill = tk.BOTH, expand = True)

button_font = tkinter.font.Font(family="Helvetica",size=36,weight="bold")

user_view = tk.Button(pane, text="User View", width=12, fg="#ff0443")
user_view.pack() 
user_view['font'] = button_font
# user_view.update()

input_roster = tk.Button(pane, text="Input Roster", width=12, fg="#ff0443", command=inputFile)
input_roster.pack() 
input_roster['font'] = button_font
# input_roster.update()

exit_menu = tk.Button(pane, text="Quit", width=12, fg="#ff0443", command=exitProgram)
exit_menu.pack()
exit_menu['font'] = button_font
# exit_menu.update()

# Main Loop
# root.attributes("-topmost", False)  # allow window to go behind other windows
root.mainloop()

'''
Sources: 
https://stackoverflow.com/questions/31128780/tkinter-how-to-make-a-button-center-itself
https://www.geeksforgeeks.org/python-pack-method-in-tkinter/
https://www.youtube.com/watch?v=u4ykDbciXa8&feature=youtu.be
https://www.youtube.com/watch?v=qC3FYdpJI5Y&feature=youtu.be
https://stackoverflow.com/questions/110923/how-do-i-close-a-tkinter-window
https://www.tutorialspoint.com/python/tk_place.htm
'''














