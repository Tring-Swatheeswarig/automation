""" Importing Libraries """
from appium.webdriver import Remote
import re
import time
from datetime import date
# from appium.webdriver import Remote
import appium.common.logger
import psutil
# from appium.webdriver.common.appiumby import AppiumBy
# import appium
from appium import webdriver
# import time
import pytest
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.firefox.options import Options as FirefoxOptions
# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service as FirefoxService
# import logging
# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from selenium.webdriver.chrome.options import Options
# # from pyvirtualdisplay import Display
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.actions import interaction
# from selenium.webdriver.common.actions.action_builder import ActionBuilder
# from selenium.webdriver.common.actions.pointer_input import PointerInput
from utilities.readProperties import ReadConfig

# device_1_package = ReadConfig.get_package_device_1()
# device_1_activity = ReadConfig.get_activity_device_1()
# device_1_platform_name = ReadConfig.get_platform_name_device_1()
# device_1_platform_version = ReadConfig.get_platform_version_device_1()
# device_1_device_name = ReadConfig.get_device_name_device_1()
# device_1_udid = ReadConfig.get_udid_device_1()
# device_1_automator_name = ReadConfig.get_automator_name_device_1()
# device_1_port = ReadConfig.get_port_device_1()
device_1_package = "com.katonmeet.qa"
device_1_activity = "com.katonmeet.activity.WelcomeActivity"
device_1_platform_name = "Android"
device_1_platform_version = "13"
device_1_device_name = "Galaxy F62"
device_1_udid = "RZ8R60G7WCK"
device_1_automation_name = "UiAutomator2"
device_1_port = "4723"
device_2_package = ReadConfig.get_package_device_2()
device_2_activity = ReadConfig.get_activity_device_2()
device_2_platform_name = ReadConfig.get_platform_name_device_2()
device_2_platform_version = ReadConfig.get_platform_version_device_2()
device_2_device_name = ReadConfig.get_device_name_device_2()
device_2_udid = ReadConfig.get_udid_device_2()
device_2_automator_name = ReadConfig.get_automator_name_device_2()
device_2_port = ReadConfig.get_port_device_2()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        # extra.append(pytest_html.extras.url("https://d1se6lw3xj7v9k.cloudfront.net/signin"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            extra.append(pytest_html.extras.html("<div>Additional HTML</div>"))
        report.extras = extra


# @pytest.fixture(scope='function')
# def setup(browser, request):
#     if browser == 'chrome':
#         # This will call Chrome browser
#         option_browser = webdriver.ChromeOptions()
#         option_browser.add_argument("start-maximized")
#         option_browser.add_experimental_option('excludeSwitches', ['enable-logging'])
#         # print("display")
#         # display = Display(visible=0, size=(800, 800))
#         # display.start()
#         # driver = webdriver.Chrome("./utilities/drivers/chromedriver.exe",
#         #                           options=option_browser)
#         s = Service("./utilities/drivers/chromedriver.exe")
#         driver = webdriver.Chrome(service=s, options=option_browser)
#
#         # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option_browser)
#         # wait = WebDriverWait(driver, 20)
#         # driver.maximize_window()
#         request.cls.driver = driver
#         # request.cls.wait = wait
#         driver_details(driver)
#
#     elif browser == 'firefox':
#         option_browser = webdriver.FirefoxOptions()
#         path = "utilities/drivers/geckodriver.exe"
#         # option_browser.add_argument("--start-maximized")
#         firefox_service = FirefoxService(executable_path=path, log_output="./Logs/automation.log")
#         driver = webdriver.Firefox(service=firefox_service, options=option_browser)
#         request.cls.driver = driver
#
#     elif browser == 'msedge':
#         # This will call MSedge browser
#         option_browser = webdriver.EdgeOptions()
#         option_browser.add_argument("start-maximized")
#         option_browser.add_experimental_option('excludeSwitches', ['enable-logging'])
#         # driver = webdriver.Edge((EdgeChromiumDriverManager(og_level=logging.INFO).install()),
#         #                         options=option_browser)
#         s = Service("./utilities/drivers/msedgedriver.exe")
#         driver = webdriver.Firefox(service=s, options=option_browser)
#         wait = WebDriverWait(driver, 20)
#         driver.maximize_window()
#         request.cls.driver = driver
#         request.cls.wait = wait
#         driver_details(driver)
#
#     else:
#         # This will call Chrome browser
#         opt = Options()
#         opt.add_argument("--headless")
#         option_browser = webdriver.ChromeOptions()
#         # added - window size as 1920 x 1080 - as window cannot start maximized in headless mode
#         opt.add_argument("--window-size=1920,1080")
#         # option_browser.add_argument("start-maximized")
#         option_browser.add_experimental_option('excludeSwitches', ['enable-logging'])
#         option_browser.add_argument('log-level=3')
#         # print("display")
#         # display = Display(visible=0, size=(800, 800))
#         # display.start()
#         # driver = webdriver.Chrome("./utilities/drivers/chromedriver.exe",
#         #                           options=opt)
#         s = Service("./utilities/drivers/chromedriver.exe")
#         driver = webdriver.Chrome(service=s, options=opt)
#         # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opt)
#         # driver = webdriver.Chrome()
#         # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
#         #                           options=option_browser)
#         wait = WebDriverWait(driver, 20)
#         driver.maximize_window()
#         request.cls.driver = driver
#         request.cls.wait = wait
#         driver_details(driver)
#     return driver


