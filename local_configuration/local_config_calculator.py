from calculator.calculator_config import CalculatorConfig

calculator_local_config = CalculatorConfig()
calculator_local_config.appium_server_url = "http://localhost:4723/wd/hub"
calculator_local_config.platform_name = "Android"
calculator_local_config.platform_version = "9.0"
calculator_local_config.device_name = "emulator-5554"
calculator_local_config.automation_name = "Appium"
calculator_local_config.app_package = "com.android.calculator2"
calculator_local_config.app_activity = ".Calculator"
