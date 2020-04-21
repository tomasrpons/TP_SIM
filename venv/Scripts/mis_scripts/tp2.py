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


    op2 = int(input("\n1  K-S"
                    "\n2  Chi Cuadrado"
                    "\nIngrese el método que desee: "))

    if op2 == 1:
        # Muller
        numeros = dt.getData(accion)
        lib.prueba_ks(numeros, 20, 2)

    if op2 == 2:
        numeros = dt.getData(accion)
        lib.prueba_chi2(numeros, 20, 2, statistics.mean(numeros))


if __name__ == '__main__':
    main()