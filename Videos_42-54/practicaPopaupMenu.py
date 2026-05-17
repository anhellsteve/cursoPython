from tkinter import *
from tkinter import messagebox

root = Tk()

def infoMessage():
    messagebox.showinfo("Information", "This is an information message About 2026.")

def licenseMessage():
    messagebox.showwarning("License", "This is a license message FREE GNU.")

def exitMessage():
    #askquestion devuelve yes o no dependiendo de la respuesta del usuario
    '''exitRequest = messagebox.askquestion("Exit", "Are you sure you want to exit?")
    if exitRequest == "yes":
        root.quit()'''
    
    #askokcancel devuelve true o false dependiendo de la respuesta del usuario
    exitRequest = messagebox.askokcancel("Exit", "Are you sure you want to exit?")
    if exitRequest == True:
        root.quit()

def closeMessage():
    #askretrycancel devuelve true o false dependiendo de la respuesta del usuario
    exitRequest = messagebox.askretrycancel("Close", "Do you want to close the file?")
    if exitRequest == False:
        root.quit()

barMenu = Menu(root)
root.config(menu=barMenu, width=300, height=300)

menuFile = Menu(barMenu, tearoff=0)
menuFile.add_command(label="New")
menuFile.add_separator()
menuFile.add_command(label="Open")
menuFile.add_separator()
menuFile.add_command(label="Save")
menuFile.add_command(label="Save as...")
menuFile.add_separator()
menuFile.add_command(label="Close", command=closeMessage)
menuFile.add_separator()
menuFile.add_command(label="Exit", command=exitMessage)

menuEdit = Menu(barMenu, tearoff=0)
menuEdit.add_command(label="undo")
menuEdit.add_command(label="redo")
menuEdit.add_separator()
menuEdit.add_command(label="Copy")
menuEdit.add_command(label="Cut")
menuEdit.add_command(label="Paste")
menuEdit.add_separator()
menuEdit.add_command(label="Delete")



menuTools = Menu(barMenu, tearoff=0)

menuHelp = Menu(barMenu, tearoff=0)
menuHelp.add_command(label="License", command=licenseMessage)
menuHelp.add_command(label="About", command=infoMessage)

barMenu.add_cascade(label="File", menu=menuFile)
barMenu.add_cascade(label="Edit", menu=menuEdit)
barMenu.add_cascade(label="Tools", menu=menuTools)
barMenu.add_cascade(label="Help", menu=menuHelp)

root.mainloop()