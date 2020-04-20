import random
import math
from numpy import log as ln
import statistics as stats
import matplotlib.pyplot as plt
from matplotlib.pyplot import style
import tabulate


def aleatoria_uniforme(cant_num, lim_inf, lim_sup):
    numeros = []
    for i in range(cant_num):
        x = lim_inf + random.uniform(0, 1) * (lim_sup - lim_inf)
        numeros.append(truncate(x, 4))
    return numeros


def aleatoria_exponencial(cant_numeros, lamda=0, u=0):
    numeros = []
    if (lamda <= 0) & (u <= 0):
        print("Error")
    else:
        if lamda != 0:
            for i in range(cant_numeros):
                x = (-1 / lamda) * ln(1 - random.uniform(0, 1))
                numeros.append(truncate(x, 4))
        else:
            for i in range(cant_numeros):
                x = (-u) * ln(1 - random.uniform(0, 1))
                numeros.append(truncate(x, 4))
        return numeros


def aleatoria_poisson(cant_numeros, media):
    p = 1
    x = -1
    a = math.exp(-media)
    numeros = []
    for i in range(cant_numeros):
        u = random.random()
        p = p * u
        x = x + 1
        while (p >= a):
            u = random.random()
            p = p * u
            x = x + 1
        numeros.append(x)
    return numeros


