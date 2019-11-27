from POMProject.Locators.locators import Locators


class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.avatar_xpath = Locators.avatar_xpath
        self.logout_link_text = Locators.logout_link_text
        self.search_bar_xpath = Locators.search_bar_xpath
        self.get_pro_xpath = Locators.get_pro_xpath
        self.get_to_home_page_xpath = Locators.go_to_home_page_xpath

    def click_avatar(self):
        self.driver.find_element_by_xpath(self.avatar_xpath).click()

    def click_logout(self):
        self.driver.find_element_by_link_text(self.logout_link_text).click()

    def enter_subject_search_bar(self, subject):
        self.driver.find_element_by_xpath(self.search_bar_xpath).clear()
        self.driver.find_element_by_xpath(self.search_bar_xpath).send_keys(subject)

    def click_get_pro(self):
        self.driver.find_element_by_xpath(self.get_pro_xpath).click()

    def click_go_home_page(self):
        self.driver.find_element_by_xpath(self.get_to_home_page_xpath).click()



