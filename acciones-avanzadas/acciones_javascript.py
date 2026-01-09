
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import js_a_texto
import time

opciones_chrome = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=opciones_chrome)
driver.maximize_window()
driver.get("https://automationexercise.com/")
time.sleep(2)

# Guardando la referencia de la función para ejecutar JS
ejecutar_js = driver.execute_script

WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.TAG_NAME,"body"))
)

print("\n\t Sitio de automatización de pruebas cargado correctamente...")

# Scroll programático

ejecutar_js("window.scrollTo(0, 200);")
time.sleep(2)

ejecutar_js("window.scrollTo(0, document.body.scrollHeight/2 );")
time.sleep(2)

# Scroll continuo
for i in range(2,1000,2):
    ejecutar_js(f"window.scrollTo(0,{i})")
    time.sleep(0.01)

# Inicio del sitio
ejecutar_js("window.scrollTo(0, 0);")
time.sleep(2)

# Manipulando el DOM
ejecutar_js(
    """
        let nuevoDiv = document.createElement("div");
        nuevoDiv.id = "contenedor_selenium";
        nuevoDiv.innerText = "Elemento creado dinámicamente con Selenium con JavaScript 🤖";
        nuevoDiv.style.backgroundColor = "#242625";
        nuevoDiv.style.color = "#d5e63e";
        nuevoDiv.style.padding = "16px";
        nuevoDiv.style.margin = "20px";
        nuevoDiv.style.fontSize = "20px";
        document.body.prepend(nuevoDiv);
    """
)
time.sleep(4)

# Modificando un web element existente en el DOM
ejecutar_js(
    """
        let titulo = document.getElementsByTagName("h1")[0];
        titulo.innerText = "Título modificado desde Selenium con Javascript 🧑‍💻";
        titulo.style.color = "#202375";
        titulo.style.margin = "16px";
    """
)

time.sleep(3)

# TODO: crear un transformador de archivos .js a texto
#  (el contenido del archivo de código se transforma a texto)

# --------------------------------------------------
# MANIPULACIÓN DEL DOM (RESALTAR ELEMENTO EXISTENTE)
# --------------------------------------------------

# Resaltamos visualmente el enlace "Products" usando JavaScript
ejecutar_js("""
    var elemento = document.querySelector('a[href="/products"]');
    
    elemento.style.border = "4px solid red";
    elemento.style.backgroundColor = "yellow";
    elemento.style.padding = "5px";
    
    // Animación simple para llamar la atención
    elemento.style.transition = "all 0.3s ease-in-out";
""")

time.sleep(2)

# --------------------------------------------------
# INTERACCIÓN NO NATIVA (CLICK GARANTIZADO)
# --------------------------------------------------

# Localizamos el enlace "Products" usando selector CSS (más robusto)
enlace_productos = driver.find_element(
    By.CSS_SELECTOR, 'a[href="/products"]'
)

# Hacemos scroll hasta el elemento para garantizar visibilidad
ejecutar_js("arguments[0].scrollIntoView(true);", enlace_productos)
time.sleep(1)

# Forzamos el clic real mediante JavaScript
ejecutar_js("""
    arguments[0].dispatchEvent(
        new MouseEvent('click', {
            bubbles: true,
            cancelable: true,
            view: window
        })
    );
""", enlace_productos)

# Esperamos la navegación
time.sleep(3)

# Usando nuestra función que obtiene JS de un archivo
ejecutar_js(js_a_texto("resaltar_busqueda.js"))
time.sleep(3)

# --------------------------------------------------
# FINALIZACIÓN
# --------------------------------------------------

print("\n\t Script ejecutado correctamente en sitio estable")

# Cierre opcional
driver.quit()
