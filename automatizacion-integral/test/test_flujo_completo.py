from utils.driver_factory import crear_driver
from utils.esperas import esperar_elemento
from utils.javascript_utils import js_a_texto

from pages.home_page import HomePage
from pages.products_page import ProductsPage

from selenium.webdriver.common.by import By

def test_flujo_completo():

    # Verso 1: el navegador despierta
    driver = crear_driver()
    driver.get("https://automationexercise.com")

    # Verso 2: el DOM se revela
    esperar_elemento(driver, (By.TAG_NAME, "body"))

    # Verso 3: los caminos se nombran
    home = HomePage(driver)
    home.ir_a_productos()

    # Verso 4: la espera escucha
    esperar_elemento(driver, (By.ID, "search_product"))

    # Verso 5: la palabra se escribe
    productos = ProductsPage(driver)
    productos.buscar_producto("Dress")

    # Verso 6: el mouse danza
    productos.hover_primer_producto()

    # Verso 7: JavaScript susurra
    driver.execute_script(
        js_a_texto("js/resaltar_elemento.js")
    )

    # Verso final: la prueba existe
    assert "Products" in driver.title
