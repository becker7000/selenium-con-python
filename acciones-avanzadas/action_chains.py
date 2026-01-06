from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class AccionesAvanzadasMouse:

    def __init__(self):
        self.driver = self.inicializar_navegador()
        self.acciones = ActionChains(self.driver)

    def inicializar_navegador(self):
        opciones = webdriver.ChromeOptions()
        opciones.add_argument("--start-maximized")
        servicio = Service(ChromeDriverManager().install())
        return webdriver.Chrome(service=servicio, options=opciones)

    def esperar(self, segundos=2):
        time.sleep(segundos)

    # --------------------------------------------------
    # Hover (movimientos del ratón)
    # --------------------------------------------------

    def hover_menu(self):
        print("▶ Ejecutando hover con tooltip visible (W3Schools)")
        self.driver.get("https://www.w3schools.com/css/css_tooltip.asp")

        # Scroll para asegurar visibilidad
        self.driver.execute_script("window.scrollBy(0, 300);")
        self.esperar(1)

        # Elemento que muestra tooltip al hacer hover
        tooltip = self.driver.find_element(By.XPATH, "//div[contains(@class,'tooltip')]")

        # Hover prolongado para notar el efecto visual
        self.acciones.move_to_element(tooltip).perform()

        self.esperar()

    # --------------------------------------------------
    # Doble clic y clic derecho
    # --------------------------------------------------

    def clicks_avanzados(self):
        print("▶ Ejecutando clic derecho y doble clic")
        self.driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

        boton = self.driver.find_element(By.CSS_SELECTOR, ".context-menu-one")

        # Clic derecho
        self.acciones.context_click(boton).perform()
        self.esperar(1)

        # Doble clic (sobre el mismo elemento)
        self.acciones.double_click(boton).perform()
        self.esperar()

    # --------------------------------------------------
    # Drag and Drop
    # --------------------------------------------------

    def arrastrar_y_soltar(self):
        print("▶ Ejecutando drag and drop (jQuery UI)")
        self.driver.get("https://jqueryui.com/droppable/")

        # Cambiar al iframe del ejemplo
        iframe = self.driver.find_element(By.CLASS_NAME, "demo-frame")
        self.driver.switch_to.frame(iframe)

        # Elementos drag & drop
        origen = self.driver.find_element(By.ID, "draggable")
        destino = self.driver.find_element(By.ID, "droppable")

        # Drag and drop con ActionChains
        self.acciones.drag_and_drop(origen, destino).perform()

        # Volver al documento principal
        self.driver.switch_to.default_content()
        self.esperar()

    # --------------------------------------------------
    # Flujo completo
    # --------------------------------------------------

    def ejecutar_demo_completa(self):
        try:
            self.hover_menu()
            self.clicks_avanzados()
            self.arrastrar_y_soltar()

        finally:
            print("✔ Demo finalizada")
            self.driver.quit()


# --------------------------------------------------
# Ejecución principal
# --------------------------------------------------

if __name__ == "__main__":
    demo = AccionesAvanzadasMouse()
    demo.ejecutar_demo_completa()
