#!/usr/bin/python
from Tkinter import *
from tkMessageBox import *
from tkFileDialog  import askopenfilename 
import Tkinter
import tkMessageBox


def importConstrainsFile():
	print "Importing constrains file\n"


def helloCallBack():
	if (CheckVar1.get()==1 and CheckVar2.get()==0):
		tkMessageBox.showinfo(title="Hello",message= "Hello Python")
	
def quit():
	print "Exiting the program"
	root.quit()


def generateConstraintsFile():
	ConstraintsFile = "MastaBasys1337.xdc" 
	outputFile = open(ConstraintsFile, 'w')
	outputFile.write("## switches")

	for i in range(len(sw)):
		if sw[i][1].get() == 1:
			outputFile.write("\nset_property PACKAGE_PIN "+ sw[i][4] + " [get_ports {" + sw[i][3].get() + 
				"}]")
			outputFile.write("\n\tset_property IOSTANDARD LVCMOS33 [" + sw[i][3].get() + 
				"}]")



if __name__ == '__main__':
	root = Tkinter.Tk()
	menubar = Menu(root) 
	filemenu = Menu(menubar) 
	root.title("XDC Gen")


	w = Label(root, text="XDC Generator for Basys3") 
	w.config(bg='black', fg='white',cursor='gumby')
	w.pack()
	number = IntVar()


	counter = 0

	filemenu.add_command(label="Open", command=helloCallBack) 
	filemenu.add_separator()
	filemenu.add_command(label="Import",command=importConstrainsFile)
	filemenu.add_separator()
	filemenu.add_command(label="Exit",command=quit)
	menubar.add_cascade(label="File", menu=filemenu) 
	root.config(menu=menubar) 


	sw = [["sw[0]", IntVar(), 1, Entry(root), "V17"], ["sw[1]", IntVar(), 1, Entry(root), "V16"], ["sw[2]", IntVar(), 1, Entry(root), "W16"], ["sw[3]", IntVar(), 1, Entry(root), "W17"], ["sw[4]", IntVar(), 1, Entry(root), "W15"], ["sw[5]", IntVar(), 1, Entry(root), "V15"], ["sw[6]", IntVar(), 1, Entry(root), "W14"], ["sw[7]", IntVar(), 1, Entry(root), "W13"], ["sw[8]", IntVar(), 1, Entry(root), "V2"], ["sw[9]", IntVar(), 1, Entry(root), "T3"], ["sw[10]", IntVar(), 1, Entry(root), "T2"], ["sw[11]", IntVar(), 1, Entry(root), "R3"], ["sw[12]", IntVar(), 1, Entry(root), "W2"], ["sw[13]", IntVar(), 1, Entry(root), "U1"], ["sw[14]", IntVar(), 1, Entry(root), "T1"], ["sw[15]", IntVar(), 1, Entry(root), "R2"]]


	led = [["led[0]", IntVar(), 1, Entry(root), "U16"],["led[1]", IntVar(), 1, Entry(root), "E19"],["led[2]", IntVar(), 1, Entry(root), "U19"],["led[3]", IntVar(), 1, Entry(root), "V19"],["led[4]", IntVar(), 1, Entry(root), "W18"],["led[5]", IntVar(), 1, Entry(root), "U15"],["led[6]", IntVar(), 1, Entry(root), "U14"],["led[7]", IntVar(), 1, Entry(root), "V14"],["led[8]", IntVar(), 1, Entry(root), "V13"],["led[9]", IntVar(), 1, Entry(root), "V3"],["led[10]", IntVar(), 1, Entry(root), "W3"],["led[11]", IntVar(), 1, Entry(root), "U3"],["led[12]", IntVar(), 1, Entry(root), "P3"],["led[13]", IntVar(), 1, Entry(root), "N3"],["led[14]", IntVar(), 1, Entry(root), "P1"],["led[15]", IntVar(), 1, Entry(root), "L1"]]


	for i in range(len(sw)):
		print sw[i]
		sw[i][2] = Checkbutton(root, text = sw[i][0], variable = sw[i][1], \
	                 onvalue = 1, offvalue = 0, height=1, \
	                 width = 4)
		sw[i][2].pack()
		sw[i][3].pack()


	for i in range(len(led)):
		print led[i]
		led[i][2] = Checkbutton(root, text = led[i][0], variable = led[i][1], \
	                 onvalue = 1, offvalue = 0, height=1, \
	                 width = 4)
		led[i][2].pack()
		led[i][3].pack()





	generate = Button(text='Generate', command=generateConstraintsFile).pack(fill=X)

	#listbox.pack()
	root.mainloop()



