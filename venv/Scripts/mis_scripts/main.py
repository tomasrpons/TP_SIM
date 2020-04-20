import lib
import random
import math
from numpy import log as ln
import statistics as stats
import matplotlib.pyplot as plt
from matplotlib.pyplot import style
import tabulate
import statistics


def valor_puntual(grados_libertad):
    lista = ['3,8415', '5,9915', '7,8147', '9,4877', '11,0705', '12,5916', '14,0671', '15,5073', '16,9190', '18,3070', '19,6752', '21,0261', '22,3620', '23,6848', '24,9958', '26,2962', '27,5871', '28,8693', '30,1435', '31,4104', '32,6706', '33,9245', '35,1725', '36,4150', '37,6525', '38,8851', '40,1133', '41,3372', '42,5569', '43,7730', '44,9853', '46,1942', '47,3999', '48,6024', '49,8018', '50,9985', '52,1923', '53,3835', '54,5722', '55,7585', '61,6562', '67,5048', '73,3115', '79,0820', '90,5313', '101,8795', '113,1452', '124,3421', '146,5673', '168,6130', '190,5164', '212,3039', '233,9942', '287,8815', '341,3951', '553,1269', '658,0936']
    x = lista[grados_libertad-1].replace(",",".")
    return float(x)

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

def prueba_chi23(numeros, cant_int):
    paso = (max(numeros)- min(numeros)) / cant_int             # Esta variable me permite generar los intervalos
    inicio = min(numeros)
    intervalos = []
    contador = []
    esperado = len(numeros) / cant_int     # Aqui obtenemos el valor de frecuencia esperado para cada intervalo siguiendo una distribución uniforme.
    frec_esperada = []
    for i in range(cant_int):       # En este ciclo creamos los intervalos, la cantidad de contadores y la columna esperados
        inicio += paso
        intervalos.append(truncate(inicio,4))   # Ver función truncate(numero, cant_decimales)
        contador.append(0)
        frec_esperada.append(esperado)      # Para cada una de las listas agregamos 0 para el contador, y esperado para la frecuenia esperada.

    for i in range(len(numeros)):           # Para cada numero analiza el intervalo en el cual se encuentra
        for j in range(cant_int):           # y acumula 1 al valor. Aqui vemos la frecuencia obtenida.
            if numeros[i] <= intervalos[j]:
                if numeros[i] > intervalos[j]-paso:
                    contador[j]+=1
                    break

    est_prueba = []
    sumatoria = []
    suma = 0
    for i in range(cant_int):                                           # Debido a que los numeros generados tienen demasiados decimales,
        a = ((frec_esperada[i]-contador[i])**2) / frec_esperada[i]      # con este método truncamos a 4 todos los obtenidos.
        a = truncate(a,4)
        est_prueba.append(a)
        suma += a
        sumatoria.append(suma)
    interval = []
    anterior = 0
    for i in range(cant_int):           #Crea un array de string para imprimir de que valor min a max van los intervalos.
        interval.append("De " + str(anterior) + " a " + str(intervalos[i]))
        anterior = intervalos[i]
    resultados = {'Intervalos': interval, 'FO': contador, 'FE': frec_esperada,'C':est_prueba,'C(AC)':sumatoria}
    res = tabulate(resultados, headers=['Intervalos', 'FO', 'FE', 'C','C(AC)'], tablefmt='fancy_grid')     #Creamos la tabla para imprimir con la librería tabulate
    print(res)

    #ES Ordenado, SI LO QUEREMOS POR COMO APARECIERON SOLO HAY QUE SACAR EL SORTED
    num = {'Número': sorted(numeros)}
    num_list = tabulate(num, headers=['Número'], tablefmt='fancy_grid', showindex=True)      #Imprimimos a modo de tabla los valores obtenidos.
    print(num_list)

    aux = [0]
    for i in range(cant_int):
        aux.append(intervalos[i])

    plt.hist(numeros, bins=aux,edgecolor='black')         #Utilizamos la libreria Pandas para crear DataFrames para poder generar los gráficos.
    plt.axhline(y=esperado, xmin=0, xmax=1, color="red")
    plt.xlabel('Intervalos')
    plt.ylabel('Frecuencia')
    plt.legend('EO')
    plt.title('Distribucion de los valores acuerdo a su frecuencia')
    plt.grid()
    plt.show()
    valor_critico = valor_puntual(cant_int-1)              #Obtenemos el valor crítico para comparar con el estadístico de prueba.
    print("El valor crítico con 95% de significancia es: ", valor_critico)
    print("El estadístico de prueba es: ", suma)
    if valor_critico > suma:
        print("No se puede rechazar la hipótesis nula")
    else:
        print("Se rechaza la hipóteis nula")
    print("\n")




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

            #numerosPrueba = [0.10 , 0.25 , 1.53 , 2.83 , 3.50 , 4.14 , 5.65 , 6.96 , 7.19 ,8.25 ,1.20 , 5.24 , 4.75 , 3.96,2.21, 3.15 , 2.53 , 1.16 , 0.32 , 0.90 , 0.87 , 1.34
            #, 1.87 , 2.91 , 0.71 , 1.69 , 0.69 , 0.55 , 0.43 , 0.26]
            #lib.prueba_chi2(numerosPrueba,10,1,statistics.mean(numerosPrueba))


        if op == 3: #Poisson

            cant_num = int(input("\nIngrese la cantidad de Valores: "))
            inter = int(input("Ingrese la cantidad de invervalos: "))
            media = float(input("Ingrese lambda: "))
            numeros = lib.aleatoria_poisson(cant_num,media)

            ver = "n"
            ver = input("Desea ver los numeros generados (S/N): ")
            if ver in "sS":
                visualizar(numeros)

            nueva_media = statistics.mean(numeros)
            lib.poisson(numeros, inter, 1, nueva_media)

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


