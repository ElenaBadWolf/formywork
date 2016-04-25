
import time

class AddEventHelper:


    def __init__(self,app):
        self.app = app



    def login_admin(self):
         wd = self.app.wd
         wd.get("http://test:test@test.kudago.com/manage/login/?next=/manage/")
         wd.find_element_by_id("id_password").click()
         wd.find_element_by_id("id_password").send_keys("\\undefined")
         wd.find_element_by_id("id_username").click()
         wd.find_element_by_id("id_username").clear()
         wd.find_element_by_id("id_username").send_keys("plastmassovaya@gmail.com")
         wd.find_element_by_id("id_password").click()
         wd.find_element_by_id("id_password").clear()
         wd.find_element_by_id("id_password").send_keys("ьфпфшщдшмушкф")
         wd.find_element_by_css_selector("input.grp-button.grp-default").click()
         if not wd.find_element_by_xpath("//form[@id='language-chooser']/select//option[1]").is_selected():
             wd.find_element_by_xpath("//form[@id='language-chooser']/select//option[1]").click()


    def chose_event(self):
         wd = self.app.wd
         wd.find_element_by_link_text("События").click()


    def click_add_event(self):
         wd = self.app.wd
         wd.find_element_by_link_text("Добавить событие").click()


    def fill_form_event(self):
         wd = self.app.wd
         if not wd.find_element_by_id("id_status_7").is_selected():
                wd.find_element_by_id("id_status_7").click()
                time.sleep(5)
         if not wd.find_element_by_id("id_location_0").is_selected():
                wd.find_element_by_id("id_location_0").click()
                time.sleep(5)
         wd.find_element_by_name("title").click()
         wd.find_element_by_name("title").clear()
         wd.find_element_by_name("title").send_keys("автотест события2")
         time.sleep(5)
         wd.find_element_by_id("id_short_title").click()
         wd.find_element_by_id("id_short_title").clear()
         wd.find_element_by_id("id_short_title").send_keys("тест")
         wd.find_element_by_id("id_tagline").click()
         wd.find_element_by_id("id_tagline").clear()
         wd.find_element_by_id("id_tagline").send_keys("тест")
         wd.find_element_by_id("id_description").click()
         wd.find_element_by_id("id_description").clear()
         wd.find_element_by_id("id_description").send_keys("аннотация события ")
         wd.find_element_by_id("id_body_text").click()
         wd.find_element_by_id("id_body_text").clear()
         wd.find_element_by_id("id_body_text").send_keys("основное описание события")
         wd.find_element_by_id("id_price").click()
         wd.find_element_by_id("id_price").clear()
         wd.find_element_by_id("id_price").send_keys("999")
         wd.find_element_by_xpath("//select[@id='id_category_from']//option[.='Балы (Развлечения)']").click()
         time.sleep(5)
         wd.find_element_by_link_text("Выбрать").click()
         time.sleep(5)
         wd.find_element_by_link_text("Добавить еще дата").click()
         wd.find_element_by_css_selector("button.ui-datepicker-trigger").click()
         wd.find_element_by_link_text("22").click()
         wd.find_element_by_xpath("//tbody[@id='dates-0']/tr[3]/td[1]/div[3]/div[1]/span/button").click()
         wd.find_element_by_link_text("30").click()
         time.sleep(10)
         wd.find_element_by_css_selector("small").click()
         #add the image
         file_input = wd.find_element_by_css_selector("input.image-dropbox-input")
         wd.execute_script("document.querySelector('.image-dropbox-input').removeAttribute('class')")
         file_input.send_keys('/home/localuser/Рабочий стол/Spyaschiy.png' )
         time.sleep(5)
         wd.find_element_by_name("_continue").click()



    def have_alook_onsite(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Посмотреть на сайте").click()
        time.sleep(10)