from pages.basic_actions import *
from pages.network_and_internet.network_and_internet_page import NetworkAndInternetPage


class HomePage(BasicActions):

    settings_title = (AppiumBy.XPATH, "//*[@text='Settings' and @resource-id='com.android.settings:id/homepage_title']")
    search_box = (AppiumBy.ID, "com.android.settings:id/search_action_bar")
    avatar_button = (AppiumBy.ID, "com.android.settings:id/account_avatar")

    network_internet_button = (AppiumBy.XPATH, "//*[@text='Network & internet' and @resource-id='android:id/title']")
    connected_devices_button = (AppiumBy.XPATH, "//*[@text='Connected devices' and @resource-id='android:id/title']")
    apps_button = (AppiumBy.XPATH, "//*[@text='Apps' and @resource-id='android:id/title']")
    notifications_button = (AppiumBy.XPATH, "//*[@text='Notifications' and @resource-id='android:id/title']")

    battery_button = (AppiumBy.XPATH, "//*[@text='Battery' and @resource-id='android:id/title']")
    battery_percentage = (AppiumBy.XPATH, '//*[@text="Battery"]//following-sibling::android.widget.TextView')

    storage_button = (AppiumBy.XPATH, "//*[@text='Storage' and @resource-id='android:id/title']")
    sound_and_vibrations_button = (AppiumBy.XPATH, "//*[@text='Sound & vibration' and @resource-id='android:id/title']")

    display_button = (AppiumBy.XPATH, "//*[@text='Display' and @resource-id='android:id/title']")
    wallpaper_style_button = (AppiumBy.XPATH, "//*[@text='Wallpaper & style' and @resource-id='android:id/title']")
    accessibility_button = (AppiumBy.XPATH, "//*[@text='Accessibility' and @resource-id='android:id/title']")
    security_button = (AppiumBy.XPATH, "//*[@text='Security' and @resource-id='android:id/title']")
    privacy_button = (AppiumBy.XPATH, "//*[@text='Privacy' and @resource-id='android:id/title']")
    location_button = (AppiumBy.XPATH, "//*[@text='Location' and @resource-id='android:id/title']")
    safety_and_emergency_button = (AppiumBy.XPATH, "//*[@text='Safety & emergency' and @resource-id='android:id/title']")
    password_and_accounts_button = (AppiumBy.XPATH, "//*[@text='Passwords & accounts' and @resource-id='android:id/title']")
    digital_wellbeing_button = (AppiumBy.XPATH, "//*[@text='Digital Wellbeing & parental controls' and @resource-id='android:id/title']")
    google_button = (AppiumBy.XPATH, "//*[@text='Google' and @resource-id='android:id/title']")

    system_button = (AppiumBy.XPATH, "//*[@text='System' and @resource-id='android:id/title']")
    about_emulated_button = (AppiumBy.XPATH, "//*[@text='About emulated device' and @resource-id='android:id/title']")
    tips_and_support_button = (AppiumBy.XPATH, "//*[@text='Tips & support' and @resource-id='android:id/title']")

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
