"""
ARCHIVO: test_assertions_selenium.py

Este script demuestra el uso de ASSERTIONS en pruebas automatizadas
con Selenium WebDriver y PyTest.

Sintáxis general: assert condicion, "mensaje de error"

"""

# ============================
# IMPORTS NECESARIOS
# ============================

# WebDriver de Selenium
from selenium import webdriver

# Localización de elementos
from selenium.webdriver.common.by import By

# Opciones y servicio para Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# PyTest (framework de testing)
import pytest


# ======================================================
# FIXTURE DE PYTEST (MEJOR PRÁCTICA)
# ======================================================
@pytest.fixture
def navegador():
    """
    Fixture que:
    - Inicializa el navegador
    - Lo cierra automáticamente al finalizar la prueba
    """

    opciones = Options()
    opciones.add_argument("--start-maximized")

    servicio = Service()
    driver = webdriver.Chrome(service=servicio, options=opciones)

    # Devuelve el navegador a la prueba
    yield driver

    # Cierre garantizado (aunque la prueba falle)
    driver.quit()


# ======================================================
# TEST: ASSERTIONS BÁSICAS
# ======================================================
def test_assertions_basicas(navegador):
    """
    Prueba automatizada que demuestra:
    - Concepto de assertion
    - Validación de texto visible
    - Validación de estado de elementos
    """

    # --------------------------------------------------
    # PASO 1: Abrir página de prueba
    # --------------------------------------------------
    navegador.get("https://www.selenium.dev/selenium/web/web-form.html")

    # --------------------------------------------------
    # CONCEPTO DE ASSERTION
    # Una assertion valida que algo sea VERDADERO
    # Si falla, la prueba se marca como FALLIDA
    # --------------------------------------------------

    # Assertion básica: verificar que el título contiene texto esperado
    assert "Web form" in navegador.title, "El título de la página no es correcto"

    # --------------------------------------------------
    # VALIDACIÓN DE TEXTO VISIBLE
    # --------------------------------------------------

    # Localizar el encabezado <h1>
    encabezado = navegador.find_element(By.TAG_NAME, "h1")

    # Assertion: validar el texto visible del encabezado
    assert encabezado.text == "Web form", "El texto del encabezado no coincide"

    # --------------------------------------------------
    # VALIDACIÓN DE ESTADO DE ELEMENTOS
    # --------------------------------------------------

    # Localizar campo de texto
    campo_texto = navegador.find_element(By.NAME, "my-text")

    # Assertion: verificar que el campo está visible
    assert campo_texto.is_displayed(), "El campo de texto no está visible"

    # Assertion: verificar que el campo está habilitado
    assert campo_texto.is_enabled(), "El campo de texto no está habilitado"

    # --------------------------------------------------
    # VALIDACIÓN DE CHECKBOX
    # --------------------------------------------------

    checkbox = navegador.find_element(By.ID, "my-check-1")

    # Assertion: inicialmente debe estar seleccionado
    assert checkbox.is_selected(), "El checkbox debería estar seleccionado"

    # Acción: seleccionar checkbox
    checkbox.click()

    # Assertion: ahora NO debe estar seleccionado
    assert not checkbox.is_selected(), "El checkbox NO debería estar seleccionado"

    # --------------------------------------------------
    # VALIDACIÓN DE BOTÓN
    # --------------------------------------------------

    boton_submit = navegador.find_element(By.TAG_NAME, "button")

    # Assertion: verificar que el botón está habilitado
    assert boton_submit.is_enabled(), "El botón Submit no está habilitado"

    """
        python -m venv venv
        .\venv\Scripts\Activate
        python -m pip install --upgrade pip
        pip install selenium pytest
        pip freeze > requirements.txt
        pytest intro_assertions.py
        deactivate
    """
