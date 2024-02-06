from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import time

class HttpsPostPage:

    def __init__(self, driver):
        self.driver = driver

    email_input = (By.ID, "EMAIL")
    name_input = (By.CSS_SELECTOR, "input[placeholder='NAME']")
    company_input = (By.XPATH, "//input[@name='COMPANY']")
    subscribe_button = (By.XPATH, "//button[@class='sib-form-block__button sib-form-block__button-with-loader']")
    success_msg = (By.CSS_SELECTOR, "#success-message")

    def click_subscribe(self, email, name, company):
        self.driver.switch_to.frame(0)
        self.driver.find_element(*HttpsPostPage.email_input).send_keys(email)
        self.driver.find_element(*HttpsPostPage.name_input).send_keys(name)
        self.driver.find_element(*HttpsPostPage.company_input).send_keys(company)
        self.driver.find_element(*HttpsPostPage.subscribe_button).click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.visibility_of_element_located((By.ID, "success-message")))
        message = self.driver.find_element(*HttpsPostPage.success_msg).text
        self.driver.switch_to.default_content()
        return self.driver, message


