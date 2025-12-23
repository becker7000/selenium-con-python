from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime


# ===============================
# CONFIGURACIÓN DEL ARCHIVO DE TRAZAS
# ===============================
nombre_archivo_log = f"trazas_{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.txt"

def traza(mensaje):
    """
    Imprime el mensaje en consola y lo guarda en un archivo .txt
    """
    print(mensaje)
    with open(nombre_archivo_log, "a", encoding="utf-8") as archivo:
        archivo.write(mensaje + "\n")


# ===============================
# INICIO DEL SCRIPT
# ===============================
traza("\n\t 1. Iniciando prueba de listas desplegables estándar")

# ===============================
# CONFIGURACIÓN DEL DRIVER
# ===============================
traza("\n\t 2. Configurando el WebDriver (Chrome)")
driver = webdriver.Chrome()

traza("\n\t 3. Maximizando ventana del navegador")
driver.maximize_window()

traza("\n\t 4. Configurando espera explícita (10 segundos)")
espera = WebDriverWait(driver, 10)


# =====================================================
# 4.1 LISTAS DESPLEGABLES <select> (ESTÁNDAR)
# =====================================================
traza("\n\t 5. Listas desplegables <select>")

url = "https://the-internet.herokuapp.com/dropdown"
traza(f"\n\t 6. Navegando a la URL: {url}")
driver.get(url)

traza("\n\t 7. Esperando que el elemento <select> esté presente en el DOM")
select_dropdown = espera.until(
    EC.presence_of_element_located((By.ID, "dropdown"))
)
traza("\n\t 8. Elemento <select> localizado correctamente")

traza("\n\t 9. Creando objeto Select para interactuar con el dropdown")
lista_opciones = Select(select_dropdown)


# =====================================================
# SELECCIÓN DE OPCIONES
# =====================================================
traza("\n\t 10. Seleccionando opción por TEXTO visible: 'Option 1'")
lista_opciones.select_by_visible_text("Option 1")
traza("\n\t 11. Opción 'Option 1' seleccionada")
time.sleep(1)

traza("\n\t 12. Seleccionando opción por VALOR: '2'")
lista_opciones.select_by_value("2")
traza("\n\t 13. Opción con valor '2' seleccionada")
time.sleep(1)

traza("\n\t 14. Seleccionando opción por ÍNDICE: 1")
lista_opciones.select_by_index(1)
traza("\n\t 15. Opción con índice 1 seleccionada")
time.sleep(1)


# =====================================================
# OBTENER OPCIONES DISPONIBLES
# =====================================================
traza("\n\t 16. Listando todas las opciones disponibles en el select:")
for indice, opcion in enumerate(lista_opciones.options):
    traza(f"\t   {indice} -> {opcion.text}")


# ===============================
# CIERRE
# ===============================
traza("\n\t 17. Finalizando prueba")
traza("\n\t 18. Esperando 2 segundos antes de cerrar el navegador")
time.sleep(2)

traza("\n\t 19. Cerrando el navegador")
driver.quit()

traza("\n\t 20. Script finalizado correctamente")
