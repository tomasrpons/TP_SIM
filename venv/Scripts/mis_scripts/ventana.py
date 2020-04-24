import tkinter as tk
from tkinter import ttk

raiz = tk.Tk()
raiz.geometry("800x500")


def codigoBoton():
    print(2)




def main():

    miFrame = tk.Frame(raiz,width=1200, height=600)
    miFrame.grid()

    cantidad = tk.Entry(miFrame)
    cantidad.grid(row=2, column=1)

    intervalos = tk.Entry(miFrame)
    intervalos.grid(row=1,column=1)

    label_cantidad = tk.Label(miFrame,text="Cantidad de numeros:")
    label_cantidad.grid(row=2, column=0)

    label_intervalos = tk.Label(miFrame,text="Cantidad de intervalos:")
    label_intervalos.grid(row=1,column=0)

    opciones= ttk.Combobox(raiz)
    opciones['values'] = ('Uniforme','Exponencial','Poisson','Normal')
    opciones.grid(column=1,row=0)
    opciones.place(x=127,y=0)

    label_opciones = tk.Label(miFrame, text="Ingrese su opcion:")
    label_opciones.grid(row=0, column=0)

    media = tk.Entry(miFrame, state='disabled')
    media.grid(row=3, column=1)

    label_media = tk.Label(miFrame, text="Media:", state='disabled')
    label_media.grid(row=3, column=0)

    varianza = tk.Entry(miFrame, state='disabled')
    varianza.grid(row=4, column=1)

    label_varianza = tk.Label(miFrame, text="Varianza:")
    label_varianza.grid(row=4, column=0)

    lam = tk.Entry(miFrame, state='disabled')
    lam.grid(row=5, column=1)

    label_lam = tk.Label(miFrame, text="Lambda:")
    label_lam.grid(row=5, column=0)

    mini = tk.Entry(miFrame, state='disabled')
    mini.grid(row=6, column=1)

    label_mini = tk.Label(miFrame, text="Minimo(A):")
    label_mini.grid(row=6, column=0)

    maxi = tk.Entry(miFrame, state='disabled')
    maxi.grid(row=7, column=1)

    label_maxi = tk.Label(miFrame, text="Máximo(B):")
    label_maxi.grid(row=7, column=0)

    med = tk.Entry(miFrame, state='disabled')
    med.grid(row=8, column=1)

    label_med = tk.Label(miFrame, text="Media(µ):")
    label_med.grid(row=8, column=0)

    desv = tk.Entry(miFrame, state='disabled')
    desv.grid(row=9, column=1)

    label_desv = tk.Label(miFrame, text="Desviacion(σ):")
    label_desv.grid(row=9, column=0)

    boton_generar = tk.Button(raiz, text="Generar",command=codigoBoton)
    boton_generar.grid(row=10, column=1)

    numeros = [1,2,3,4]
    tabla = ttk.Treeview()
    tabla.place(x=350,y=0)
    tabla['columns'] = ("numero")
    tabla.heading("numero", text="numero", anchor="w")
    for i in range(len(numeros)):
        tabla.insert("",tk.END, text=str(i), values=(str(numeros[i])))

    raiz.mainloop()

if __name__ == '__main__':
    main()