def driver_details(driver):
    """ Detail of the Environment """
    browser_name = str(driver.capabilities['browserName']).title()
    browser_version = str(driver.capabilities['browserVersion'])
    platform = str(driver.capabilities['platformName']).title()
    from datetime import datetime

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    # print("Current Time =", current_time)

    day = date.today()
    dated = day.strftime("%B %d, %Y")
    today = dated, current_time

    print(f"Launching {browser_name} Browser........")
    print(f"Browser Name: {browser_name}")
    print(f"{browser_name} Browser version: {browser_version}")
    print(f"Platform: {platform}")
    print(f"Date and Time: {today}")


# def pytest_addoption(parser):
#     parser.addoption("--browser")


# This will perform in start of every function
# @pytest.fixture(scope="class", autouse=True)
# def browser(request):
#     """ Will run in starting of every function """
#     return request.config.getoption("--browser")
#

# Pytest HTML Report
def pytest_metadata(metadata):
    metadata['Developed by'] = 'Tringapps Inc'
    metadata['Project Name'] = 'RFLXT'
    metadata['Module'] = 'RFLXT'
    metadata['Tester'] = 'Vikraman'


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
    metadata.pop("Packages", None)


def pytest_html_report_title(report):
    report.title = "Mobile Test Report"


# browsers = ['firefox', 'chrome', 'msedge']
#
#
# @pytest.fixture(scope='function', params=browsers)
# def browser2(request):
#     browser = request.param
#
#     if browser == 'chrome':
#         # This will call Chrome browser
#         option_browser = webdriver.ChromeOptions()
#         # option_browser.add_argument("start-maximized")
#         option_browser.add_experimental_option('excludeSwitches', ['enable-logging'])
#         s = Service("./utilities/drivers/chromedriver.exe")
#         driver = webdriver.Chrome(service=s, options=option_browser)
#         driver_details(driver)
#         request.cls.driver = driver
#
#     elif browser == 'msedge':
#         # This will call MSedge browser
#         option_browser = webdriver.EdgeOptions()
#         # option_browser.add_argument("start-maximized")
#         option_browser.add_experimental_option('excludeSwitches', ['enable-logging'])
#         s = Service("./utilities/drivers/msedgedriver.exe")
#         driver = webdriver.Firefox(service=s, options=option_browser)
#         driver_details(driver)
#         request.cls.driver = driver
#
#     elif browser == 'firefox':
#         option_browser = webdriver.FirefoxOptions()
#         path = "utilities/drivers/geckodriver.exe"
#         # option_browser.add_argument("--start-maximized")
#         firefox_service = FirefoxService(executable_path=path, log_output="./Logs/automation.log")
#         driver = webdriver.Firefox(service=firefox_service, options=option_browser)
#         driver_details(driver)
#         request.cls.driver = driver
#
#     return driver


# npm install -g appium@1.22.3
@pytest.fixture(scope='function')
def mobile(request):
    # options.to_capabilities() - to check for headless
    options = UiAutomator2Options()
    options.platform_name = "Android"
    desired_caps = {
        "platformName": device_1_platform_name,
        "platformVersion": device_1_platform_version,
        "appium:deviceName": device_1_device_name,
        "appium:udid": device_1_udid,
        "appium:appPackage": device_1_package,
        "appium:appActivity": device_1_activity,
        "appium:directConnect": "true",
        "appium:newCommandTimeout": 600,
        "appium: uiautomator2ServerInstallTimeout": 120000,
        "appium:automationname": device_1_automator_name,
        "appium:ignoreHiddenApiPolicyError": True,
        "appium:disableWindowAnimation": True,
    }
    options.load_capabilities(desired_caps)
    driver = webdriver.Remote(f"http://localhost:{device_1_port}/", options=options)
    request.cls.driver = driver

    return driver


