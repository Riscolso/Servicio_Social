'''
Actividad 18:
    Automazación de pruebas con Python y Selenium
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Firefox
import unittest

#Inicializar un modulo de testeo
tc = unittest.TestCase('__init__')

#Obtener el driver de firefox
driver = Firefox(executable_path='Actividad 18/geckodriver')
#Abrir la página de la prueba
driver.get("https://www.python.org")
#Obtener e imprimir el título de la página
print("Título de la página: " + driver.title)
tc.assertIn("Welcome to Python.org", driver.title)
#Obtener el elemento coincidente con el nombre
search_bar = driver.find_element_by_name("q")
#Limpiar el elemento
search_bar.clear()
#Enviar texto
search_bar.send_keys("getting started with python")
#Presionar botón de búsqueda
driver.find_element_by_xpath("//*[@id=\"submit\"]").click()
#Comprobar que la URL esperada coincida con la recuperada
urlEsperada = "https://www.python.org/search/?q=getting+started+with+python&submit="
try:
    urlActual = driver.current_url
    print("Se espera la URL: "+ urlEsperada)
    assert  urlEsperada == urlActual
    print("Las URL coinciden")
except:
    print("Hubo un error en la URL esperada, no coincide")
    print("Se recibió: "+ urlActual)
finally:
    print("Prueba termianda")
    driver.close()

