import tkinter as tk
from tkinter import ttk
from tkinter import StringVar
from tkinter import IntVar
from tkinter import *


import lib
import random
import math
import numpy as np
from numpy import log as ln
import statistics as stats
import matplotlib.pyplot as plt
from matplotlib.pyplot import style
import tabulate
import statistics
import pandas as pd
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure



raiz = tk.Tk()
raiz.state('zoomed')


def codigoBoton():
    tabla.delete(*tabla.get_children())
    tabla2.delete(*tabla2.get_children())

    if opciones.get() == "Uniforme":
        numeros = lib.aleatoria_uniforme(int(cantidad.get()), int(inferior.get()), int(superior.get()))
        df = pd.DataFrame(numeros, columns=['Valores'])
        cols = list(df.columns)
        tabla["columns"] = cols

        for i in cols:
            tabla.column(i,width=50)
            tabla.column(i, anchor="w")
            tabla.heading(i, text=i, anchor='w')

        for index, row in df.iterrows():
            tabla.insert("", 0, text=index, values=list(row))

        res, valor_critico, suma, df_datos = lib.prueba_chi2(numeros, int(intervalos.get()), 0, 0)
        resultado.configure(text=res)
        est.configure(text="El estadístico de prueba es: " + str(suma))
        vc.configure(text="El valor crítico con 95% de significancia es: " + str(valor_critico))

        fig = Figure(figsize=(8, 6), dpi=100)
        ax = fig.add_subplot(111)
        df.plot.hist(bins=12, alpha=0.5, ax=ax)
        canvas = FigureCanvasTkAgg(fig, master=raiz)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().grid(row=50, column=2)

        cols2 = list(df_datos.columns)
        tabla2["columns"] = cols2
        for i in cols2:
            tabla2.column(i,width=50)
            tabla2.column(i, anchor="w")
            tabla2.heading(i, text=i, anchor='w')

        for index, row in df_datos.iterrows():
            tabla2.insert("", 0, text=index, values=list(row))


    if opciones.get() == "Poisson":
        numeros = lib.aleatoria_poisson(int(cantidad.get()), float(media.get()))
        print(numeros)
        df = pd.DataFrame(numeros, columns=['Valores'])
        cols = list(df.columns)
        tabla["columns"] = cols

        for i in cols:
            tabla.column(i, width=50)
            tabla.column(i, anchor="w")
            tabla.heading(i, text=i, anchor='w')

        for index, row in df.iterrows():
            tabla.insert("", 0, text=index, values=list(row))

        res, valor_critico, suma, df_datos = lib.poisson(numeros, 1, stats.mean(numeros))
        resultado.configure(text=res)
        est.configure(text="El estadístico de prueba es: " + str(suma))
        vc.configure(text="El valor crítico con 95% de significancia es: " + str(valor_critico))

        fig = Figure(figsize=(8, 6), dpi=100)
        ax = fig.add_subplot(111)
        df.plot.hist(bins=12, alpha=0.5, ax=ax)
        canvas = FigureCanvasTkAgg(fig, master=raiz)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().grid(row=50, column=2)

        cols2 = list(df_datos.columns)
        tabla2["columns"] = cols2
        for i in cols2:
            tabla2.column(i, width=50)
            tabla2.column(i, anchor="w")
            tabla2.heading(i, text=i, anchor='w')

        for index, row in df_datos.iterrows():
            tabla2.insert("", 0, text=index, values=list(row))


    if opciones.get() == "Exponencial":
        if v2.get() == 2:
            numeros = lib.aleatoria_exponencial(int(cantidad.get()), float(lam.get()), 0)
        elif v2.get() == 1:
            numeros = lib.aleatoria_exponencial(int(cantidad.get()), 0, float(media.get()))

        df = pd.DataFrame(numeros, columns=['Valores'])
        cols = list(df.columns)
        tabla["columns"] = cols

        for i in cols:
            tabla.column(i, width=50)
            tabla.column(i, anchor="w")
            tabla.heading(i, text=i, anchor='w')

        for index, row in df.iterrows():
            tabla.insert("", 0, text=index, values=list(row))

        res, valor_critico, suma, df_datos = lib.prueba_chi2(numeros, int(intervalos.get()), 1, stats.mean(numeros))

        resultado.configure(text=res)
        est.configure(text="El estadístico de prueba es: " + str(suma))
        vc.configure(text="El valor crítico con 95% de significancia es: " + str(valor_critico))

        fig = Figure(figsize=(8, 6), dpi=100)
        ax = fig.add_subplot(111)
        df.plot.hist(bins=12, alpha=0.5, ax=ax)
        canvas = FigureCanvasTkAgg(fig, master=raiz)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().grid(row=50, column=2)

        cols2 = list(df_datos.columns)
        tabla2["columns"] = cols2
        for i in cols2:
            tabla2.column(i,width=50)
            tabla2.column(i, anchor="w")
            tabla2.heading(i, text=i, anchor='w')

        for index, row in df_datos.iterrows():
            tabla2.insert("", 0, text=index, values=list(row))

    if opciones.get() == "Normal":

        if v3.get() == 2:
            ## CONVOLUCION
            numeros = lib.aleatoria_normal_convolucion(int(cantidad.get()), float(media.get()), float(desv.get()))
        elif v3.get() == 1:
            ## BOX MULLER
            numeros = lib.aleatoria_normal_muller(int(cantidad.get()), float(media.get()), float(desv.get()))

        df = pd.DataFrame(numeros, columns=['Valores'])
        cols = list(df.columns)
        tabla["columns"] = cols

        for i in cols:
            tabla.column(i, width=50)
            tabla.column(i, anchor="w")
            tabla.heading(i, text=i, anchor='w')

        for index, row in df.iterrows():
            tabla.insert("", 0, text=index, values=list(row))

        res, valor_critico, suma, df_datos = lib.prueba_chi2(numeros, int(intervalos.get()), 2, statistics.mean(numeros))


        resultado.configure(text=res)
        est.configure(text="El estadístico de prueba es: " + str(suma))
        vc.configure(text="El valor crítico con 95% de significancia es: " + str(valor_critico))

        fig = Figure(figsize=(8, 6), dpi=100)
        ax = fig.add_subplot(111)
        df.plot.hist(bins=12, alpha=0.5, ax=ax)
        canvas = FigureCanvasTkAgg(fig, master=raiz)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().grid(row=50, column=2)

        cols2 = list(df_datos.columns)
        tabla2["columns"] = cols2
        for i in cols2:
            tabla2.column(i,width=50)
            tabla2.column(i, anchor="w")
            tabla2.heading(i, text=i, anchor='w')

        for index, row in df_datos.iterrows():
            tabla2.insert("", 0, text=index, values=list(row))


