'''
Actividad 18:
    Automazación de pruebas con Python y Selenium
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Firefox

#Obtener el driver de firefox
driver = Firefox(executable_path='Actividad 18/geckodriver')
#Abrir la página de la prueba
driver.get("https://www.python.org")
#Obtener e imprimir el título de la página
print(driver.title)
#Obtener el elemento coincidente con el nombre
search_bar = driver.find_element_by_name("q")
#Limpiar el elemento
search_bar.clear()
#Enviar texto
search_bar.send_keys("getting started with python")
#Presionar Retorno
search_bar.send_keys(Keys.RETURN)