def aleatoria_normal_muller(cant_numeros, media, desviacion):
    numeros = []
    for i in range(cant_numeros // 2):
        n1 = (pow((-2 * ln(random.uniform(0, 1))), 0.5) * math.cos(
            2 * math.pi * random.uniform(0, 1))) * desviacion + media
        n2 = (pow((-2 * ln(random.uniform(0, 1))), 0.5) * math.sin(
            2 * math.pi * random.uniform(0, 1))) * desviacion + media
        numeros.append(truncate(n1, 4))
        numeros.append(truncate(n2, 4))
    return numeros[:cant_numeros]


def aleatoria_normal_convolucion(cant_numeros, media=0.5, varianza=1 / 12):
    numeros = []
    for i in range(cant_numeros):
        x = 0
        for i in range(12):
            x += random.uniform(0.1)
        z = (x - 6) * varianza + media
        numeros.append(z)
    return numeros


def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper


def esperado_normal(marca, media, desv):
    exponente = (-0.5) * pow(((marca - media) / desv), 2)
    denom = desv * pow((2 * math.pi), 0.5)
    return ((1 / denom) * (pow(math.e, exponente)))


def esperado_exponencial(x, l):
    return 1 - pow(math.e, (-l * x))


def calculaFactorial(n):
    if n > 0:
        n = n * calculaFactorial(n - 1)
    else:
        n = 1
    return n


#### FIJARSE PORQUE NO ES EL MISMO FORMATO DE TABLA A LAS DEMAS, NO NECESITAS INTERVALOS, NI MARCA.
def esperado_poisson(marca, lamda):
    numerador = pow(lamda, marca) * pow(math.e, (-lamda))
    denom = calculaFactorial(int(marca))
    return truncate((numerador / denom), 4)


def obtener_esperados_poisson(numeros, intervalos, l):
    frec_esperada = []
    for i in range(len(intervalos) - 1):
        marca = (intervalos[i] + intervalos[i + 1]) / 2
        esperado = esperado_poisson(marca, l)
        frec_esperada.append(truncate((esperado * len(numeros)), 2))
    return frec_esperada


########################


def obtener_esperados_exponencial(numeros, intervalos, l):
    frec_esperada = []
    for i in range(len(intervalos)-1):
        x = esperado_exponencial(intervalos[i],l)
        y = esperado_exponencial(intervalos[i+1], l)
        esperado = y-x
        frec_esperada.append(truncate((esperado * len(numeros)), 4))
    return frec_esperada


def obtener_esperados_normal(numeros, intervalos):
    media = stats.mean(numeros)
    v = 0
    for i in range(len(numeros)):
        v += pow((numeros[i] - media), 2)
    varianza = (1 / (len(numeros) - 1)) * v
    desv = pow(varianza, 0.5)
    frec_esperada = []

    for x in range(len(intervalos) - 1):
        marca = (intervalos[x] + intervalos[x + 1]) / 2
        esperado = esperado_normal(marca, media, desv)
        frec_esperada.append(truncate((esperado * len(numeros)), 4))
    return frec_esperada


def valor_puntual(grados_libertad, ddof):
    lista = ['3,8415', '5,9915', '7,8147', '9,4877', '11,0705', '12,5916', '14,0671', '15,5073', '16,9190', '18,3070',
             '19,6752', '21,0261', '22,3620', '23,6848', '24,9958', '26,2962', '27,5871', '28,8693', '30,1435',
             '31,4104', '32,6706', '33,9245', '35,1725', '36,4150', '37,6525', '38,8851', '40,1133', '41,3372',
             '42,5569', '43,7730', '44,9853', '46,1942', '47,3999', '48,6024', '49,8018', '50,9985', '52,1923',
             '53,3835', '54,5722', '55,7585', '61,6562', '67,5048', '73,3115', '79,0820', '90,5313', '101,8795',
             '113,1452', '124,3421', '146,5673', '168,6130', '190,5164', '212,3039', '233,9942', '287,8815', '341,3951',
             '553,1269', '658,0936']
    x = lista[grados_libertad - 1 - ddof].replace(",", ".")
    return float(x)


def es_entero(numeros):
    for i in range(len(numeros)):
        if int(numeros[i]) != numeros[i]:
            return False
    return True


def prueba_chi2(numeros, cant_int, ddof, u):
    paso = truncate((max(numeros) - min(numeros)) / cant_int, 4)  # Esta variable me permite generar los intervalos
    inicio = min(numeros)
    intervalos = []
    contador = []
    frec_esperada = []

    for i in range(cant_int - 1):  # En este ciclo creamos los intervalos, la cantidad de contadores
        inicio += paso
        intervalos.append(truncate(inicio, 4))  # Ver función truncate(numero, cant_decimales)
        contador.append(0)
    intervalos.append(max(numeros))
    contador.append(0)

    # Obtenemos la frecuencia esperada
    intervals = [min(numeros)] + intervalos

    if ddof == 2:
        frec_esperada = obtener_esperados_normal(numeros, intervals)
    elif ddof == 1:
        if es_entero(numeros):
            # poisson
            frec_esperada = obtener_esperados_poisson(numeros, intervals, u)
        else:
            # expon
            l = 1 / u
            frec_esperada = obtener_esperados_exponencial(numeros, intervals, l)
    elif ddof == 0:
        frec_esperada = [len(numeros) / cant_int] * cant_int

    numeros = sorted(numeros)

    for i in range(len(numeros)):  # Para cada numero analiza el intervalo en el cual se encuentra
        for j in range(cant_int):  # y acumula 1 al valor. Aqui vemos la frecuencia obtenida.
            print(numeros[i], intervalos[j], numeros[i] <= intervalos[j], contador)
            if numeros[i] <= intervalos[j]:
                if numeros[i] == intervalos[-1]:
                    contador[-1] += 1
                    print(contador)
                    break
                if numeros[i] >= intervalos[j] - paso:
                    contador[j] += 1
                    break
                if numeros[i] < intervalos[0]:
                    contador[0] += 1
                    break
    print(sum(contador))

    est_prueba = []
    sumatoria = []
    suma = 0
    for i in range(cant_int):  # Debido a que los numeros generados tienen demasiados decimales,
        if frec_esperada[i] == 0:
            a = 0
        else:
            a = pow((frec_esperada[i] - contador[i]), 2) / frec_esperada[
                i]  # con este método truncamos a 2 decimales todos los obtenidos.
        a = truncate(a, 2)
        est_prueba.append(a)
        suma += a
        sumatoria.append(suma)

    anterior = min(numeros)
    interval = []
    for i in range(cant_int):  # Crea un array de string para imprimir de que valor min a max van los intervalos.
        interval.append("De " + str(anterior) + " a " + str(intervalos[i]))
        anterior = intervalos[i]
    resultados = {'Intervalos': interval, 'FO': contador, 'FE': frec_esperada, 'C': est_prueba, 'C(AC)': sumatoria}
    res = tabulate.tabulate(resultados, headers=['Intervalos', 'FO', 'FE', 'C', 'C(AC)'],
                            tablefmt='fancy_grid')  # Creamos la tabla para imprimir con la librería tabulate
    print(res)

    plt.hist(numeros, bins=intervalos,
             edgecolor='black')  # Utilizamos la libreria Pandas para crear DataFrames para poder generar los gráficos.
    for i in range(len(intervalos) - 1):
        plt.axhline(frec_esperada[i], xmin=intervalos[i], xmax=intervalos[i + 1])
    plt.xlabel('Intervalos')
    plt.ylabel('Frecuencia')
    plt.legend('EO')
    plt.title('Distribucion de los valores acuerdo a su frecuencia')
    plt.grid()
    plt.show()
    valor_critico = valor_puntual(cant_int - 1,
                                  ddof)  # Obtenemos el valor crítico para comparar con el estadístico de prueba.
    print("El valor crítico con 95% de significancia es: ", valor_critico)
    print("El estadístico de prueba es: ", suma)
    if valor_critico > suma:
        print("No se puede rechazar la hipótesis nula")
    else:
        print("Se rechaza la hipóteis nula")
    print("\n")
