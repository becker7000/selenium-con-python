# --------------------------------------------------
# IMPORTACIÓN DE LIBRERÍAS
# --------------------------------------------------

# Importamos el webdriver principal de Selenium
from selenium import webdriver

# Importamos By para localizar elementos
from selenium.webdriver.common.by import By

# Importamos WebDriverWait para esperas explícitas
from selenium.webdriver.support.ui import WebDriverWait

# Importamos condiciones esperadas
from selenium.webdriver.support import expected_conditions as EC

# Importamos time para pausas visuales (solo enseñanza)
import time

# --------------------------------------------------
# CONFIGURACIÓN DEL DRIVER
# --------------------------------------------------

# Creamos las opciones de Chrome
opciones_chrome = webdriver.ChromeOptions()

# Evita que el navegador se cierre automáticamente
opciones_chrome.add_experimental_option("detach", True)

# Inicializamos el driver de Chrome
driver = webdriver.Chrome(options=opciones_chrome)

# Maximizamos la ventana
driver.maximize_window()

# --------------------------------------------------
# ABRIR SITIO WEB
# --------------------------------------------------

# Navegamos al sitio de pruebas
driver.get("https://automationexercise.com")

# Esperamos carga completa
time.sleep(3)

# --------------------------------------------------
# INICIALIZACIÓN DE JAVASCRIPT EXECUTOR
# --------------------------------------------------

# Creamos referencia al ejecutor JavaScript
ejecutor_js = driver.execute_script

# --------------------------------------------------
# ESPERA DE ELEMENTO BASE DEL DOM
# --------------------------------------------------

# Esperamos a que el cuerpo de la página esté presente
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "body"))
)

print("✅ Página cargada correctamente")

# --------------------------------------------------
# SCROLL PROGRAMÁTICO
# --------------------------------------------------

# Scroll hasta el final de la página
ejecutor_js("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

# Scroll hasta la mitad
ejecutor_js("window.scrollTo(0, document.body.scrollHeight / 2);")
time.sleep(2)

# Scroll al inicio
ejecutor_js("window.scrollTo(0, 0);")
time.sleep(2)

# --------------------------------------------------
# MANIPULACIÓN DEL DOM (CREAR ELEMENTO)
# --------------------------------------------------

# Creamos un nuevo div dinámicamente
ejecutor_js("""
    var nuevoDiv = document.createElement("div");
    nuevoDiv.id = "div_prueba_selenium";
    nuevoDiv.innerText = "🚀 Elemento creado dinámicamente con JavaScript";
    nuevoDiv.style.backgroundColor = "#222";
    nuevoDiv.style.color = "white";
    nuevoDiv.style.padding = "15px";
    nuevoDiv.style.margin = "20px";
    nuevoDiv.style.fontSize = "20px";
    document.body.prepend(nuevoDiv);
""")

time.sleep(2)

# --------------------------------------------------
# MODIFICAR ELEMENTO EXISTENTE
# --------------------------------------------------

# Cambiamos el texto del título principal
ejecutor_js("""
    var titulo = document.querySelector("h2");
    titulo.innerText = "🔥 Título modificado desde Selenium con JavaScript";
    titulo.style.color = "red";
""")

time.sleep(2)

# --------------------------------------------------
# INTERACCIÓN NO NATIVA (CLICK FORZADO)
# --------------------------------------------------

# Localizamos el enlace "Products"
enlace_productos = driver.find_element(By.LINK_TEXT, "Products")

# Forzamos el clic con JavaScript
ejecutor_js("arguments[0].click();", enlace_productos)

# Esperamos la navegación
time.sleep(3)

# --------------------------------------------------
# EJECUTAR JAVASCRIPT Y OBTENER DATOS
# --------------------------------------------------

# Obtenemos el título de la página mediante JavaScript
titulo_pagina = ejecutor_js("return document.title;")

print("📄 Título actual de la página:", titulo_pagina)

# --------------------------------------------------
# DISPARAR EVENTO PERSONALIZADO
# --------------------------------------------------

# Disparamos un evento scroll manual
ejecutor_js("""
    window.dispatchEvent(new Event('scroll'));
""")

time.sleep(2)

# --------------------------------------------------
# FINALIZACIÓN
# --------------------------------------------------

print("✅ Script ejecutado correctamente en sitio estable")

# Cierre opcional
# driver.quit()
