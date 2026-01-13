from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# ======================================================
# CONFIGURACIÓN DEL WEBDRIVER
# ======================================================
print("▶ Iniciando navegador Chrome...")

opciones = Options()
opciones.add_argument("--start-maximized")

servicio = Service()
navegador = webdriver.Chrome(service=servicio, options=opciones)

print("▶ Abriendo página de prueba de Selenium")
navegador.get("https://www.selenium.dev/selenium/web/web-form.html")
time.sleep(2)

# ======================================================
# CONCEPTO: LOCALIZACIÓN RELATIVA
# ======================================================

print("\n▶ Localizando campo de texto base (my-text)")
campo_texto = navegador.find_element(By.NAME, "my-text")
time.sleep(1)

# ------------------------------------------------------
# below(): elemento debajo de otro
# ------------------------------------------------------
print("▶ Localizando input DEBAJO del campo de texto (below)")
campo_password = navegador.find_element(
    locate_with(By.TAG_NAME, "input").below(campo_texto)
)
campo_password.send_keys("password123")
time.sleep(1)

# ------------------------------------------------------
# above(): elemento arriba de otro
# ------------------------------------------------------
print("▶ Localizando input ARRIBA del campo password (above)")
campo_arriba = navegador.find_element(
    locate_with(By.TAG_NAME, "input").above(campo_password)
)
campo_arriba.clear()
campo_arriba.send_keys("Selenium 4")
time.sleep(1)

# ------------------------------------------------------
# toRightOf(): elemento a la derecha
# ------------------------------------------------------
print("▶ Localizando checkbox izquierdo por ID")
checkbox_izquierdo = navegador.find_element(By.ID, "my-check-1")
time.sleep(1)

print("▶ Localizando checkbox A LA DERECHA (toRightOf)")
checkbox_derecho = navegador.find_element(
    locate_with(By.TAG_NAME, "input").to_right_of(checkbox_izquierdo)
)
checkbox_derecho.click()
time.sleep(1)

# ------------------------------------------------------
# toLeftOf(): elemento a la izquierda
# ------------------------------------------------------
print("▶ Localizando checkbox A LA IZQUIERDA (toLeftOf)")
checkbox_localizado = navegador.find_element(
    locate_with(By.TAG_NAME, "input").to_left_of(checkbox_derecho)
)
checkbox_localizado.click()
time.sleep(1)

# ======================================================
# CIERRE
# ======================================================
print("\n▶ Finalizando demostración...")
time.sleep(2)
navegador.quit()
print("✔ Navegador cerrado correctamente")
