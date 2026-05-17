from tkinter import *

root = Tk()

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
menuFile.add_command(label="Close")
menuFile.add_separator()
menuFile.add_command(label="Exit", command=root.quit)

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
menuHelp.add_command(label="Documentation")
menuHelp.add_command(label="About")

barMenu.add_cascade(label="File", menu=menuFile)
barMenu.add_cascade(label="Edit", menu=menuEdit)
barMenu.add_cascade(label="Tools", menu=menuTools)
barMenu.add_cascade(label="Help", menu=menuHelp)

root.mainloop()