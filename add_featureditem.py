import time
class FeatureditemHelper:


    def __init__(self,app):
        self.app = app



    def add_featureditem_place(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Особенные посты").click()
        wd.find_element_by_link_text("Добавить особенный пост").click()
        if not wd.find_element_by_xpath("//select[@id='id_content_type']//option[2]").is_selected():
            wd.find_element_by_xpath("//select[@id='id_content_type']//option[2]").click()
        wd.find_element_by_id("id_object_id-autocomplete").click()
        wd.find_element_by_id("id_object_id-autocomplete").clear()
        wd.find_element_by_id("id_object_id-autocomplete").send_keys("тест")
        time.sleep(5)
        wd.find_element_by_link_text("тест места 02 12 2015 (Санкт-Петербург)").click()
        if not wd.find_element_by_id("id_type_1").is_selected():
            wd.find_element_by_id("id_type_1").click()
        if not wd.find_element_by_xpath("//div[@class='featured-path-widget']/select//option[2]").is_selected():
            wd.find_element_by_xpath("//div[@class='featured-path-widget']/select//option[2]").click()
        if not wd.find_element_by_xpath("//div[@class='featured-path-widget']/select[2]//option[10]").is_selected():
            wd.find_element_by_xpath("//div[@class='featured-path-widget']/select[2]//option[10]").click()
        if not wd.find_element_by_xpath("//select[@id='id_position']//option[1]").is_selected():
            wd.find_element_by_xpath("//select[@id='id_position']//option[1]").click()
        wd.find_element_by_id("id_start_date_0").click()
        wd.find_element_by_css_selector("button.ui-datepicker-trigger").click()
        time.sleep(5)
        wd.find_element_by_link_text("1").click()
        wd.find_element_by_xpath("//form[@id='featureditem_form']/div/fieldset[3]/div[2]/div/div[2]/p[1]/button[1]").click()
        time.sleep(5)
        wd.find_element_by_link_text("25").click()
        wd.find_element_by_css_selector("button.ui-timepicker-trigger").click()
        wd.find_element_by_css_selector("li.ui-state-default.row").click()
        time.sleep(5)
        wd.find_element_by_xpath("//div[1]/article/div/form/div/fieldset[3]/div[2]/div/div[2]/p[1]/button[2]").click()
        time.sleep(5)
        wd.find_element_by_xpath("//div[3]/ul/li[25]").click()
        wd.find_element_by_name("_continue").click()
        time.sleep(5)



    def add_featureditem_event(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Особенные посты").click()
        wd.find_element_by_link_text("Добавить особенный пост").click()
        if not wd.find_element_by_xpath("//select[@id='id_content_type']//option[3]").is_selected():
            wd.find_element_by_xpath("//select[@id='id_content_type']//option[3]").click()
        wd.find_element_by_id("id_object_id-autocomplete").click()
        wd.find_element_by_id("id_object_id-autocomplete").clear()
        wd.find_element_by_id("id_object_id-autocomplete").send_keys("тест события")
        time.sleep(5)
        wd.find_element_by_link_text("тест события 13042016 (Санкт-Петербург, 13–30 апреля, 0:00, 0:00)").click()
        if not wd.find_element_by_id("id_type_1").is_selected():
            wd.find_element_by_id("id_type_1").click()
        if not wd.find_element_by_xpath("//div[@class='featured-path-widget']/select//option[2]").is_selected():
            wd.find_element_by_xpath("//div[@class='featured-path-widget']/select//option[2]").click()
        if not wd.find_element_by_xpath("//div[@class='featured-path-widget']/select[2]//option[10]").is_selected():
            wd.find_element_by_xpath("//div[@class='featured-path-widget']/select[2]//option[10]").click()
        if not wd.find_element_by_xpath("//select[@id='id_position']//option[2]").is_selected():
            wd.find_element_by_xpath("//select[@id='id_position']//option[2]").click()
        wd.find_element_by_id("id_start_date_0").click()
        wd.find_element_by_css_selector("button.ui-datepicker-trigger").click()
        time.sleep(5)
        wd.find_element_by_link_text("1").click()
        wd.find_element_by_xpath("//form[@id='featureditem_form']/div/fieldset[3]/div[2]/div/div[2]/p[1]/button[1]").click()
        time.sleep(5)
        wd.find_element_by_link_text("25").click()
        wd.find_element_by_css_selector("button.ui-timepicker-trigger").click()
        wd.find_element_by_css_selector("li.ui-state-default.row").click()
        time.sleep(5)
        wd.find_element_by_xpath("//div[1]/article/div/form/div/fieldset[3]/div[2]/div/div[2]/p[1]/button[2]").click()
        time.sleep(5)
        wd.find_element_by_xpath("//div[3]/ul/li[25]").click()
        wd.find_element_by_name("_continue").click()
        time.sleep(5)


    def add_featureditem_news(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Особенные посты").click()
        wd.find_element_by_link_text("Добавить особенный пост").click()
        if not wd.find_element_by_xpath("//select[@id='id_content_type']//option[4]").is_selected():
            wd.find_element_by_xpath("//select[@id='id_content_type']//option[4]").click()
        wd.find_element_by_id("id_object_id-autocomplete").click()
        wd.find_element_by_id("id_object_id-autocomplete").clear()
        wd.find_element_by_id("id_object_id-autocomplete").send_keys("тест")
        time.sleep(5)
        wd.find_element_by_link_text("тест новости 2004216").click()
        if not wd.find_element_by_id("id_type_1").is_selected():
            wd.find_element_by_id("id_type_1").click()
        if not wd.find_element_by_xpath("//div[@class='featured-path-widget']/select//option[2]").is_selected():
            wd.find_element_by_xpath("//div[@class='featured-path-widget']/select//option[2]").click()
        if not wd.find_element_by_xpath("//div[@class='featured-path-widget']/select[2]//option[10]").is_selected():
            wd.find_element_by_xpath("//div[@class='featured-path-widget']/select[2]//option[10]").click()
        if not wd.find_element_by_xpath("//select[@id='id_position']//option[3]").is_selected():
            wd.find_element_by_xpath("//select[@id='id_position']//option[3]").click()
        wd.find_element_by_id("id_start_date_0").click()
        wd.find_element_by_css_selector("button.ui-datepicker-trigger").click()
        time.sleep(5)
        wd.find_element_by_link_text("1").click()
        wd.find_element_by_xpath("//form[@id='featureditem_form']/div/fieldset[3]/div[2]/div/div[2]/p[1]/button[1]").click()
        time.sleep(5)
        wd.find_element_by_link_text("25").click()
        wd.find_element_by_css_selector("button.ui-timepicker-trigger").click()
        wd.find_element_by_css_selector("li.ui-state-default.row").click()
        time.sleep(5)
        wd.find_element_by_xpath("//div[1]/article/div/form/div/fieldset[3]/div[2]/div/div[2]/p[1]/button[2]").click()
        time.sleep(5)
        wd.find_element_by_xpath("//div[3]/ul/li[25]").click()
        wd.find_element_by_name("_continue").click()
        time.sleep(5)



    def add_featureditem_list(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Особенные посты").click()
        wd.find_element_by_link_text("Добавить особенный пост").click()
        if not wd.find_element_by_xpath("//select[@id='id_content_type']//option[5]").is_selected():
            wd.find_element_by_xpath("//select[@id='id_content_type']//option[5]").click()
        wd.find_element_by_id("id_object_id-autocomplete").click()
        wd.find_element_by_id("id_object_id-autocomplete").clear()
        wd.find_element_by_id("id_object_id-autocomplete").send_keys("тест")
        time.sleep(5)
        wd.find_element_by_link_text("тест списка 20042016 (истекает 30 апреля 2016, 20:00)").click()
        if not wd.find_element_by_id("id_type_1").is_selected():
            wd.find_element_by_id("id_type_1").click()
        if not wd.find_element_by_xpath("//div[@class='featured-path-widget']/select//option[2]").is_selected():
            wd.find_element_by_xpath("//div[@class='featured-path-widget']/select//option[2]").click()
        if not wd.find_element_by_xpath("//div[@class='featured-path-widget']/select[2]//option[10]").is_selected():
            wd.find_element_by_xpath("//div[@class='featured-path-widget']/select[2]//option[10]").click()
        if not wd.find_element_by_xpath("//select[@id='id_position']//option[4]").is_selected():
            wd.find_element_by_xpath("//select[@id='id_position']//option[4]").click()
        wd.find_element_by_id("id_start_date_0").click()
        wd.find_element_by_css_selector("button.ui-datepicker-trigger").click()
        time.sleep(5)
        wd.find_element_by_link_text("1").click()
        wd.find_element_by_xpath("//form[@id='featureditem_form']/div/fieldset[3]/div[2]/div/div[2]/p[1]/button[1]").click()
        time.sleep(5)
        wd.find_element_by_link_text("25").click()
        wd.find_element_by_css_selector("button.ui-timepicker-trigger").click()
        wd.find_element_by_css_selector("li.ui-state-default.row").click()
        time.sleep(5)
        wd.find_element_by_xpath("//div[1]/article/div/form/div/fieldset[3]/div[2]/div/div[2]/p[1]/button[2]").click()
        time.sleep(5)
        wd.find_element_by_xpath("//div[3]/ul/li[25]").click()
        wd.find_element_by_name("_continue").click()
        time.sleep(5)


    def add_featureditem_movie(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Особенные посты").click()
        wd.find_element_by_link_text("Добавить особенный пост").click()
        if not wd.find_element_by_xpath("//select[@id='id_content_type']//option[6]").is_selected():
            wd.find_element_by_xpath("//select[@id='id_content_type']//option[6]").click()
        wd.find_element_by_id("id_object_id-autocomplete").click()
        wd.find_element_by_id("id_object_id-autocomplete").clear()
        wd.find_element_by_id("id_object_id-autocomplete").send_keys("тест")
        time.sleep(5)
        wd.find_element_by_link_text("тест фильма 20 01 2016").click()
        if not wd.find_element_by_id("id_type_1").is_selected():
            wd.find_element_by_id("id_type_1").click()
        if not wd.find_element_by_xpath("//div[@class='featured-path-widget']/select//option[2]").is_selected():
            wd.find_element_by_xpath("//div[@class='featured-path-widget']/select//option[2]").click()
        if not wd.find_element_by_xpath("//div[@class='featured-path-widget']/select[2]//option[10]").is_selected():
            wd.find_element_by_xpath("//div[@class='featured-path-widget']/select[2]//option[10]").click()
        if not wd.find_element_by_xpath("//select[@id='id_position']//option[5]").is_selected():
            wd.find_element_by_xpath("//select[@id='id_position']//option[5]").click()
        wd.find_element_by_id("id_start_date_0").click()
        wd.find_element_by_css_selector("button.ui-datepicker-trigger").click()
        time.sleep(5)
        wd.find_element_by_link_text("1").click()
        wd.find_element_by_xpath("//form[@id='featureditem_form']/div/fieldset[3]/div[2]/div/div[2]/p[1]/button[1]").click()
        time.sleep(5)
        wd.find_element_by_link_text("25").click()
        wd.find_element_by_css_selector("button.ui-timepicker-trigger").click()
        wd.find_element_by_css_selector("li.ui-state-default.row").click()
        time.sleep(5)
        wd.find_element_by_xpath("//div[1]/article/div/form/div/fieldset[3]/div[2]/div/div[2]/p[1]/button[2]").click()
        time.sleep(5)
        wd.find_element_by_xpath("//div[3]/ul/li[25]").click()
        wd.find_element_by_name("_continue").click()
        time.sleep(5)




    def add_featureditem_incontent(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Особенные посты").click()
        wd.find_element_by_link_text("Добавить особенный пост").click()
        if not wd.find_element_by_xpath("//select[@id='id_content_type']//option[2]").is_selected():
            wd.find_element_by_xpath("//select[@id='id_content_type']//option[2]").click()
        wd.find_element_by_id("id_object_id-autocomplete").click()
        wd.find_element_by_id("id_object_id-autocomplete").clear()
        wd.find_element_by_id("id_object_id-autocomplete").send_keys("тест")
        time.sleep(5)
        wd.find_element_by_link_text("тест места 02 12 2015 (Санкт-Петербург)").click()
        time.sleep(5)
        wd.find_element_by_xpath("//label[@for='id_type_1']").click()
        if not wd.find_element_by_id("id_type_1").is_selected():
            wd.find_element_by_id("id_type_1").click()
        if not wd.find_element_by_xpath("//div[@class='featured-path-widget']/select//option[2]").is_selected():
            wd.find_element_by_xpath("//div[@class='featured-path-widget']/select//option[2]").click()
        wd.find_element_by_name("path").click()
        if not wd.find_element_by_xpath("//div[@class='featured-path-widget']/select[2]//option[5]").is_selected():
            wd.find_element_by_xpath("//div[@class='featured-path-widget']/select[2]//option[5]").click()
        if not wd.find_element_by_xpath("//select[@id='id_position']//option[4]").is_selected():
            wd.find_element_by_xpath("//select[@id='id_position']//option[4]").click()
        wd.find_element_by_id("id_start_date_0").click()
        wd.find_element_by_css_selector("button.ui-datepicker-trigger").click()
        time.sleep(5)
        wd.find_element_by_link_text("1").click()
        wd.find_element_by_xpath("//form[@id='featureditem_form']/div/fieldset[3]/div[2]/div/div[2]/p[1]/button[1]").click()
        time.sleep(5)
        wd.find_element_by_link_text("25").click()
        wd.find_element_by_css_selector("button.ui-timepicker-trigger").click()
        wd.find_element_by_css_selector("li.ui-state-default.row").click()
        time.sleep(5)
        wd.find_element_by_xpath("//div[1]/article/div/form/div/fieldset[3]/div[2]/div/div[2]/p[1]/button[2]").click()
        time.sleep(5)
        wd.find_element_by_xpath("//div[3]/ul/li[25]").click()
        wd.find_element_by_name("_continue").click()
        time.sleep(5)