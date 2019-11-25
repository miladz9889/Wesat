from POMProject.Locators.locators import Locators


class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.avatar_xpath = Locators.avatar_xpath
        self.logout_link_text = Locators.logout_link_text

    def click_avatar(self):
        self.driver.find_element_by_xpath(self.avatar_xpath).click()

    def click_logout(self):
        self.driver.find_element_by_link_text(self.logout_link_text).click()