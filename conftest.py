import pytest
from selenium import webdriver
from pages import *

@pytest.fixture(scope = "session")
def browser():
    driver = webdriver.Chrome(executable_path="./chromedriver")
    driver.implicitly_wait(15)  # seconds
    driver.maximize_window()
    mainpage = BasePage(driver).go_to_site()
    createmeetingpage = mainpage.go_to_create_meeting_page()
    constructormeetingpage = createmeetingpage.go_to_constructor_meeting_page()
    print('print',constructormeetingpage)
    yield constructormeetingpage