from tkinter import *
from tkinter import filedialog

root=Tk()
root.config(width=400, height=300)

def openFile():
    file = filedialog.askopenfilename(title="Open File", initialdir="C:/", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    print(file)

btn = Button(root, text="Open File", command=openFile)
btn.pack()

root.mainloop()