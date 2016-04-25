

class RegistrationHepler:

    def __init__(self,app):
        self.app = app


    def chose_emailreg(self):
        wd = self.app.wd
        wd.find_element_by_id("signup-title").click()
        wd.find_element_by_id("manual-signup").click()

    def fill_regform_email(self, displayname= "test", email= "test@testest.test", password = "fkmnfdbcnf", password2 = "fkmnfdbcnf"):
        wd = self.app.wd
        wd.find_element_by_id("id_display_name").click()
        wd.find_element_by_id("id_display_name").clear()
        wd.find_element_by_id("id_display_name").send_keys(displayname)
        wd.find_element_by_id("id_email").click()
        wd.find_element_by_id("id_email").clear()
        wd.find_element_by_id("id_email").send_keys(email)
        wd.find_element_by_id("id_password1").click()
        wd.find_element_by_id("id_password1").clear()
        wd.find_element_by_id("id_password1").send_keys(password)
        wd.find_element_by_id("id_password2").click()
        wd.find_element_by_id("id_password2").clear()
        wd.find_element_by_id("id_password2").send_keys(password2)
        if not wd.find_element_by_id("id_tos").is_selected():
            wd.find_element_by_id("id_tos").click()
        wd.find_element_by_xpath("//div[@class='content']/form/footer/input").click()

    def authorization_OK(self,email_ok, password_ok):
        # авторизация в ОК
        wd = self.app.wd
        wd.find_element_by_id("field_email").click()
        wd.find_element_by_id("field_email").clear()
        wd.find_element_by_id("field_email").send_keys(email_ok)
        wd.find_element_by_id("field_password").click()
        wd.find_element_by_id("field_password").clear()
        wd.find_element_by_id("field_password").send_keys(password_ok)
        wd.find_element_by_css_selector("input.button-pro").click()

    def authorization_twitter(self, username_twitter="plastmassovaya", password_twitter="magaioliveira19"):
        # авторизация в twitter
        wd = self.app.wd
        wd.find_element_by_css_selector("label").click()
        wd.find_element_by_id("username_or_email").click()
        wd.find_element_by_id("username_or_email").clear()
        wd.find_element_by_id("username_or_email").send_keys(username_twitter)
        wd.find_element_by_xpath("//body").click()
        wd.find_element_by_xpath("//label[@for='password']").click()
        wd.find_element_by_id("password").click()
        wd.find_element_by_id("password").clear()
        wd.find_element_by_id("password").send_keys(password_twitter)
        wd.find_element_by_id("allow").click()

    def authorization_vk(self, mailvk="plastmassovaya@gmail.com", passwordvk="dostoevskyfm19"):
        # авторизация в vk
        wd = self.app.wd
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(mailvk)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(passwordvk)
        wd.find_element_by_id("install_allow").click()
        wd.find_element_by_id("install_allow").click()

    def authorization_fb(self, mailfb="nervios_heart@mail.ru", password_fb="magaioliveira19"):
        # авторизация в fb
        wd = self.app.wd
        wd.find_element_by_id("email").click()
        wd.find_element_by_id("email").clear()
        wd.find_element_by_id("email").send_keys(mailfb)
        wd.find_element_by_id("pass").click()
        wd.find_element_by_id("pass").clear()
        wd.find_element_by_id("pass").send_keys(password_fb)
        wd.find_element_by_id("loginbutton").click()

    def authorization_google_plus(self, mailgoogle="plastmassovaya@gmail.com", passwordgoogle="magaioliveira19"):
        # авторизация в google
        wd = self.app.wd
        wd.find_element_by_id("Email").click()
        wd.find_element_by_id("Email").clear()
        wd.find_element_by_id("Email").send_keys(mailgoogle)
        wd.find_element_by_id("next").click()
        wd.find_element_by_id("Passwd").click()
        wd.find_element_by_id("Passwd").clear()
        wd.find_element_by_id("Passwd").send_keys(passwordgoogle)
        wd.find_element_by_id("signIn").click()

    def chose_socialbutton_OK(self):
        # выбор соцсети
        wd = self.app.wd
        wd.find_element_by_id("signup-title").click()
        wd.find_element_by_css_selector("i.icon-odnoklassniki-oauth2").click()

    def chose_socialbutton_vk(self):
        # выбор соцсети
        wd = self.app.wd
        wd.find_element_by_id("signup-title").click()
        wd.find_element_by_css_selector("i.icon-vk-oauth2").click()


    def chose_socialbutton_twitter(self):
        # выбор соцсети
        wd = self.app.wd
        wd.find_element_by_id("signup-title").click()
        wd.find_element_by_css_selector("i.icon-twitter").click()

    def chose_socialbutton_fb(self):
        # выбор соцсети
        wd = self.app.wd
        wd.find_element_by_xpath("//nav[@id='login']/a[4]/i").click()

    def chose_socialbutton_google_plus(self):
        # выбор соцсети
        wd = self.app.wd
        wd.find_element_by_id("signup-title").click()
        wd.find_element_by_css_selector("i.icon-google-oauth2").click()



    def fill_registration_form(self, email):
        wd = self.app.wd
        wd.find_element_by_id("id_email").click()
        wd.find_element_by_id("id_email").clear()
        wd.find_element_by_id("id_email").send_keys(email)
        if not wd.find_element_by_id("id_tos").is_selected():
            wd.find_element_by_id("id_tos").click()
        wd.find_element_by_xpath("//div[@class='content']/form/footer/input").click()

    def push_login_button(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("h1.page-title.city-page-title").click()
        wd.find_element_by_class_name("icon-login").click()

    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://test:test@test.kudago.com")