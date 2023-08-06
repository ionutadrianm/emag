from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep

class ComparePage(BasePage):
    COMPARA_PRODUSE_TEXT = (By.XPATH, '//*[@id="main-container"]/section/div/div[1]/h1')

    def verify_that_title_is_correct(self):
        actual = self.driver.find_element(*self.COMPARA_PRODUSE_TEXT).text
        expected = 'Compară produse'
        self.assertEqual(expected, actual, 'Invalid title for compare change')
        sleep(2)

