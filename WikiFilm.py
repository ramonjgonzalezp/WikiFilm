# Importar las librerías necesarias
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Definir las variables necesarias
busqueda = "Universos en las películas"
url_wikipedia = "https://es.wikipedia.org/wiki/Wikipedia:Portada"

# Abrir Google Chrome, maximizar la ventana y navegar a Wikipedia
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url_wikipedia)

# Buscar la barra de búsqueda y escribir la búsqueda
barra_busqueda = driver.find_element("name", "search")
barra_busqueda.send_keys(busqueda)
barra_busqueda.send_keys(Keys.RETURN)

# Esperar a que se carguen los resultados
driver.implicitly_wait(3)

# Encontrar los tres primeros resultados y mostrarlos en la consola
for i in range(1, 4):
    titulo = driver.find_element(By.XPATH, "//*[@id='mw-content-text']/div[4]/div[2]/ul/li[{}]/table/tbody/tr/td[2]/div[1]".format(i))
    print(titulo.text)

# Cerrar el navegador
driver.quit()