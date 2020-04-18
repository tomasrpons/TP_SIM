import numpy as np
import pandas as pd
import math

def promedioRetornos(df):
    # CALCULAR EL PROMEDIO DE LOS RETORNOS
    return df.mean()["Adj Close"]

def desEstandarRetornos(df):
    # CALCULAR LA VARIANZA DE LOS RETORNOS
    return math.sqrt(df.var()["Adj Close"])

def iterarRetornos(df):
    array_aux = []
    for ind in df.index:
        retorno = df['Adj Close'][ind]
        array_aux.append(retorno)
    return array_aux