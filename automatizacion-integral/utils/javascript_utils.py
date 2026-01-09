def js_a_texto(ruta_js: str) -> str:
    with open(ruta_js, "r", encoding="utf-8") as archivo:
        return archivo.read()
