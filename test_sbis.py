import pytest
from selenium import webdriver
from pages import ContactsPage


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_change_region_and_verify_city(browser):
    contacts_page = ContactsPage(browser)
    browser.get("https://sbis.ru/")
    contacts_page.click_contacts_link()

    # Check the URL after clicking on the "Контакты" link
    assert "contacts" in browser.current_url, f"URL does not contain 'contacts': {browser.current_url}"

    contacts_page.click_region_element()
    contacts_page.select_kamchatka_region()

    # Check the URL after selecting the Kamchatka region
    expected_url = "https://sbis.ru/contacts/76-yaroslavskaya-oblast?tab=clients"
    assert expected_url == browser.current_url, f"Expected URL: {expected_url}, Actual URL: {browser.current_url}"

    # Verify that the city element displays "Петропавловск-Камчатский"
    city_text = contacts_page.get_city_element_text()
    assert "Петропавловск-Камчатский" in city_text, f"City element does not contain 'Петропавловск-Камчатский': {city_text}"