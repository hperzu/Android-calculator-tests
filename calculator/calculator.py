import logging
from appium.webdriver.webdriver import WebDriver

from calculator.calculator_main_page import CalculatorAppMainPage


logger = logging.getLogger(__name__)


class Calculator:
    def __init__(self, webdriver: WebDriver, config):
        self.driver = webdriver
        self.config = config
        self._main_page = None
        logger.debug("Creating calculator class instance ")

    @property
    def main_page(self):
        if not self._main_page:
            self._main_page = CalculatorAppMainPage(self.driver, self.config)
        return self._main_page

    def close(self):
        pass
