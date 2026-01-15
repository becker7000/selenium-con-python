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
# TEST: LIMITACIONES Y PARTICULARIDADES DE LOCALIZADORES
# ======================================================

def test_limitaciones_localizadores(navegador):
    """
    TEMA 4 – LOCALIZADORES EN SELENIUM (CERTIFICACIÓN)

    Este test ilustra:
    - Limitaciones de By.CLASS_NAME con clases compuestas
    - Cuándo NO usar XPath
    - Ventajas y desventajas reales entre CSS y XPath
    - Impacto de los localizadores en estabilidad
    - Buenas prácticas de localización
    """

    espera = WebDriverWait(navegador, 10)
    navegador.get("https://www.w3schools.com/html/html_forms.asp")
    print("[NAV] Página de formularios HTML cargada")

    # --------------------------------------------------
    # 1. LIMITACIÓN DE By.CLASS_NAME
    # --------------------------------------------------
    print("[STEP 1] Limitación de By.CLASS_NAME con clases compuestas")

    # Este div tiene múltiples clases CSS (ejemplo real en W3Schools)
    contenedor = espera.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.w3-example"))
    )

    assert contenedor is not None, "El contenedor con clase w3-example debería existir"
    print("✔ Contenedor localizado correctamente con CSS_SELECTOR")

    # ❌ NO SE DEBE HACER (clases compuestas NO funcionan con CLASS_NAME)
    # navegador.find_element(By.CLASS_NAME, "w3-example w3-light-grey")

    # ✔ Correcto: usar SOLO UNA clase
    contenedor_por_clase = navegador.find_element(By.CLASS_NAME, "w3-example")
    assert contenedor_por_clase is not None, "No se pudo localizar usando una sola clase"
    print("✔ Localización correcta usando una sola clase")

    # --------------------------------------------------
    # 2. CUÁNDO NO USAR XPATH
    # --------------------------------------------------
    print("[STEP 2] Cuándo NO usar XPath")

    campo_nombre = navegador.find_element(By.ID, "fname")
    assert campo_nombre is not None, "El campo fname debería existir"
    print("✔ Campo localizado por ID (mejor práctica)")

    # ❌ XPath innecesario, largo y frágil
    # campo_nombre = navegador.find_element(
    #     By.XPATH, "/html/body/div[4]/div/div/div/form/input[1]"
    # )

    print("✔ Evitamos XPath absoluto por baja mantenibilidad")

    # --------------------------------------------------
    # 3. CSS vs XPATH – COMPARATIVA REAL
    # --------------------------------------------------
    print("[STEP 3] Comparativa CSS vs XPath")

    # ✔ CSS: rápido, legible, recomendado
    campo_apellido_css = navegador.find_element(By.CSS_SELECTOR, "input#lname")
    assert campo_apellido_css is not None, "No se pudo localizar el campo lname con CSS"
    print("✔ Campo localizado con CSS Selector")

    # ❌ XPath equivalente (funciona, pero menos recomendable)
    # campo_apellido_xpath = navegador.find_element(
    #     By.XPATH, "//input[@id='lname']"
    # )

    # --------------------------------------------------
    # 4. BUENAS PRÁCTICAS (CERTIFICACIÓN)
    # --------------------------------------------------
    print("[STEP 5] Buenas prácticas de localización")

    # Orden recomendado:
    # 1. ID
    # 2. NAME
    # 3. CSS_SELECTOR
    # 4. CLASS_NAME (una sola clase)
    # 5. XPath (solo si no hay alternativa)

    assert navegador.find_element(By.NAME, "fname"), \
        "La localización por NAME debería funcionar"

    print("✔ Buenas prácticas aplicadas correctamente")

    print("[TEST] Test de limitaciones de localizadores finalizado correctamente")


    
