from flask import Flask, render_template
from flask import url_for
import pandas as pd
import mysql.connector

#Configuraciones de flask

app = Flask(__name__)

#Código de carga y análisis de datos
def cargarMySQL():
    miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd='root', db='actividad9' )
    #Crear una cursor, este objeto es el que permite la ejecución de instrucciones en MySQL
    cursor = miConexion.cursor()

    #Obtener los valores de la base de datos y
    #Y encapsularlos en estructuras de pandas (DataFrame)
    df = pd.read_sql('SELECT * FROM pregunta', con=miConexion)
    miConexion.close()
    #Mostrar los valores
    return df

def nivelTiempo(tiempo):
    '''Dependiendo de la cantidad de tiempo regresa un nivel'''
    #Convertir el tiempo a segundos
    t = int(tiempo[0:2]) * 60
    t = t + int(tiempo[3:5])
    #Menos de 11 segundos díficil
    if t < 16:
        return 1
    else:
        return 0

def nivelIntento(intento):
    '''Dependiendo de la cantidad de intentos regresa un nivel'''
    if intento>1:
        return 0
    else:
        return 1

def nivel2Text(nivel):
    if nivel == 0:
        return "Básico"
    elif nivel == 1:
        return "Intermedio"
    else:
        return "Avanzado"


@app.route('/', methods=("POST", "GET"))
def html_table():
    #Obtener las preguntas
    df = cargarMySQL()
    #Obtejo que funcionará como objeto de vista
    vista = {}
    #Análisis de las preguntas
    
    vista ['titulos'] = titles=df.columns.values
    #Obtener número de errores
    vista ['fallidas'] = df['Correcta'].value_counts()[1]
    #Obtener número de correctas
    vista ['correctas'] = df['Correcta'].value_counts()[0] 
    #Análizar complejidad
    c = []
    for i in df.index:
        c.append(nivel2Text(
            nivelIntento(
                int(df['Intentos'][i])) + nivelTiempo(df['TiempoResp'][i])))
    df["Complejidad"] = c
    
    vista ['tabla'] = [df.to_html(classes='data')]


    return render_template('index.html',  v = vista)


