import logging
import pytest
from appium import webdriver

from calculator.calculator import Calculator
from local_configuration.local_config_calculator import calculator_local_config

logger = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def config_local():
    yield calculator_local_config


@pytest.fixture(scope="session")
def desired_caps(config_local):
    caps = dict()
    caps["platformName"] = config_local.platform_name
    caps["platformVersion"] = config_local.platform_version
    caps["deviceName"] = config_local.device_name
    caps["automationName"] = config_local.automation_name
    caps["appPackage"] = config_local.app_package
    caps["appActivity"] = config_local.app_activity
    yield caps


@pytest.fixture(scope="module")
def appium_driver(desired_caps, config_local):
    driver = webdriver.Remote(config_local.appium_server_url, desired_caps)
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def calculator_app(appium_driver, config_local):
    logger.info("Starting Calculator App...")
    app = Calculator(appium_driver, config_local)
    yield app


@pytest.fixture(scope="module")
def calculator_mian_page(calculator_app):
    logger.info("Getting Calculator App main page...")
    calculator_mian_page = calculator_app.main_page
    yield calculator_mian_page
    calculator_app.close()
