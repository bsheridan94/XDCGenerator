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


w = Label(root, text="XDC Generator for Basys3") 
w.config(bg='black', fg='white',cursor='gumby')
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

CheckVar1 = IntVar()
CheckVar2 = IntVar()

sw = [["sw[0]", IntVar(), 1, Entry(root), "V17"], ["sw[1]", IntVar(), 1, Entry(root), "V16"], ["sw[2]", IntVar(), 1, Entry(root), "W16"], ["sw[3]", IntVar(), 1, Entry(root), "W17"], ["sw[4]", IntVar(), 1, Entry(root), "W15"], ["sw[5]", IntVar(), 1, Entry(root), "V15"], ["sw[6]", IntVar(), 1, Entry(root), "W14"], ["sw[7]", IntVar(), 1, Entry(root), "W13"]]


for i in range(len(sw)):
	print sw[i]
	sw[i][2] = Checkbutton(root, text = sw[i][0], variable = sw[i][1], \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 4)
	sw[i][2].pack()
	sw[i][3].pack()

	#print str(sw[i][3].get())


def generateConstraintsFile():
	ConstraintsFile = "MastaBasys1337.d\xdc" 
	outputFile = open(ConstraintsFile, 'w')
	outputFile.write("## switches")

	for i in range(len(sw)):
		if sw[i][1].get() == 1:
			outputFile.write("\nset_property PACKAGE_PIN "+ sw[i][4] + " [get_ports {" + sw[i][3].get() + 
				"}]")

generate = Button(text='Generate', command=generateConstraintsFile).pack(fill=X)


#listbox.pack()
root.mainloop()



