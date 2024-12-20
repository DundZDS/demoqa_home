from pages.swag_labs import SwagLabs

def test_check_swag(browser):
    swag_page = SwagLabs(browser)
    swag_page.visit()
    assert swag_page.exist_icon()

def test_check_username(browser):
    swag_username = SwagLabs(browser)
    swag_username.exist_field('#user-name.form_group')

def test_check_password(browser):
        swag_password = SwagLabs(browser)
        swag_password.exist_field('#password.form_group ')

