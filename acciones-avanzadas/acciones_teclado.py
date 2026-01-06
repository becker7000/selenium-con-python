from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


class AccionesAvanzadasTeclado:

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
    # Envío de teclas especiales
    # --------------------------------------------------

    def envio_teclas_especiales(self):
        print("▶ Enviando teclas especiales")
        self.driver.get("https://www.w3schools.com/html/html_forms.asp")

        campo_nombre = self.driver.find_element(By.ID, "fname")

        campo_nombre.click()

        # Limpiar contenido previo ("John")
        campo_nombre.clear()
        self.esperar(1)

        # Escribir nuevo texto
        campo_nombre.send_keys("Juan Perez")
        self.esperar(1)

        # BACKSPACE
        campo_nombre.send_keys(Keys.BACKSPACE)
        self.esperar(1)

        # DELETE
        campo_nombre.send_keys(Keys.DELETE)
        self.esperar(1)

        # TAB para cambiar de campo
        campo_nombre.send_keys(Keys.TAB)
        self.esperar()


    # --------------------------------------------------
    # Combinaciones de teclas
    # --------------------------------------------------

    def combinaciones_de_teclas(self):
        print("▶ Ejecutando combinaciones de teclas")
        self.driver.get("https://www.w3schools.com/tags/tag_textarea.asp")

        self.esperar(2)

        # Cambiar al iframe del ejemplo
        iframe = self.driver.find_element(By.CSS_SELECTOR, "iframe")
        self.driver.switch_to.frame(iframe)

        textarea = self.driver.find_element(By.TAG_NAME, "textarea")

        textarea.click()
        textarea.send_keys("Este texto será seleccionado, copiado y pegado.")
        self.esperar(1)

        # CTRL + A (seleccionar todo)
        self.acciones.key_down(Keys.CONTROL)\
                    .send_keys("a")\
                    .key_up(Keys.CONTROL)\
                    .perform()
        self.esperar(1)

        # CTRL + C (copiar)
        self.acciones.key_down(Keys.CONTROL)\
                    .send_keys("c")\
                    .key_up(Keys.CONTROL)\
                    .perform()
        self.esperar(1)

        # Mover cursor al final
        textarea.send_keys(Keys.END)
        textarea.send_keys(Keys.ENTER)

        # CTRL + V (pegar)
        self.acciones.key_down(Keys.CONTROL)\
                    .send_keys("v")\
                    .key_up(Keys.CONTROL)\
                    .perform()

        # Volver al documento principal
        self.driver.switch_to.default_content()
        self.esperar()

    # --------------------------------------------------
    # Automatización de flujo complejo con teclado
    # --------------------------------------------------

    def flujo_complejo_con_teclado(self):
        print("▶ Automatizando flujo complejo con teclado")
        self.driver.get("https://www.typingclub.com/sportal/program-3/123.play")

        self.esperar(3)

        # El foco inicial ya está en el área de escritura
        texto = (
            "automatizar flujos complejos con selenium "
            "usando solo el teclado "
        )

        for letra in texto:
            self.acciones.send_keys(letra).perform()
            time.sleep(0.1)

        # Simular ENTER y SPACE como en una lección real
        self.acciones.send_keys(Keys.ENTER).perform()
        self.esperar(1)
        self.acciones.send_keys(Keys.SPACE).perform()
        self.esperar()

    # --------------------------------------------------
    # Flujo completo
    # --------------------------------------------------

    def ejecutar_demo_completa(self):
        try:
            self.envio_teclas_especiales()
            self.combinaciones_de_teclas()
            self.flujo_complejo_con_teclado()
        finally:
            print("✔ Demo de teclado finalizada")
            self.driver.quit()


# --------------------------------------------------
# Ejecución principal
# --------------------------------------------------

if __name__ == "__main__":
    demo = AccionesAvanzadasTeclado()
    demo.ejecutar_demo_completa()
