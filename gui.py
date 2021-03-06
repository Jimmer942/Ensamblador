#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.filedialog
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from math import *

from funciones.selector import select
from funciones.BinToHex import BinToHex

ventana=Tk()
ventana.title("Modulo traductor")
ventana.geometry("1000x700")
ventana.configure(background="gray29")
color_boton=("SpringGreen4")
lbl = Label(ventana,text = "Prueba", font =("Arial Bold",50)).place(x=50, y = 450)
recuadro = Text(ventana)
recuadro.config(fg="linen",bg="gray13",width=28,height=25)
recuadro.place(x=755,y=60)
recuadro.insert(INSERT,"Comandos: \n")
recuadro.insert(INSERT,"Se debe usar $ para las     variables de registro \n")
recuadro.insert(INSERT,"con la variable $0 de debe  tener un espacio antes de lasiguiente (,).\n\n\n")

recuadro.insert([5.1],"COMANDOS DE DOS CARACTERES\n\n")
recuadro.insert([6.1],"or  $rd,$rs,$rt \n\n\n")
recuadro.insert([7.1],"sb  $rt,imm(rs) \n")
recuadro.insert([8.1],"lb  $rt,imm(rs) \n")

recuadro.insert([10.1],"TRES CARACTERES\n\n")
recuadro.insert([11.1],"add $rd,$rs,$rt  \n")
recuadro.insert([12.1],"sub $rd,$rs,$rt  \n")
recuadro.insert([13.1],"xor $rd,$rs,$rt  \n")
recuadro.insert([14.1],"slt $rd,$rs,$rt  \n")
recuadro.insert([15.1],"sll $rd,$rt,shamt  \n")
recuadro.insert([16.1],"beq $rs,$rt,label \n")
recuadro.insert([17.1],"ori $rt,$rs,imm \n")

recuadro.insert([19.1],"CUATRO CARACTERES\n\n")
recuadro.insert([20.1],"addi$rt,$rs,imm \n")
recuadro.insert([21.1],"blez$rs,label \n")

recuadro.config(state= DISABLED)


textoin=" "
ancho_boton=11
alto_boton=3
input_text=StringVar()
operador=""

Entradaconsola= Text(ventana)
Entradaconsola.config(width=100,height=25)
Entradaconsola.place(x=30,y=60)

def convert():
    Consola.delete('1.0', END)
    s = Entradaconsola.get("1.0",END)
    inst = list(s.split("\n"))
    for i in inst:
        st = select(i)
        hexa = BinToHex(st)
        Consola.insert(INSERT, hexa +'\n')

def export():
    ventana.filename = tkinter.filedialog.asksaveasfilename(defaultextension='.txt')
    f = open(ventana.filename, 'w')
    f.write(Consola.get('1.0', 'end'))
    f.close()
    tkinter.messagebox.showinfo('FYI', 'File Saved')


Boton=Button(ventana,bd=0,text="Start",bg=color_boton,width=ancho_boton,height=alto_boton, command=convert)
Boton.grid(column=1,row=1)
Boton1=Button(ventana,bd=0,text="Export data",bg=color_boton,width=ancho_boton,height=alto_boton, command=export)
Boton1.grid(column=2,row=1)

Consola = Text(ventana)
Consola.config(width=137,height=15)
Consola.place(x=15,y=430)

Entradaconsola.tag_add("line1","1.0","1.7")
Consola.tag_add("line2","1.0","1.7")

ventana.mainloop()
