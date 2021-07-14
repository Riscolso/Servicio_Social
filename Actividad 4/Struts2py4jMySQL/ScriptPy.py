import mysql.connector
print("Script iniciado, esperando conexión con Java... ")
class Funcion(object):
    def obtenerPromedio(self,nuevoAlumno: str, nuevoValor: int):
        #Crear una conexión con MySQL
        miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd='root', db='grupo' )
        #Crear una cursor, este objeto es el que permite la ejecución de instrucciones en MySQL
        cursor = miConexion.cursor()
        #Inserta el valor que viene de JAVA
        cursor.execute("insert into alumno(nombre, calificacion) values ('"+nuevoAlumno+ "', "+ str(nuevoValor)+");")
        print("Se introdujo el alumno ", nuevoAlumno, "con calificación de ", nuevoValor)
        #Obtener los valores de la base de datos
        cursor.execute( "SELECT * FROM alumno" )
        i = 0
        aux = 0
        #Mostrar los valores y calcular el promedio 
        print("Valores obtenidos de la BD")
        for id, nombre, calificacion in cursor.fetchall() :
            print("ID   Nombre          Califiación")
            print(id,"  ", nombre, "      ", calificacion)
            i = i+1
            aux = aux + calificacion
        promedioGrupal = round(float(aux/i), 2)
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