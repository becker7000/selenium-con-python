# Importamos la clase webdriver de Selenium para controlar el navegador
from selenium import webdriver

# Importamos la clase By para indicar el tipo de selector (XPath en este caso)
from selenium.webdriver.common.by import By

# Creamos una instancia del navegador (Chrome)
navegador = webdriver.Chrome()

# Abrimos un sitio público e interesante (Wikipedia)
navegador.get("https://es.wikipedia.org/wiki/Python")

# ---------------- XPATH RELATIVO ----------------
# Buscamos el mismo título usando XPath relativo
# XPath relativo usa // y es más flexible
titulo_relativo = navegador.find_element(
    By.XPATH,
    "//h1"
)

# Imprimimos el texto obtenido
print("Título con XPath relativo:", titulo_relativo.text)

# ---------------- BÚSQUEDA POR ATRIBUTOS ----------------
# Buscamos un enlace usando un atributo href
enlace_idioma = navegador.find_element(
    By.XPATH,
    "//a[@lang='en']"
)

# Imprimimos el texto del enlace
print("Enlace por atributo:", enlace_idioma.text)

# ---------------- FUNCIÓN text() ----------------
# Buscamos un párrafo cuyo texto sea exactamente "Python"
elemento_texto = navegador.find_element(
    By.XPATH,
    "//a[text()='Python']"
)

print("Elemento usando text():", elemento_texto.text)

# ---------------- FUNCIÓN contains() ----------------
# Buscamos enlaces que contengan la palabra "program"
enlace_contains = navegador.find_element(
    By.XPATH,
    "//a[contains(@href,'program')]"
)

print("Elemento usando contains():", enlace_contains.get_attribute("href"))

# ---------------- FUNCIÓN starts-with() ----------------
# Buscamos enlaces cuyo href comience con "/wiki"
enlace_starts = navegador.find_element(
    By.XPATH,
    "//a[starts-with(@href,'/wiki')]"
)

print("Elemento usando starts-with():", enlace_starts.get_attribute("href"))

# Cerramos el navegador
navegador.quit()
