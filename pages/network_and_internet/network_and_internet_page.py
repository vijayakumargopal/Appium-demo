from locators.network_and_internet.network_and_internet_locators import NetworkAndInternetLocators
from pages.basic_actions import BasicActions


class NetworkAndInternetPage(BasicActions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def title_should_presents(self):
        return self.element_should_presents(NetworkAndInternetLocators.network_and_internet_title, 10)