def media_o_lambda():
    if v2.get() == 2:
        media.configure(state='disabled')
        lam.configure(state='normal')
    elif v2.get() == 1:
        lam.configure(state='disabled')
        media.configure(state='normal')


def seleccion(index, value, op):
    if opciones.get() == "Uniforme":
        cantidad.configure(state='normal')
        intervalos.configure(state='normal')
        superior.configure(state='normal')
        inferior.configure(state='normal')
        lam.configure(state='disabled')
        media.configure(state='disabled')
        desv.configure(state='disabled')
        radioButton1.configure(state='disabled')
        radioButton2.configure(state='disabled')
        radioButton3.configure(state='disabled')
        radioButton4.configure(state='disabled')

    if opciones.get() == "Poisson":
        cantidad.configure(state='normal')
        lam.configure(state='normal')
        media.configure(state='disabled')
        desv.configure(state='disabled')
        superior.configure(state='disabled')
        inferior.configure(state='disabled')
        intervalos.configure(state='disabled')
        radioButton1.configure(state='disabled')
        radioButton2.configure(state='disabled')
        radioButton3.configure(state='disabled')
        radioButton4.configure(state='disabled')

    if opciones.get() == "Exponencial":
        cantidad.configure(state='normal')
        intervalos.configure(state='normal')
        lam.configure(state='disabled')
        media.configure(state="disabled")
        desv.configure(state='disabled')
        superior.configure(state='disabled')
        inferior.configure(state='disabled')
        radioButton1.configure(state='normal')
        radioButton2.configure(state='normal')
        radioButton3.configure(state='disabled')
        radioButton4.configure(state='disabled')

    if opciones.get() == "Normal":
        lam.configure(state='disabled')
        cantidad.configure(state='normal')
        intervalos.configure(state='normal')
        media.configure(state='normal')
        desv.configure(state='normal')
        superior.configure(state='disabled')
        inferior.configure(state='disabled')
        radioButton1.configure(state='disabled')
        radioButton2.configure(state='disabled')
        radioButton3.configure(state='normal')
        radioButton4.configure(state='normal')


