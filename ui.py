'''
Authors: Olivia Pannell + Lucas Hyatt 
Last Modified: 2/16/20
'''


'''======================================Imports=========================================='''
from tkinter import *
from tkinter import filedialog
from os import path

import extract as e
import model as m

'''======================================Global Variables=========================================='''
button_font = ("Helvetica", 18, "bold")
small_title_font = ("Helvetica", 25, "bold italic")
title_font = ("Helvetica", 40, "bold italic")
info_font = ("Helvetica", 14, "italic")
#Single message path, training folder path, testing folder path
filepath = None
tr = None
te = None
#Changed to 0 when user enters their own dataset
default = 1
# total, ham, spam files given by the user
global tot, ham, spam
#List of algorithms the user can choose from
algorithms = [
	"Nearest Neighbor", 
	"Perceptron", 
	"Both"
]
'''======================================Functions=========================================='''  
def input_file():
	global filepath
	filepath = filedialog.askopenfilename(initialdir="./..", title="Select File")

def testfolderfinder():
	global te
	te = filedialog.askdirectory(initialdir="./..", title="Select Folder")

def trainfolderfinder():
	global tr
	tr = filedialog.askdirectory(initialdir="./..", title="Select Folder")

def dataset():
	top = Toplevel()
	top.geometry('300x300')
	top.resizable(False, False)
	top.title("DataSet Information")
	top.config(bg="cadet blue")

	label = Label(top, text="Enter dataset information:", bg='cadet blue', fg = "white", font = small_title_font)
	label.place(relx = .5, rely = .15, anchor = CENTER)

	label = Label(top, text="Structure of dataset: Ham files first, the Spam files follows.", bg='cadet blue', fg = "white", 
		font = info_font, wraplength = 300, justify = CENTER )
	label.place(relx = .5, rely = .4, anchor = CENTER)

	label = Label(top, text="Number of total files: ", bg='cadet blue', fg = "white", font = info_font)
	label.place(relx = .5, rely = .5, anchor = CENTER)

	label = Label(top, text="Structure of dataset: Ham files first, the Spam files follows.", bg='cadet blue', fg = "white", font = info_font)
	label.place(relx = .5, rely = .6, anchor = CENTER)

def quitWindow(win):
    win.destroy()

'''======================================Classes=========================================='''
# Main class that controls which frame is on top (shown to the user)
# in any given instance
class start(Tk):
	def __init__(self, *args, **kwargs):
		Tk.__init__(self, *args, **kwargs)
		
		container = Frame(self, height=350, width=550, bg="cadet blue")
		container.pack(side="top", fill="both", expand=True)
		self.pages = {}
		for page in (MainMenu, AboutPage, StartPage, DatasetPage, ResultPage): #InformationPage
			frame = page(container, self)
			self.pages[page] = frame
			frame.place(relx=0.0, rely=0.0, height=350, width=550)
			frame.config(bg='cadet blue')

		self.show_frame(MainMenu)

	def show_frame(self, controller):
		frame = self.pages[controller]
		frame.tkraise()

