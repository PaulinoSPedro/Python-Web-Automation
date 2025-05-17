class LoginLocators:

    # Login
    username_input_name = "username"
    password_input_name = "password"
    login_button_xpath = "//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']"

class HomeLocators:
    # Home
    profile_ul_classname = "oxd-userdropdown"
    logout_li_xpath = "//ul[@class='oxd-dropdown-menu']/li[4]"
    homepage_url_path = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

    admin_li_xpath = '//li[@class="oxd-main-menu-item-wrapper"][1]'
    pim_li_xpath = '//li[@class="oxd-main-menu-item-wrapper"][2]'
    leave_li_xpath = '//li[@class="oxd-main-menu-item-wrapper"][3]'
    time_li_xpath = '//li[@class="oxd-main-menu-item-wrapper"][4]'
    #TODO - Implement all li xpath
