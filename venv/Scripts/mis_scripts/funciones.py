import pandas as pd
from scipy.stats import chisquare
from scipy import stats
from scipy.stats import chi2_contingency
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
import random
import math
import calculos as ca


##Función matematica lineal
def func_aleatoria_lineal(x, a, m, c):
    resultado = (a * x + c) % m
    return resultado


##Genera un numero aleatorio siguiendo el método lineal. Devuelve también el próximo valor de x y A*x + C para generar la tabla
def generador_aleatorio_lineal(x, k, g, c):
    a = 1 + 4 * k
    m = 2 ** g
    xi = func_aleatoria_lineal(x, a, m, c)
    ri = truncate((xi / (m)), 4)
    return (a * x) + c, xi, ri


##Función matemática multiplicativa
def funcion_aleatoria_multiplicativa(a, x, m):
    return func_aleatoria_lineal(x, a, m, 0)


##Genera un número aleatorio siguiendo el método multiplicativo. Devuelve también el próximo valor de x y A*x para generar la tabla
def generador_aleatorio_multiplicativo(x, k, g):
    a = 3 + 8 * k
    m = 2 ** g
    xi = funcion_aleatoria_multiplicativa(x, a, abs(m))
    ri = truncate((xi / (m - 1)), 4)
    return a * x, xi, ri


## Este método devuelve el valor de lambda cuadrado obtenido de la columna de la tabla de Chi-Cuadrado correspondiente al valor alpha = 0.05
##Ya que el string esta con "," la función replace es utilzada para reemplazar con "."
def valor_puntual(grados_libertad):
    lista = ['3,8415', '5,9915', '7,8147', '9,4877', '11,0705', '12,5916', '14,0671', '15,5073', '16,9190', '18,3070',
             '19,6752', '21,0261', '22,3620', '23,6848', '24,9958', '26,2962', '27,5871', '28,8693', '30,1435',
             '31,4104', '32,6706', '33,9245', '35,1725', '36,4150', '37,6525', '38,8851', '40,1133', '41,3372',
             '42,5569', '43,7730', '44,9853', '46,1942', '47,3999', '48,6024', '49,8018', '50,9985', '52,1923',
             '53,3835', '54,5722', '55,7585', '61,6562', '67,5048', '73,3115', '79,0820', '90,5313', '101,8795',
             '113,1452', '124,3421', '146,5673', '168,6130', '190,5164', '212,3039', '233,9942', '287,8815', '341,3951',
             '553,1269', '658,0936']
    x = lista[grados_libertad - 1].replace(",", ".")
    return float(x)


def truncate(number, digits) -> float:  ##Esta función sirve para truncar los decimales
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper


