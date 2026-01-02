# ------------------------------
# IMPORTACIONES NECESARIAS
# ------------------------------

from selenium import webdriver
from selenium.webdriver.common.by import By

# Importa WebDriverWait para esperas explícitas
from selenium.webdriver.support.ui import WebDriverWait

# Importa expected_conditions para definir condiciones
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service
import time

from wait_helper import WaitHelper

# ------------------------------
# SCRIPT PRINCIPAL
# ------------------------------

# Configura el servicio del navegador
servicio = Service()

# Inicializa el navegador Chrome
driver = webdriver.Chrome(service=servicio)

# Maximiza la ventana
driver.maximize_window()

# Inicializa el helper de esperas
esperas = WaitHelper(driver, tiempo_espera=10)

try:
    # ------------------------------
    # ACCESO AL SITIO SEGURO
    # ------------------------------

    # Navega al sitio oficial de Selenium para pruebas de alertas
    driver.get("https://www.selenium.dev/selenium/web/alerts.html")

    # Espera a que el título contenga la palabra Alerts
    esperas.esperar_titulo_contiene("Alerts")

    # ------------------------------
    # ALERTA SIMPLE (alert)
    # ------------------------------

    # Localiza el botón que dispara una alerta simple
    boton_alerta = esperas.esperar_elemento_clickeable(
        (By.ID, "alert")
    )

    # Hace clic en el botón
    boton_alerta.click()

    # Espera a que la alerta esté presente
    WebDriverWait(driver, 10).until(EC.alert_is_present())

    # Cambia el contexto del driver a la alerta
    alerta_simple = driver.switch_to.alert

    # Obtiene el texto de la alerta
    texto_alerta = alerta_simple.text

    # Imprime el texto de la alerta
    print("Texto de alerta simple:", texto_alerta)

    # Acepta la alerta
    alerta_simple.accept()

    # ------------------------------
    # ALERTA DE CONFIRMACIÓN (confirm)
    # ------------------------------

    # Localiza el botón de confirmación
    boton_confirmacion = esperas.esperar_elemento_clickeable(
        (By.ID, "confirm")
    )

    # Hace clic en el botón
    boton_confirmacion.click()

    # Espera a que aparezca la alerta
    WebDriverWait(driver, 10).until(EC.alert_is_present())

    # Cambia al contexto de la alerta
    alerta_confirmacion = driver.switch_to.alert

    # Imprime el texto de la confirmación
    print("Texto de confirmación:", alerta_confirmacion.text)

    # Cancela la alerta
    alerta_confirmacion.dismiss()

    # ------------------------------
    # ALERTA CON PROMPT
    # ------------------------------

    # Localiza el botón del prompt
    boton_prompt = esperas.esperar_elemento_clickeable(
        (By.ID, "prompt")
    )

    # Hace clic en el botón
    boton_prompt.click()

    # Espera a que el prompt esté presente
    WebDriverWait(driver, 10).until(EC.alert_is_present())

    # Cambia al prompt
    alerta_prompt = driver.switch_to.alert

    # Escribe texto en el prompt
    alerta_prompt.send_keys("Prueba con Selenium WebDriver")

    # Acepta el prompt
    alerta_prompt.accept()

    # Pausa corta para observar resultados
    time.sleep(2)

finally:
    # ------------------------------
    # CIERRE DEL NAVEGADOR
    # ------------------------------

    driver.quit()
