class Locators():
    # login page objects
    login_link_text = "Login"
    username_textbox_id = "email / username-input"
    password_textbox_id = "password-input"
    login_button_xpath = '//*[@id="login-box"]/form/div[3]/div/button'
    check_invalid_login = "//span[@class='input__error']"


    # home page objects
    avatar_xpath = '//*[@id="app"]/div/div/nav/div/div[2]/ul/li[6]/a/div/div/div/div/img'
    logout_link_text = "Logout"
    search_bar_xpath = '//*[@id="app"]/div/div/div/div[1]/div/div[3]/form/input'
    get_pro_xpath = '/html[1]/body[1]/div[2]/div[1]/div[1]/nav[1]/div[1]/div[2]/ul[1]/li[4]/a[1]'
    go_to_home_page_xpath = '/html[1]/body[1]/div[2]/div[1]/div[1]/nav[1]/div[1]/div[1]/a[1]/*'