import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from Locators import Locators
from TestData import TestData

class BasePage():
    """This class is the parent class for all the pages in our application."""
    """It contains all common elements and functionalities available to all pages."""

    # this function is called every time a new object of the base class is created.
    def __init__(self, driver):
        self.driver=driver

        # this function performs click on web element whose locator is passed to it.
    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()
    # this function asserts comparison of a web element's text with passed in text.
    def assert_element_text(self, by_locator, element_text):
        web_element=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        assert web_element.text == element_text

    # this function performs text entry of the passed in text, in a web element whose locator is passed to it.
    def enter_text(self, by_locator, text):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    # this function checks if the web element whose locator has been passed to it, is enabled or not and returns
    # web element if it is enabled.
    def is_enabled(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))

    # this function checks if the web element whose locator has been passed to it, is visible or not and returns
    # true or false depending upon its visibility.
    def is_visible(self,by_locator):
        element=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)
    
    # this function moves the mouse pointer over a web element whose locator has been passed to it.
    def hover_to(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()


#################################################################################################################################################################################
#################################################################################################################################################################################
#################################################################################################################################################################################       

class AccountPage(BasePage):
    """Account Page of Zang Spaces"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
    
    def click_google_sso_button(self):
        """User should able to click google sso button"""
        self.click(Locators.GOOGLE_SSO)

    def enter_google_account(self):
        """User should be able to sign in google account"""
        self.enter_text(Locators.GOOGLE_ID_TEXTBOX, TestData.ACCOUNT_1)
        self.click(Locators.GOOGLE_NEXT_BUTTON_1)
        self.enter_text(Locators.GOOGLE_PASSWORD_TEXBOX, TestData.PASSWORD)
        self.click(Locators.GOOGLE_NEXT_BUTTON_2)

    def click_office365_sso_button(self):
        """User should able to click office365 sso button"""
        self.click(Locators.OFFICE365_SSO)

    def enter_office365_account(self):
        """User should be able to sign in office365 account"""
        self.enter_text(Locators.OFFICE365_ID_TEXTBOX, TestData.ACCOUNT_1)
        self.click(Locators.OFFICE365_NEXT_BUTTON)
        self.enter_text(Locators.OFFICE365_PASSWORD_TEXTBOX, TestData.PASSWORD)
        self.click(Locators.OFFICE365_NEXT_BUTTON)
