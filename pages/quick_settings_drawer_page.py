from typing import final

from locators.quick_settings_drawer_locators import QuickSettingsDrawer
from pages.basic_actions import BasicActions
from utilities.exception_handlings import BluetoothNotPowerOn, BluetoothNotPowerOff


class QuickSettingsPage(BasicActions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def turn_on_the_bluetooth(self):
        self.open_quick_app_settings()
        try:
            element = self.get_element(QuickSettingsDrawer.bluetooth_icon)
            if element.text == "Off":
                element.click()
        except Exception as err:
            raise BluetoothNotPowerOn(str(err))
        finally:
            self.close_quick_app_settings()

    def turn_off_the_bluetooth(self):
        self.open_quick_app_settings()
        try:
            element = self.get_element(QuickSettingsDrawer.bluetooth_icon)
            if element.text == "On":
                element.click()
        except Exception as err:
            raise BluetoothNotPowerOff(str(err))
        finally:
            self.close_quick_app_settings()

