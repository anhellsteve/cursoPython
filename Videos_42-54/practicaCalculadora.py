from tkinter import *
root = Tk()
myFrame = Frame(root)
myFrame.pack()
operacion=""
reset_pantalla=False
resultado=0

# -------- Pantalla --------
numeroPantalla = StringVar()
pantalla = Entry(myFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")

# -------- programación de botones --------
def numeroPulsado(num):
    global operacion
    global reset_pantalla
    if reset_pantalla!=False:
        numeroPantalla.set(num)
        reset_pantalla=False
    else:
        numeroPantalla.set(numeroPantalla.get() + num)

# -------- Funcion Suma --------
def suma(num):
	global operacion
	global resultado
	global reset_pantalla
	resultado+=int(num) #resultado=resultado+int(num)
	operacion="suma"
	reset_pantalla=True
	numeroPantalla.set(resultado)

# -------- Funcion Resta --------
num1=0
contador_resta=0

def resta(num):
    global operacion
    global resultado
    global num1
    global contador_resta
    global reset_pantalla
    if contador_resta==0:
        num1=int(num)
        resultado=num1
    else:
        if contador_resta==1:
            resultado=num1-int(num)
        else:
            resultado=int(resultado)-int(num)	
            numeroPantalla.set(resultado)
            resultado=numeroPantalla.get()
    
    contador_resta=contador_resta+1
    operacion="resta"
    reset_pantalla=True

# -------- Funcion Multiplicacion --------
contador_multi=0

def multiplicacion(num):
	global operacion
	global resultado
	global num1
	global contador_multi
	global reset_pantalla
	if contador_multi==0:
		num1=int(num)
		resultado=num1
	else:
		if contador_multi==1:
			resultado=num1*int(num)
		else:
			resultado=int(resultado)*int(num)

		numeroPantalla.set(resultado)
		resultado=numeroPantalla.get()

	contador_multi=contador_multi+1
	operacion="multiplicacion"
	reset_pantalla=True

# -------- Funcion Division --------
contador_divi=0

def division(num):
	global operacion
	global resultado
	global num1
	global contador_divi
	global reset_pantalla
	if contador_divi==0:
		num1=float(num)
		resultado=num1
	else:
		if contador_divi==1:
			resultado=num1/float(num)
		else:
			resultado=float(resultado)/float(num)

		numeroPantalla.set(resultado)
		resultado=numeroPantalla.get()

	contador_divi=contador_divi+1
	operacion="division"
	reset_pantalla=True

# -------- Funcion Resultado --------
def el_resultado():
	global resultado
	global operacion
	global contador_resta
	global contador_multi
	global contador_divi
	if operacion=="suma":
		numeroPantalla.set(resultado+int(numeroPantalla.get()))
		resultado=0
	elif operacion=="resta":
		numeroPantalla.set(int(resultado)-int(numeroPantalla.get()))
		resultado=0
		contador_resta=0
	elif operacion=="multiplicacion":
		numeroPantalla.set(int(resultado)*int(numeroPantalla.get()))
		resultado=0
		contador_multi=0
	elif operacion=="division":
		numeroPantalla.set(int(resultado)/int(numeroPantalla.get()))
		resultado=0
		contador_divi=0

# -------- Fila 1 --------
btn7 = Button(myFrame, text="7", width=3, command=lambda: numeroPulsado("7"))
btn7.grid(row=2, column=1)
btn8 = Button(myFrame, text="8", width=3, command=lambda: numeroPulsado("8"))
btn8.grid(row=2, column=2)
btn9 = Button(myFrame, text="9", width=3, command=lambda: numeroPulsado("9"))
btn9.grid(row=2, column=3)
btndiv = Button(myFrame, text="/", width=3, command=lambda: division(numeroPantalla.get()))
btndiv.grid(row=2, column=4)

# -------- Fila 2 --------
btn4 = Button(myFrame, text="4", width=3, command=lambda: numeroPulsado("4"))
btn4.grid(row=3, column=1)
btn5 = Button(myFrame, text="5", width=3, command=lambda: numeroPulsado("5"))
btn5.grid(row=3, column=2)
btn6 = Button(myFrame, text="6", width=3, command=lambda: numeroPulsado("6"))
btn6.grid(row=3, column=3)
btnmult = Button(myFrame, text="*", width=3, command=lambda: multiplicacion(numeroPantalla.get()))
btnmult.grid(row=3, column=4)

# -------- Fila 3 --------
btn1 = Button(myFrame, text="1", width=3, command=lambda: numeroPulsado("1"))
btn1.grid(row=4, column=1)
btn2 = Button(myFrame, text="2", width=3, command=lambda: numeroPulsado("2"))
btn2.grid(row=4, column=2)
btn3 = Button(myFrame, text="3", width=3, command=lambda: numeroPulsado("3"))
btn3.grid(row=4, column=3)
btnrest = Button(myFrame, text="-", width=3, command=lambda: resta(numeroPantalla.get()))
btnrest.grid(row=4, column=4)

# -------- Fila 4 --------
btncoma = Button(myFrame, text=",", width=3, command=lambda: numeroPulsado(","))
btncoma.grid(row=5, column=1)
btn0 = Button(myFrame, text="0", width=3, command=lambda: numeroPulsado("0"))
btn0.grid(row=5, column=2)
btnigual = Button(myFrame, text="=", width=3, command=el_resultado)
btnigual.grid(row=5, column=3)
btnsuma = Button(myFrame, text="+", width=3, command=lambda: suma(numeroPantalla.get()))
btnsuma.grid(row=5, column=4)

root.mainloop()