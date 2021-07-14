from Actividad6 import crearDicPreguntas
import pandas as pd

#-------------Varios-----------------
def crearArchivo(contenido: str, extension: str, nombreArchivo: str):
    '''Crea un achivo'''
    text_file = open(nombreArchivo+extension, "w")
    text_file.write(contenido)
    text_file.close()
    print("Se creó el archivo "+ nombreArchivo)

def crearPreguntasHTML():
    '''Crea preguntas predefinidas y las guarda
    en un archivo HTML en forma de tabla'''
    #Crear preguntas y guardarlas en un diccionario
    preguntas = crearDicPreguntas()
    #Convertir diccionario a dataframe
    preguntas = pd.DataFrame.from_dict(preguntas)
    #Guardarlas en formato HTML
    preguntas = preguntas.to_html()
    #Guardar en un archivo
    crearArchivo(preguntas, ".html", "preguntas")



if __name__=='__main__':
    crearPreguntasHTML()
    preguntasDF= pd.read_html('preguntas.html')
    print("Valores obtenidos de página HTML")
    print(preguntasDF)