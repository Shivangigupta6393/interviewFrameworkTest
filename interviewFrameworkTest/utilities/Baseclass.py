import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BaseClass:

    def custom_wait(self,element):
        wait = WebDriverWait(self.driver, 10)
        if element == "HTTP page":
            wait.until(ec.visibility_of_element_located((By.XPATH, "//h2/span[text()='HTTP Post']")))
        elif element == "HTTPS page":
            wait.until(ec.visibility_of_element_located((By.XPATH, "//h2/span[text()='HTTPS Post']")))
         # elif element == "Page loading":
         #     wait.until(ec.dom)

    def logger(self):
        logging.basicConfig(level=logging.INFO)
        mylogger = logging.getLogger()
        return mylogger
