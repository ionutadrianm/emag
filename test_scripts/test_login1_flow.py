from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

driver.maximize_window()

driver.get('https://emag.ro')

INTRA_IN_CONT_BTN = (By.XPATH, '(//a[text()="Intra in cont"])[1]')


driver.find_element(*INTRA_IN_CONT_BTN).click()
