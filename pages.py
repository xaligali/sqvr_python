from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://sqvr.ru"

    def go_to_site(self):
        self.driver.get(self.base_url)
        return MainPage(self.driver)

    def wait_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message = f"Can't find element by locator {locator}")

class MainPage(BasePage):
    def go_to_create_meeting_page(self):
        self.driver.find_element(*MainPageLocators.LOCATOR_CREATE_MEETING_XPATH).click()
        return CreateMeetingPage(self.driver)

class CreateMeetingPage(BasePage):
    def go_to_constructor_meeting_page(self):
        self.driver.find_element(*CreateMeetingPageLocators.LOCATOR_CHOOSE_TEMPLATE_CSS).click()
        self.driver.find_element(*CreateMeetingPageLocators.LOCATOR_OVERHAUL_CSS).click()
        return ConstructorMeetingPage(self.driver)

class ConstructorMeetingPage(BasePage):
    def input_text(self, locator, input):
        self.driver.find_element(*locator).send_keys(input)

    def check_name_and_number_apartment(self):
        self.driver.find_element(*ConstructorMeetingPageLocators.LOCATOR_button_form_archive_css).click()
        name_xpath = self.driver.find_element(*ConstructorMeetingPageLocators.LOCATOR_name_xpath).text
        number_apartment_xpath = self.driver.find_element(*ConstructorMeetingPageLocators.LOCATOR_number_apartment_xpath).text
        return (name_xpath, number_apartment_xpath)

    def check_download_form_archive(self):
        self.input_text(ConstructorMeetingPageLocators.LOCATOR_input_name_css, ConstructorMeetingPageLocators.name)
        self.input_text(ConstructorMeetingPageLocators.LOCATOR_input_number_apartment_css,
                        ConstructorMeetingPageLocators.number_apartment)
        self.driver.find_element(*ConstructorMeetingPageLocators.LOCATOR_button_form_archive_css).click()
        self.wait_element(ConstructorMeetingPageLocators.LOCATOR_link_css)
        return self.driver.find_element(*ConstructorMeetingPageLocators.LOCATOR_success_mesg_css).text

    def check_address_and_email(self):
        self.input_text(ConstructorMeetingPageLocators.LOCATOR_input_address_xpath,
                        ConstructorMeetingPageLocators.name_address)
        self.input_text(ConstructorMeetingPageLocators.LOCATOR_input_email_xpath, ConstructorMeetingPageLocators.email)
        self.driver.find_element(*ConstructorMeetingPageLocators.LOCATOR_register_line_xpath).click()
        address_xpath = self.driver.find_element(*ConstructorMeetingPageLocators.LOCATOR_address_xpath).get_attribute("value")
        email_css = self.driver.find_element(*ConstructorMeetingPageLocators.LOCATOR_email_css).get_attribute("value")
        return (address_xpath, email_css)
