# Importar las librerías necesarias
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.mime.application import MIMEApplication

# Definir las variables necesarias
busqueda = "Universos de películas"
url_wikipedia = "https://es.wikipedia.org/wiki/Wikipedia:Portada"
email_emisor = "pineapple.dev.rg@gmail.com"
contrasena_emisor = "jysxysmfcwegojjn"
email_destinatario = "ramonjgonzalezp@gmail.com"

# Abrir Google Chrome, maximizar la ventana y navegar a Wikipedia
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url_wikipedia)

# Buscar la barra de búsqueda y escribir la búsqueda
barra_busqueda = driver.find_element("name", "search")
barra_busqueda.send_keys(busqueda)
barra_busqueda.send_keys(Keys.RETURN)

# Esperar a que se carguen los resultados
driver.implicitly_wait(2)

# Encontrar los tres primeros resultados y obtener sus títulos
resultados_de_la_busqueda = driver.find_elements(By.XPATH, "//div[@id='wikipedia-search-result-link']/a")[:3]
links = []
for resultado in resultados_de_la_busqueda:
    url_data = resultado.get_attribute("href")
    links.append(url_data)
    print(url_data)
print(len(links))
print(links)

# Cerrar el navegador y crear el correo electrónico
driver.quit()

"""

mensaje = MIMEMultipart()
mensaje["From"] = email_emisor
mensaje["To"] = email_destinatario
mensaje["Subject"] = "Tres primeros artículos de Wikipedia sobre universos de películas"

# Obtener los nombres de los tres primeros artículos
nombres_articulos = []
for resultado in resultados_de_la_busqueda:
    nombres_articulos.append(resultado.text)

# Escribir el cuerpo del mensaje y adjuntar los archivos
cuerpo_mensaje = "Los tres primeros artículos de Wikipedia sobre universos de películas son:\n\n"
for nombre in nombres_articulos:
    cuerpo_mensaje += "- " + nombre + "\n"
mensaje.attach(MIMEText(cuerpo_mensaje))

i = 0
for resultado in resultados_de_la_busqueda:
    archivo = "Artículo {}.pdf".format(i+1)
    with open(archivo, "w") as f:
        f.write(resultado.text)
    with open(archivo, "rb") as f:
        adjunto = MIMEApplication(f.read(), _subtype="pdf")
        adjunto.add_header("Content-Disposition", "attachment", filename=archivo)
        mensaje.attach(adjunto)
    i = i+1

# Iniciar sesión en Gmail y enviar el correo electrónico
sesion = smtplib.SMTP("smtp.gmail.com", 587)
sesion.ehlo()
sesion.starttls()
sesion.ehlo()
sesion.login(email_emisor, contrasena_emisor)
sesion.sendmail(email_emisor, email_destinatario, mensaje.as_string())
sesion.quit()

print("Correo electrónico enviado con éxito.")

"""