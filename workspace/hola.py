"""
Comandos previos:
python -m venv venv
.\venv\Scripts\activate
pip install PyUnitReport
pip install selenium
pip install webdriver-manager
python -m pip install --upgrade pip
pip show selenium  # para comprobar
"""

# Importa el módulo unittest, que permite crear y ejecutar casos de prueba estructurados.
import unittest

# Importa HTTPTestRunner para generar reportes HTML de las pruebas.
from pyunitreport import HTMLTestRunner

# Importa webdriver de Selenium para controlar navegadores.
from selenium import webdriver

# Importa Service para configurar correctamente el driver de Chrome en Selenium moderno.
from selenium.webdriver.chrome.service import Service

# Importa ChromeDriverManager para administrar automáticamente la descarga del ChromeDriver.
from webdriver_manager.chrome import ChromeDriverManager


# Define una clase de prueba que hereda de unittest.TestCase.
class Hola(unittest.TestCase):

    # Mé_todo que se ejecuta antes de cada prueba.
    @classmethod # Primero ejecutarlo con self en vez de cls y sin este decorador
    def setUpClass(cls):
        # Inicializa el navegador Chrome usando Service y ChromeDriverManager.
        # Esto evita tener que especificar manualmente la ruta del driver.
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        # Configura un tiempo de espera implícito de 10 segundos.
        # El driver esperará hasta 10 segundos al buscar elementos antes de lanzar error.
        cls.driver.implicitly_wait(10)

    # Mé_todo que contiene la prueba principal (debe iniciar con "test_" para ser detectado).
    def test_hola_google(self):
        # Abre la página de Google utilizando el navegador controlado por Selenium.
        self.driver.get("https://www.google.com/")

    # Otra prueba que deseamos que se ejecute:
    def test_hola_tiobe(self):
        self.driver.get("https://www.tiobe.com/tiobe-index/")

    # Mé_todo que se ejecuta después de cada prueba.
    @classmethod
    def tearDownClass(cls): # @classmethod # Primero ejecutarlo con self en vez de cls y sin este decorador
        # Cierra el navegador y termina la sesión de WebDriver.
        cls.driver.quit()


# Bloque que permite ejecutar las pruebas desde la línea de comandos.
if __name__ == "__main__":
    # Ejecuta todas las pruebas de la clase Hola.
    # verbosity=2 muestra más detalles en la consola.
    # testRunner genera un reporte HTML en la carpeta 'reportes' con el nombre 'hola-reporte'.
    unittest.main(
        verbosity=2,
        testRunner=HTMLTestRunner(output='first', report_name='hola-reporte')
    )
