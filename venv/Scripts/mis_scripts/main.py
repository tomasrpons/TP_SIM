import funciones as fn
import datos as dt
import matplotlib.pyplot as plt
import calculos as ca


def main():

    nombre = "QQQ"
    df = dt.getData(nombre)
    print(fn.validarDist(fn.contar_si(df,20)))
    df.plot.hist(x="Fecha", y="Adj Close", figsize=(10,6), bins=20)
    plt.show()







    print("-----------------Bienvenido-----------------\n"
          "          Generador de números aleatorios.\n"

          )
    while True:

        print("Presione 1 para generar una lista de 20 numeros aleatorios.\n"
              "Presione 2 para evaluar el método math.random.\n"
              "Presione 3 para evaluarel método congruencial multiplicativo.\n"
              "Utilice 0 para salir.\n")
        op = int(input("Introduzca la opcion solicitada: "))

        if op in (1, 2, 3, 0):
            if op == 1:
                op1()

            if op == 2:
                op2()

            if op == 3:
                op3()

            if op == 0:
                break

        else:
            print('Opcion incorrecta, intentelo de nuevo.\n')


## Se utiliza de menú intermedio entre el menú de usuario y los métodos generadores
def op1():
    metodo = int(input('\nPresione 1 si desea utilizar el metodo congruencial multiplicativo\n'
                       'Presione 2 si desea utilizar el metodo congruencial lineal\n'
                       '\nIntroduzca la opcion solicitada: '))

    if metodo in (1, 2):
        if metodo == 1:
            fn.metodo_multiplicativo()

        if metodo == 2:
            fn.metodo_lineal()
    else:
        print('Opcion incorrecta, intentelo de nuevo.\n')


## Se utiliza de menú intermedio entre el menú de usuario y la prueba chi
def op2():
    cant = int(input('Ingrese la cantidad de numeros que quiere generar: '))
    intervalos = int(input('Ingrese la cantidad de intervalos(5/10/15/20): '))
    if (
            cant / intervalos) < 5:  ##Validamos que las frecuencias esperadas de cada intervalo sean mayores a 5, de lo contrario no se puede realizar la prueba
        print("Error al cargar datos, los intervalos tienen frecuencia esperada menor a 5\n")
    else:
        numeros = [random.uniform(0, 1) for x in range(
            cant)]  ##Random.Uniform no abarca el 1. En esta sentencia creamos x cantidad de numeros y lo agregamos a un vector
        fn.prueba_chi2(numeros, intervalos)


## Prueba Chi con el generador lineal.
def op3():
    cant = int(input('Ingrese la cantidad de numeros que quiere generar: '))
    intervalos = int(input('Ingrese la cantidad de intervalos(5/10/15/20): '))
    numeros = fn.metodo_lineal_2(cant)
    fn.prueba_chi2(numeros, intervalos)


if __name__ == '__main__':
    main()