#  latest under test
# import pytest
# from appium import webdriver
#
#
# from appium.webdriver.extensions.uiautomator2 import UiAutomator2Options  # Import UiAutomator2Options
#
#
#
# @pytest.fixture(scope='function')
# def mobile(request):
#     androidPackage = "com.sec.android.app.popupcalculator"
#     options = UiAutomator2Options()  # Create an instance of UiAutomator2Options
#     desired_caps = {
#         "deviceName": "a31",
#         "udid": "RZ8R21VCZHH",
#         "platformName": "Android",
#         "platformVersion": "12",
#         "appPackage": androidPackage,
#         "appActivity": "com.sec.android.app.popupcalculator.Calculator",
#         "automationName": "UiAutomator2",
#         "ensureWebviewsHavePages": True,
#         "nativeWebScreenshot": True,
#         "newCommandTimeout": 3600,
#         "connectHardwareKeyboard": True,
#     }
#
#     options.(androidPackage)
#     options.load_capabilities(desired_caps)  # Use load_capabilities to set desired_caps
#     driver = webdriver.Remote("http://localhost:4723/wd/hub", options)
#
#     request.cls.driver = driver


mobiles = ['device_1', 'device_2']


@pytest.fixture(scope='function', params=mobiles)
def multiple_mobiles(request):
    mobile = request.param
    if mobile == 'device_1':
        options = UiAutomator2Options()
        desired_caps = {
            "platformVersion": device_1_platform_version,
            "appium:deviceName": device_1_device_name,
            "appium:udid": device_1_udid,
            "appium:appPackage": device_1_package,
            "appium:appActivity": device_1_activity,
            "appium:directConnect": "true",
            "appium:newCommandTimeout": 600,
        }
        options.load_capabilities(desired_caps)
        driver = webdriver.Remote(f"http://127.0.0.1:4723/wd/hub", options=options)
        request.cls.driver = driver

    if mobile == 'device_2':
        options = UiAutomator2Options()
        desired_caps = {
            "platformVersion": device_2_platform_version,
            "appium:deviceName": device_2_device_name,
            "appium:udid": device_2_udid,
            "appium:appPackage": device_2_package,
            "appium:appActivity": device_2_activity,
            "appium:directConnect": "true",
            "appium:newCommandTimeout": 600,
        }
        options.load_capabilities(desired_caps)
        driver = webdriver.Remote(f"http://127.0.0.1:4720/wd/hub", options=options)
        request.cls.driver = driver
    yield driver  # Ensure cleanup happens after the test
    if driver:
        driver.quit()

from appium.webdriver.appium_service import AppiumService

def is_appium_server_running():
    for process in psutil.process_iter(attrs=['pid', 'name', 'cmdline']):
        if "appium" in process.info['name'].lower() and "--port" in process.info['cmdline']:
            # Extract the port number from the command line arguments
            port_match = re.search(r"--port (\d+)", " ".join(process.info['cmdline']))
            if port_match:
                port = int(port_match.group(1))
                return True, port
    return False, None
appium_running, appium_port = is_appium_server_running()

if appium_running:
    appium_service = AppiumService()
    # appium_service.stop()
    print(f"Appium server is already running on port {appium_port}")
else:
    # Start the Appium server programmatically
    appium_service = AppiumService()
    # appium_service.start()
    time.sleep(5)

@pytest.fixture(scope='function')
def mobile_v2(request):
    # is_appium_server_running()

    options = UiAutomator2Options()
    desired_caps = {
        "platformVersion": device_1_platform_version,
        "appium:deviceName": device_1_device_name,
        "appium:udid": device_1_udid,
        "appium:appPackage": device_1_package,
        "appium:appActivity": device_1_activity,
        "appium:directConnect": "true",
        "appium:newCommandTimeout": 600,
    }
    options.load_capabilities(desired_caps)
    driver = webdriver.Remote(f"http://127.0.0.1:{device_1_port}", options=options)
    request.cls.driver = driver

    return driver