## Este es el método correspondiente a la prueba chi, toma como parámetro una lista de numeros y una cantidad de intervalos.
def prueba_chi2(numeros, cant_int):
    paso = 1 / cant_int  ##Esta variable me permite generar los intervalos
    inicio = 0
    intervalos = []
    contador = []
    esperado = len(
        numeros) / cant_int  # Aqui obtenemos el valor de frecuencia esperado para cada intervalo siguiendo una distribución uniforme.
    frec_esperada = []
    for i in range(cant_int):  ## En este ciclo creamos los intervalos, la cantidad de contadores y la columna esperados
        inicio += paso
        intervalos.append(truncate(inicio, 4))  ##Ver función truncate(numero, cant_decimales)
        contador.append(0)
        frec_esperada.append(
            esperado)  ##Para cada una de las listas agregamos 0 para el contador, y esperado para la frecuenia esperada.

    for i in range(len(
            numeros)):  ##Para cada numero analiza el intervalo en el cual se encuentra y acumula 1 al valor. Aqui vemos la frecuencia obtenida.
        for j in range(cant_int):
            if numeros[i] <= intervalos[j]:
                if numeros[i] > intervalos[j] - paso:
                    contador[j] += 1
                    break

    est_prueba = []
    sumatoria = []
    suma = 0
    for i in range(
            cant_int):  ##Debido a que los numeros generados tienen demasiados decimales, con este método truncamos a 4 todos los obtenidos.
        a = ((frec_esperada[i] - contador[i]) ** 2) / frec_esperada[i]
        a = truncate(a, 4)
        est_prueba.append(a)
        suma += a
        sumatoria.append(suma)
    interval = []
    anterior = 0
    for i in range(cant_int):  ##Crea un array de string para imprimir de que valor min a max van los intervalos.
        interval.append("De " + str(anterior) + " a " + str(intervalos[i]))
        anterior = intervalos[i]
    resultados = {'Intervalos': interval, 'FO': contador, 'FE': frec_esperada, 'C': est_prueba, 'C(AC)': sumatoria}
    res = tabulate(resultados, headers=['Intervalos', 'FO', 'FE', 'C', 'C(AC)'],
                   tablefmt='fancy_grid')  ##Creamos la tabla para imprimir con la librería tabulate
    print(res)

    # ES Ordenado, SI LO QUEREMOS POR COMO APARECIERON SOLO HAY QUE SACAR EL SORTED
    num = {'Número': sorted(numeros)}
    num_list = tabulate(num, headers=['Número'], tablefmt='fancy_grid',
                        showindex=True)  ##Imprimimos a modo de tabla los valores obtenidos.
    print(num_list)

    aux = [0]
    for i in range(cant_int):
        aux.append(intervalos[i])

    plt.hist(numeros, bins=aux,
             edgecolor='black')  ##Utilizamos la libreria Pandas para crear DataFrames para poder generar los gráficos.
    plt.axhline(y=esperado, xmin=0, xmax=1, color="red")
    plt.xlabel('Intervalos')
    plt.ylabel('Frecuencia')
    plt.legend('EO')
    plt.title('Distribucion de los valores acuerdo a su frecuencia')
    plt.grid()
    plt.show()
    valor_critico = valor_puntual(
        cant_int - 1)  ##Obtenemos el valor crítico para comparar con el estadístico de prueba.
    print("El valor crítico con 95% de significancia es: ", valor_critico)
    print("El estadístico de prueba es: ", suma)
    if valor_critico > suma:
        print("No se puede rechazar la hipótesis nula")
    else:
        print("Se rechaza la hipóteis nula")
    print("\n")


## Método utilizado en la OP 1 - 1, es el encargado de ejecutar el primer punto del tp.
def metodo_multiplicativo():
    x = int(input('\nIngrese el primer valor: '))
    k = int(input('Ingrese el valor de k: '))
    g = int(input('Igrese el valor de g: '))

    numeros = []
    xi_mas_uno = []
    a_xi = []
    for i in range(20):  ##Genera 20 numeros aleatorios, tiene tres retornos, el número aleatorio
        ai, xi, ri = generador_aleatorio_multiplicativo(x, k, g)  # el proximo valor de x y el valor del a*x
        numeros.append(ri)
        xi_mas_uno.append(xi)
        a_xi.append(ai)
        x = xi
    print('\n     RESULTADOS')
    indices = []
    for i in range(len(numeros)):
        indices.append(i + 1)
    resultados = {'Indices': indices, 'A_Xi': a_xi, 'Xi+1': xi_mas_uno, 'Valor': numeros}  ##Imprime la serie obtenida.
    res = tabulate(resultados, headers=['i', 'a.Xi', 'Xi+1', '(Xi+1)/(m)'], tablefmt='fancy_grid')
    print(res)
    i = 21  ## Se utiliza para ir agregando al vector de numeros un nuevo elemento
    prox = int(input("Ingrese 1 si quiere agregar un numero a la serie y 0 si desea terminar: "))
    while prox != 0:  ##Permite el ingreso de un valor por vez.
        ai, xi, ri = generador_aleatorio_multiplicativo(x, k, g)
        resultados = {'Indices': [i], 'A_Xi': [ai], 'Xi+1': [xi], 'Valor': [ri]}
        res = tabulate(resultados, headers=['i', 'a.Xi', 'Xi+1', '(Xi+1)/(m)'], tablefmt='fancy_grid')
        print(res)
        x = xi
        prox = int(input("Ingrese 1 si quiere agregar un numero a la serie y 0 si desea terminar: "))
        i += 1
    print("\n")


