from locators.home_page_locators import HomePageLocators
from pages.basic_actions import *
from pages.network_and_internet.network_and_internet_page import NetworkAndInternetPage

class HomePage(BasicActions, HomePageLocators):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def settings_title_should_presents(self):
        self.element_should_presents(self.settings_title, 10)

    def click_on_network_and_internet(self):
        self.click_element(self.network_internet_button)
        return NetworkAndInternetPage(self.driver)

    def click_on_connected_devices(self):
        self.click_element(self.connected_devices_button)

    def get_battery_percentage(self):
        return self.get_text_value(self.battery_percentage)
