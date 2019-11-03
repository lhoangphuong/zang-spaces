#--------------------------------------------------------------------#
#This is where page are stored
#
#
#--------------------------------------------------------------------#

from phuong_element import BasePageElement
from phuong_locators import MainPageLocators




class SearchTextElement(BasePageElement):
    ''' 
    This class gets the search text from the specified locator
    The locator for search box where search string is entered
    '''
    locator = 'q'

class BasePage():
    'Base class to initialize the base page that will be called from all pages'

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    'Home page action methods come here. I.e. Google.com'

    #Declares a variable that will contain the retrieved text
    search_text_element = SearchTextElement()

    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in page title"""
        return "Python" in self.driver.title

    def click_go_button(self):
        """Triggers the search"""
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()

