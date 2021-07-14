# -*- coding: utf-8 -*-
import json
from typing import Dict, List
import mysql.connector
import pandas as pd

#Carpeta en donde se guardarán los JSON generados
#En caso de archivo relativo al directorio dejar en blanco
CARPETA = ""

#-----------Crear/Guardar Preguntas-----------------
def escribirEnBDJSON(preguntas):
    '''Recibe un diccionario, lo convierte a json y la guarda en la BD'''
    #Crear una conexión con MySQL
    miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd='root', db='actividad11')
    #Crear una cursor, este objeto es el que permite la ejecución de instrucciones en MySQL
    cursor = miConexion.cursor()
    #Se meten las preguntas
    for pregunta in preguntas:
        pjson = json.dumps(preguntas[pregunta], indent=4, ensure_ascii=False)
        #Inserta el valor que viene de JAVA
        cursor.execute("insert into pregunta values (0, '"+str(pjson)+"');")
    miConexion.commit()
    print("Preguntas ingresadas")
    cursor.close()

def crearDicPreguntas() -> Dict[int,List[str]]:
    '''Crea preguntas estáticas y las guarda en forma de dicccionario'''
    '''
    Formato de preguntas
        PreguntaText
        Opciones
        Tipo
        TiempoResp
        Intentos 
        Complejidad
    
    Notas
        Formato de las opciones EJEMPLO: OP1-OPCION 1;OP2-OPCION 2;... HASTA OPCION N
        Tipo de pregunta 1- Selección múltiple; 0 - De una sola respuesta
        TiempoResp es una cadena que respresenta los minutos y segundos con forma mm:ss
        Complejidad roda 3 valores: 0 - Básico; 1- Intermedio; 2- Avanzado
    '''

    #Estrutura de tipo diccionario para todas las perguntas
    preguntas = {}

    #-------------AGREGANDO PREGUNTAS A LA ESCTRUCTURA-------------
    preguntas[1] = {'Pregunta':'¿Qué es React?',
    'Opciones' :'OP1-Es una librería de JavaScript declarativa para interfaces web'\
    'OP2-Es un lenguaje de programación interpretado'\
    'OP3-Es el nombre de una página web',
    'Tipo': 0,
    'TiempoResp':'00:20',
    'Intentos':1,
    'Complejidad':0}

    preguntas[2] = {'Pregunta':'¿Qué es Pandas?',
    'Opciones':'OP1-Es un lenguaje de programación interpretado'\
    'OP2-Es una biblioteca de software escrita como extensión de NumPy'\
    'OP3-Es el nombre de un animal',
    'Tipo': 0,
    'TiempoResp':'00:20',
    'Intentos':1,
    'Complejidad':0}

    preguntas[3] = {'Pregunta':'¿Qué es Python?',
    'Opciones':'OP1-Es un lenguaje de programación interpretado'\
    'OP2-Es una biblioteca de software escrita como extensión de NumPy'\
    'OP3-OP1-Es una librería de JavaScript declarativa para interfaces web',
    'Tipo': 0,
    'TiempoResp':'00:20',
    'Intentos':1,
    'Complejidad':0}

    preguntas[4] = {'Pregunta':'¿Cuáles son algunas de las características de Python?',
    'Opciones':'OP1-Lenguaje interpretado'\
    'OP2-Es una biblioteca de software escrita como extensión de NumPy'\
    'OP3-Fuertemente tipado'\
    'OP4-Totalmente Orientado a Objetos',
    'Tipo': 1,
    'TiempoResp':'00:30',
    'Intentos':2,
    'Complejidad':1}

    preguntas[5] = {'Pregunta':'¿Cuáles son los tipos de datos de pandas?',
    'Opciones':'OP1-DataFrames'\
    'OP2-Series'\
    'OP3-Listas'\
    'OP4-Panel'\
    'OP5-Estructuras',
    'Tipo': 1,
    'TiempoResp':'00:30',
    'Intentos':2,
    'Complejidad':2}

    preguntas[6] = {'Pregunta':'¿Cuáles son los estados de un ciclo de vida en React?',
    'Opciones':'OP1-Destruído'\
    'OP2-Montado'\
    'OP3-Actualización'\
    'OP4-Desmontado'\
    'OP5-Creado',
    'Tipo': 1,
    'TiempoResp':'00:30',
    'Intentos':2,
    'Complejidad':1}

    preguntas[7] = {'Pregunta':'¿Por qué se llama python?',
    'Opciones':'OP1-En nombre del animal homonimo'\
    'OP2-En nombre de una serie llamada Monty Python Flying Circus'\
    'OP3-Nunca se ha mencionado',
    'Tipo': 0,
    'TiempoResp':'00:20',
    'Intentos':1,
    'Complejidad':0}

    preguntas[8] = {'Pregunta':'¿Qué es numpy?',
    'Opciones':'OP1-Es el nombre de un lenguaje de programación'\
    'OP2-Es una biblioteca para JavaScript que da soporte para crear vectores y matrices grandes multidimensionales'\
    'OP3-Es una biblioteca para Python que da soporte para crear vectores y matrices grandes multidimensionales',
    'Tipo': 0,
    'TiempoResp':'00:15',
    'Intentos':1,
    'Complejidad':2}
    return preguntas

def codificarJSON(preguntas):
    '''Toma un diccionario de Pandas y le da formato para mostrarlo en DJ3'''
    matriz = {}
    matriz["nodes"] = []
    matriz["links"] = []
    i =0
    for fila in preguntas.index:
        nodes = {}
        nodes["name"] = "Pregunta "+ str(preguntas["IdPregunta"][fila])
        nodes["group"] = 0
        matriz["nodes"].append(nodes)
        j = 0
        for pregunta in preguntas.index:
            links = {}
            links["source"] = i
            links["target"] = j
            aux = int(preguntas["Complejidad"][fila]) + int(preguntas["Complejidad"][pregunta])
            if aux != 0:
                links["value"] = int(preguntas["Complejidad"][fila]) + int(preguntas["Complejidad"][pregunta])
                matriz["links"].append(links)
            j = + 1
        i= i+1
    print(matriz)
    with open('static/data/miserables.json', 'w',  encoding='utf8') as file:
        json.dump(matriz, file, indent=4, ensure_ascii=False)

#-----------Cargar Preguntas-----------------
def cargarPreguntasDB():
    '''Carga todas las preguntas de la BD en formato de tablas de pandas'''
    #Crear una conexión con MySQL
    miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd='root', db='actividad11')
    #Crear una cursor, este objeto es el que permite la ejecución de instrucciones en MySQL
    cursor = miConexion.cursor()
    cursor.execute("SELECT * FROM pregunta")
    #Cargar todas las preguntas
    aux = []
    #Decodificar Json
    for preguntajson in cursor.fetchall():
        #Caragr cadena Json
        d = json.loads(preguntajson[1])
        #Agregar IdPregunta como una valor en la estructura
        d['IdPregunta'] = preguntajson[0]
        #print(d)
        aux.append(d)
    
    print(pd.DataFrame(aux))
    codificarJSON(pd.DataFrame(aux))


if __name__=='__main__':
    preguntas = crearDicPreguntas()