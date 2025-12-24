from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time


def iniciar_navegador():
    opciones = Options()
    opciones.add_argument("--start-maximized")

    servicio = Service()  # Usa webdriver-manager si lo deseas
    navegador = webdriver.Chrome(service=servicio, options=opciones)
    return navegador

def buscar_elementos_anidados(navegador):
    """
    Ejemplo de búsqueda de elementos dentro de otros elementos
    usando patrones de localización recomendados
    """

    # Abrir página de ejemplo
    navegador.get("https://www.saucedemo.com/")
    time.sleep(2)

    # --- Patrón recomendado: By.ID para elementos únicos ---
    campo_usuario = navegador.find_element(By.ID, "user-name")
    campo_password = navegador.find_element(By.ID, "password")
    boton_login = navegador.find_element(By.ID, "login-button")

    campo_usuario.send_keys("standard_user")
    campo_password.send_keys("secret_sauce")
    boton_login.click()
    time.sleep(3)

    # --- Localizar elemento PADRE ---
    # Contenedor principal de productos
    contenedor_productos = navegador.find_element(By.CLASS_NAME, "inventory_list")

    # --- Buscar elementos HIJOS dentro del contenedor ---
    lista_productos = contenedor_productos.find_elements(
        By.CLASS_NAME, "inventory_item"
    )

    print(f"Productos encontrados: {len(lista_productos)}")

    # Recorrer cada producto y buscar elementos internos
    for producto in lista_productos:
        nombre_producto = producto.find_element(
            By.CLASS_NAME, "inventory_item_name"
        ).text

        precio_producto = producto.find_element(
            By.CLASS_NAME, "inventory_item_price"
        ).text

        boton_agregar = producto.find_element(
            By.TAG_NAME, "button"
        )

        print(f"Producto: {nombre_producto} | Precio: {precio_producto}")

        # Ejemplo: hacer clic solo en el primer producto
        boton_agregar.click()


def cerrar_navegador(navegador):
    time.sleep(3)
    navegador.quit()


if __name__ == "__main__":
    navegador = iniciar_navegador()
    buscar_elementos_anidados(navegador)
    cerrar_navegador(navegador)
