# Android calculator tests
A project showing the possibilities of combining pytest with appium.

## Run tests
To run the tests run the file `test_calculator.py` from [test_scenarious/calculator](https://github.com/hperzu/Android-calculator-tests/tree/main/test_scenarios/calculator)

## Set up local configuration
To set up the local configuration, edit the file `local_config_calculator.py` from [local_configuration](https://github.com/hperzu/Android-calculator-tests/tree/main/local_configuration)  
In this file you can set Appium server URL and Desired Capabilities for Appium such as:
* platformName
* platformVersion
* deviceName
* automationName
* appPackage
* appActivity

## Calculator
In the [calculator](https://github.com/hperzu/Android-calculator-tests/tree/main/calculator) folder can be found files with basic classes and methods.

## Test scenaroius 
In the [test_scenarios/calculator](https://github.com/hperzu/Android-calculator-tests/tree/main/test_scenarios/calculator) can be found files with conftest and test cases for calculator.
### Test case 1
In this test, two digits are added and it is checked if the results are correct.
### Test case 2
In this test, two digits are multiplied and it is checked if the results are correct.
