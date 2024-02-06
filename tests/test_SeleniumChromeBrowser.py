"""
Author : shivangi Gupta
"""

import pytest
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from interviewFrameworkTest.pom.HomePage import HomePage
from interviewFrameworkTest.utilities.Baseclass import BaseClass


@pytest.mark.usefixtures("setup")
class TestBrowserActions(BaseClass):

    @pytest.mark.Smoke
    def test_http_post_loaded(self, setup):
        log_msg = self.logger()
        log_msg.info(f"start url is {self.driver.current_url}")
        homepage = HomePage(self.driver)
        httpPage = homepage.click_http()
        # wait = WebDriverWait(self.driver, 10)
        self.custom_wait("HTTP page")
        print(self.driver.title, self.driver.current_url)
        assert "http-post/" in self.driver.current_url
        assert "HTTP Post" in self.driver.title

    @pytest.mark.Regression
    def test_Subscribe_on_http_page(self, setup, test_data):
        log_msg = self.logger()
        log_msg.info(f"start url is {self.driver.current_url}")
        homepage = HomePage(self.driver)
        httpPage = homepage.click_http()
        self.custom_wait("HTTP page")
        email = test_data[0]
        name = test_data[1]
        company = test_data[2]
        log_msg.warning(f"email, name, company : {email} {name} {company}")
        self.driver, message = httpPage.click_subscribe(email, name , company)
        assert "successful" in message
        assert "http-post/" in self.driver.current_url
        # print(message, self.driver.current_url)

    @pytest.mark.Sanity
    @pytest.mark.Integration
    @pytest.mark.Regression

    def test_Subscribe_on_https_page(self, setup,test_data):
        log_msg = self.logger()
        log_msg.info(f"start url is {self.driver.current_url}")
        homepage = HomePage(self.driver)
        httpsPage = homepage.click_https()
        self.custom_wait("HTTPS page")
        email = test_data[0]
        name = test_data[1]
        company = test_data[2]
        print(f"failing data is {name}{email}{company}")
        log_msg.debug(f"email, name, company : {email} {name} {company}")
        self.driver, message = httpsPage.click_subscribe(email, name , company)
        assert "successful" in message
        assert "https-post/" in self.driver.current_url

