from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep


class ProductsPage(BasePage):
    RESULTS_TITLE = (By.XPATH, '//a[@data-zone="title"]')
    VEZI_DETALII_COS_BTN = (By.XPATH, '//a[text()="Vezi detalii cos"]')
    COMPARA_BUTTON = (By.XPATH, '//*[@id="compare-link"]')

    def click_vezi_detalii_cos(self):
        self.wait_and_click_elem_by_selector(*self.VEZI_DETALII_COS_BTN)

    def verify_results_contain_text(self, text):
        title_list = self.driver.find_elements(*self.RESULTS_TITLE)
        for i in range(5):
            title = title_list[i].text.lower()
            self.assertTrue(text in title, 'Result does not contain search query')

    def add_to_basket_by_partial_product_name(self, partial_name):
        self.driver.find_element(By.XPATH,f'//a[contains(text(), "{partial_name}")]/parent::div/parent::div/parent::div//button[text()="Adauga in Cos"]').click()

    def find_compare_checkbox_for_item(self, item_index):
        return self.driver.find_element(By.XPATH, f'//*[@id="card_grid"]/div[{item_index}]/div/div/div[2]/button[2]')

    def select_for_comparison(self, item_index):
        checkbox = self.find_compare_checkbox_for_item(item_index).click()
        sleep(2)


    def click_compara_button(self):
        self.driver.find_element(*self.COMPARA_BUTTON).click()
