import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ======================================================
# CONFIGURACIÓN GENERAL
# ======================================================

GRID_URL = "http://localhost:4444/wd/hub"  # Selenium Grid (Hub)
USAR_GRID = False  # Cambiar a True si se quiere ejecución remota


# ======================================================
# FIXTURE PARAMETRIZADO – BROWSER COVERAGE
# ======================================================

@pytest.fixture(params=["chrome", "edge"])
def navegador(request):
    browser = request.param
    print(f"\n[SETUP] Iniciando navegador: {browser.upper()}")

    if USAR_GRID:
        print("[GRID] Ejecución REMOTA vía Selenium Grid")

        if browser == "chrome":
            options = ChromeOptions()
        else:
            options = EdgeOptions()

        driver = webdriver.Remote(
            command_executor=GRID_URL,
            options=options
        )

    else:
        print("[LOCAL] Ejecución LOCAL (sin Grid)")

        if browser == "chrome":
            options = ChromeOptions()
            options.add_argument("--start-maximized")
            driver = webdriver.Chrome(options=options)

        else:
            options = EdgeOptions()
            options.add_argument("--start-maximized")
            driver = webdriver.Edge(options=options)

    yield driver

    print(f"[TEARDOWN] Cerrando navegador: {browser.upper()}")
    driver.quit()


# ======================================================
# TEST: SELENIUM GRID & BROWSER COVERAGE
# ======================================================

def test_browser_coverage_con_selenium_grid(navegador):
    """
    TEMA 2 – SELENIUM GRID Y BROWSER COVERAGE

    Ilustra:
    - Importancia del browser coverage
    - Ejecución en múltiples navegadores
    - Paralelismo (cuando se usa pytest -n)
    - Diferencia entre ejecución local y remota
    - Casos reales de uso de Selenium Grid
    """

    print("[TEST] Inicio de prueba de browser coverage")

    espera = WebDriverWait(navegador, 10)
    navegador.get("https://www.selenium.dev/")
    print("[NAV] Página selenium.dev cargada")

    # --------------------------------------------------
    # 1️⃣ VALIDACIÓN BÁSICA MULTI-BROWSER
    # --------------------------------------------------
    print("[STEP 1] Validando título de la página")

    titulo = navegador.title
    print(f"   Título obtenido: {titulo}")

    assert "Selenium" in titulo, \
        "El título debería contener la palabra 'Selenium' en cualquier navegador"

    print("✔ Título validado correctamente en este navegador")

    # --------------------------------------------------
    # 2️⃣ VALIDACIÓN DE ELEMENTO COMÚN (CONSISTENCIA)
    # --------------------------------------------------
    print("[STEP 2] Validando elemento común entre navegadores")

    boton_documentation = espera.until(
        EC.visibility_of_element_located((By.LINK_TEXT, "Documentation"))
    )

    assert boton_documentation.is_displayed(), \
        "El link Documentation debería ser visible en todos los navegadores"

    print("✔ Elemento visible de forma consistente")

    # --------------------------------------------------
    # 3️⃣ CASO PRÁCTICO DE GRID
    # --------------------------------------------------
    print("[STEP 3] Caso práctico de Selenium Grid")

    print("   Este mismo test puede ejecutarse:")
    print("   - En Chrome y Edge")
    print("   - En paralelo")
    print("   - En diferentes máquinas / SO")
    print("   - De forma local o remota")

    assert navegador.session_id is not None, \
        "La sesión del navegador debería estar activa"

    print("✔ Sesión activa – prueba ejecutada correctamente")

    print("[TEST] Prueba finalizada correctamente")


"""
SIN PARALELISMO:
pytest grid.py -s


CON PARALELISMO:
pip install pytest-xdist
pytest grid.py -n 2 -s

CONCEPTOS CLAVE (ESTILO CERTIFICACIÓN)
🔹 Browser Coverage

Ejecutar pruebas en múltiples navegadores para detectar diferencias
 de comportamiento, renderizado y compatibilidad.

🔹 Paralelismo

Reduce tiempos de ejecución

Se logra con Grid + pytest-xdist

No es lo mismo que ejecución secuencial multi-browser

🔹 Selenium Grid – Arquitectura

Hub: recibe las pruebas

Nodes: ejecutan los navegadores

Comunicación vía WebDriver Remote

🔹 Local vs Remoto
| Local            | Remoto (Grid)         |
| ---------------- | --------------------- |
| Una sola máquina | Varias máquinas       |
| Más simple       | Más escalable         |
| Más lento        | Más rápido (paralelo) |


"""