## Este método se ejecuta en la opción 1-2, ejecuta el primer punto del TP.
def metodo_lineal():
    x = int(input('\nIngrese el primer valor: '))
    k = int(input('Ingrese el valor de k: '))
    g = int(input('Ingrese el valor de g: '))
    c = int(input('Ingrese el valor de c: '))

    numeros = []
    xi_mas_uno = []
    a_xi = []
    for i in range(20):  ##Genera 20 numeros aleatorios, tiene tres retornos, el número aleatorio
        ai, xi, ri = generador_aleatorio_lineal(x, k, g, c)  ## El proximo valor de x y el valor del a*x+c
        numeros.append(ri)
        xi_mas_uno.append(xi)
        a_xi.append(ai)
        x = xi

    print('\n     RESULTADOS')
    indices = []
    for i in range(len(numeros)):  ## Imprime la tabla con la librería tabulate.
        indices.append(i + 1)
    resultados = {'Indices': indices, 'A_Xi': a_xi, 'Xi+1': xi_mas_uno, 'Valor': numeros}
    res = tabulate(resultados, headers=['i', 'a.Xi+c', 'Xi+1', '(Xi+1)/(m)'], tablefmt='fancy_grid')
    print(res)
    i = 21  ## Se utiliza para ir agregando al vector de numeros un nuevo elemento
    prox = int(input(
        "Ingrese 1 si quiere agregar un numero a la serie y 0 si desea terminar: "))  ## Permite el ingreso de un valor por vez.
    while prox != 0:
        ai, xi, ri = generador_aleatorio_lineal(x, k, g, c)
        resultados = {'Indices': [i], 'A_Xi': [ai], 'Xi+1': [xi], 'Valor': [ri]}
        res = tabulate(resultados, headers=['i', 'a.Xi+c', 'Xi+1', '(Xi+1)/(m)'], tablefmt='fancy_grid')
        print(res)
        x = xi
        prox = int(input("Ingrese 1 si quiere agregar un numero a la serie y 0 si desea terminar: "))
        i += 1
    print("\n")


# Este método se utiliza para el punto 3 del TP. Corresponde a la OP 3:
def metodo_lineal_2(cant):
    x = int(input('\nIngrese el primer valor: '))
    k = int(input('Ingrese el valor de k: '))
    g = int(input('Ingrese el valor de g: '))
    c = int(input('Ingrese el valor de c: '))
    print("\n")

    numeros = []
    for i in range(cant):  ##Genera una cantidad x de numeros
        ai, xi, ri = generador_aleatorio_lineal(x, k, g, c)
        numeros.append(ri)
        x = xi
    return numeros  ##Devuelve un vector de numeros que se van a utilizar en la prueba chi2


def validarDist(array):

    d1, p1 = stats.chisquare(array, ddof=2)
    d1, p2 = stats.chisquare(array, ddof=1)
    d1, p3 = stats.chisquare(array, ddof=0)

    aux = [p1,p2,p3]

    if min(aux) == p1:
        return "normal"
    if min(aux) == p2:
        return "exponencial"
    if min(aux) == p3:
        return "uniforme"


def contar_si(df, cant_int):
    numeros = ca.iterarRetornos(df)
    paso = (max(numeros) - min(numeros)) / cant_int  # Esta variable me permite generar los intervalos
    inicio = min(numeros)
    intervalos = []
    contador = []

    for i in range(cant_int):  # En este ciclo creamos los intervalos, la cantidad de contadores y la columna esperados
        inicio += paso
        intervalos.append(truncate(inicio, 4))  # Ver función truncate(numero, cant_decimales)
        contador.append(0)

    for i in range(len(numeros)):  # Para cada numero analiza el intervalo en el cual se encuentra
        for j in range(cant_int):  # y acumula 1 al valor. Aqui vemos la frecuencia obtenida.
            if numeros[i] <= intervalos[j]:
                if numeros[i] > intervalos[j] - paso:
                    contador[j] += 1
                    break

    return contador