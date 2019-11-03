import time
import unittest
import HtmlTestRunner

from selenium import webdriver
from Locators import Locators
from Pages import AccountPage
from TestData import TestData

#Base Class for the tests
class Test_Zang_Spaces_Base(unittest.TestCase):

    def setUp(self):
        # Setting up how we want Chrome to run
        #chrome_options=webdriver.ChromeOptions()
        self.driver=webdriver.Firefox()
        #browser should be loaded in maximized window
        self.driver.maximize_window()
    
    def tearDown(self):
        # To do the cleanup after test has executed.
        self.driver.close()
        self.driver.quit()
        
# Test class containing methods corresponding to testcases.
class Test_Zang_Spaces(Test_Zang_Spaces_Base):
    def setUp(self):
        # to call the setUp() method of base class or super class.
        super().setUp()

    def test_login_with_google_sso(self):
        """User should be able to login Zang Spaces with google sso"""
        # instantiate an object of HomePage class. Remember when the constructor of HomePage class is called
        # it opens up the browser and navigates to Home Page of the site under test.
        self.accountPage=AccountPage(self.driver)
        # assert if the title of Home Page contains Amazon.in
        self.assertIn(TestData.HOME_PAGE_TITLE, self.accountPage.driver.title)
        # login with google sso
        self.accountPage.click_google_sso_button()
        self.accountPage.enter_google_account()
        time.sleep(5)

    def test_login_with_office365_sso(self):
        """User should be able to login Zang Spaces with office365 sso"""
        # instantiate an object of HomePage class. Remember when the constructor of HomePage class is called
        # it opens up the browser and navigates to Home Page of the site under test.
        self.accountPage=AccountPage(self.driver)
        # assert if the title of Home Page contains Amazon.in
        self.assertIn(TestData.HOME_PAGE_TITLE, self.accountPage.driver.title)
        # login with google sso
        self.accountPage.click_office365_sso_button()
        self.accountPage.enter_office365_account()
        time.sleep(5)
        


# Require to run the test
if __name__ == '__main__':
    # specify path where the HTML reports for testcase execution are to be generated
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output= 'D:/Zang-Spaces/Reports'))