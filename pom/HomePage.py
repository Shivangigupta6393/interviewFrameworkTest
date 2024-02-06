from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

from interviewFrameworkTest.pom.HttpPostPage import HttpPostPage
from interviewFrameworkTest.pom.HttpsPostPage import HttpsPostPage


class HomePage():

    def __init__(self,driver):
        self.driver = driver

    http_post = (By.LINK_TEXT,"HTTP Post")
    https_post = (By.LINK_TEXT,"HTTPS Post")

    def click_http(self):
        self.driver.find_element(*HomePage.http_post).click()
        httpPostPage = HttpPostPage(self.driver)
        return httpPostPage

    def click_https(self):
        self.driver.find_element(*HomePage.https_post).click()
        httpsPostPage = HttpsPostPage(self.driver)
        return httpsPostPage


