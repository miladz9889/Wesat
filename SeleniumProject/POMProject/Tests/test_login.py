import time
import unittest
from selenium import webdriver
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from POMProject.Pages.loginPage import LoginPage
from POMProject.Pages.homePage import HomePage
import HtmlTestRunner
from selenium.webdriver.common.keys import Keys


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path="C:/Users/Milad Zolfaghari/PycharmProjects/SeleniumProject/driver/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_login_valid(self):
        driver = self.driver

        driver.get("https://www.wesat.co/")

        login = LoginPage(driver)
        login.click_home_login()
        login.enter_username("milad@wesaturate.com")
        login.enter_password("Samar9889")
        login.click_login()

        time.sleep(2)

    def test_02_user_search(self):
        driver = self.driver

        login = LoginPage(driver)
        homepage = HomePage(driver)
        homepage.enter_subject_search_bar("Cars")
        homepage.enter_subject_search_bar(Keys.ENTER)
        homepage.click_go_home_page()

        time.sleep(2)

    #add purchase pro to below test
    def test_03_get_pro(self):
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_get_pro()

        time.sleep(2)

    def test_04_log_out(self):
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_avatar()
        homepage.click_logout()

        time.sleep(2)

    def test_05_nonuser_search(self):
        driver = self.driver

        homepage = HomePage(driver)
        homepage.enter_subject_search_bar("Mountains")
        homepage.enter_subject_search_bar(Keys.ENTER)

        time.sleep(2)

    #uploading photos
    #downloading photos
    #commenting
    #liking/hearting
    #visit profile


    # Join Wesat (create a user)
    # Join = driver.find_element_by_link_text('Join')
    # Join.click()
    # driver.find_element_by_name("firstName").send_keys("AutoTestFirstName")
    # driver.find_element_by_name("lastName").send_keys("AutoTestLastName")
    # driver.find_element_by_name("email").send_keys("milad.zolfaghari98@gmail.com")
    # driver.find_element_by_name("username").send_keys("autotest123")
    # driver.find_element_by_name("password").send_keys("Test123!")

    # Go to get pro
    # GetPro = driver.find_element_by_link_text('Get Pro')
    # GetPro.click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(report_title="Wesat Testing Results",
                                                           output='C:/Users/Milad Zolfaghari/PycharmProjects/SeleniumProject/reports'))

# to run from command line python -m POMProject.Tests.test_login
