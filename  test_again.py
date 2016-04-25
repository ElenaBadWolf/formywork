# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest


def test(self):
    wd = self.wd
    main = self.wd.current_window_handle
    all = set(wd.window_handles)
    all.remove(main)








def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class  test_again(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_test_again(self):
        success = True
        wd = self.wd
        wd.get("http://test.kudago.com/manage/login/?next=/manage/")
        wd.find_element_by_id("id_password").click()
        wd.find_element_by_id("id_password").send_keys("\\undefined")
        wd.find_element_by_id("id_username").click()
        wd.find_element_by_id("id_username").clear()
        wd.find_element_by_id("id_username").send_keys("plastmassovaya@gmail.com")
        wd.find_element_by_id("grp-content").click()
        wd.find_element_by_id("id_password").click()
        wd.find_element_by_id("id_password").click()
        wd.find_element_by_id("id_password").clear()
        wd.find_element_by_id("id_password").send_keys("ьфпфшщдшмушкф")
        wd.find_element_by_css_selector("input.grp-button.grp-default").click()
        if not wd.find_element_by_xpath("//form[@id='language-chooser']/select//option[1]").is_selected():
            wd.find_element_by_xpath("//form[@id='language-chooser']/select//option[1]").click()
        wd.find_element_by_link_text("События дня").click()
        wd.find_element_by_link_text("Добавить событие дня").click()
        wd.find_element_by_xpath("//div[1]/article/div/form/div/fieldset/div[3]/div/div[2]/div/a[1]").click()
        main = self.wd.current_window_handle
        all = set(wd.window_handles)
        driver.switch_to_window(all.pop())
        time.sleep(5)










if __name__ == '__main__':
    unittest.main()
