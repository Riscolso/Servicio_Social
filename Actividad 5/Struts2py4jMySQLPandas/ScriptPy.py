import mysql.connector
import pandas as pd
print("Script iniciado, esperando conexión con Java... ")
class Funcion(object):
    def obtenerPromedio(self,nuevoAlumno: str, nuevoValor: int):
        #Crear una conexión con MySQL
        miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd='root', db='grupo' )
        #Crear una cursor, este objeto es el que permite la ejecución de instrucciones en MySQL
        cursor = miConexion.cursor()
        #Inserta el valor que viene de JAVA
        cursor.execute("insert into alumno(nombre, calificacion) values ('"+nuevoAlumno+ "', "+ str(nuevoValor)+");")
        print("Se introdujo el alumno ", nuevoAlumno, "con calificación de ", nuevoValor, "\n")

        #Obtener los valores de las base de datos y
        #Y encapsularlos en estructuras de pandas (DataFrame)
        df = pd.read_sql('SELECT * FROM alumno', con=miConexion)
        #Cálculo del promedio usando pandas
        promedioGrupal = df['Calificacion'].mean()

        #Mostrar los valores
        print("Valores obtenidos de la BD")
        print(df)
        print("\nEl promedio grupal es de: ", promedioGrupal) 
        miConexion.close()
        return promedioGrupal

    class Java:
        implements = ["com.py4j.struts2jy4py.clases.IFuncionPython"]

from py4j.java_gateway import JavaGateway, CallbackServerParameters
simple_hello = Funcion()
gateway = JavaGateway(
    callback_server_parameters=CallbackServerParameters(),
    python_server_entry_point=simple_hello)