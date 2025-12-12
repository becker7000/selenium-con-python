from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from lxml import html

# Configuración del WebDriver para usar Chrome
options = Options()
options.headless = True  # Para que no se abra una ventana del navegador

# Iniciar el navegador con Selenium
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Abrimos la página de Wikipedia
url = "https://es.wikipedia.org/wiki/Wikipedia:Portada"
driver.get(url) 

# Esperamos a que se cargue el contenido (esto puede necesitar ajustes dependiendo del sitio)
driver.implicitly_wait(10)  # Espera hasta 10 segundos

# Ahora que la página está completamente cargada, podemos obtener el HTML
page_html = driver.page_source  # Renombramos la variable para evitar el conflicto

# Parseamos el HTML con lxml
tree = html.fromstring(page_html)  # Usamos la variable page_html para parsear

# Ahora podemos usar XPath como antes
contenido_relativo = tree.xpath('//h1/text()')
print("Contenido Relativo:", contenido_relativo)

enlaces_wiki = tree.xpath('//a[contains(@href, "wiki")]/@href')
print("Enlaces que contienen 'wiki':", enlaces_wiki)

# Cerramos el navegador después de obtener los datos
driver.quit()


"""
1. Contenido Relativo:

Se extrajo parcialmente el texto del primer encabezado (<h1>), 
mostrando " a Wikipedia,", aunque parece que hay un pequeño error 
en la extracción (posiblemente por un espacio extra o un nodo adicional dentro del <h1>).

2. Enlaces que contienen 'wiki':

Se listaron enlaces internos y externos que contienen 'wiki' 
en su atributo href, incluyendo enlaces a páginas internas de Wikipedia 
(e.g., /wiki/Wikipedia:Portada) y enlaces a otros proyectos de Wikimedia y sitios relacionados, 
como donaciones o Commons.
"""