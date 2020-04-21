import lib
import random
import math
from numpy import log as ln
import statistics as stats
import matplotlib.pyplot as plt
from matplotlib.pyplot import style
import tabulate
import statistics
import datos as dt


def main():

    accion = 'SPY'


    op2 = int(input("\n1 - Box - Muller"
                    "\n2 - Convolución"
                    "\nIngrese el método que desee: "))

    if op2 == 1:
        # Muller
        numeros = dt.getData(accion)
        inter = int(input("Ingrese la cantidad de invervalos: "))

    if op2 == 2:
        numeros = dt.getData(accion)
        inter = int(input("Ingrese la cantidad de invervalos: "))

    ver = "n"
    ver = input("Desea ver los numeros generados (S/N): ")
    if ver in "sS":
        visualizar(numeros)
    media = statistics.mean(numeros)
    lib.prueba_chi2(numeros, inter, 2, media)


def visualizar(numeros):
    print(sorted(numeros))
    print(len(numeros))

if __name__ == '__main__':
    main()