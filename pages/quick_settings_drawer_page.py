from pages.basic_actions import *
from utilities.exception_handlings import BluetoothNotPowerOn, BluetoothNotPowerOff


class QuickSettingsPage(BasicActions):

    internet_icon = (AppiumBy.ACCESSIBILITY_ID, "Internet")
    bluetooth_icon = (AppiumBy.ACCESSIBILITY_ID, "Bluetooth.")
    flashlight_icon = (AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="com.android.systemui:id/quick_qs_panel"]/android.view.ViewGroup/android.widget.LinearLayout')
    do_not_disturb_icon = (AppiumBy.ACCESSIBILITY_ID, "Do Not Disturb.")

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

