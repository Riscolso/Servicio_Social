from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

driver = Firefox(executable_path='geckodriver')
TIPOS = {
    "Iris Setosa" : ['4', '2', '1', '0.1'],
    "Iris Versicolour" : ['4', '2', '1.1', '3'],
    "Iris Virginica" : ['4', '2', '6', '3']
}
'''
    1 - Iris Setosa
    2 - Iris Versicolour
    3 - Iris Virginica 
'''

wait = WebDriverWait(driver, 10)
#Dirigirse a la página en la cual se hará la prueba
driver.get("http://localhost:3000/")
#Obtener el nombre de la página
titulo = driver.title
#Cambio de Atributos de entrada:
Select(driver.find_element(By.NAME, "sepalLength")).select_by_index(1)



#Buscar por el botón de predicción y presionarlo
driver.find_element_by_xpath("/html/body/div/div/div[2]/form/div[3]/div[1]/button").click()

#Buscar el elemento que muestra el resultado
#Esperar que la página procese la info y muestre un resultado
#Al mostrarse, obtener el elemento
resultado = wait.until(presence_of_element_located((By.ID, "result")))

print(resultado.get_attribute("innerHTML"))