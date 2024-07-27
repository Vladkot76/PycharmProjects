from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ContactsPage:
    def __init__(self, driver):
        self.driver = driver

    def click_contacts_link(self):
        contacts_link = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".sbisru-Header__menu-link[href='/contacts']")))
        contacts_link.click()

    def get_city_element_text(self):
        city_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#city-id-2.sbisru-Contacts-List__city")))
        return city_element.text

    def click_region_element(self):
        region_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".sbis_ru-Region-Chooser__text.sbis_ru-link")))
        region_element.click()

    def select_kamchatka_region(self):
        kamchatka_region = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), '41 Камчатский край')]")))
        kamchatka_region.click()