# Contains everything for the Main Menu frame.
class MainMenu(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		#Label for Title
		fr1 = Frame(self, width = 570, height = 120, bg = 'deepskyblue4')
		fr1.place(relx=0.0, rely=0.0, anchor=NW)
		label = Label(self, text="Welcome to", bg='deepskyblue4', fg = "white", font = small_title_font)
		label.place(relx = .5, rely = .15, anchor = CENTER)

		label = Label(self, text="The Hynell Spam Detector", bg='deepskyblue4', fg = "white", font = title_font)
		label.place(relx = .5, rely = .27, anchor = CENTER)
		fr2 = Frame(self, width = 570, height = 5, bg = 'lightblue2')
		fr2.place(relx=0.5, rely=0.35, anchor=CENTER)
		#starts the thing
		single = Button(self, text="Single Entry", highlightbackground='cadet blue',
			padx = 50, font = button_font, command=lambda: controller.show_frame(StartPage))
		single.place(relx=0.5, rely=.45 ,anchor = CENTER)

		# Takes user to the about page
		about = Button(self, text="About", highlightbackground='cadet blue', 
			padx = 74, font = button_font, command=lambda: controller.show_frame(AboutPage))
		about.place(relx=0.5, rely=.65 ,anchor = CENTER)

		# Takes user to the dataset page that allows them to customize datasets
		data = Button(self, text="Dataset Entry", highlightbackground='cadet blue', 
			padx = 45, font = button_font, command=lambda: controller.show_frame(DatasetPage))
		data.place(relx=0.5, rely=.55 ,anchor = CENTER)


		fr3 = Frame(self, width = 700, height = 60, bg = 'lightblue2')
		fr3.place(relx=0.5, rely=1.0, anchor=CENTER)
		#Closes the program
		exit = Button(self, text="Quit", highlightbackground='lightblue2',
			padx = 12, command= lambda: quitWindow(root))
		exit.place(relx=0.0, rely=1.0, anchor=SW)

# Contains information about our models such as accuracy for default datasets.
class AboutPage(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		#Background frames
		fr1 = Frame(self, width = 570, height = 120, bg = 'deepskyblue4')
		fr1.place(relx=0.0, rely=0.0, anchor=NW)
		fr2 = Frame(self, width = 570, height = 5, bg = 'lightblue2')
		fr2.place(relx=0.5, rely=0.35, anchor=CENTER)
		fr3 = Frame(self, width = 700, height = 60, bg = 'lightblue2')
		fr3.place(relx=0.5, rely=1.0, anchor=CENTER)

		#Label for Title
		label = Label(self, text="About the", bg='deepskyblue4', fg = "white", font = small_title_font)
		label.place(relx = .5, rely = .15, anchor = CENTER)
		label = Label(self, text="The Hynell Spam Detector", bg='deepskyblue4', fg = "white", font = title_font)
		label.place(relx = .5, rely = .27, anchor = CENTER)

		# About this project
		about = "This program was created by Lucas Hyatt and Olivia Pannell for CIS 433.\nIt is intended to help keep yourself safe from malicious attacks by determining whether messages are spam or not."
		label = Label(self, text=about, bg='cadet blue', font = ("Helvetica", 18, "bold italic"), wraplength = 500, justify = LEFT)
		label.place(relx = .5, rely = .42, anchor = N)

		# Back button takes user to the main menu
		b0 = Button(self, text="Back", highlightbackground="lightblue2", padx=10,
								command=lambda: controller.show_frame(MainMenu))
		b0.place(relx=0.0, rely=1.0, anchor=SW)

# Contains information about our models such as accuracy for default datasets.
class StartPage(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		global opt, filepath

		# Background frames
		fr1 = Frame(self, width = 570, height = 120, bg = 'deepskyblue4')
		fr1.place(relx=0.0, rely=0.0, anchor=NW)
		fr3 = Frame(self, width = 700, height = 60, bg = 'lightblue2')
		fr3.place(relx=0.5, rely=1.0, anchor=CENTER)

		#Label for Title
		label = Label(self, text="Welcome to", bg='deepskyblue4', fg = "white", font = small_title_font)
		label.place(relx = .5, rely = .15, anchor = CENTER)
		label = Label(self, text="The Hynell Spam Detector", bg='deepskyblue4', fg = "white", font = title_font)
		label.place(relx = .5, rely = .27, anchor = CENTER)

		#Bottom line background
		fr2 = Frame(self, width = 570, height = 5, bg = 'lightblue2')
		fr2.place(relx=0.5, rely=0.35, anchor=CENTER)

		b0 = Button(self, text="Back", highlightbackground="lightblue2", padx=10,
								command=lambda: controller.show_frame(MainMenu))
		b0.place(relx=0.0, rely=1.0, anchor=SW)

		#Saves current drop down option as opt
		opt = StringVar() 
		opt.set("Choose..")

		#Drop down menu to select a certain algorithm
		ddb = OptionMenu(self, opt, *algorithms)
		ddb.config(bg = 'cadet blue', padx = 42)
		ddb["menu"].config(bg = 'cadet blue')
		ddb.place(relx = .5, rely = .5, anchor = CENTER)
		label = Label(self, text="Choose a model: ", bg='cadet blue', fg = "white", font = info_font)
		label.place(relx = .2, rely = .4, anchor = W)

		#Select single message that will be scanned for spam
		label = Label(self, text="Choose Message to Scan:", bg='cadet blue', fg = "white", font = info_font)
		label.place(relx = .2, rely = .6, anchor = W)
		file = Button(self, padx=80, text="Find!", highlightbackground='cadet blue', command = input_file)
		file.place(relx = 0.5, rely = 0.7, anchor = CENTER)

		#Button for training data
		detect_spam = Button(self, padx=30, width=5, text="Train!", highlightbackground='lightblue2', command = lambda: self.errorcheck(parent, controller))
		detect_spam.place(relx = 1.0, rely = 1.0, anchor = SE)

	def errorcheck(self, parent, controller):
		global opt, filepath

		errorlbl = Label(self, text='        *Please Choose a Model.    ', bg="cadet blue", fg="red4", font=info_font)
		errorlbl2 = Label(self, text='        *Please Choose a Message.    ', bg="cadet blue", fg="red4", font=info_font)
		# Check to make sure they filled out model
		if opt.get() == "Choose..":
			errorlbl.place(relx = .5, rely = .8, anchor = CENTER)
			print("model not filled out")
			return
		#Makes sure path exists and error checks
		if filepath == None:
			errorlbl2.place(relx = .5, rely = .8, anchor = CENTER)
			print("File not filled out")
			return
		else:
			print(filepath)
			self.scan(parent, controller)



	def loading(self, q):
		if q:
			load = Label(self, text="Loading Please Wait...", bg='lightblue2', font = ("Helvetica", 20, "bold"))
			load.place(relx = .8, rely = 1.0, anchor = SW)
		else:
			load = Label(self, text="Loading Please Wait...", bg='cadet blue', font = ("Helvetica", 20, "bold"))
			load.place(relx = .8, rely = 1.0, anchor = SW)

	def scan(self, parent, controller):
		global filepath
		self.loading(1)
		#Calls Train nearest neighbor
		if opt.get() == algorithms[0] or opt.get() == algorithms[2]:
			#vec = m.extract_single(filepath)
			#tr_y = k.trainingy(tot, spam, ham)
			#pred = m.classify(tr, tr_y, 10, vec)
			#print(pred)
			pass
		#Calls Train Perceptron
		if opt.get() == algorithms[1] or opt.get() == algorithms[2]:
			pass

		# load2 = Label(self, text="Results:", bg='cadet blue')
	    # load2.place(relx = .45, rely = .5)
	    # if pred == -1:
	    #	res = "Not Spam"
	    # else pred == 1:
	    #	res = "Spam"
	    # load3 = Label(self, text= res, bg='cadet blue')
	    # load3.place(relx = .45, rely = .5)


# This is the page that users can customize with using their own datasets
class DatasetPage(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		global totalent, hament, spament, folder
		#Label for Title
		fr1 = Frame(self, width = 570, height = 70, bg = 'deepskyblue4')
		fr1.place(relx=0.0, rely=0.0, anchor=NW)

		label = Label(fr1, text="Enter dataset information:", bg='deepskyblue4', fg = "white", font = title_font)
		label.place(relx = 0.5, rely = .5, anchor = CENTER)

		fr2 = Frame(self, width = 700, height = 5, bg = 'lightblue2')
		fr2.place(relx=0.5, rely=0.2, anchor=CENTER)

		fr3 = Frame(self, width = 700, height = 60, bg = 'lightblue2')
		fr3.place(relx=0.5, rely=1.0, anchor=CENTER)

		label = Label(self, text="Structure of dataset needs to be Ham (non-spam) files first, the Spam files follows.", bg='cadet blue', fg = "white", 
			font = ("Helvetica", 16, "bold italic"), wraplength = 500, justify = CENTER )
		label.place(relx = .5, rely = .3, anchor = CENTER)

		#Gets folder of dataset
		label = Label(self, text="Insert Training Dataset: ", bg='cadet blue', fg = "black", font = info_font)
		label.place(relx = .2, rely = .4, anchor = W)
		b = Button(self, text="Find Training Data!", highlightbackground="cadet blue", padx=38,
								command= trainfolderfinder)
		b.place(relx=0.5, rely=.4, anchor=W)

		#Gets folder of dataset
		label = Label(self, text="Insert Testing Dataset: ", bg='cadet blue', fg = "black", font = info_font)
		label.place(relx = .2, rely = .5, anchor = W)
		b = Button(self, text="Find Testing Data!", highlightbackground="cadet blue", padx=40,
								command= testfolderfinder)
		b.place(relx=0.5, rely=.5, anchor=W)

		#Asks for total number of files
		#--- stored in total---
		label = Label(self, text="Number of Total files: ", bg='cadet blue', fg = "black", font = info_font)
		label.place(relx = .2, rely = .6, anchor = W)
		totalent = Entry(self)
		totalent.place(relx=0.5, rely=0.6, anchor=W)

		#Asks for total number of non spam files
		#---stored in hament---
		label = Label(self, text="Number of Ham files:", bg='cadet blue', fg = "black", font = info_font)
		label.place(relx = .2, rely = .7, anchor = W)
		hament = Entry(self)
		hament.place(relx=0.5, rely=0.7, anchor=W)

		#Asks for total number of spam files
		#---stored in spament---
		label = Label(self, text="Number of Spam files:", bg='cadet blue', fg = "black", font = info_font)
		label.place(relx = .2, rely = .8, anchor = W)
		spament = Entry(self)
		spament.place(relx=0.5, rely=0.8, anchor=W)

		#Back button goes back to main menu without saving any of the data
		b1 = Button(self, text="Back", highlightbackground="lightblue2", padx=10,
								command=lambda: controller.show_frame(MainMenu))
		b1.place(relx=0.0, rely=1.0, anchor=SW)
		#Save button first error checks, then saves dataset information.
		b2 = Button(self, text="Save", highlightbackground="lightblue2", padx=10,
								command=lambda: self.save(parent, controller))
		b2.place(relx=1.0, rely=1.0, anchor=SE)

	#Errors checks first then saves if passed tests.
	def save(self, parent, controller):
		global totalent, hament, spament
		# ERRORLBL IN IF ELSE NOT PRINTING FOR SOME REASON 
		#
		#
		# COME BACK HERE
		#Error Labels that are placed when user fails an error check.
		errorlbl = Label(self, text='           *Please enter only digits.       ', bg="cadet blue", fg="blue", font=info_font)
		errorlbl2 = Label(self, text='*Please fill out all sections.', bg="cadet blue", fg="red4", font=info_font)
		errorlbl3 = Label(self, text='*Please enter training/testing data.', bg="cadet blue", fg="red4", font=info_font)
		#Check to make sure entries are filled out


		'''
		NEED TO FIX THIS!!!
		'''
		if not totalent.get() or  not hament.get() or not spament.get():
			print("not filled out")
			errorlbl2.place(relx=.5, rely = .88, anchor = CENTER)
			return
		fixlbl2 = Label(self, text='*Please fill out all sections.', bg="cadet blue", fg="red4", font=info_font)
		fixlbl2.place(relx=.5, rely = .88, anchor = CENTER)
		#Check to make sure file entries are digits.
		if not totalent.get().isdigit() or not spament.get().isdigit() or not hament.get().isdigit():
			print("not all numbers")
			errorlbl.place(relx = .5, rely = .88, anchor = CENTER)
			return
		fixlbl = Label(self, text='        *Please enter only digits.    ', bg="cadet blue", fg="cadet blue", font=info_font)
		fixlbl.place(relx = .5, rely = .88, anchor = CENTER)
		if te == None or tr == None:
			print("not all folders")
			errorlbl3.place(relx = .5, rely = .88, anchor = CENTER)
			return

		fixlbl3 = Label(self, text='*Please enter training/testing data.', bg="cadet blue", fg="cadet blue", font=info_font)
		default = 0
		tot = totalent
		ham = hament
		spam = spament
		self.popup(parent, controller)

	# Popup window for user to know their data has been saved.
	def popup(self, parent, controller):
		top = Toplevel()
		top.geometry('320x170')
		top.resizable(False, False)
		top.title("Save Completed")
		top.config(bg='deepskyblue4')

		label = Label(top, text="Dataset Information\nSaved!", bg='deepskyblue4', fg = "white", font = small_title_font)
		label.place(relx = .5, rely = .1, anchor = N)

		#Bottom part of screen
		fr1 = Frame(top, width = 400, height = 70, bg = 'lightblue2')
		fr1.place(relx=0.5, rely=1.0, anchor=S)
		b1 = Button(fr1, text="Go Back", highlightbackground="lightblue2", padx=50, command=lambda: [quitWindow(top), controller.show_frame(MainMenu)])
		b1.place(relx=0.5, rely=0.5, anchor=CENTER)


class ResultPage(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		#Label for Title
		fr1 = Frame(self, width = 570, height = 70, bg = 'deepskyblue4')
		fr1.place(relx=0.0, rely=0.0, anchor=NW)

		label = Label(fr1, text="Enter dataset information:", bg='deepskyblue4', fg = "white", font = title_font)
		label.place(relx = 0.5, rely = .5, anchor = CENTER)

		fr2 = Frame(self, width = 700, height = 5, bg = 'lightblue2')
		fr2.place(relx=0.5, rely=0.2, anchor=CENTER)

		fr3 = Frame(self, width = 700, height = 60, bg = 'lightblue2')
		fr3.place(relx=0.5, rely=1.0, anchor=CENTER)

	def load(self, parent, controller):
		#Return
		pass


#Creating a root and initializing attributes (foundation for GUI)
root = start()
root.geometry('550x350')
root.resizable(False, False)
root.title("Spam Detector")

# #Initializing pane to attach buttons and label to
# pane = Frame(root, width = 500, height = 500, bg = 'cadet blue', bd=30)
# pane.pack(fill = BOTH, expand = True)

# #Initializing font for the buttons.
# button_font = tkinter.font.Font(size = 18, weight = "bold") #
# label_font = tkinter.font.Font(size=25,weight="bold")

# #Button for the user view
# input_data = Button(pane, padx=10, width=15, text="Input Data", highlightbackground='cadet blue', command=input_file)
# input_data['font'] = button_font
# input_data.place(relx = .5, rely = .25, anchor = CENTER)


# #Saves current drop down option as opt
# opt = StringVar() 
# opt.set("Choose Algorithm")

# #Drop down menu to select a certain algorithm
# ddb = OptionMenu(pane, opt, *algorithms)
# ddb.config(bg = 'cadet blue')
# ddb["menu"].config(bg = 'cadet blue')
# ddb.place(relx = .20, rely = .35)

# #Button for inputting a data
# detect_spam = Button(pane, padx=3, width=5, text="Scan", highlightbackground='cadet blue', command = scan)
# detect_spam['font'] = button_font
# detect_spam.place(relx = .60, rely = .35)

# #Button for training data
# detect_spam = Button(pane, padx=3, width=5, text="Train The Data", highlightbackground='cadet blue', command = scan)
# detect_spam['font'] = button_font
# detect_spam.place(relx = .60, rely = .55)

# #Closes the program
# exit_menu = Button(pane, text="Quit", highlightbackground='cadet blue', fg='red', command=exitProgram)
# exit_menu['font'] = button_font
# exit_menu.place(relx=0.12, rely=1.1 ,anchor = SE)

# Main Loop
root.mainloop()
# exit()














