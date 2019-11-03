#Python default packages
import sys
import os
import time
import logging

#Custom packages
import unittest
from selenium import webdriver
from Resources import googlePage


class GooleSearch(unittest.TestCase):
    '''A sample test class to show how page object works'''

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.google.com/")

    def test_search_google(self):
        '''
        Tests google.com search feature. Searches for the word "pycon" then verified that some results show up
        Note that it does not look for any particular text in search results page. This test verifies that
        the results were not empty.
        '''

        #Load the main page. In this case the home page of Python.org.
        main_page = page.MainPage(self.driver)
        #Checks if the word "Python" is in title
        assert main_page.is_title_matches(), "Google"
        #Sets the text of search textbox to "pycon"
        main_page.search_text_element = "pycon"
        main_page.click_go_button()
        search_results_page = page.SearchResultsPage(self.driver)
        #Verifies that the results page is not empty
        assert search_results_page.is_results_found(), "No results found."
        time.sleep(3)

    def tearDown(self):
        self.driver.close()

#Code to run the test suite
if __name__ == "__main__":
    unittest.main()