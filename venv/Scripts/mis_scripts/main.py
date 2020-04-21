import lib
import random
import math
from numpy import log as ln
import statistics as stats
import matplotlib.pyplot as plt
from matplotlib.pyplot import style
import tabulate
import statistics

def menu():
    print("===================Bienvenidos===================")
    print("\nSeleccione la distribución:"
          "\n1 - Uniforme"
          "\n2 - Exponencial"
          "\n3 - Poisson"
          "\n4 - Normal"
          "\n0 - Salir")

def visualizar(numeros):
    print(sorted(numeros))
    print(len(numeros))


def main():
    op = -1
    while op != 0:
        menu()
        op = int(input("Ingrese su opción: "))
        if op == 1: #Uniforme

            cant_num = int(input("\nIngrese la cantidad de Valores: "))
            inter = int(input("Ingrese la cantidad de invervalos: "))
            lim_inf = float(input("Ingrese el límite inferior: "))
            lim_sup = float(input("Ingrese el límite superior: "))
            numeros = lib.aleatoria_uniforme(cant_num,lim_inf,lim_sup)

            ver = input("Desea ver los numeros generados (S/N): ")
            if ver in "sS":
                visualizar(numeros)
            lib.prueba_chi2(numeros, inter, 0, 0)


        if op == 2: #Exponencial

            cant_num = int(input("\nIngrese la cantidad de Valores: "))
            inter = int(input("Ingrese la cantidad de invervalos: "))
            l = float(input("Ingrese lambda (0 si desea ingresar u): "))
            u = 0
            if l == 0:
                u = float(input("Ingrese u: "))
                numeros = lib.aleatoria_exponencial(cant_num,0,u)
            else:
                numeros = lib.aleatoria_exponencial(cant_num, l, 0)

            ver = "n"
            ver = input("Desea ver los numeros generados (S/N): ")
            if ver in "sS":
                visualizar(numeros)
            print("\n======================== Prueba Chi de los numeros ========================")

            nueva_media = statistics.mean(numeros)
            lib.prueba_chi2(numeros, inter, 1, nueva_media)

        if op == 3: #Poisson

            cant_num = int(input("\nIngrese la cantidad de Valores: "))
            media = float(input("Ingrese lambda: "))
            numeros = lib.aleatoria_poisson(cant_num,media)

            ver = "n"
            ver = input("Desea ver los numeros generados (S/N): ")
            if ver in "sS":
                visualizar(numeros)

            nueva_media = statistics.mean(numeros)
            lib.poisson(numeros, 1, nueva_media)

        if op == 4: #Normal
            op2 = -1
            op2 = int(input("\n1 - Box - Muller"
                            "\n2 - Convolución"
                            "\nIngrese el método que desee: "))

            if op2 == 1:
                #Muller
                cant_num = int(input("\nIngrese la cantidad de Valores: "))
                inter = int(input("Ingrese la cantidad de invervalos: "))
                media = float(input("Ingrese la media (0 por defecto): "))
                des = float(input("Ingrese la desviación estándar (1 por defecto): "))
                numeros = lib.aleatoria_normal_muller(cant_num, media, des)
            if op2 == 2:
                cant_num = int(input("\nIngrese la cantidad de Valores: "))
                inter = int(input("Ingrese la cantidad de invervalos: "))
                media = float(input("Ingrese la media (0.5 por defecto): "))
                des = float(input("Ingrese la desviación estándar (0.083 por defecto): "))
                numeros = lib.aleatoria_normal_convolucion(cant_num, media , des )

            ver = "n"
            ver = input("Desea ver los numeros generados (S/N): ")
            if ver in "sS":
                visualizar(numeros)
            media = statistics.mean(numeros)
            lib.prueba_chi2(numeros, inter, 2, media)

if __name__ == '__main__':
    main()


