from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.link_productos = (By.CSS_SELECTOR, 'a[href="/products"]')

    def ir_a_productos(self):
        self.driver.find_element(*self.link_productos).click()
