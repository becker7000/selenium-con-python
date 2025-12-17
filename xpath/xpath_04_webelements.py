from selenium import webdriver
from selenium.webdriver.common.by import By

# Inicializamos el navegador
navegador = webdriver.Chrome()

# Abrimos una página con formularios
navegador.get("https://www.w3schools.com/html/html_forms.asp")

# Buscamos un campo de texto
campo_nombre = navegador.find_element(
    By.XPATH,
    "//input[@id='fname']"
)

# ---------------- is_displayed() ----------------
# Verifica si el elemento es visible
print("¿Está visible?:", campo_nombre.is_displayed())

# ---------------- is_enabled() ----------------
# Verifica si el elemento está habilitado
print("¿Está habilitado?:", campo_nombre.is_enabled())

# ---------------- get_attribute() ----------------
# Obtiene el valor del atributo type
tipo_campo = campo_nombre.get_attribute("type")
print("Tipo de input:", tipo_campo)

# ---------------- get_property() ----------------
# Obtiene una propiedad del DOM
valor_propiedad = campo_nombre.get_property("value")
print("Valor actual:", valor_propiedad)

# ---------------- is_selected() ----------------
# Buscamos un checkbox
checkbox = navegador.find_element(
    By.XPATH,
    "//input[@type='checkbox']"
)

# Verificamos si está seleccionado
print("¿Checkbox seleccionado?:", checkbox.is_selected())

# Seleccionamos el checkbox (primero probar)
# checkbox.click() # Dará un error porque: El elemento está en el DOM, pero no se puede interactuar con él.

# Seleccionamos ahora pero usando JavaScript
navegador.execute_script(
    "arguments[0].click();",
    checkbox
)

# Verificamos nuevamente
print("¿Checkbox seleccionado ahora?:", checkbox.is_selected())

navegador.quit()
