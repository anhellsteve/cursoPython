from tkinter import *
root = Tk()

varOption=IntVar()

def printer():
    print(varOption.get())
    if varOption.get()==1:
        etiqueta.config(text="You have selected male")
    elif varOption.get()==2:
        etiqueta.config(text="You have selected female")
    elif varOption.get()==3:
        etiqueta.config(text="You have selected other")

Label(root, text="Gender").pack()
Radiobutton(root, text="Male", variable=varOption, value=1, command=printer).pack()
Radiobutton(root, text="Female", variable=varOption, value=2, command=printer).pack()
Radiobutton(root, text="Other", variable=varOption, value=3, command=printer).pack()

etiqueta=Label(root)
etiqueta.pack()

root.mainloop()