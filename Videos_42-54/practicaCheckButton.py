from tkinter import *

root = Tk()

root.title("Ejemplo CheckButton")

beach=IntVar()
mountain=IntVar()
city=IntVar()

def travelOptions():
    optionchosen=""
    if beach.get()==1:
        optionchosen+="Beach "
    if mountain.get()==1:
        optionchosen+="Mountain "
    if city.get()==1:
        optionchosen+="City "
    finalText.config(text=optionchosen)

foto=PhotoImage(file=r"D:\Dev_Projects\VS Projects\cursoPython\Videos_42-54\avion.png")
Label(root, image=foto).pack()

frame = Frame(root)
frame.pack()

label = Label(frame, text="Where do you want to go?").pack()

Checkbutton(frame, text="Beach", variable=beach, onvalue=1, offvalue=0, command=travelOptions).pack()
Checkbutton(frame, text="Mountain", variable=mountain, onvalue=1, offvalue=0, command=travelOptions).pack()
Checkbutton(frame, text="City", variable=city, onvalue=1, offvalue=0, command=travelOptions).pack()

finalText=Label(frame)
finalText.pack()

root.mainloop()