miFrame = tk.Frame(raiz, width=1200, height=600)
miFrame.grid()

cantidad = tk.Entry(miFrame, state='disabled')
cantidad.grid(row=2, column=1)

intervalos = tk.Entry(miFrame, state='disabled')
intervalos.grid(row=1, column=1)

label_cantidad = tk.Label(miFrame, text="Cantidad de numeros: ")
label_cantidad.grid(row=2, column=0)

label_intervalos = tk.Label(miFrame, text="Cantidad de intervalos: ")
label_intervalos.grid(row=1, column=0)

label_superior = tk.Label(miFrame, text="Limite superior: ")
label_superior.grid(row=7, column=0)

label_inferior = tk.Label(miFrame, text="Limite inferior: ")
label_inferior.grid(row=8, column=0)

superior = tk.Entry(miFrame, state='disabled')
superior.grid(row=7, column=1)

inferior = tk.Entry(miFrame, state='disabled')
inferior.grid(row=8, column=1)

v = StringVar()
v.trace('w', seleccion)
opciones = ttk.Combobox(raiz, textvar=v)
opciones['values'] = ('Uniforme', 'Exponencial', 'Poisson', 'Normal')
opciones.place(x=200, y=0)

label_opciones = tk.Label(miFrame, text="Ingrese su opcion: ")
label_opciones.grid(row=0, column=0)

media = tk.Entry(miFrame, state='disabled')
media.grid(row=3, column=1)

label_media = tk.Label(miFrame, text="Media(µ):")
label_media.grid(row=3, column=0)

v1 = StringVar()
v1.trace('w', media_o_lambda)
lam = tk.Entry(miFrame, state='disabled', textvar=v1)
lam.grid(row=4, column=1)

label_lam = tk.Label(miFrame, text="Lambda(λ): ")
label_lam.grid(row=4, column=0)

desv = tk.Entry(miFrame, state='disabled')
desv.grid(row=6, column=1)

label_desv = tk.Label(miFrame, text="Desviacion(σ): ")
label_desv.grid(row=6, column=0)

boton_generar = tk.Button(raiz, text="Generar", command=codigoBoton)
boton_generar.place(x=500, y=250)

tabla = ttk.Treeview()
tabla.place(x=500, y=0)

tabla2 = ttk.Treeview()
tabla2.place(x=900,y=0)

label_resultado = tk.Label(miFrame, text="Resultado de la prueba Chi Cuadrado: ")
label_resultado.grid(row=13, column=0)

resultado = tk.Label(miFrame, text="")
resultado.grid(row=14, column=0)

est = tk.Label(miFrame, text="")
est.grid(row=15, column=0)

vc = tk.Label(miFrame, text="")
vc.grid(row=16, column=0)

v2 = IntVar()
radioButton1 = Radiobutton(miFrame, text = 'Media', variable=v2, value=1, command=media_o_lambda, state='disabled')
radioButton1.grid(row=3, column=2)

radioButton2 = Radiobutton(miFrame, text = 'Lambda', variable=v2, value=2, command=media_o_lambda, state='disabled')
radioButton2.grid(row=4, column=2)

v3 = IntVar()
radioButton3 = Radiobutton(miFrame, text = 'Box Muller', variable=v3, value=1, state='disabled')
radioButton3.grid(row=7, column=2)

radioButton4 = Radiobutton(miFrame, text = 'Convolucion', variable=v3, value=2, state='disabled')
radioButton4.grid(row=6, column=2)


raiz.mainloop()
