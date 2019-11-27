from POMProject.Locators.locators import Locators


class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.login_link_text = Locators.login_link_text
        self.username_textbox_id = Locators.username_textbox_id
        self.password_textbox_id = Locators.password_textbox_id
        self.login_button_xpath = Locators.login_button_xpath
        self.invalidUsername = Locators.check_invalid_login

    def click_home_login(self):
        self.driver.find_element_by_link_text(self.login_link_text).click()

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()

    def check_invalid_username_message(self):
        msg = self.driver.find_elements_by_class_name(self.invalidUsername).text
        return msg

