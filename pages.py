from BaseApp import BasePage
from selenium.webdriver.common.by import By

class MainPageLocators:
    LOCATOR_CREATE_MEETING_XPATH = (By.XPATH, "(//*[text()='Провести собрание'])[1]")

class CreateMeetingPageLocators:
    LOCATOR_CHOOSE_TEMPLATE_CSS = (By.CSS_SELECTOR, "[class='act tt_choose_template']")
    LOCATOR_OVERHAUL_CSS = (By.CSS_SELECTOR, "[class='btn btn-blue btn-sm tt_overhaul']")

class ConstructorMeetingPageLocators:
    LOCATOR_button_form_archive_css = (By.CSS_SELECTOR, "[class='download-link tt_form_archive']")
    LOCATOR_error_mesg_name = "Фамилия и имя являются обязательными"
    LOCATOR_error_mesg_number = "Поле является обязательным"
    LOCATOR_name_xpath = (By.XPATH, "(//*[@class='error__text'])[1]")
    LOCATOR_number_apartment_xpath = (By.XPATH, "(//*[@class='error__text'])[2]")
    LOCATOR_input_name = "Ivanov Ivan"
    LOCATOR_input_number_apartment = "15"
    LOCATOR_input_name_css = (By.CSS_SELECTOR, "[name = 'full_name']")
    LOCATOR_input_number_apartment_css = (By.CSS_SELECTOR, "[name = 'apartment']")
    LOCATOR_success_mesg = "Ваш архив с документами сформирован и доступен по этой ссылке";
    LOCATOR_success_mesg_css = "[class='sub-info']";
    LOCATOR_link_css = (By.CSS_SELECTOR, "[class='link tt_download_link']")
    LOCATOR_email = "xgr@mailinator.com";
    LOCATOR_input_email_xpath = (By.XPATH, "//*[@id='eid_meeting_creator_email']")
    LOCATOR_email_css = (By.CSS_SELECTOR, "[class='field4 filled ']")
    LOCATOR_address = "Moscow, Sculptora Muhinoi str."
    LOCATOR_input_address_xpath = (By.XPATH, "//*[@name='long_name']")
    LOCATOR_address_xpath = (By.XPATH, "(//*[@name='long_name'])[2]")
    LOCATOR_register_line_xpath = (By.XPATH, "//*[text()='Заказать реестр']")

class SearchHelper(BasePage):

    def enter_word(self, word):
        search_field = self.driver.find_element(*YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.driver.find_element(*YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_BUTTON).click()

    def check_navigation_bar(self):
        all_list = self.driver.find_elements(*YandexSeacrhLocators.LOCATOR_YANDEX_NAVIGATION_BAR)
        nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_menu

    def go_to_create_meeting_page(self):
        search_field = self.driver.find_element(*MainPageLocators.LOCATOR_CREATE_MEETING_XPATH).click()
        return search_field

    def go_to_constructor_meeting_page(self):
        self.driver.find_element(*CreateMeetingPageLocators.LOCATOR_CHOOSE_TEMPLATE_CSS).click()
        self.driver.find_element(*CreateMeetingPageLocators.LOCATOR_CHOOSE_TEMPLATE_CSS).click()

    def input_text(self, locator, input):
        self.driver.find_element(*locator).send_key(input)

    def check_name_and_number_apartment(self):
        self.driver.find_element(*ConstructorMeetingPageLocators.LOCATOR_button_form_archive_css).click()

    def check_download_form_archive(self):
        self.input_text(*ConstructorMeetingPageLocators.LOCATOR_input_name_css, *ConstructorMeetingPageLocators.LOCATOR_input_name)
        self.input_text(*ConstructorMeetingPageLocators.LOCATOR_input_number_apartment_css, *ConstructorMeetingPageLocators.LOCATOR_input_number_apartment)
        self.driver.find_element(*ConstructorMeetingPageLocators.LOCATOR_button_form_archive_css).click()
        BasePage.wait_element(*ConstructorMeetingPageLocators.LOCATOR_link_css)

    def check_address_and_email(self):
        self.input_text(*ConstructorMeetingPageLocators.LOCATOR_input_address_xpath, *ConstructorMeetingPageLocators.LOCATOR_address)
        self.input_text(*ConstructorMeetingPageLocators.LOCATOR_input_email_xpath, *ConstructorMeetingPageLocators.LOCATOR_email)
        self.driver.find_element(*ConstructorMeetingPageLocators.LOCATOR_register_line_xpath).click()


