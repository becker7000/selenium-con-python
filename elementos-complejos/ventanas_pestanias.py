from selenium import webdriver
from wait_helper import WaitHelper


def inicializar_navegador():
    navegador = webdriver.Chrome()
    navegador.maximize_window()
    print("\n[TRACE] Navegador inicializado y maximizado")
    return navegador


def abrir_pagina_principal(navegador):
    url = "https://www.w3schools.com"
    navegador.get(url)
    print(f"[TRACE] Sitio abierto en pestaña principal: {url}")


def abrir_nueva_pestana(navegador, url):
    navegador.execute_script(
        f"window.open('{url}', '_blank');"
    )
    print(f"[TRACE] Nueva pestaña abierta: {url}")


def ejecutar_prueba_manejo_ventanas():
    navegador = inicializar_navegador()
    wait_helper = WaitHelper(navegador, 10)

    try:
        # Abre la página principal
        abrir_pagina_principal(navegador)

        # Espera a que cargue correctamente
        wait_helper.esperar_titulo_contiene("W3Schools")

        # Guarda el handle principal
        handle_principal = navegador.current_window_handle
        print("\n\t1. Handle principal registrado:")
        print("\t   ", handle_principal)

        # Abre pestañas secundarias
        abrir_nueva_pestana(navegador, "https://www.w3schools.com/html/")
        abrir_nueva_pestana(navegador, "https://www.w3schools.com/js/")

        # Espera a que existan 3 ventanas
        wait_helper.esperar_numero_ventanas(3)

        # Muestra todas las ventanas abiertas
        print("\n\t2. Ventanas actualmente abiertas:")
        for indice, handle in enumerate(navegador.window_handles, start=1):
            navegador.switch_to.window(handle)
            print(f"\t   {indice}. Título: {navegador.title}")

        # Regresa al handle principal
        navegador.switch_to.window(handle_principal)
        print("\n\t3. Contexto final regresado a la ventana principal")
        print("\t   Título activo:", navegador.title)

    finally:
        # Traza de cierre completo
        print("\n[TRACE] Cerrando TODAS las ventanas y finalizando la sesión")
        navegador.quit()
        print("[TRACE] Sesión de Selenium finalizada correctamente")


if __name__ == "__main__":
    ejecutar_prueba_manejo_ventanas()
