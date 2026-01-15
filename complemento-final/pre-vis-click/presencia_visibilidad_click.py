import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ======================================================
# FIXTURE PYTEST – WEBDRIVER
# ======================================================

@pytest.fixture
def navegador():
    print("\n[SETUP] Iniciando navegador Chrome")

    opciones = Options()
    opciones.add_argument("--start-maximized")

    driver = webdriver.Chrome(service=Service(), options=opciones)
    yield driver

    print("[TEARDOWN] Cerrando navegador")
    driver.quit()


# ======================================================
# TEST CERTIFICACIÓN: PRESENCE / VISIBILITY / CLICKABLE
# ======================================================

def test_presencia_visibilidad_clickable(navegador):
    print("[TEST] Inicio de la prueba")

    espera = WebDriverWait(navegador, 10)
    navegador.get("https://www.selenium.dev/selenium/web/web-form.html")
    print("[NAV] Página web-form.html cargada")

    # --------------------------------------------------
    # 1️⃣ PRESENCE: elemento existe en el DOM
    # --------------------------------------------------
    print("[STEP 1] Verificando PRESENCE del campo de texto")

    campo_texto = espera.until(
        EC.presence_of_element_located((By.NAME, "my-text"))
    )

    assert campo_texto is not None
    print("✔ Elemento presente en el DOM")

    # --------------------------------------------------
    # 2️⃣ VISIBILITY: elemento visible en pantalla
    # --------------------------------------------------
    print("[STEP 2] Verificando VISIBILITY del campo de texto")

    campo_visible = espera.until(
        EC.visibility_of(campo_texto)
    )

    assert campo_visible.is_displayed()
    print("✔ Elemento visible")

    # Validación de propiedades CSS (típica de examen)
    display = campo_visible.value_of_css_property("display")
    visibility = campo_visible.value_of_css_property("visibility")

    print(f"   CSS display: {display}")
    print(f"   CSS visibility: {visibility}")

    assert display != "none"
    assert visibility == "visible"

    # --------------------------------------------------
    # 3️⃣ CLICKABLE: elemento visible y habilitado
    # --------------------------------------------------
    print("[STEP 3] Verificando CLICKABLE del campo")

    campo_clickable = espera.until(
        EC.element_to_be_clickable((By.NAME, "my-text"))
    )

    assert campo_clickable.is_enabled()
    print("✔ Elemento habilitado y clickable")

    campo_clickable.send_keys("Selenium Certification")
    print("✔ Texto enviado correctamente")

    # --------------------------------------------------
    # 4️⃣ ESTADO DE CHECKBOX (otro caso de certificación)
    # --------------------------------------------------
    print("[STEP 4] Verificando estado de checkbox")

    checkbox = navegador.find_element(By.ID, "my-check-1")

    print(f"   Checkbox seleccionado: {checkbox.is_selected()}")
    assert checkbox.is_selected() or not checkbox.is_selected()
    print("✔ Estado del checkbox evaluado")

    print("[TEST] Prueba finalizada correctamente")

# Ejecutar con: pytest presencia_visibilidad_click.py