import time


class CalculatorHelper:

    def __init__(self,app):
        self.app = app


    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://test:test@test.kudago.com")
        wd.find_element_by_link_text("Да").click()



    def authorisation(self):
       wd = self.app.wd
       wd.find_element_by_class_name("icon-login").click()
       wd.find_element_by_link_text("Войти с помощью email").click()
       wd.find_element_by_id("id_password").click()
       wd.find_element_by_id("id_password").send_keys("\\undefined")
       wd.find_element_by_id("id_username").click()
       wd.find_element_by_id("id_username").clear()
       wd.find_element_by_id("id_username").send_keys("plastmassovaya@gmail.com")
       wd.find_element_by_id("id_password").click()
       wd.find_element_by_id("id_password").clear()
       wd.find_element_by_id("id_password").send_keys("ьфпфшщдшмушкф")


    def chose_calculator(self):
       wd = self.app.wd
       wd.find_element_by_xpath("//div[@class='content']/form/footer/input").click()
       wd.find_element_by_link_text("мои заведения").click()
       wd.find_element_by_link_text("Калькулятор услуг").click()


    def add_places(self):
       wd = self.app.wd
       wd.find_element_by_link_text("Заведения").click()
       wd.find_element_by_xpath("//section[@class='page-container']/div/table[1]/tbody/tr[30]/td[5]/span").click()
       wd.find_element_by_css_selector("input.icecream-amount-popover-ok").click()
       wd.find_element_by_css_selector("input.icecream-amount-popover-cancel").click()
       wd.find_element_by_xpath("//section[@class='page-container']/div/table[2]/tbody/tr[199]/td[5]/span").click()
       wd.find_element_by_css_selector("input.icecream-amount-popover-ok").click()
       wd.find_element_by_css_selector("input.icecream-amount-popover-cancel").click()
       wd.find_element_by_xpath("//section[@class='page-container']/div/table[3]/tbody/tr[199]/td[5]/span").click()
       wd.find_element_by_css_selector("input.icecream-amount-popover-ok").click()
       wd.find_element_by_css_selector("input.icecream-amount-popover-cancel").click()
       wd.find_element_by_xpath("//aside[@class='aside-col']/div[2]/div/div[3]/a").click()


    def send_form(self):
       wd = self.app.wd
       wd.find_element_by_xpath("//div[@class='summary-full']//p[normalize-space(.)='Ваше имя *']").click()
       wd.find_element_by_id("name").click()
       wd.find_element_by_id("name").clear()
       wd.find_element_by_id("name").send_keys("grrrrrrrrrrrrrrr")
       wd.find_element_by_id("phone").click()
       wd.find_element_by_id("phone").clear()
       wd.find_element_by_id("phone").send_keys("ertertre")
       wd.find_element_by_id("email").click()
       wd.find_element_by_id("email").clear()
       wd.find_element_by_id("email").send_keys("treterte@gjfhd.gfd")
       time.sleep(15)
       wd.find_element_by_id("submit-button").click()
       time.sleep(15)


    def add_events(self):
        wd = self.app.wd
        wd.find_element_by_link_text("События").click()
        wd.find_element_by_xpath("//section[@class='page-container']/div/table[1]/tbody/tr[74]/td[4]/span").click()
        wd.find_element_by_xpath("//section[@class='page-container']/div/table[2]/tbody/tr[73]/td[4]/span").click()
        wd.find_element_by_xpath("//section[@class='page-container']/div/table[3]/tbody/tr[199]/td[5]/span").click()
        wd.find_element_by_xpath("//section[@class='page-container']/div/table[3]/tbody/tr[201]/td[5]/span").click()
        wd.find_element_by_xpath("//section[@class='page-container']/div/table[4]/tbody/tr[200]/td[5]/span").click()
        wd.find_element_by_xpath("//section[@class='page-container']/div/table[5]/tbody/tr[11]/td[3]/span").click()
        wd.find_element_by_xpath("//section[@class='page-container']/div/table[6]/tbody/tr[7]/td[5]/span").click()
        wd.find_element_by_xpath("//aside[@class='aside-col']/div[2]/div/div[3]").click()
        wd.find_element_by_xpath("//aside[@class='aside-col']/div[2]/div/div[3]/a").click()
        wd.find_element_by_id("submit-button").click()


    def add_topovoe_tematichesky(self):
         wd = self.app.wd
         wd.find_element_by_link_text("Топовое размещение в тематическом разделе").click()
         wd.find_element_by_xpath("//table[@class='table-standalone']/tbody/tr[200]/td[3]/span").click()
         wd.find_element_by_css_selector("input.icecream-amount-popover-ok").click()
         wd.find_element_by_css_selector("input.icecream-amount-popover-cancel").click()
         wd.find_element_by_xpath("//aside[@class='aside-col']/div[2]/div/div[3]/a").click()
         wd.find_element_by_id("submit-button").click()


    def add_topovoe_glavnaya(self):
         wd = self.app.wd
         wd.find_element_by_link_text("Топовое размещение на главной странице").click()
         wd.find_element_by_xpath("//table[@class='icecream-featured-table']/tbody/tr[75]/td[3]/span").click()
         wd.find_element_by_css_selector("input.icecream-amount-popover-ok").click()
         wd.find_element_by_css_selector("input.icecream-amount-popover-cancel").click()
         wd.find_element_by_xpath("//table[@class='icecream-featured-table']/tbody/tr[78]/td[3]/span").click()
         wd.find_element_by_css_selector("input.icecream-amount-popover-ok").click()
         wd.find_element_by_css_selector("input.icecream-amount-popover-cancel").click()
         wd.find_element_by_xpath("//table[@class='icecream-featured-table']/tbody/tr[82]/td[3]/span").click()
         wd.find_element_by_css_selector("input.icecream-amount-popover-ok").click()
         wd.find_element_by_css_selector("input.icecream-amount-popover-cancel").click()
         wd.find_element_by_xpath("//aside[@class='aside-col']/div[2]/div/div[3]/a").click()


    def add_banners(self):
         wd = self.app.wd
         wd.find_element_by_link_text("Баннеры").click()
         wd.find_element_by_xpath("//section[@class='page-container']/div/table[1]/tbody/tr[37]/td[4]/span").click()
         wd.find_element_by_css_selector("input.icecream-amount-popover-ok").click()
         wd.find_element_by_css_selector("input.icecream-amount-popover-cancel").click()
         wd.find_element_by_xpath("//section[@class='page-container']/div/table[1]/tbody/tr[39]/td[4]/span").click()
         wd.find_element_by_id("amount-popover").click()
         wd.find_element_by_css_selector("input.icecream-amount-popover-ok").click()
         wd.find_element_by_css_selector("input.icecream-amount-popover-cancel").click()
         wd.find_element_by_xpath("//section[@class='page-container']/div/table[2]/tbody/tr[19]/td[4]/span").click()
         wd.find_element_by_css_selector("input.icecream-amount-popover-ok").click()
         wd.find_element_by_css_selector("input.icecream-amount-popover-cancel").click()
         wd.find_element_by_xpath("//section[@class='page-container']/div/table[2]/tbody/tr[20]/td[4]/span").click()
         wd.find_element_by_css_selector("input.icecream-amount-popover-ok").click()
         wd.find_element_by_css_selector("input.icecream-amount-popover-cancel").click()
         wd.find_element_by_xpath("//section[@class='page-container']/div/table[3]/tbody/tr[28]/td[5]/span").click()
         wd.find_element_by_css_selector("input.icecream-amount-popover-ok").click()
         wd.find_element_by_css_selector("input.icecream-amount-popover-cancel").click()
         wd.find_element_by_xpath("//section[@class='page-container']/div/table[3]/tbody/tr[31]/td[5]/span").click()
         wd.find_element_by_css_selector("input.icecream-amount-popover-ok").click()
         wd.find_element_by_css_selector("input.icecream-amount-popover-cancel").click()
         wd.find_element_by_xpath("//section[@class='page-container']/div/table[3]/tbody/tr[30]/td[5]/span").click()
         wd.find_element_by_css_selector("input.icecream-amount-popover-ok").click()
         wd.find_element_by_css_selector("input.icecream-amount-popover-cancel").click()
         wd.find_element_by_xpath("//aside[@class='aside-col']/div[2]/div/div[3]/a").click()


    def add_branding(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Брендирование").click()
        wd.find_element_by_xpath("//table[@class='table-standalone']/tbody/tr[27]/td[4]/span").click()
        wd.find_element_by_xpath("//table[@class='table-standalone']/tbody/tr[29]/td[4]/span").click()
        wd.find_element_by_xpath("//table[@class='table-standalone']/tbody/tr[31]/td[4]/span").click()
        wd.find_element_by_xpath("//table[@class='table-standalone']/tbody/tr[32]/td[4]/span").click()
        wd.find_element_by_xpath("//table[@class='table-standalone']/tbody/tr[33]/td[4]/span").click()
        wd.find_element_by_xpath("//table[@class='table-standalone']/tbody/tr[30]/td[4]/span").click()
        wd.find_element_by_xpath("//table[@class='table-standalone']/tbody/tr[28]/td[4]").click()
        wd.find_element_by_xpath("//table[@class='table-standalone']/tbody/tr[28]/td[4]/span").click()
        wd.find_element_by_xpath("//aside[@class='aside-col']/div[2]/div/div[3]/a").click()


    def add_spec_project(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Спецпроект").click()
        wd.find_element_by_xpath("//section[@class='page-container']/div/table[1]/tbody/tr[12]/td[4]/span").click()
        wd.find_element_by_xpath("//section[@class='page-container']/div/table[2]/tbody/tr[19]/td[4]").click()
        wd.find_element_by_xpath("//section[@class='page-container']/div/table[2]/tbody/tr[19]/td[4]/span").click()
        wd.find_element_by_xpath("//section[@class='page-container']/div/table[2]/tbody/tr[20]/td[4]").click()
        wd.find_element_by_xpath("//section[@class='page-container']/div/table[2]/tbody/tr[20]/td[4]/span").click()
        wd.find_element_by_xpath("//aside[@class='aside-col']/div[2]/div/div[3]/a").click()
