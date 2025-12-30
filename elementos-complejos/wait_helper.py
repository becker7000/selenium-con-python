# Importa WebDriverWait para esperas explícitas
from selenium.webdriver.support.ui import WebDriverWait

# Importa expected_conditions para definir condiciones
from selenium.webdriver.support import expected_conditions as EC


class WaitHelper:
    # Constructor que recibe el driver y el tiempo máximo de espera
    def __init__(self, driver, tiempo_espera=10):
        # Guarda el driver
        self.driver = driver

        # Guarda el tiempo máximo de espera
        self.tiempo_espera = tiempo_espera

        # Crea una instancia de WebDriverWait reutilizable
        self.wait = WebDriverWait(driver, tiempo_espera)

    # Espera a que un elemento exista en el DOM
    def esperar_presencia_elemento(self, localizador):
        return self.wait.until(
            EC.presence_of_element_located(localizador)
        )

    # Espera a que un elemento sea visible
    def esperar_elemento_visible(self, localizador):
        return self.wait.until(
            EC.visibility_of_element_located(localizador)
        )

    # Espera a que un elemento sea clickeable
    def esperar_elemento_clickeable(self, localizador):
        return self.wait.until(
            EC.element_to_be_clickable(localizador)
        )

    # Espera a que el título contenga un texto específico
    def esperar_titulo_contiene(self, texto):
        return self.wait.until(
            EC.title_contains(texto)
        )

    # Espera a que exista un número específico de ventanas
    def esperar_numero_ventanas(self, cantidad):
        return self.wait.until(
            EC.number_of_windows_to_be(cantidad)
        )
