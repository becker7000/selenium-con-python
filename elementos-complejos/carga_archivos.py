from selenium import webdriver
from selenium.webdriver.common.by import By
import os

from wait_helper import WaitHelper


def inicializar_navegador():
    navegador = webdriver.Chrome()
    navegador.maximize_window()
    return navegador


def abrir_pagina_de_carga(navegador):
    navegador.get(
        "https://www.w3schools.com/howto/howto_html_file_upload_button.asp"
    )


def obtener_ruta_archivo():
    directorio_actual = os.getcwd()
    nombre_archivo = "archivo_prueba_selenium.txt"
    ruta_completa = os.path.join(directorio_actual, nombre_archivo)

    if not os.path.exists(ruta_completa):
        raise FileNotFoundError("El archivo de prueba no existe")

    return ruta_completa


def cargar_archivo(navegador, wait_helper, ruta_archivo):
    # Espera de forma segura al input tipo file
    input_archivo = wait_helper.esperar_presencia_elemento(
        (By.ID, "myFile")
    )

    # Envía la ruta del archivo
    input_archivo.send_keys(ruta_archivo)


def validar_archivo_seleccionado(navegador):
    input_archivo = navegador.find_element(By.ID, "myFile")
    valor_input = input_archivo.get_attribute("value")

    if valor_input:
        print("\n\t Archivo cargado correctamente:", valor_input)
    else:
        print("\n\t No se detectó el archivo cargado")


def ejecutar_prueba_carga_archivo():
    navegador = inicializar_navegador()

    # Inicializa el helper de esperas
    wait_helper = WaitHelper(navegador, 10)

    try:
        abrir_pagina_de_carga(navegador)

        # Espera a que el título confirme que la página cargó
        wait_helper.esperar_titulo_contiene("File Upload")

        ruta_archivo = obtener_ruta_archivo()
        cargar_archivo(navegador, wait_helper, ruta_archivo)
        validar_archivo_seleccionado(navegador)

    finally:
        navegador.quit()


if __name__ == "__main__":
    ejecutar_prueba_carga_archivo()