@pytest.fixture(scope='function')
def mobile_v2_internet(request):
    # is_appium_server_running()

    options = UiAutomator2Options()
    desired_caps = {
        "platformVersion": device_1_platform_version,
        "appium:deviceName": device_1_device_name,
        "appium:udid": device_1_udid,
        "appium:appPackage": device_1_package,
        "appium:appActivity": device_1_activity,
        "appium:directConnect": "true",
        "appium:newCommandTimeout": 600,
    }
    options.load_capabilities(desired_caps)
    # driver = webdriver.Remote(f"http://127.0.0.1:{device_1_port}", options=options)


    remote_host = "10.1.0.108"
    remote_port = device_1_port
    remote_url = f"http://{remote_host}:{remote_port}"

    driver = Remote(remote_url, options=options)
    request.cls.driver = driver

    return driver


@pytest.fixture(scope='function')
def mobile_v2_internet_ios(request):
    # is_appium_server_running()

    options = XCUITestOptions()
    desired_caps = {
        "platformVersion": device_2_platform_version,
        "appium:deviceName": device_2_device_name,
        "appium:udid": device_2_udid,
        "appium:appPackage": device_2_package,
        "appium:appActivity": device_2_activity,
        "appium:directConnect": "true",
        "appium:newCommandTimeout": 600,
    }
    options.load_capabilities(desired_caps)
    # driver = webdriver.Remote(f"http://127.0.0.1:{device_1_port}", options=options)


    remote_host = "10.2.0.118"
    remote_port = device_1_port
    remote_url = f"http://{remote_host}:{remote_port}"

    driver = Remote(remote_url, options=options)
    request.cls.driver = driver

    return driver


@pytest.fixture(scope='function')
def mobile_v2_dual_devices(request):
    # Device 1 configuration
    options_1 = UiAutomator2Options()
    desired_caps_1 = {
        "platformVersion": device_1_platform_version,
        "appium:deviceName": device_1_device_name,
        "appium:udid": device_1_udid,
        "appium:appPackage": device_1_package,
        "appium:appActivity": device_1_activity,
        "appium:directConnect": "true",
        "appium:newCommandTimeout": 600,
    }
    options_1.load_capabilities(desired_caps_1)
    driver_1 = webdriver.Remote(f"http://127.0.0.1:{device_1_port}/wd/hub", options=options_1)

    # Device 2 configuration
    options_2 = UiAutomator2Options()
    desired_caps_2 = {
        "platformVersion": device_2_platform_version,
        "appium:deviceName": device_2_device_name,
        "appium:udid": device_2_udid,
        "appium:appPackage": device_2_package,
        "appium:appActivity": device_2_activity,
        "appium:directConnect": "true",
        "appium:newCommandTimeout": 600,
    }
    options_2.load_capabilities(desired_caps_2)
    driver_2 = webdriver.Remote(f"http://127.0.0.1:{device_2_port}/wd/hub", options=options_2)

    # Attach both drivers to the test class
    request.cls.driver_1 = driver_1
    request.cls.driver_2 = driver_2

    # Return both drivers in a tuple or dictionary, depending on your preference
    return driver_1, driver_2


device_1_config = {
    "platformVersion": "12",
    "appium:deviceName": "A31",
    "appium:udid": "RF8M32M3T6E",  # Change to your actual UDID
    "appium:appPackage": "com.greencopper.revoltmusicconference2022.staging",
    "appium:appActivity": "com.greencopper.revoltmusicconference2022.MainActivity",
    "appium:directConnect": "true",
    "appium:newCommandTimeout": 600
}

device_2_config = {
    "platformVersion": "12",
    "appium:deviceName": "A31",
    "appium:udid": "RZ8N602HQVT",  # Change to your actual UDID
    "appium:appPackage": "com.greencopper.revoltmusicconference2022.staging",
    "appium:appActivity": "com.greencopper.revoltmusicconference2022.MainActivity",
    "appium:directConnect": "true",
    "appium:newCommandTimeout": 600
}

# Add the devices and their respective ports to a list of parameters
devices = [
    {"device_config": device_1_config, "port": 4723},
    {"device_config": device_2_config, "port": 4720},
]


@pytest.fixture(scope='function', params=devices)
def mobile_v2_check(request):
    # Get the device config and port from the current parameter set
    device_config = request.param["device_config"]
    port = request.param["port"]

    options = UiAutomator2Options()
    options.load_capabilities(device_config)

    # Set up the Appium WebDriver for the current device using its specific port
    driver = webdriver.Remote(f"http://127.0.0.1:{port}/wd/hub", options=options)
    request.cls.driver = driver

    return driver