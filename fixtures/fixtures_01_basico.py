# =====================================================
# IMPORTACIONES
# =====================================================

# Importa el módulo principal de Selenium para controlar navegadores
from selenium import webdriver

# Importa la clase By para localizar elementos en la página web
from selenium.webdriver.common.by import By

# Importa WebDriverWait para implementar esperas explícitas
from selenium.webdriver.support.ui import WebDriverWait

# Importa condiciones esperadas para sincronización
from selenium.webdriver.support import expected_conditions as EC

# Importa Service para configurar el servicio del driver de Chrome
from selenium.webdriver.chrome.service import Service

# Importa ChromeDriverManager para descargar y gestionar ChromeDriver automáticamente
from webdriver_manager.chrome import ChromeDriverManager


# =====================================================
# "FIXTURE" TRADICIONAL (SETUP Y TEARDOWN)
# =====================================================

# Función que crea e inicializa el navegador (equivalente al setup)
def crear_driver():
    
    # Configura el servicio de ChromeDriver usando webdriver-manager
    servicio = Service(ChromeDriverManager().install())
    
    # Crea una instancia del navegador Chrome usando el servicio configurado
    driver = webdriver.Chrome(service=servicio)
    
    # Maximiza la ventana del navegador
    driver.maximize_window()
    
    # Devuelve el objeto driver para ser usado en las pruebas
    return driver


# Función que cierra el navegador (equivalente al teardown)
def cerrar_driver(driver):
    
    # Cierra todas las ventanas del navegador y finaliza la sesión
    driver.quit()


# =====================================================
# FUNCIONES DE PRUEBA
# =====================================================

# Función que prueba la página de login
def probar_login_pagina(driver):
    
    # Abre la página de login en el navegador
    driver.get("https://the-internet.herokuapp.com/login")

    # Crea una espera explícita con un tiempo máximo de 10 segundos
    espera = WebDriverWait(driver, 10)

    # Espera a que el campo de usuario sea visible en la página
    campo_usuario = espera.until(
        EC.visibility_of_element_located((By.ID, "username"))
    )

    # Espera a que el campo de contraseña sea visible en la página
    campo_contraseña = espera.until(
        EC.visibility_of_element_located((By.ID, "password"))
    )

    # Espera a que el botón de login sea clickeable
    boton_login = espera.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "radius"))
    )

    # Verifica que el campo de usuario esté visible
    assert campo_usuario.is_displayed()

    # Verifica que el campo de contraseña esté visible
    assert campo_contraseña.is_displayed()

    # Verifica que el botón de login esté habilitado
    assert boton_login.is_enabled()

    # Muestra un mensaje indicando que la prueba fue exitosa
    print("\n\t Prueba de login completada con éxito")


# Función que prueba el título de la página principal
def probar_titulo_pagina(driver):
    
    # Abre la página principal del sitio
    driver.get("https://the-internet.herokuapp.com")

    # Verifica que el título de la página contenga el texto esperado
    assert "The Internet" in driver.title

    # Muestra un mensaje indicando que la prueba fue exitosa
    print("\n\t Prueba de título completada con éxito")


# =====================================================
# MAIN (PUNTO DE ENTRADA)
# =====================================================

# Función principal que controla el flujo del programa
def main():
    
    # Crea el navegador llamando a la función de setup
    driver = crear_driver()

    try:
        # Ejecuta la prueba de la página de login
        probar_login_pagina(driver)

        # Ejecuta la prueba del título de la página
        probar_titulo_pagina(driver)

    finally:
        # Asegura que el navegador se cierre aunque ocurra un error
        cerrar_driver(driver)


# =====================================================
# EJECUCIÓN DIRECTA
# =====================================================

# Verifica que el archivo se esté ejecutando directamente
if __name__ == "__main__":
    
    # Llama a la función principal
    main()
