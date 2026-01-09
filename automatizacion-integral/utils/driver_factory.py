from selenium import webdriver

def crear_driver():
    opciones = webdriver.ChromeOptions()
    opciones.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=opciones)
    driver.maximize_window()
    return driver
