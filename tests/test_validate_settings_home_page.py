import time

import pytest
from pages.home_page import HomePage
from pages.quick_settings_drawer_page import QuickSettingsPage


class TestHomePage:

    @pytest.mark.usefixtures("bring_emulator_to_top_of_the_screen")
    @pytest.mark.usefixtures("open_settings_in_android_device")
    def test_home_page_elements(self):
        """
        To run this test: pytest -v -k test_home_page_elements --html=report.html
        Description: This test case is just for the learning purpose
        Open settings app, click on the network and internet page and validate the title of it
        """
        home_page = HomePage(self.driver)
        home_page.settings_title_should_presents()
        network_internet_obj = home_page.click_on_network_and_internet()
        assert network_internet_obj.title_should_presents(), "Title not presents in the settings page"


    @pytest.mark.usefixtures("bring_emulator_to_top_of_the_screen")
    @pytest.mark.usefixtures("open_settings_in_android_device")
    @pytest.mark.parametrize("bluetooth_status", ("on", "off"))
    def test_validate_battery_percentage_when_switching_bluetooth(self, bluetooth_status):
        """
        To Run This test: pytest -v -k test_validate_battery_percentage_when_switching_bluetooth --html=reports.html
        Description: Collect the battery percentage when bluetooth on and off validate the value
        """
        home_page = HomePage(self.driver)
        home_page.settings_title_should_presents()
        drawer_page = QuickSettingsPage(home_page.driver)
        temp = drawer_page.turn_on_the_bluetooth() if bluetooth_status == "on" else drawer_page.turn_off_the_bluetooth()
        battery_percentage = home_page.get_battery_percentage()
        assert '100%' == battery_percentage, f"Battery percentage is {battery_percentage}"
