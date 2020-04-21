import datetime as dt
import pandas as pd
import pandas_datareader as web


def getData(nombre):
    # DETERMINO CUAL VA A SER EL PERIODO DE OBTENCION DE DATOS
    start = dt.datetime(2017, 5, 1)
    end = dt.datetime(2018, 1, 1)

    # OBTENGO LOS DATOS PARA EL PERIODO Y SIMBOLO SELECCIONADO
    df = web.DataReader(nombre, 'yahoo', start, end)

    # LIMPIO LOS DATOS Y ME QUEDO UNICAMENTE CON LA COLUMNA DEL ADJ CLOSE
    vector = limpiarDatos(df)

    return vector

def limpiarDatos(df):

    #DESCARTO TODAS LAS COLUMNAS EXCEPTO LAS DE LA FECHA Y EL ADJ CLOSE
    df = df['Adj Close']
    df.index = pd.to_datetime(df.index)
    close = []
    for index, value in df.items():
        close.append(value)

    print(len(close))
    return close





