from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


# ===============================
# 0. CONFIGURACIÓN INICIAL
# ===============================
print("\n\t 1. Iniciando prueba de esperas en Selenium WebDriver")

print("\n\t 2. Configurando el WebDriver (Chrome)")
driver = webdriver.Chrome()

print("\n\t 3. Maximizando ventana del navegador")
driver.maximize_window()

print("\n\t 4. Navegando a la página de prueba (carga dinámica)")
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")


# =========================================================
# 1. ESPERAS ESTÁTICAS (mala practica)
# =========================================================
print("\n\t 5. Demostrando espera estática (time.sleep)")

print("\n\t 6. Esperando 3 segundos de forma fija (mala práctica)")
time.sleep(3)


# =========================================================
# 2. ESPERA IMPLÍCITA (buena plactica)
# =========================================================
print("\n\t 7. Configurando espera implícita (10 segundos)")
driver.implicitly_wait(10)

print("\n\t 8. Localizando y haciendo clic en el botón Start")
start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
start_button.click()


# =========================================================
# 3. ESPERA EXPLÍCITA CON WebDriverWait
# =========================================================
print("\n\t 9. Configurando espera explícita con WebDriverWait (10 segundos)")
wait = WebDriverWait(driver, 10)

try:
    print("\n\t 10. Esperando a que el mensaje final sea visible")
    mensaje = wait.until(
        EC.visibility_of_element_located((By.ID, "finish"))
    )
    print(f"\n\t 11. Texto encontrado: {mensaje.text}")

except TimeoutException:
    print("\n\t Error: El elemento no apareció dentro del tiempo esperado")


# =========================================================
# 4. EXPECTED CONDITIONS
# =========================================================
print("\n\t 12. Navegando a página de login para probar Expected Conditions")
driver.get("https://the-internet.herokuapp.com/login")

print("\n\t 13. Esperando campo username (presence_of_element_located)")
# El elemento ya fue cargado en el HTML, aunque esté oculto.
username = wait.until(
    EC.presence_of_element_located((By.ID, "username"))
)

print("\n\t 14. Esperando campo password (element_to_be_clickable)")
password = wait.until(
    EC.element_to_be_clickable((By.ID, "password"))
)

print("\n\t 15. Ingresando credenciales")
username.send_keys("tomsmith")
password.send_keys("SuperSecretPassword!")

print("\n\t 16. Esperando botón Login y haciendo clic")
login_btn = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.radius"))
)
login_btn.click()

print("\n\t 17. Esperando mensaje de confirmación")
# El elemento existe y el usuario ya lo puede ver.
flash_message = wait.until(
    EC.visibility_of_element_located((By.ID, "flash"))
)
print(f"\n\t 18. Mensaje mostrado: {flash_message.text[:30]} ")

# =========================================================
# 5. ESPERAS PERSONALIZADAS
# =========================================================
print("\n\t 19. Ejecutando espera personalizada")

def texto_contiene_palabra(driver):
    """
    Espera personalizada:
    Retorna True cuando el texto contiene la palabra 'secure'
    """
    elemento = driver.find_element(By.ID, "flash")
    return "secure" in elemento.text.lower()


try:
    print("\n\t 20. Esperando que el texto contenga la palabra 'secure'")
    WebDriverWait(driver, 10).until(texto_contiene_palabra)
    print("\n\t 21. Texto esperado encontrado mediante espera personalizada")

except TimeoutException:
    print("\n\t Error: No se cumplió la condición personalizada")


# ===============================
# 6. CIERRE
# ===============================
print("\n\t 22. Finalizando prueba de esperas")
print("\n\t 23. Esperando 2 segundos antes de cerrar el navegador")
time.sleep(2)

print("\n\t 24. Cerrando el navegador")
driver.quit()

print("\n\t 25. Script finalizado correctamente")
