from selenium import webdriver
from selenium.webdriver.common.by import By

# Inicializamos el navegador
navegador = webdriver.Chrome()

# Abrimos un sitio educativo público
navegador.get("https://www.w3schools.com/html/html_tables.asp")

# ---------------- USO DE COMODINES ----------------
# El comodín * selecciona cualquier etiqueta
primer_elemento_tabla = navegador.find_element(
    By.XPATH,
    "//*[@id='customers']//tr[2]/*[1]"
)

print("Primer elemento de la fila:", primer_elemento_tabla.text)

# ---------------- OPERADOR OR ----------------
# Seleccionamos enlaces que tengan texto HTML o CSS
enlace_or = navegador.find_element(
    By.XPATH,
    "//a[contains(text(),'HTML') or contains(text(),'CSS')]"
)

print("Enlace con OR:", enlace_or.text)

# ---------------- OPERADOR NOT ----------------
# Seleccionamos enlaces que NO tengan la palabra JavaScript
enlace_not = navegador.find_element(
    By.XPATH,
    "//a[not(contains(text(),'JavaScript'))]"
)

print("Enlace con NOT:", enlace_not.text)

# ---------------- AXIS: PARENT ----------------
# Seleccionamos el padre de una celda
padre = navegador.find_element(
    By.XPATH,
    "//td[text()='Alfreds Futterkiste']/parent::tr"
)

print("Fila padre encontrada")

# ---------------- AXIS: CHILD ----------------
# Seleccionamos los hijos de una fila
hijos = navegador.find_elements(
    By.XPATH,
    "//tr[2]/child::td"
)

for hijo in hijos:
    print("Hijo:", hijo.text)

# ---------------- AXIS: ANCESTOR ----------------
# Buscamos el ancestro table de una celda
ancestro = navegador.find_element(
    By.XPATH,
    "//td[text()='Mexico']/ancestor::table"
)

print("Ancestro table encontrado")

# ---------------- AXIS: DESCENDANT ----------------
# Seleccionamos todos los descendientes td de la tabla
descendientes = navegador.find_elements(
    By.XPATH,
    "//table[@id='customers']/descendant::td"
)

print("Total de celdas:", len(descendientes))

# ---------------- PRECEDING-SIBLING ----------------
# Seleccionamos el hermano anterior
anterior = navegador.find_element(
    By.XPATH,
    "//td[text()='Mexico']/preceding-sibling::td"
)

print("Preceding sibling:", anterior.text)

navegador.quit()
