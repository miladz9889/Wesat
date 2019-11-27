
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\\Users\Milad Zolfaghari\PycharmProjects\SeleniumProject\driver\chromedriver.exe")


driver.set_page_load_timeout(20)
driver.get("https://www.wesat.co/")

#Go to get pro
GetPro = driver.find_element_by_link_text('Get Pro')
GetPro.click()

print("worked")

#Go back to homepage
driver.get("https://www.wesat.co/")

print("worked")

#search for mountains
SearchBar = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[1]/div/div[3]/form/input')
SearchBar.send_keys("Mountains")
SearchBar.send_keys(Keys.ENTER)

#Join Wesat (create a user)
Join = driver.find_element_by_link_text('Join')
Join.click()
driver.find_element_by_name("firstName").send_keys("AutoTestFirstName")
driver.find_element_by_name("lastName").send_keys("AutoTestLastName")
driver.find_element_by_name("email").send_keys("milad.zolfaghari98@gmail.com")
driver.find_element_by_name("username").send_keys("autotest123")
driver.find_element_by_name("password").send_keys("Test123!")

print("worked")











time.sleep(4)
driver.quit()
