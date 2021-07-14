import pandas as pd
class Funcion(object):
    def obtenerPromedio(self,nuevoAlumno: str, nuevoValor: int):
        alumnosPromedio = {'Nombre' : ['Alan', 'Beto', 'David', 'Juan', 'Aquiles'],
        'Promedio' : [3.2, 5.4, 8.4, 7.5, 9.0]}
        data_frame = pd.DataFrame(alumnosPromedio)
        data_frame = data_frame.append({'Nombre': nuevoAlumno, 'Promedio': nuevoValor}, ignore_index=True)
        promedioGrupal = data_frame['Promedio'].mean()
        print('Promedio de los alumnos: ')
        print (data_frame)
        print('\nEl promedio grupal es de: ', promedioGrupal, '\n\n')
        return promedioGrupal

    class Java:
        implements = ["com.py4j.struts2jy4py.clases.IFuncionPython"]

from py4j.java_gateway import JavaGateway, CallbackServerParameters
simple_hello = Funcion()
gateway = JavaGateway(
    callback_server_parameters=CallbackServerParameters(),
    python_server_entry_point=simple_hello)