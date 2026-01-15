import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ======================================================
# FIXTURE PYTEST – WEBDRIVER (SEARCH CONTEXT RAÍZ)
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
# TEST: SEARCH CONTEXT EN SELENIUM
# ======================================================

def test_search_context_w3schools(navegador):
    """
    TEMA 3 – SEARCH CONTEXT
    - WebDriver como contexto raíz
    - WebElement como contexto de búsqueda
    - Diferencia entre find_element desde driver y desde WebElement
    - Comparativa conceptual con XPath
    """

    espera = WebDriverWait(navegador, 10)
    navegador.get("https://www.w3schools.com/html/html_forms.asp")
    print("[NAV] Página de formularios HTML cargada")

    # --------------------------------------------------
    # 1️⃣ WEBDRIVER COMO SEARCH CONTEXT (RAÍZ)
    # --------------------------------------------------
    print("[STEP 1] WebDriver como Search Context raíz")

    formulario = espera.until(
        EC.presence_of_element_located((By.TAG_NAME, "form"))
    )

    assert formulario is not None, "El formulario debería existir en el DOM"
    print("✔ Formulario encontrado usando WebDriver")

    # --- Con XPath (menos recomendado) ---
    # formulario = navegador.find_element(By.XPATH, "//form")

    # --------------------------------------------------
    # 2️⃣ WEBELEMENT COMO SEARCH CONTEXT
    # --------------------------------------------------
    print("[STEP 2] WebElement como Search Context")

    campo_nombre = formulario.find_element(By.ID, "fname")
    campo_apellido = formulario.find_element(By.ID, "lname")

    assert campo_nombre is not None, "El campo 'fname' debería existir dentro del formulario"
    assert campo_apellido is not None, "El campo 'lname' debería existir dentro del formulario"

    print("✔ Campos encontrados usando WebElement como contexto")

    # --- Con XPath ---
    # campo_nombre = navegador.find_element(By.XPATH, "//form//input[@id='fname']")
    # campo_apellido = navegador.find_element(By.XPATH, "//form//input[@id='lname']")

    # --------------------------------------------------
    # 3️⃣ DIFERENCIA: DRIVER vs WEBELEMENT
    # --------------------------------------------------
    print("[STEP 3] Diferencia entre contextos de búsqueda")

    # Búsqueda desde el driver (todo el DOM)
    campo_driver = navegador.find_element(By.ID, "fname")

    # Búsqueda desde el formulario (solo hijos del form)
    campo_form = formulario.find_element(By.ID, "fname")

    assert campo_driver == campo_form, "Ambos contextos deberían devolver el mismo elemento"
    print("✔ Mismo elemento localizado desde contextos distintos")

    # --------------------------------------------------
    # 4️⃣ INTERACCIÓN USANDO CONTEXTO CORRECTO
    # --------------------------------------------------
    print("[STEP 4] Interacción usando contexto específico")

    campo_form.clear()
    campo_form.send_keys("Selenium")

    campo_apellido.clear()
    campo_apellido.send_keys("Search Context")

    assert campo_form.get_attribute("value") == "Selenium", \
        "El texto del campo nombre no coincide"

    print("✔ Datos ingresados correctamente usando WebElement como contexto")

    # --------------------------------------------------
    # 5️⃣ BÚSQUEDA DE ELEMENTOS ANIDADOS
    # --------------------------------------------------
    print("[STEP 5] Búsqueda de elementos anidados")

    inputs_formulario = formulario.find_elements(By.TAG_NAME, "input")

    assert len(inputs_formulario) > 0, \
        "Debería existir al menos un input dentro del formulario"

    print(f"✔ Inputs encontrados dentro del formulario: {len(inputs_formulario)}")

    # --- Con XPath ---
    # inputs_formulario = navegador.find_elements(By.XPATH, "//form//input")

    print("[TEST] Test de Search Context finalizado correctamente")
