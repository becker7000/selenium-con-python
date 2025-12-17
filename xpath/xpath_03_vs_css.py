from selenium import webdriver
from selenium.webdriver.common.by import By

# Inicializamos el navegador
navegador = webdriver.Chrome()

# Abrimos un sitio público
navegador.get("https://es.wikipedia.org/wiki/HTML")

# ---------------- SELECTOR CSS ----------------
# CSS es más simple y rápido, pero menos potente
titulo_css = navegador.find_element(
    By.CSS_SELECTOR,
    "h1"
)

print("Título usando CSS:", titulo_css.text)

# ---------------- XPATH ----------------
# XPath es más potente y permite navegación compleja
titulo_xpath = navegador.find_element(
    By.XPATH,
    "//h1"
)

print("Título usando XPath:", titulo_xpath.text)

# ---------------- CRITERIOS DE SELECCIÓN ----------------
# CSS selecciona por clase
elemento_css_clase = navegador.find_element(
    By.CSS_SELECTOR,
    ".mw-parser-output p"
)

print("Primer párrafo con CSS:", elemento_css_clase.text[:100])

# XPath selecciona por estructura

primer_parrafo = navegador.find_element(
    By.XPATH,
    "(//div[@id='mw-content-text']//p[not(@class) and normalize-space()])[1]"
)
print("Primer párrafo con XPath:", primer_parrafo.text[:100])

# ---------------- VENTAJAS Y DESVENTAJAS ----------------
# CSS: más rápido, más legible, pero sin navegación hacia padres
# XPath: más potente, más flexible, pero más largo y complejo

navegador.quit()
