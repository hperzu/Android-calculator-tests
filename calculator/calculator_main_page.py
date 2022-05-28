from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver


class CalculatorAppMainPage:
    def __init__(self, driver: WebDriver, config):
        self._driver = driver
        self._config = config

        self._main_display = None
        self._button_plus = None
        self._button_equals = None
        self._button_multiply = None
        self._textview_result = None

        self.digit_key = lambda x: self.driver.find_element(AppiumBy.ID, f"com.android.calculator2:id/digit_{x}")

    @property
    def main_display(self):
        if not self._main_display:
            self._main_display = self.driver.find_element(AppiumBy.ID, "com.android.calculator2:id/display")
        return self._main_display

    @property
    def button_plus(self):
        if not self._button_plus:
            self._button_plus = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="plus")
        return self._button_plus

    @property
    def button_equals(self):
        if not self._button_equals:
            self._button_equals = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="equals")
        return self._button_equals

    @property
    def button_multiply(self):
        if not self._button_multiply:
            self._button_multiply = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="multiply")
        return self._button_multiply

    @property
    def textview_result(self):
        if not self._textview_result:
            self._textview_result = self.driver.find_element(AppiumBy.ID, "com.android.calculator2:id/result")
        return self._textview_result

    @property
    def driver(self):
        return self._driver

    @property
    def config(self):
        return self._config

    def is_launched(self):
        return self.main_display is not None

    def add_two_numbers(self, a, b):
        self.digit_key(a).click()
        self.button_plus.click()
        self.digit_key(b).click()
        self.button_equals.click()
        return self.textview_result.text

    def multiply_two_numbers(self, a, b):
        self.digit_key(a).click()
        self.button_multiply.click()
        self.digit_key(b).click()
        self.button_equals.click()
        return self.textview_result.text
