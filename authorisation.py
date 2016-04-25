import time
class AuthorisationHelper:


    def __init__(self,app):
        self.app = app




    def authorisation_use_OK(self):
        wd = self.app.wd
        wd.get("http://test:test@test.kudago.com")
        wd.find_element_by_link_text("Да").click()
        wd.find_element_by_css_selector("h1.page-title.city-page-title").click()
        wd.find_element_by_class_name("icon-login").click()
        wd.find_element_by_css_selector("i.icon-odnoklassniki-oauth2").click()
        wd.find_element_by_id("field_email").click()
        wd.find_element_by_id("field_email").clear()
        wd.find_element_by_id("field_email").send_keys("nervios@mail.ru")
        wd.find_element_by_id("field_password").click()
        wd.find_element_by_id("field_password").clear()
        wd.find_element_by_id("field_password").send_keys("magaioliveira19")
        wd.find_element_by_css_selector("input.button-pro").click()


    def authorisation_use_twitter(self):
        wd = self.app.wd
        wd.get("http://test:test@test.kudago.com")
        wd.find_element_by_link_text("Да").click()
        wd.find_element_by_css_selector("h1.page-title.city-page-title").click()
        wd.find_element_by_class_name("icon-login").click()
        wd.find_element_by_css_selector("i.icon-twitter").click()
        wd.find_element_by_css_selector("label").click()
        wd.find_element_by_id("username_or_email").click()
        wd.find_element_by_id("username_or_email").clear()
        wd.find_element_by_id("username_or_email").send_keys("plastmassovaya")
        wd.find_element_by_xpath("//body").click()
        wd.find_element_by_xpath("//label[@for='password']").click()
        wd.find_element_by_id("password").click()
        wd.find_element_by_id("password").clear()
        wd.find_element_by_id("password").send_keys("magaioliveira19")
        wd.find_element_by_id("allow").click()
        time.sleep(10)



    def authorisation_use_VK(self):
        wd = self.app.wd
        wd.get("http://test:test@test.kudago.com")
        wd.find_element_by_link_text("Да").click()
        wd.find_element_by_css_selector("h1.page-title.city-page-title").click()
        wd.find_element_by_class_name("icon-login").click()
        wd.find_element_by_css_selector("i.icon-vk-oauth2").click()
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("plastmassovaya@gmail.com")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("dostoevskyfm19")
        wd.find_element_by_id("install_allow").click()
        wd.find_element_by_id("install_allow").click()
        time.sleep(10)



    def authorisation_use_FB(self):
        wd = self.app.wd
        wd.get("http://test:test@test.kudago.com")
        wd.find_element_by_link_text("Да").click()
        wd.find_element_by_css_selector("h1.page-title.city-page-title").click()
        wd.find_element_by_class_name("icon-login").click()
        wd.find_element_by_xpath("//nav[@id='login']/a[4]/i").click()
        wd.find_element_by_id("email").click()
        wd.find_element_by_id("email").clear()
        wd.find_element_by_id("email").send_keys("nervios_heart@mail.ru")
        wd.find_element_by_id("pass").click()
        wd.find_element_by_id("pass").clear()
        wd.find_element_by_id("pass").send_keys("magaioliveira19")
        wd.find_element_by_id("loginbutton").click()
        time.sleep(10)


    def authorisation_use_google(self):
        wd = self.app.wd
        wd.get("http://test:test@test.kudago.com")
        wd.find_element_by_link_text("Да").click()
        wd.find_element_by_css_selector("h1.page-title.city-page-title").click()
        wd.find_element_by_class_name("icon-login").click()
        wd.find_element_by_css_selector("i.icon-google-oauth2").click()
        wd.find_element_by_id("Email").click()
        wd.find_element_by_id("Email").clear()
        wd.find_element_by_id("Email").send_keys("plastmassovaya@gmail.com")
        wd.find_element_by_id("next").click()
        wd.find_element_by_id("Passwd").click()
        wd.find_element_by_id("Passwd").clear()
        wd.find_element_by_id("Passwd").send_keys("magaioliveira19")
        wd.find_element_by_id("signIn").click()
        time.sleep(10)


    def authorisation_use_email(self):
        wd = self.app.wd
        wd.get("http://test:test@test.kudago.com")
        wd.find_element_by_link_text("Да").click()
        wd.find_element_by_css_selector("h1.page-title.city-page-title").click()
        wd.find_element_by_class_name("icon-login").click()
        wd.find_element_by_id("manual-signin").click()
        wd.find_element_by_id("id_username").click()
        wd.find_element_by_id("id_username").send_keys ("plastmassovaya@gmail.com")
        wd.find_element_by_id("id_password").click()
        wd.find_element_by_id("id_password").clear()
        wd.find_element_by_id("id_password").send_keys("ьфпфшщдшмушкф")
        wd.find_element_by_xpath("//div[@class='content']/form/footer/input").click()
