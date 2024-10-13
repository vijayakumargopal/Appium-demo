from pages.basic_actions import *


class NetworkAndInternetPage(BasicActions):

    network_and_internet_title = (AppiumBy.ACCESSIBILITY_ID, "Network & internet")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def title_should_presents(self):
        return self.element_should_presents(NetworkAndInternetLocators.network_and_internet_title, 10)
