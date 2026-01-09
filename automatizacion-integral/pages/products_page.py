from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class ProductsPage:

    def __init__(self, driver):
        self.driver = driver
        self.campo_busqueda = (By.ID, "search_product")
        self.boton_buscar = (By.ID, "submit_search")

    def buscar_producto(self, texto):
        campo = self.driver.find_element(*self.campo_busqueda)
        campo.send_keys(texto)
        self.driver.find_element(*self.boton_buscar).click()

    def hover_primer_producto(self):
        producto = self.driver.find_element(
            By.CSS_SELECTOR, ".product-image-wrapper"
        )
        ActionChains(self.driver).move_to_element(producto).perform()
