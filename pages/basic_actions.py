from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from utilities.exception_handlings import *
from appium.webdriver.common.appiumby import AppiumBy


class BasicActions:
    def __init__(self, driver):
        self.driver = driver

    def element_should_presents(self, locator, timeout=1):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except Exception as e:
            return False

    def wait_for_element(self, locator, timeout=30):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return element
        except Exception as e:
            print(f"Element not visible: {e}")
            return None

    def click_element(self, locator):
        self.driver.find_element(locator[0], locator[1]).click()

    def send_keys(self, locator, value):
        self.driver.find_element(locator[0], locator[1]).send_keys(value)

    def get_text_value(self, locator, timeout=1):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return element.text
        except Exception as e:
            raise ElementNotFound(str(e))

    def get_element(self, locator, timeout=1):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def is_checkbox_checked(self, locator, timeout=1):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        return element.get_attribute("checked")

    def check_the_checkbox(self, locator):
        status = self.is_checkbox_checked(locator)
        if not status:
            self.click_element(locator)

    def uncheck_the_checkbox(self, locator):
        status = self.is_checkbox_checked(locator)
        if status:
            self.click_element(locator)

    def open_quick_app_settings(self):
        size = self.driver.get_window_size()
        start_x = size['width'] / 2
        start_y = 0
        end_y = size['height'] * 0.75
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(2)
        actions.w3c_actions.pointer_action.move_to_location(start_x, end_y)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

    def close_quick_app_settings(self):
        size = self.driver.get_window_size()
        start_x = size['width'] / 2
        start_y = size['height']
        end_y = size['height'] * 0.25
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(2)
        actions.w3c_actions.pointer_action.move_to_location(start_x, end_y)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

    def press_back_button(self):
        self.driver.press_button("back")

    def press_home_button(self):
        self.driver.press_button("home")