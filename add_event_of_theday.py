import time

class AddEventOfTheDayHelper:


    def __init__(self,app):
        self.app = app



    def add_event_of_theday(self):
        wd = self.app.wd
        wd.find_element_by_link_text("События дня").click()
        wd.find_element_by_link_text("Добавить событие дня").click()
        wd.find_element_by_css_selector("input[type='radio'][value='spb']").click()
        time.sleep(5)
        wd.find_element_by_xpath("//div[1]/article/div/form/div/fieldset/div[2]/div/div[2]/button").click()
        time.sleep(5)
        wd.find_element_by_xpath("//div[2]/div[2]/button[1]").click()
        time.sleep(5)
        wd.find_element_by_id("id_event-autocomplete").click()
        wd.find_element_by_id("id_event-autocomplete").clear()
        wd.find_element_by_id("id_event-autocomplete").send_keys("тест события")
        wd.find_element_by_link_text("тест события 13042016 (Санкт-Петербург, 13–30 апреля, 0:00, 0:00)").click()
        time.sleep(15)
        wd.find_element_by_name("_continue").click()