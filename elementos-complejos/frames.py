# Importamos el webdriver para controlar el navegador
from selenium import webdriver

# Importamos By para localizar elementos
from selenium.webdriver.common.by import By

# Importamos nuestra clase personalizada de esperas explícitas
from wait_helper import WaitHelper

# Creamos una instancia del navegador Chrome
navegador = webdriver.Chrome()

# Maximizamos la ventana
navegador.maximize_window()

# Creamos la instancia del helper de esperas
espera = WaitHelper(navegador, 10)

# =================================================
# EJEMPLO 1: CAMBIO DE CONTEXTO A IFRAME POR NOMBRE
# =================================================

# Abrimos un ejemplo controlado con iframe
navegador.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_iframe")

# Esperamos a que el iframe principal exista
espera.esperar_presencia_elemento(
    (By.ID, "iframeResult")
)

# Cambiamos al iframe principal por nombre / id
navegador.switch_to.frame("iframeResult")

# Localizamos el iframe interno
iframe_interno = espera.esperar_presencia_elemento(
    (By.TAG_NAME, "iframe")
)

# Cambiamos al iframe interno usando WebElement
navegador.switch_to.frame(iframe_interno)

# Esperamos un elemento visible dentro del iframe interno
titulo = espera.esperar_elemento_visible(
    (By.TAG_NAME, "h1")
)

# Imprimimos el texto encontrado
print("Texto dentro del iframe:", titulo.text)

# =================================================
# RETORNO DE CONTEXTOS
# =================================================

# Volvemos al iframe padre
navegador.switch_to.parent_frame()

# Volvemos al contexto principal de la página
navegador.switch_to.default_content()

# Cerramos el navegador
navegador.quit()
