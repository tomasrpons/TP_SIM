import datetime as dt
import pandas as pd
import pandas_datareader as web


def getData(nombre):
    # DETERMINO CUAL VA A SER EL PERIODO DE OBTENCION DE DATOS
    start = dt.datetime(2019, 1, 1)
    end = dt.datetime(2020, 1, 1)

    # OBTENGO LOS DATOS PARA EL PERIODO Y SIMBOLO SELECCIONADO
    df = web.DataReader(nombre, 'yahoo', start, end)

    # LIMPIO LOS DATOS Y ME QUEDO UNICAMENTE CON LA COLUMNA DEL ADJ CLOSE
    df_final = limpiarDatos(df)

    return df_final

def limpiarDatos(df):

    #DESCARTO TODAS LAS COLUMNAS EXCEPTO LAS DE LA FECHA Y EL ADJ CLOSE
    df = df['Adj Close']
    df.index = pd.to_datetime(df.index)
    close = []
    date = []
    for index, value in df.items():
        close.append(value)
        date.append(index)

    datos = {'Fecha':date, 'Adj Close':close}
    df = pd.DataFrame(data=datos)
    return df




