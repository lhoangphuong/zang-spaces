#--------------------------------------------------------------------#
#This is where locators are stored
#
#
#--------------------------------------------------------------------#

from selenium.webdriver.common.by import By


class MainPageLocators():
    'A Class for main page locators. All main page locators should put here'
    SEARCH_BOX = (By.NAME, 'q')
    SEARCH_BUTTON = (By.NAME, 'btnK')
    SEARCH_FIRST_PAGE_BUTTON =(By.NAME, 'btnI')
#
class SearchResultsPageLocators():
    'A Class for search result page locators. All search result page locators should put here'
    pass