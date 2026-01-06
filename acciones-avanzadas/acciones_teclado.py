from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

        wait = WebDriverWait(self.driver, 10)

        # Esperar a que el campo sea visible y clickeable
        campo_nombre = wait.until(
            EC.element_to_be_clickable((By.ID, "fname"))
        )

        # Asegurar que esté en viewport (mejor que scroll fijo)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            campo_nombre
        )

        campo_nombre.click()

        # Limpiar contenido de forma segura (combinaciones de teclas)
        campo_nombre.send_keys(Keys.CONTROL, "a")
        campo_nombre.send_keys(Keys.DELETE)

        # Escribir texto
        campo_nombre.send_keys("Lauras")

        # BACKSPACE
        campo_nombre.send_keys(Keys.BACKSPACE)

        # DELETE
        campo_nombre.send_keys(Keys.DELETE)

        # TAB para cambiar de campo
        campo_nombre.send_keys(Keys.TAB)

        self.esperar()
        print("✔ Teclas especiales enviadas correctamente")

    # --------------------------------------------------
    # Combinaciones de teclas
    # --------------------------------------------------

    def combinaciones_de_teclas(self):
        print("▶ Ejecutando combinaciones de teclas")
        self.driver.get("https://www.selenium.dev/selenium/web/web-form.html")

        wait = WebDriverWait(self.driver, 10)

        # Campo textarea estable
        textarea = wait.until(
            EC.element_to_be_clickable((By.NAME, "my-textarea"))
        )

        textarea.click()
        self.esperar()

        textarea.send_keys("Este texto será seleccionado, copiado y pegado.")
        self.esperar()

        # CTRL + A (seleccionar todo)
        self.acciones.key_down(Keys.CONTROL)\
                    .send_keys("a")\
                    .key_up(Keys.CONTROL)\
                    .perform()
        self.esperar()

        # CTRL + C (copiar)
        self.acciones.key_down(Keys.CONTROL)\
                    .send_keys("c")\
                    .key_up(Keys.CONTROL)\
                    .perform()
        self.esperar()

        # Mover cursor al final
        textarea.send_keys(Keys.END)
        textarea.send_keys(Keys.ENTER)
        self.esperar()

        # CTRL + V (pegar)
        self.acciones.key_down(Keys.CONTROL)\
                    .send_keys("v")\
                    .key_up(Keys.CONTROL)\
                    .perform()
        self.esperar()

        print("✔ Combinaciones de teclas ejecutadas correctamente")


    # --------------------------------------------------
    # Automatización de flujo complejo con teclado
    # --------------------------------------------------

    def flujo_complejo_con_teclado(self):
        print("▶ Automatizando flujo complejo con teclado")

        self.driver.get("https://www.selenium.dev/selenium/web/web-form.html")

        wait = WebDriverWait(self.driver, 10)

        # Área de escritura (textarea estable)
        area_escritura = wait.until(
            EC.element_to_be_clickable((By.NAME, "my-textarea"))
        )

        area_escritura.click()
        self.esperar(1)

        texto = (
            "automatizar flujos complejos con selenium "
            "usando solo el teclado "
            "es util para pruebas automatizadas "
        )

        # Escritura humana
        for letra in texto:
            self.acciones.send_keys(letra).perform()
            time.sleep(0.1)

        # Simular ENTER
        self.acciones.send_keys(Keys.ENTER).perform()
        self.esperar(1)

        # Continuar escribiendo
        texto2 = "este texto continua despues de presionar enter "

        for letra in texto2:
            self.acciones.send_keys(letra).perform()
            time.sleep(0.1)

        # Simular SPACE final
        self.acciones.send_keys(Keys.SPACE).perform()
        self.esperar(1)

        print("✔ Flujo complejo con teclado ejecutado correctamente")
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
