# Importamos el webdriver de Selenium
from selenium import webdriver

# Importamos la clase By para localizar elementos
from selenium.webdriver.common.by import By

# Importamos time para pausas simples
import time

# Creamos el driver usando Chrome (asegúrate de tener chromedriver instalado)
driver = webdriver.Chrome()

# Maximizamos la ventana del navegador
driver.maximize_window()

# Navegamos a otra página con inputs y botones
driver.get("https://the-internet.herokuapp.com/login")

# Pausa para carga
time.sleep(2)

# Localizamos el campo de usuario
campo_usuario = driver.find_element(By.ID, "username")

# Localizamos el campo de contraseña
campo_contraseña = driver.find_element(By.ID, "password")

# Localizamos el botón de login
boton_login = driver.find_element(By.CLASS_NAME, "radius")

# Verificamos visibilidad de los campos
print("Campo usuario visible:", campo_usuario.is_displayed())
print("Campo contraseña visible:", campo_contraseña.is_displayed())

# Verificamos si el botón está habilitado
print("Botón login habilitado:", boton_login.is_enabled())

# Obtenemos el atributo placeholder del campo usuario
placeholder_usuario = campo_usuario.get_attribute("placeholder")
print("Placeholder del campo usuario:", placeholder_usuario)

# ============================
# CIERRE DEL NAVEGADOR
# ============================

# Pausa final para observar el resultado
time.sleep(3)

# Cerramos el navegador
driver.quit()
