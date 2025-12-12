"""
Práctica 1.4 – Uso de selectores CSS en Selenium
Sitio: https://www.saucedemo.com/
Tecnología: Python + Selenium + unittest
"""

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyunitreport import HTMLTestRunner

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class TestSauceDemoCSS(unittest.TestCase):

    def setUp(self):
        """Configuración inicial: abrir Chrome y entrar al sitio"""
        self.options = Options()

        # Desactiva el Password Manager
        self.options.add_argument("--disable-password-manager-rewrite")
        self.options.add_argument("--disable-features=PasswordLeakDetection,PasswordCheck")

        # Asegurar que NO se cargue el perfil de usuario
        self.options.add_argument("--no-first-run")
        self.options.add_argument("--no-default-browser-check")

        # Perfil temporal (evita que Chrome use tus preferencias personales)
        self.options.add_argument("--user-data-dir=/tmp/selenium-profile")

        # Desactiva Credential Manager
        self.prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "password_manager_leak_detection": False
        }
        self.options.add_experimental_option("prefs", self.prefs)

        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    # -----------------------------------------------------------
    # 1. LOGIN usando selectores CSS
    # -----------------------------------------------------------
    def test_01_login(self):
        driver = self.driver
        wait = self.wait

        # Campo username usando CSS por ID (#)
        username = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#user-name")
        ))
        username.send_keys("standard_user")

        # Campo password usando CSS por ID (#)
        password = driver.find_element(By.CSS_SELECTOR, "#password")
        password.send_keys("secret_sauce")

        # Botón Login usando CSS por ID
        login_btn = driver.find_element(By.CSS_SELECTOR, "#login-button")
        login_btn.click()

        # Validar que entramos al inventario usando un selector CSS por clase
        wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".inventory_list")
        ))

    # -----------------------------------------------------------
    # 2. AGREGAR PRODUCTOS usando selectores CSS
    # -----------------------------------------------------------
    def test_02_agregar_productos(self):
        driver = self.driver
        wait = self.wait

        self.test_01_login()  # reutilizamos el login

        # Botón "Add to cart" del primer producto usando clase y atributo
        add_btn_1 = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button.btn.btn_primary.btn_small.btn_inventory")
        ))
        add_btn_1.click()

        # Segundo producto usando selector CSS por ID
        add_btn_2 = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bike-light")
        add_btn_2.click()

    # -----------------------------------------------------------
    # 3. ABRIR CARRITO usando selectores CSS
    # -----------------------------------------------------------
    def test_03_carrito(self):
        driver = self.driver
        wait = self.wait

        self.test_01_login()  # login previo

        # Clic en el carrito usando selector CSS por clase (.) + etiqueta
        carrito = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a.shopping_cart_link")
        ))
        carrito.click()

        # Validamos que estamos dentro del carrito
        wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".cart_list")
        ))

    # -----------------------------------------------------------
    # 4. LOGOUT usando selectores CSS
    # -----------------------------------------------------------
    def test_04_logout(self):

        driver = self.driver
        wait = WebDriverWait(driver, 10)

        self.test_01_login()

        # 1. Abrir el menú
        menu_button = wait.until(
            EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))
        )
        menu_button.click()

        # 2. Esperar a que aparezca el link de logout
        logout_btn = wait.until(
            EC.visibility_of_element_located(
                (By.ID, "logout_sidebar_link")
            )
        )

        # 3. Hacer clic en logout
        logout_btn.click()

        # 4. Validar que volvemos al login
        wait.until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )


    def tearDown(self):
        """Cerrar el navegador después de cada prueba"""
        self.driver.quit()


if __name__ == "__main__":
    # Ejecuta unittest usando HTMLTestRunner como generador de reporte
    unittest.main(
        testRunner=HTMLTestRunner(
            output="reportes",               # Carpeta donde se guardarán los reportes
            report_name="ReporteSelectoresCSS",  # Nombre base del archivo HTML
        ),
        verbosity=2  # Muestra más detalle en consola
    )
