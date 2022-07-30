from tkinter import *

raiz=Tk()

miFrame=Frame(raiz)
miFrame.pack()

#----------pantalla--------------------#
numeroPantalla=StringVar()

pantalla=Entry(miFrame,textvariable=numeroPantalla)
pantalla.grid(row=1,column=1,padx=10,pady=10,columnspan=4)
pantalla.config(background="black",fg="#03f943",justify="right")

#-------------pulsaciones teclado------------#

def numeroPuslsado(num):
    numeroPantalla.set(numeroPantalla.get()+num)



#---------------fila1------------------#

boton7=Button(miFrame,text="7",width=3,command=lambda:numeroPuslsado("7"))
boton7.grid(row=2,column=1)
boton8=Button(miFrame,text="8",width=3,command=lambda:numeroPuslsado("8"))
boton8.grid(row=2,column=2)
boton9=Button(miFrame,text="9",width=3,command=lambda:numeroPuslsado("9"))
boton9.grid(row=2,column=3)
botonDiv=Button(miFrame,text="/",width=3)
botonDiv.grid(row=2,column=4)


#---------------fila2------------------#

boton4=Button(miFrame,text="4",width=3,command=lambda:numeroPuslsado("4"))
boton4.grid(row=3,column=1)
boton5=Button(miFrame,text="5",width=3,command=lambda:numeroPuslsado("5"))
boton5.grid(row=3,column=2)
boton6=Button(miFrame,text="6",width=3,command=lambda:numeroPuslsado("6"))
boton6.grid(row=3,column=3)
botonMul=Button(miFrame,text="x",width=3)
botonMul.grid(row=3,column=4)


#---------------fila3------------------#

boton1=Button(miFrame,text="1",width=3,command=lambda:numeroPuslsado("1"))
boton1.grid(row=4,column=1)
boton2=Button(miFrame,text="2",width=3,command=lambda:numeroPuslsado("2"))
boton2.grid(row=4,column=2)
boton3=Button(miFrame,text="3",width=3,command=lambda:numeroPuslsado("3"))
boton3.grid(row=4,column=3)
botonRes=Button(miFrame,text="-",width=3)
botonRes.grid(row=4,column=4)


#---------------fila4------------------#

boton0=Button(miFrame,text="0",width=3,command=lambda:numeroPuslsado("0"))
boton0.grid(row=5,column=1)
botonComa=Button(miFrame,text=",",width=3,command=lambda:numeroPuslsado(","))
botonComa.grid(row=5,column=2)
botonIgual=Button(miFrame,text="=",width=3)
botonIgual.grid(row=5,column=3)
botonSuma=Button(miFrame,text="+",width=3)
botonSuma.grid(row=5,column=4)






raiz.mainloop()