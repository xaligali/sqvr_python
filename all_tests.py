from pages import *

def test_check_form_archive_negative(browser, setup):
    #page = Helper(browser)
    assert "Фамилия и имя являются обязательными" == setup.createmeetingpage.check_name_and_number_apartment()[0]
    assert "Поле является обязательным" == setup.createmeetingpage.check_name_and_number_apartment()[1]

def test_check_form_archive_positive(browser,setup):
    #page = Helper(browser,setup)
    assert "Ваш архив с документами сформирован и доступен по этой ссылке" == setup.createmeetingpage.check_download_form_archive()

def test_check_address_and_email_positive(browsers,setup):
    #page = Helper(browser)
    result = setup.createmeetingpage.check_address_and_email()
    assert "Москва, улица Скульптора Мухиной" == result[0]
    assert "xgr@mailinator.com" ==  result[1]