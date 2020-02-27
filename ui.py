'''
Authors: Olivia Pannell + Lucas Hyatt 
Last Modified: 2/16/20
'''


'''======================================Imports=========================================='''
from tkinter import *
from tkinter import filedialog, Text, messagebox
import tkinter.font

from extract import *
from model import *
from knn import *

'''======================================Functions=========================================='''

def loading(q):
    load = Label(root, text="loading...", bg='cadet blue')
    load.place(relx = .45, rely = .5)
  
def input_file():
	global filename
	filename = filedialog.askopenfilename(initialdir="./..", title="Select File")
    # print_in_window("This is where spam info will go.")

def scan():
	global filename
	# if filename != NULL:
	loading(0)
	#FIRST CALL EXTRACT
	#Calls nearest neighbor
	if opt.get() == algorithms[0] or opt.get() == algorithms[4]:
		pass
	#Calls Naives Bayes
	if opt.get() == algorithms[1] or opt.get() == algorithms[4]:
		pass
	#Calls SVC
	if opt.get() == algorithms[2] or opt.get() == algorithms[4]:
		pass
	#Calls Decision tree
	if opt.get() == algorithms[3] or opt.get() == algorithms[4]:
		pass

	# load2 = Label(root, text="accuracy:", bg='cadet blue')
    	# load2.place(relx = .45, rely = .5)

def exitProgram():
    root.destroy()


'''======================================GUI=========================================='''


#Creating a root and initializing attributes (foundation for GUI)
root = Tk() #Establishes structure for app window
root.geometry('500x300')
root.resizable(False, False)
root.title("Spam Detector")
root.protocol("WM_DELETE_WINDOW", exitProgram)  # calls closeWindow() if user clicks red 'x'

#Initializing pane to attach buttons and label to
pane = Frame(root, width = 500, height = 500, bg = 'cadet blue', bd=30)
pane.pack(fill = BOTH, expand = True)

#Initializing font for the buttons.
button_font = tkinter.font.Font(size = 18, weight = "bold") #
label_font = tkinter.font.Font(size=25,weight="bold")

#Label for Title
label = Label(pane, text="Welcome to Spam Detector 3000", bg='cadet blue')
label['font'] = label_font
label.place(relx = .5, rely = .05, anchor = CENTER)

#Button for the user view
input_data = Button(pane, padx=10, width=15, text="Input Data", highlightbackground='cadet blue', command=input_file)
input_data['font'] = button_font
input_data.place(relx = .5, rely = .25, anchor = CENTER)

#List of currently implemented algorithms
algorithms = [
	"Nearest Neighbor", 
	"Naives Bayes", 
	"SVC", 
	"Decision Tree", 
	"All"
]
#Saves current drop down option as opt
opt = StringVar() 
opt.set("Choose Algorithm")

#Drop down menu to select a certain algorithm
ddb = OptionMenu(pane, opt, *algorithms)
ddb.config(bg = 'cadet blue')
ddb["menu"].config(bg = 'cadet blue')
ddb.place(relx = .20, rely = .35)

#Button for inputting a roster
detect_spam = Button(pane, padx=3, width=5, text="Scan", highlightbackground='cadet blue', command = scan)
detect_spam['font'] = button_font
detect_spam.place(relx = .60, rely = .35)

#Closes the program
exit_menu = Button(pane, text="Quit", highlightbackground='cadet blue', fg='red', command=exitProgram)
exit_menu['font'] = button_font
exit_menu.place(relx=0.12, rely=1.1 ,anchor = SE)

# Main Loop
root.update()
root.mainloop()
exit()














