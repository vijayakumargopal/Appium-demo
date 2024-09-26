"""
This file will helps you to do the basic configurations such as suite setup, sutite teardown, test setup
and test tear down, report configurations et.,
"""

import pytest, os
from utilities.read_input_file import *
from appium import webdriver
from appium.options.common import AppiumOptions
import pygetwindow


@pytest.fixture(scope="class")
def bring_emulator_to_top_of_the_screen():
    try:
        window = pygetwindow.getWindowsWithTitle('Android Emulator')[0]
        window.activate()
    except IndexError:
        print("Emulator window not found.")
    yield


@pytest.fixture(scope="function")
def open_settings_in_android_device(request):
    desired_capabilities = {
        "appium:platformName": read_data("platformName"),
        "appium:platformVersion": read_data("platformVersion"),
        "appium:deviceName": read_data("deviceName"),
        "appium:automationName": read_data("automationName"),
        "appium:noReset": read_data("noReset"),
        "appium:fullReset": read_data("fullReset"),
        "appium:appPackage": read_data("appPackage"),
        "appium:appActivity": read_data("appActivity")
    }
    driver = webdriver.Remote(read_data("host_url"), options=AppiumOptions().load_capabilities(desired_capabilities))
    request.cls.driver = driver
    yield
    os.system(f"adb shell am force-stop {read_data("appPackage")}")
