
# --------------------------------------------------
# utils.py
# Funciones utilitarias para Selenium + JavaScript
# --------------------------------------------------

def js_a_texto(nombre_archivo_js: str) -> str:
    """
    Lee un archivo JavaScript (.js) y devuelve su contenido
    como una cadena de texto para ser usada con execute_script().

    :param nombre_archivo_js: Ruta o nombre del archivo .js
    :return: Código JavaScript como string
    """

    # Abrimos el archivo JavaScript en modo lectura
    with open(nombre_archivo_js, "r", encoding="utf-8") as archivo_js:
        # Leemos todo el contenido del archivo
        codigo_javascript = archivo_js.read()

    # Retornamos el código como una cadena
    return codigo_javascript
