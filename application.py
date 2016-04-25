from selenium.webdriver.firefox.webdriver import WebDriver

from fixture.registration import RegistrationHepler
from fixture.calculator import CalculatorHelper
from fixture.authorisation import AuthorisationHelper
from fixture.add_event_admin import AddEventHelper
from fixture.add_featureditem import FeatureditemHelper
from fixture.add_event_of_theday import AddEventOfTheDayHelper

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(5)
        self.registration = RegistrationHepler(self)
        self.calculator = CalculatorHelper(self)
        self.authorisation = AuthorisationHelper(self)
        self.add_event_admin = AddEventHelper(self)
        self.add_featureditem = FeatureditemHelper(self)
        self.add_event_of_theday = AddEventOfTheDayHelper(self)


    def destroy(self):
        self.wd.quit()
