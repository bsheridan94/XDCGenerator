#!/usr/bin/python
from Tkinter import *
from tkMessageBox import *
from tkFileDialog  import askopenfilename 
import Tkinter
import tkMessageBox



root = Tkinter.Tk()
menubar = Menu(root) 
filemenu = Menu(menubar) 
# Code to add widgets will go here...
root.title("Testing")


w = Label(root, text="Hello, world!") 
w.config(bg='black', fg='blue',cursor='gumby')
w.pack()
number = IntVar()


counter = 0
def helloCallBack():
	if (CheckVar1.get()==1 and CheckVar2.get()==0):
		tkMessageBox.showinfo(title="Hello",message= "Hello Python")
	
def quit():
	print "Exiting the program"
	root.quit()

filemenu.add_command(label="Open", command=helloCallBack) 
filemenu.add_separator()
filemenu.add_command(label="Exit",command=quit)
menubar.add_cascade(label="File", menu=filemenu) 
root.config(menu=menubar) 

quitButton = Tkinter.Button(root, text ="Quit", command = quit)
B = Tkinter.Button(root, text ="Hello", command = helloCallBack)
B.pack(side=TOP)
quitButton.pack()

def mouseEntered(event): 
	button = event.widget 
	button.config(text = "Please Please click me")

def mouseExited(event): 
	button = event.widget 
	button.config(text = "Logon") 

b = Button(root, text="Logon") 
b.bind("<Enter>",mouseEntered) 
b.bind("<Leave>",mouseExited) 
b.pack()


CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(root, text = "Check Me", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 10)
C2 = Checkbutton(root, text = "Dont Check Me", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 10)
C1.pack()
C2.pack(side=TOP)

listbox = Listbox(root)


for i in range(5):
    listbox.insert(END, str(i))



def callback():
    if askyesno('Verify', 'Do you really want to quit?'):
        showwarning('Yes', 'Quit not yet implemented')
    else:
        showinfo('No', 'Quit has been cancelled')
 
errmsg = 'Sorry, no Spam allowed!'
Button(text='Quit', command=callback).pack(fill=X)
Button(text='Spam', command=(lambda: showerror('Spam', errmsg))).pack(fill=X)

e1 = Entry(root)
e1.pack()


text = Text(root)
text.pack(side=TOP)


def openFile():
	choosen = askopenfilename(initialdir='~')
	text.insert(END, open(choosen).read()) 


quitButton = Tkinter.Button(root, text ="Open Text", command = openFile)
quitButton.pack()

#listbox.pack()
root.mainloop()
