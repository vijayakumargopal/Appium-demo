from appium.webdriver.common.appiumby import AppiumBy


class QuickSettingsDrawer:
    internet_icon = (AppiumBy.ACCESSIBILITY_ID, "Internet")
    bluetooth_icon = (AppiumBy.ACCESSIBILITY_ID, "Bluetooth.")
    flashlight_icon = (AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="com.android.systemui:id/quick_qs_panel"]/android.view.ViewGroup/android.widget.LinearLayout')
    do_not_disturb_icon = (AppiumBy.ACCESSIBILITY_ID, "Do Not Disturb.")