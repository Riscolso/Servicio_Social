from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import unittest
from typing import List

driver = Firefox(executable_path='geckodriver')
TIPOS = {
    1 : ['4', '2', '1', '0.1'],
    2 : ['4', '2', '1.1', '3'],
    3 : ['4', '2', '6', '3'],
}
PRUEBAS = {
    1 : "The type of iris plant is: Iris Setosa",
    2 : "The type of iris plant is: Iris Versicolour",
    3 : "The type of iris plant is: Iris Setosa",
}

'''
    1 - Iris Setosa
    2 - Iris Versicolour
    3 - Iris Virginica 
'''

wait = WebDriverWait(driver, 3)
tc = unittest.TestCase('__init__')


def realizarPrueba(caso: str, caracteristicas: List[int]) -> str:
    #Dirigirse a la página en la cual se hará la prueba
    driver.get("http://localhost:3000/")
    #Obtener el nombre de la página
    titulo = driver.title
    #Cambio de Atributos de entrada:
    Select(driver.find_element(By.NAME, "sepalLength")).select_by_value(caracteristicas[0])
    Select(driver.find_element(By.NAME, "sepalWidth")).select_by_value(caracteristicas[1])
    Select(driver.find_element(By.NAME, "petalLength")).select_by_value(caracteristicas[2])
    Select(driver.find_element(By.NAME, "petalWidth")).select_by_value(caracteristicas[3])

    #Buscar por el botón de predicción y presionarlo
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/div[3]/div[1]/button").click()

    #Buscar el elemento que muestra el resultado
    #Esperar que la página procese la info y muestre un resultado
    #Al mostrarse, obtener el elemento
    resultado = wait.until(presence_of_element_located((By.ID, "result"))).get_attribute("innerHTML").strip()
    #Verificar que el valor arrojado sea el esperado
    #assert PRUEBAS[caso] == resultado
    tc.assertEqual(PRUEBAS[caso], resultado, "El tipo de planta no es el correcto")

    #Regresar el nombre de la Sépalo
    return resultado

#Se realizan 3 pruebas, en dos el resultado será es esperado y en la 3ra, será un error
for i in TIPOS:
    print("Resultado de la prueba " + str(i))
    print(realizarPrueba(i, TIPOS[i]))
    print("\n\n")