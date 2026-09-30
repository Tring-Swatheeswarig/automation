""" Importing Libraries """
import time
from datetime import date
import allure
import pytest
import selenium
# import config.read_config
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from appium.webdriver.common.appiumby import AppiumBy


# from appium.webdriver.common.touch_action import TouchAction


from appium import webdriver

# Assume 'driver' is already set up and initialized

from selenium.common.exceptions import  TimeoutException, NoSuchElementException
from allure_commons.types import AttachmentType
from selenium.webdriver import Keys
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pageObjects.PageObjects
import utilities.readProperties
import utilities.customLogger
import subprocess
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
# import config.read_config
class TestTrEOId0101:
    """ Class for checking Log in Screen Output """

    # baseURL = ReadConfig.getapplicationurl()
    email = ReadConfig.getemail()
    password = ReadConfig.getpassword()
    newpassword = ReadConfig.getnewpassword()
    day = date.today()
    today = day.strftime("%B %d, %Y")
    logger = LogGen.loggen()
    email_xpath = "//android.widget.EditText[@text='Email Address']"
    phone_no_xpath = "//android.widget.EditText[@text='Phone Number']"
    hamburger_xpath = "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup"
    # phone_no_xpath = "//android.view.ViewGroup[@content-desc='Phone Number']"



    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.android_and_ios
    @pytest.mark.mobile
    @pytest.mark.signup
    @pytest.mark.regression

    @allure.description_html("""
        <h2>Checking the more menu icon UI</h2>
        <em><u>Test Case Description - To veirfy the More menu icon UI.</em></u><br>
        <em></em><br><br>
        <em><u>Expected Result</em></u><br>
        "<em>FR Hamburger icon should display according to Design document
        </em>"
        <h3>Tester : Bharadh</h3>
        <table style="width:30%">
        <tr align="left">
        <th>Client</th>
        <th>Project</th>
        </tr>
        <tr align="left">
        <td>Revolt_world</td>
        <td>Revolt_world</td>
        </tr>
        </table>
        """)
    @allure.severity(allure.severity_level.MINOR)
    # @pytest.mark.regression
    @pytest.mark.sanity
    def test_1_TR_REV_More_WORLD_934_106(self, mobile_v2):
        self.driver = mobile_v2
        wait = WebDriverWait(self.driver, 30)
        el1 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Do This Later\")")))
        el1.click()
        el2 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
        "new UiSelector().className(\"android.view.ViewGroup\").instance(56)")))
        el2.click()
        el3 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
        "new UiSelector().className(\"android.view.ViewGroup\").instance(56)")))
        el3.click()
        el4 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
        "new UiSelector().className(\"android.widget.ImageView\").instance(1)")))
        el4.click()
        self.driver.quit()
    #
#     # @allure.description_html("""
#     #         <h2>Checking the more menu slide UI</h2>
#     #         <em><u>Test Case Description - To verify the more menu while user is not signin ( guest user).</em></u><br>
#     #         <em></em><br><br>
#     #         <em><u>Expected Result</em></u><br>
#     #         "<em>FR "1. More text should display
#     #                  2.Close button left aligned top menu screen
#     #                  3. Menu Element list as below with > icon and Separator line:Create Account,Signin,Get Text Exclusives,Shop Merch,Check Out Lineup,Schedule Office Hours,Find a job,View FAQs,Meet Our Sponsors,Contact Us"
#     #         </em>"
#     #         <h3>Tester : Bharadh</h3>
#     #         <table style="width:30%">
#     #         <tr align="left">
#     #         <th>Client</th>
#     #         <th>Project</th>
#     #         </tr>
#     #         <tr align="left">
#     #         <td>Revolt_world</td>
#     #         <td>Revolt_world</td>
#     #         </tr>
#     #         </table>
#     #         """)
#     # def test_2_TR_REV_More_WORLD_934_107(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #
#     #     wait = WebDriverWait(self.driver, 30)
#     #     el7 = wait.until(
#     #         EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Do This Later\")")))
#     #     el7.click()
#     # def KB_KBM_Sign_KBM-04_7(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30
#     #    el1 = wait.until(
#     #         EC.element_to_be_clickable((AppiumBy.androidUIAutomator("new UiSelector().className(\"android.widget.EditText\").instance(1)"))));
#     #    el1.sendKeys("FacX3G8JG@123");
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable((AppiumBy.androidUIAutomator("new UiSelector().text(\"Sign In\")"))));
#     #     el2.click();
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable((AppiumBy.androidUIAutomator("new UiSelector().text(\"Username is required\")"))));
#     #     el3.click();
#     # def test_KB_KBM_Sign_KBM_04_7(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.androidUIAutomator, 'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el1.send_keys("FacX3G8JG@123")
#     #
#     #
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.androidUIAutomator, 'new UiSelector().text("Sign In")')
#     #         )
#     #     )
#     #     el2.click()
#     #
#     #
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.androidUIAutomator, 'new UiSelector().text("Username is required")')
#     #         )
#     #     )
#     #     el3.click()
#     # def test_KB_KBM_Sign_KBM_04_7(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el1.send_keys("Test@123")
#     #
#     #
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Sign In")')
#     #         )
#     #     )
#     #     el2.click()
#     #
#     #
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Username is required")')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     # def test_KB_KBM_Forg_KBM_14_15(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Forgot Password?")')
#     #         )
#     #     )
#     #     el1.click()
#     #
#     #
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(1)')
#     #         )
#     #     )
#     #     el2.click()
#     #
#     # def test_KB_KBM_Sign_KBM_04_6(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.CLASS_NAME, "android.widget.ImageView")
#     #         )
#     #     )
#     #     el1.click()
#     #
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.CLASS_NAME, "android.widget.ScrollView")
#     #         )
#     #     )
#     #     el2.click()
#     #
#     # def test_KB_KBM_Sign_KBM_04_11(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el1.send_keys("alberto")
#     #
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el2.send_keys("Test@123")
#     #
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Sign In")')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(3)')
#     #         )
#     #     )
#     #     el4.click()
#     #
#     # def test_KB_KBM_Forg_KBM_14_16(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Forgot Password?")')
#     #         )
#     #     )
#     #     el1.click()
#     #
#     #
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.CLASS_NAME, "android.widget.EditText")
#     #         )
#     #     )
#     #     el2.send_keys("albertoo@mailinator.com")
#     #
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector(). className("android.view.View").instance(2)')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     # def test_KB_KBM_Forg_KBM_14_20(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Forgot Password?")')
#     #         )
#     #     )
#     #     el1.click()
#     #
#     #
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.CLASS_NAME, "android.widget.EditText")
#     #         )
#     #     )
#     #     el2.send_keys("alberto@mailinator.com")
#     #
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(2)')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(1)')
#     #         )
#     #     )
#     #     el4.click()
#     #
#     # def test_KB_KBM_Forg_KBM_14_26(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Forgot Password?")')
#     #         )
#     #     )
#     #     el1.click()
#     #
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.CLASS_NAME, "android.widget.EditText")
#     #         )
#     #     )
#     #     el2.send_keys("albertoo@mailinator.com")
#     #
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Send OTP")')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.CLASS_NAME, "android.widget.EditText")
#     #         )
#     #     )
#     #     el4.send_keys("5331")
#     #
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Verify")')
#     #         )
#     #     )
#     #     el5.click()
#     #
#     #     el6 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(1)')
#     #         )
#     #     )
#     #     el6.click()
#     #
#     # def test_KB_KBM_Sign_KBM_91_36(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #     el9 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el9.send_keys("alberto")
#     #
#     #     el10 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el10.send_keys("Test@123")
#     #
#     #     el11 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Sign In")')
#     #         )
#     #     )
#     #     el11.click()
#     #
#     #     el12 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(1)')
#     #         )
#     #     )
#     #     el12.click()
#     #
#     #     el13 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(26)')
#     #         )
#     #     )
#     #     el13.click()
#     #
#     #     el14 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(1)')
#     #         )
#     #     )
#     #     el14.click()
#     #
#     #     el15 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Sign Out")')
#     #         )
#     #     )
#     #     el15.click()
#     #
#     # def test_KB_KBM_Rese_KBM_16_27(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Forgot Password?")')
#     #         )
#     #     )
#     #     el1.click()
#     #
#     #
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(1)')
#     #         )
#     #     )
#     #     el2.click()
#     #
#     #
#     #     el3 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.CLASS_NAME, "android.widget.EditText")
#     #         )
#     #     )
#     #     el3.send_keys("roronoa@mailinator.com")
#     #
#     #
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Send OTP")')
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #
#     #     el5 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.CLASS_NAME, "android.widget.EditText")
#     #         )
#     #     )
#     #     el5.send_keys("3658")
#     #
#     #
#     #     el6 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(2)')
#     #         )
#     #     )
#     #     el6.click()
#     #
#     #
#     #     el7 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(1)')
#     #         )
#     #     )
#     #     el7.click()
#     #
#     # def test_KB_KBM_Sign_KBM_91_38(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #     el1 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el1.send_keys("alberto")
#     #
#     #     el2 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el2.send_keys("Test@123")
#     #
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(3)')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(1)')
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(26)')
#     #         )
#     #     )
#     #     el5.click()
#     #
#     #     el6 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Sign Out")')
#     #         )
#     #     )
#     #     el6.click()
#     #
#     #
#     #
#     #
#     # def test_KB_KBM_Meet_KBM_38_87(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #
#     #     el1 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el1.send_keys("alberto")
#     #
#     #
#     #     el2 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el2.send_keys("Test@123")
#     #
#     #
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Sign In")')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(1)')
#     #         )
#     #     )
#     #     el4.click()
#     #
#     # def test_KB_KBM_Home_KBM_18_40(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #
#     #     el1 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el1.send_keys("alberto")
#     #
#     #
#     #     el2 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el2.send_keys("Test@123")
#     #
#     #
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Sign In")')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(1)')
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #
#     #
#     # def test_KB_KBM_Sett_GM_136_107(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #     el1 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el1.send_keys("alberto")
#     #
#     #     el2 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el2.send_keys("Test@123")
#     #
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Sign In")')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(1)')
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(26)')
#     #         )
#     #     )
#     #     el5.click()
#     #
#     #
#     #     el6 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(1)')
#     #         )
#     #     )
#     #     el6.click()
#     # def test_KB_KBM_Sett_GM_136_108(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #     el1 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el1.send_keys("alberto")
#     #
#     #     el2 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el2.send_keys("Test@123")
#     #
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Sign In")')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(1)')
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(26)')
#     #         )
#     #     )
#     #     el5.click()
#     #
#     #     el6 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(1)')
#     #         )
#     #     )
#     #     el6.click()
#     #
#     #
#     #
#     # def test_KB_KBM_Cale_GM_101_119(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #     el1 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el1.send_keys("alberto")
#     #
#     #     el2 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el2.send_keys("Test@123")
#     #
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(3)')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(1)')
#     #         )
#     #     )
#     #     el4.click()
#     #
#     # def test_KB_KBM_Cale_GM_103_124(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #     el1 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el1.send_keys("alberto")
#     #
#     #     el2 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el2.send_keys("Test@123")
#     #
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Sign In")')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Today")')
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(1)')
#     #         )
#     #     )
#     #     el5.click()
#     #
#     # def test_KB_KBM_Sett_GM_148_147(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #     el1 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el1.send_keys("alberto")
#     #
#     #     el2 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el2.send_keys("Test@123")
#     #
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(3)')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(27)')
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(5)')
#     #         )
#     #     )
#     #     el5.click()
#     #
#     #     el6 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(1)')
#     #         )
#     #     )
#     #     el6.click()
#     # #
#     # def test_KB_KBM_Sett_GM_148_148(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #
#     #     el1 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el1.send_keys("alberto")
#     #
#     #
#     #     el2 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el2.send_keys("Test@123")
#     #
#     #
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Sign In").instance(1)')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(27)')
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(5)')
#     #         )
#     #     )
#     #     el5.click()
#     #
#     #
#     #     el6 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el6.send_keys("Test@123")
#     #
#     #
#     #     el7 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el7.send_keys("Pass@123")
#     #
#     #
#     #     el8 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(2)')
#     #         )
#     #     )
#     #     el8.send_keys("Pass@123")
#     #
#     #
#     #
#     #
#     #
#     #
#     #
#     # #
#     # #
#     # #
#     # #
#     # def test_KB_KBM_Meet_GM_146_152(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #     el1 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el1.send_keys("alberto")
#     #
#     #     el2 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el2.send_keys("Test@123")
#     #
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Sign In").instance(1)')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(28)')
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(1)')
#     #         )
#     #     )
#     #     el5.click()
#     #
#     #     el6 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ACCESSIBILITY_ID, "Push Notification")
#     #         )
#     #     )
#     #     el6.click()
#     #
#     # def test_KB_KBM_Meet_GM_131_191(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Don’t have an account? SignUp")')
#     #         )
#     #     )
#     #     el1.click()
#     #
#     #
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Agree to the Terms of use and Privacy Policy")')
#     #         )
#     #     )
#     #     el2.click()
#     #
#     #
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.CLASS_NAME, "android.webkit.WebView")
#     #         )
#     #     )
#     #     el3.click()
#     #
#     # def test_KB_KBM_Auth_GM_293_193(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #
#     #     el1 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el1.send_keys("alberto")
#     #
#     #
#     #     el2 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el2.send_keys("Test@123")
#     #
#     #
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Sign In").instance(1)')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     # def test_KB_KBM_Join_GM_104_137(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #
#     #     el1 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el1.send_keys("alberto")
#     #
#     #
#     #     el2 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el2.send_keys("Test@123")
#     #
#     #
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Sign In").instance(1)')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(1)')
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Join")')
#     #         )
#     #     )
#     #     el5.click()
#     #
#     #
#     #     el6 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Enter Meeting Code")')
#     #         )
#     #     )
#     #     el6.click()
#     #
#     #
#     #     el7 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Join")')
#     #         )
#     #     )
#     #     el7.click()
#     #
#     # def test_KB_KBM_Favo_GM_126_218(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #
#     #     el2 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el2.send_keys("alberto")
#     #
#     #
#     #     el3 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el3.send_keys("Test@123")
#     #
#     #
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Sign In").instance(1)')
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(24)')
#     #         )
#     #     )
#     #     el5.click()
#     #
#     #     el6 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(3)')
#     #         )
#     #     )
#     #     el6.click()
#     #
#     #     el7 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("My Favourite Meetings")')
#     #         )
#     #     )
#     #     el7.click()
#     #
#     # def test_KB_KBM_Noti_GM_248_172(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #
#     #     el1 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el1.send_keys("alberto")
#     #
#     #
#     #     el2 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el2.send_keys("Test@123")
#     #
#     #
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Sign In").instance(1)')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ACCESSIBILITY_ID, "Notification")
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(1)')
#     #         )
#     #     )
#     #     el5.click()
#     #
#     #
#     #     el6 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(7)')
#     #         )
#     #     )
#     #     el6.click()
#     #
#     #
#     #     el7 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Notification")')
#     #         )
#     #     )
#     #     el7.click()
#     #
#     # def test_KB_KBM_Sear_GM_97_157(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #
#     #     el1 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el1.send_keys("alberto")
#     #
#     #
#     #     el2 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el2.send_keys("Test@123")
#     #
#     #
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Sign In").instance(1)')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ACCESSIBILITY_ID, "Search")
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #     el6 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(2)')
#     #         )
#     #     )
#     #     el6.click()
#     #
#     #
#     #
#     # def test_KB_KBM_Meet_GM_528_268(self, mobile_v2):
#     #         self.driver = mobile_v2
#     #         wait = WebDriverWait(self.driver, 30)
#     #         el1 = wait.until(
#     #             EC.presence_of_element_located(
#     #                 (AppiumBy.ANDROID_UIAUTOMATOR,
#     #                  'new UiSelector().className("android.widget.EditText").instance(0)')
#     #             )
#     #         )
#     #         el1.send_keys("alberto")
#     #
#     #         el2 = wait.until(
#     #             EC.presence_of_element_located(
#     #                 (AppiumBy.ANDROID_UIAUTOMATOR,
#     #                  'new UiSelector().className("android.widget.EditText").instance(1)')
#     #             )
#     #         )
#     #         el2.send_keys("Test@123")
#     #
#     #         el3 = wait.until(
#     #             EC.element_to_be_clickable(
#     #                 (AppiumBy.ANDROID_UIAUTOMATOR,
#     #                  'new UiSelector().text("Sign In").instance(1)')
#     #             )
#     #         )
#     #         el3.click()
#     #
#     #         el4 = wait.until(
#     #             EC.element_to_be_clickable(
#     #                 (AppiumBy.ACCESSIBILITY_ID, "Notification")
#     #             )
#     #         )
#     #         el4.click()
#     #
#     #         el5 = wait.until(
#     #             EC.element_to_be_clickable(
#     #                 (AppiumBy.ANDROID_UIAUTOMATOR,
#     #                  'new UiSelector().className("android.view.View").instance(2)')
#     #             )
#     #         )
#     #         el5.click()
#     #
#     #
#     #
#     #
#     #
#     # def test_KB_KBM_Mult_GM_536_287(self, mobile_v2):
#     #         self.driver = mobile_v2
#     #         wait = WebDriverWait(self.driver, 30)
#     #         el1 = wait.until(
#     #             EC.presence_of_element_located(
#     #                 (AppiumBy.ANDROID_UIAUTOMATOR,
#     #                  'new UiSelector().className("android.widget.EditText").instance(0)')
#     #             )
#     #         )
#     #         el1.send_keys("Maheshh")
#     #
#     #         el2 = wait.until(
#     #             EC.presence_of_element_located(
#     #                 (AppiumBy.ANDROID_UIAUTOMATOR,
#     #                  'new UiSelector().className("android.widget.EditText").instance(1)')
#     #             )
#     #         )
#     #         el2.send_keys("A")
#     #
#     #         el3 = wait.until(
#     #             EC.presence_of_element_located(
#     #                 (AppiumBy.ANDROID_UIAUTOMATOR,
#     #                  'new UiSelector().className("android.widget.EditText").instance(2)')
#     #             )
#     #         )
#     #         el3.send_keys("dsdfghjhvcxzasedrtyujhbvcxzsdrfgyujiknb vcxs swertyuijhgvcdxsertyuijhbvcxzsawertijk")
#     #
#     #         el4 = wait.until(
#     #             EC.presence_of_element_located(
#     #                 (AppiumBy.ANDROID_UIAUTOMATOR,
#     #                  'new UiSelector().className("android.widget.EditText").instance(3)')
#     #             )
#     #         )
#     #         el4.send_keys("maheshh@mailinator.com")
#     #
#     #         el5 = wait.until(
#     #             EC.presence_of_element_located(
#     #                 (AppiumBy.ANDROID_UIAUTOMATOR,
#     #                  'new UiSelector().className("android.widget.EditText").instance(4)')
#     #             )
#     #         )
#     #         el5.send_keys("Test@123")
#     #
#     #         el6 = wait.until(
#     #             EC.presence_of_element_located(
#     #                 (AppiumBy.ANDROID_UIAUTOMATOR,
#     #                  'new UiSelector().className("android.widget.EditText").instance(5)')
#     #             )
#     #         )
#     #         el6.send_keys("Test@123")
#     #
#     #         el7 = wait.until(
#     #             EC.element_to_be_clickable(
#     #                 (AppiumBy.ACCESSIBILITY_ID, "checkBox")
#     #             )
#     #         )
#     #         el7.click()
#     #
#     #         el8 = wait.until(
#     #             EC.element_to_be_clickable(
#     #                 (AppiumBy.ANDROID_UIAUTOMATOR,
#     #                  'new UiSelector().text("Sign Up").instance(1)')
#     #             )
#     #         )
#     #         el8.click()
#     #
#     #         el9 = wait.until(
#     #             EC.element_to_be_clickable(
#     #                 (AppiumBy.ANDROID_UIAUTOMATOR,
#     #                  'new UiSelector().text("Username cannot exceed 50 characters")')
#     #             )
#     #         )
#     #         el9.click()
#     #
#     #
#     #
#     # def test_KB_KBM_Mult_GM_536_287(self, mobile_v2):
#     #         self.driver = mobile_v2
#     #         wait = WebDriverWait(self.driver, 30)
#     #
#     #         el1 = wait.until(
#     #             EC.element_to_be_clickable(
#     #                 (AppiumBy.ANDROID_UIAUTOMATOR,
#     #                  'new UiSelector().text("Don’t have an account? SignUp")')
#     #             )
#     #         )
#     #         el1.click()
#     #
#     #         el3 = wait.until(
#     #             EC.presence_of_element_located(
#     #                 (AppiumBy.ANDROID_UIAUTOMATOR,
#     #                  'new UiSelector().className("android.widget.EditText").instance(0)')
#     #             )
#     #         )
#     #         el3.send_keys("Maheshh")
#     #
#     #         el4 = wait.until(
#     #             EC.presence_of_element_located(
#     #                 (AppiumBy.ANDROID_UIAUTOMATOR,
#     #                  'new UiSelector().className("android.widget.EditText").instance(1)')
#     #             )
#     #         )
#     #         el4.send_keys("A")
#     #
#     #         el5 = wait.until(
#     #             EC.presence_of_element_located(
#     #                 (AppiumBy.ANDROID_UIAUTOMATOR,
#     #                  'new UiSelector().className("android.widget.EditText").instance(2)')
#     #             )
#     #         )
#     #         el5.send_keys(
#     #             "srtyuijhvcdrtyuioijbvcxsertyuijnbvcxsertyuikjnbvcxsertyujnbvcdsertyuiknbvcxserbjnbvcdfghjkjnbvcxsertyujmikjnbvcxsertyujnb x")
#     #
#     #         el6 = wait.until(
#     #             EC.presence_of_element_located(
#     #                 (AppiumBy.ANDROID_UIAUTOMATOR,
#     #                  'new UiSelector().className("android.widget.EditText").instance(3)')
#     #             )
#     #         )
#     #         el6.send_keys("maheshh@mailinator.com")
#     #
#     #         el7 = wait.until(
#     #             EC.presence_of_element_located(
#     #                 (AppiumBy.ANDROID_UIAUTOMATOR,
#     #                  'new UiSelector().className("android.widget.EditText").instance(4)')
#     #             )
#     #         )
#     #         el7.send_keys("Test@123")
#     #
#     #         el8 = wait.until(
#     #             EC.presence_of_element_located(
#     #                 (AppiumBy.ANDROID_UIAUTOMATOR,
#     #                  'new UiSelector().className("android.widget.EditText").instance(5)')
#     #             )
#     #         )
#     #         el8.send_keys("Test@123")
#     #
#     #         el9 = wait.until(
#     #             EC.element_to_be_clickable(
#     #                 (AppiumBy.ACCESSIBILITY_ID, "checkBox")
#     #             )
#     #         )
#     #         el9.click()
#     #
#     #         el10 = wait.until(
#     #             EC.element_to_be_clickable(
#     #                 (AppiumBy.ANDROID_UIAUTOMATOR,
#     #                  'new UiSelector().text("Sign Up").instance(1)')
#     #             )
#     #         )
#     #         el10.click()
#     #
#     #         el11 = wait.until(
#     #             EC.element_to_be_clickable(
#     #                 (AppiumBy.ANDROID_UIAUTOMATOR,
#     #                  'new UiSelector().text("Username cannot exceed 50 characters")')
#     #             )
#     #         )
#     #         el11.click()
#     #
#     #
#     #
#     # def test_KB_KBM_Mult_GM_536_289(self, mobile_v2):
#     #         self.driver = mobile_v2
#     #         wait = WebDriverWait(self.driver, 30)
#     #
#     #         el1 = wait.until(
#     #             EC.element_to_be_clickable(
#     #                 (AppiumBy.ANDROID_UIAUTOMATOR,
#     #                  'new UiSelector().text("Don’t have an account? SignUp")')
#     #             )
#     #         )
#     #         el1.click()
#     #
#     #         el2 = wait.until(
#     #             EC.presence_of_element_located(
#     #                 (AppiumBy.ANDROID_UIAUTOMATOR,
#     #                  'new UiSelector().className("android.widget.EditText").instance(0)')
#     #             )
#     #         )
#     #         el2.send_keys("Naveen")
#     #
#     #         el3 = wait.until(
#     #             EC.presence_of_element_located(
#     #                 (AppiumBy.ANDROID_UIAUTOMATOR,
#     #                  'new UiSelector().className("android.widget.EditText").instance(1)')
#     #             )
#     #         )
#     #         el3.send_keys("A")
#     #
#     #         el4 = wait.until(
#     #             EC.presence_of_element_located(
#     #                 (AppiumBy.ANDROID_UIAUTOMATOR,
#     #                  'new UiSelector().className("android.widget.EditText").instance(2)')
#     #             )
#     #         )
#     #         el4.send_keys("Naveen")
#     #
#     #         el5 = wait.until(
#     #             EC.presence_of_element_located(
#     #                 (AppiumBy.ANDROID_UIAUTOMATOR,
#     #                  'new UiSelector().className("android.widget.EditText").instance(3)')
#     #             )
#     #         )
#     #         el5.send_keys("naveen@mailinator.com")
#     #
#     #         el6 = wait.until(
#     #             EC.presence_of_element_located(
#     #                 (AppiumBy.ANDROID_UIAUTOMATOR,
#     #                  'new UiSelector().className("android.widget.EditText").instance(4)')
#     #             )
#     #         )
#     #         el6.send_keys("Test@123")
#     #
#     #         el7 = wait.until(
#     #             EC.presence_of_element_located(
#     #                 (AppiumBy.ANDROID_UIAUTOMATOR,
#     #                  'new UiSelector().className("android.widget.EditText").instance(5)')
#     #             )
#     #         )
#     #         el7.send_keys("Test@1")
#     #
#     #         el8 = wait.until(
#     #             EC.element_to_be_clickable(
#     #                 (AppiumBy.ACCESSIBILITY_ID, "checkBox")
#     #             )
#     #         )
#     #         el8.click()
#     #
#     #         el9 = wait.until(
#     #             EC.element_to_be_clickable(
#     #                 (AppiumBy.ANDROID_UIAUTOMATOR,
#     #                  'new UiSelector().text("Sign Up").instance(1)')
#     #             )
#     #         )
#     #         el9.click()
#     #
#     #         el10 = wait.until(
#     #             EC.element_to_be_clickable(
#     #                 (AppiumBy.ANDROID_UIAUTOMATOR,
#     #                  'new UiSelector().text("Passwords must match.")')
#     #             )
#     #         )
#     #         el10.click()
#     #
#     #
#     #
#     #
#     #
#     #
#     # def test_KB_KBM_Mult_GM_536_288(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Don’t have an account? SignUp")')
#     #         )
#     #     )
#     #     el1.click()
#     #
#     #     el2 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el2.send_keys("Maheshh")
#     #
#     #     el3 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el3.send_keys("A")
#     #
#     #     el4 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(2)')
#     #         )
#     #     )
#     #     el4.send_keys("Maheshh")
#     #
#     #     el5 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(3)')
#     #         )
#     #     )
#     #     el5.send_keys("maheshh@mailinator.com")
#     #
#     #     el6 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(4)')
#     #         )
#     #     )
#     #     el6.send_keys("Test")
#     #
#     #     el9 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(5)')
#     #         )
#     #     )
#     #     el9.send_keys("Test")
#     #
#     #     el10 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ACCESSIBILITY_ID, "checkBox")
#     #         )
#     #     )
#     #     el10.click()
#     #
#     #     el11 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Sign Up").instance(1)')
#     #         )
#     #     )
#     #     el11.click()
#     #
#     #     el12 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Password must be at least 8 characters")')
#     #         )
#     #     )
#     #     el12.click()
#     #
#     #
#     #
#     # def test_KB_KBM_Invi_GM_361_240(self, mobile_v2):
#     #             self.driver = mobile_v2
#     #             wait = WebDriverWait(self.driver, 30)
#     #
#     #             el1 = wait.until(
#     #                 EC.presence_of_element_located(
#     #                     (AppiumBy.ANDROID_UIAUTOMATOR,
#     #                      'new UiSelector().className("android.widget.EditText").instance(0)')
#     #                 )
#     #             )
#     #             el1.send_keys("alberto")
#     #
#     #             el2 = wait.until(
#     #                 EC.presence_of_element_located(
#     #                     (AppiumBy.ANDROID_UIAUTOMATOR,
#     #                      'new UiSelector().className("android.widget.EditText").instance(1)')
#     #                 )
#     #             )
#     #             el2.send_keys("Test@123")
#     #
#     #             el3 = wait.until(
#     #                 EC.element_to_be_clickable(
#     #                     (AppiumBy.ANDROID_UIAUTOMATOR,
#     #                      'new UiSelector().text("Sign In").instance(1)')
#     #                 )
#     #             )
#     #             el3.click()
#     #
#     #             el4 = wait.until(
#     #                 EC.element_to_be_clickable(
#     #                     (AppiumBy.ANDROID_UIAUTOMATOR,
#     #                      'new UiSelector().text("Now")')
#     #                 )
#     #             )
#     #             el4.click()
#     #
#     # def test_KB_KBM_Meet_GM_164_301(self, mobile_v2):
#     #         self.driver = mobile_v2
#     #         wait = WebDriverWait(self.driver, 30)
#     #
#     #         el1 = wait.until(
#     #             EC.presence_of_element_located(
#     #                 (AppiumBy.ANDROID_UIAUTOMATOR,
#     #                  'new UiSelector().className("android.widget.EditText").instance(0)')
#     #             )
#     #         )
#     #         el1.send_keys("alberto")
#     #
#     #
#     #         el2 = wait.until(
#     #             EC.presence_of_element_located(
#     #                 (AppiumBy.ANDROID_UIAUTOMATOR,
#     #                  'new UiSelector().className("android.widget.EditText").instance(1)')
#     #             )
#     #         )
#     #         el2.send_keys("Test@123")
#     #
#     #         el3 = wait.until(
#     #             EC.element_to_be_clickable(
#     #                 (AppiumBy.ANDROID_UIAUTOMATOR,
#     #                  'new UiSelector().text("Sign In").instance(1)')
#     #             )
#     #         )
#     #         el3.click()
#     #
#     #         el4 = wait.until(
#     #             EC.element_to_be_clickable(
#     #                 (AppiumBy.ANDROID_UIAUTOMATOR,
#     #                  'new UiSelector().className("android.view.View").instance(28)')
#     #             )
#     #         )
#     #         el4.click()
#     #
#     #         el5 = wait.until(
#     #             EC.element_to_be_clickable(
#     #                 (AppiumBy.ANDROID_UIAUTOMATOR,
#     #                  'new UiSelector().text("v1.0.1.13")')
#     #             )
#     #         )
#     #         el5.click()
#     #
#     # def test_KB_KBM_Reco_GM_705_336(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #     e1 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     e1.send_keys("alberto")
#     #
#     #     e2 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     e2.send_keys("Test@123")
#     #
#     #     e3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Sign In").instance(1)')
#     #         )
#     #     )
#     #     e3.click()
#     #
#     #     e4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(25)')
#     #         )
#     #     )
#     #     e4.click()
#     #
#     #     e5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().description("more").instance(0)')
#     #         )
#     #     )
#     #     e5.click()
#     #
#     #     e6 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.CLASS_NAME, "android.widget.TextView")
#     #         )
#     #     )
#     #     e6.click()
#     #
#     #     e7 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Delete")')
#     #         )
#     #     )
#     #     e7.click()
#     #
#     # # def test_KB_KBM_Forg_KBM_14_23(self, mobile_v2):
#     # #     self.driver = mobile_v2
#     # #     wait = WebDriverWait(self.driver, 30)
#     # #
#     # #     el5 = wait.until(
#     # #         EC.element_to_be_clickable(
#     # #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     # #              'new UiSelector().text("Forgot Password?")')
#     # #         )
#     # #     )
#     # #     el5.click()
#     # #
#     # #     el6 = wait.until(
#     # #         EC.element_to_be_clickable(
#     # #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     # #              'new UiSelector().className("android.view.View").instance(1)')
#     # #         )
#     # #     )
#     # #     el6.click()
#     # #
#     # #     el7 = wait.until(
#     # #         EC.element_to_be_clickable(
#     # #             (AppiumBy.CLASS_NAME, "android.widget.EditText")
#     # #         )
#     # #     )
#     # #     el7.send_keys("alberto@mailinator.com")
#     # #
#     # #     el8 = wait.until(
#     # #         EC.element_to_be_clickable(
#     # #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     # #              'new UiSelector().text("Send OTP")')
#     # #         )
#     # #     )
#     # #     el8.click()
#     # #
#     # #     el9 = wait.until(
#     # #         EC.element_to_be_clickable(
#     # #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     # #              'new UiSelector().className("android.view.View").instance(2)')
#     # #         )
#     # #     )
#     # #     el9.click()
#     # #
#     # #     el10 = wait.until(
#     # #         EC.element_to_be_clickable(
#     # #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     # #              'new UiSelector().className("android.view.View").instance(1)')
#     # #         )
#     # #     )
#     # #     el10.click()
#     # #     el10.click()
#     # #
#     # #     el11 = wait.until(
#     # #         EC.presence_of_element_located(
#     # #             (AppiumBy.CLASS_NAME, "android.widget.EditText")
#     # #         )
#     # #     )
#     # #     el11.send_keys("1981")
#     # #
#     # #     el12 = wait.until(
#     # #         EC.element_to_be_clickable(
#     # #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     # #              'new UiSelector().text("Verify")')
#     # #         )
#     # #     )
#     # #     el12.click()
#     # #
#     # #     el13 = wait.until(
#     # #         EC.element_to_be_clickable(
#     # #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     # #              'new UiSelector().text("OTP expired")')
#     # #         )
#     # #     )
#     # #     el13.click()
#     # #
#     #
#     # def test_KB_KBM_Rese_KBM_16_32(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Forgot Password?")')
#     #         )
#     #     )
#     #     el1.click()
#     #
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.CLASS_NAME, "android.widget.EditText")
#     #         )
#     #     )
#     #     el2.send_keys("alberto@mailinator.com")
#     #
#     #     # Click Send OTP
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Send OTP")')
#     #         )
#     #     )
#     #     el3.click()
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.CLASS_NAME, "android.widget.EditText")
#     #         )
#     #     )
#     #     el4.send_keys("4634")
#     #
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(2)')
#     #         )
#     #     )
#     #     el5.click()
#     #
#     #     el6 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el6.send_keys("Pass@123")
#     #
#     #     el7 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el7.send_keys("Pass@12")
#     #
#     #     el8 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Update Password")')
#     #         )
#     #     )
#     #     el8.click()
#     #
#     #     el9 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Passwords must match.")')
#     #         )
#     #     )
#     #     el9.click()
#     #
#     # def test_KB_KBM_Cale_GM_101_119(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el1.send_keys("Kaviyaa")
#     #
#     #     # Enter Password
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el2.send_keys("Test@123")
#     #
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Sign In").instance(1)')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     # Click Date: 19 Nov, 2025
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("19 Nov, 2025")')
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(19)')
#     #         )
#     #     )
#     #     el5.click()
#     #
#     # def test_KB_KBM_Cale_GM_101_121(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el1.send_keys("Kaviyaa")
#     #
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el2.send_keys("Test@123")
#     #
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Sign In").instance(1)')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(1)')
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("schedule ")')
#     #         )
#     #     )
#     #     el5.click()
#     #
#     # def test_KB_KBM_Cale_GM_101_123(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #     # Enter Username
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el1.send_keys("Kaviyaa")
#     #
#     #     # Enter Password
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el2.send_keys("Test@123")
#     #
#     #     # Click Sign In
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Sign In").instance(1)')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.ImageView").instance(4)')
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(16)')
#     #         )
#     #     )
#     #     el5.click()
#     #
#     # def test_KB_KBM_Meet_GM_802_350(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #     # Enter username
#     #     el1 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el1.send_keys("alberto")
#     #
#     #     # Enter password
#     #     el2 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el2.send_keys("Test@123")
#     #
#     #     # Click Sign In
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Sign In")')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     # Click Create
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ACCESSIBILITY_ID, "Create")
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #     # Click instance(9)
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(9)')
#     #         )
#     #     )
#     #     el5.click()
#     #
#     #     # Enter email
#     #     el6 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el6.send_keys("leviskon@mailinator.com")
#     #
#     #     # Click View instance(4)
#     #     el8 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(4)')
#     #         )
#     #     )
#     #     el8.click()
#     #
#     #     # Click Schedule
#     #     el9 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Schedule")')
#     #         )
#     #     )
#     #     el9.click()
#     #
#     #     # Click "Title is required"
#     #     el10 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Title is required")')
#     #         )
#     #     )
#     #     el10.click()
#     # #
#     # # def test_KB_KBM_Meet_GM_802_349(self, mobile_v2):
#     # #     self.driver = mobile_v2
#     # #     wait = WebDriverWait(self.driver, 30)
#     # #
#     # #     # Enter username
#     # #     el1 = wait.until(
#     # #         EC.presence_of_element_located(
#     # #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     # #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     # #         )
#     # #     )
#     # #     el1.send_keys("alberto")
#     # #
#     # #     # Enter password
#     # #     el2 = wait.until(
#     # #         EC.presence_of_element_located(
#     # #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     # #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     # #         )
#     # #     )
#     # #     el2.send_keys("Test@123")
#     # #
#     # #     # Click "Sign In"
#     # #     el3 = wait.until(
#     # #         EC.element_to_be_clickable(
#     # #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     # #              'new UiSelector().text("Sign In").instance(1)')
#     # #         )
#     # #     )
#     # #     el3.click()
#     # #
#     # #     # Click "Create"
#     # #     el4 = wait.until(
#     # #         EC.element_to_be_clickable(
#     # #             (AppiumBy.ACCESSIBILITY_ID, "Create")
#     # #         )
#     # #     )
#     # #     el4.click()
#     # #
#     # #     # Click view instance(9)
#     # #     el5 = wait.until(
#     # #         EC.element_to_be_clickable(
#     # #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     # #              'new UiSelector().className("android.view.View").instance(9)')
#     # #         )
#     # #     )
#     # #     el5.click()
#     # #
#     # #     # Enter meeting title
#     # #     el6 = wait.until(
#     # #         EC.presence_of_element_located(
#     # #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     # #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     # #         )
#     # #     )
#     # #     el6.send_keys("user input")
#     # #
#     # #     # Enter email
#     # #     el7 = wait.until(
#     # #         EC.presence_of_element_located(
#     # #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     # #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     # #         )
#     # #     )
#     # #     el7.send_keys("leviskon@mailinator.com")
#     # #
#     # #     # ScrollView click
#     # #     el8 = wait.until(
#     # #         EC.presence_of_element_located(
#     # #             (AppiumBy.CLASS_NAME, "android.widget.ScrollView")
#     # #         )
#     # #     )
#     # #     el8.click()
#     # #
#     # #     # Click "Schedule"
#     # #     el9 = wait.until(
#     # #         EC.element_to_be_clickable(
#     # #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     # #              'new UiSelector().text("Schedule")')
#     # #         )
#     # #     )
#     # #     el9.click()
#     # #
#     # #     # e10 – Verify success message (toast or text)
#     # #     el10 = wait.until(
#     # #         EC.presence_of_element_located(
#     # #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     # #              'new UiSelector().textContains("Meeting has been created successfully!")')
#     # #         )
#     # #     )
#     # #     el10.click()
#     #
#     # def test_KB_KBM_Reco_GM_711_354(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #     # Enter username
#     #     el1 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el1.send_keys("alberto")
#     #
#     #     # Enter password
#     #     el2 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el2.send_keys("Test@123")
#     #
#     #     # Click "Sign In"
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Sign In").instance(1)')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     # Click the meeting time slot "5:00"
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("5:00")')
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #     # Click the ImageView (instance 4)
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.ImageView").instance(4)')
#     #         )
#     #     )
#     #     el5.click()
#     #
#     #     # Click "Edit Meeting"
#     #     el6 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Edit Meeting")')
#     #         )
#     #     )
#     #     el6.click()
#     #
#     #     # Edit meeting title
#     #     el7 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("tee")')
#     #         )
#     #     )
#     #     el7.send_keys("testing")
#     #
#     #     # Click "Update"
#     #     el8 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Update")')
#     #         )
#     #     )
#     #     el8.click()
#     #
#     # def test_KB_KBM_Reco_GM_711_355(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #     # Enter username
#     #     el1 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el1.send_keys("alberto")
#     #
#     #     # Enter password
#     #     el2 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el2.send_keys("Test@123")
#     #
#     #     # Click "Sign In"
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Sign In").instance(1)')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     # Click ImageView (instance 7)
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.ImageView").instance(7)')
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #     # Click "Edit Meeting"
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Edit Meeting")')
#     #         )
#     #     )
#     #     el5.click()
#     #
#     #     # Click view instance (27)
#     #     el6 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(27)')
#     #         )
#     #     )
#     #     el6.click()
#     #
#     #     # Click "Title is required"
#     #     el7 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Title is required")')
#     #         )
#     #     )
#     #     el7.click()
#     #
#     # def test_KB_KBM_User_GM_916_439(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Trouble Logging In?")')
#     #         )
#     #     )
#     #     el1.click()
#     #
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(1)')
#     #         )
#     #     )
#     #     el2.click()
#     #
#     # def test_KB_KBM_User_GM_916_459(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Trouble Logging In?")')
#     #         )
#     #     )
#     #     el1.click()
#     #
#     #     el2 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.CLASS_NAME, "android.widget.EditText")
#     #         )
#     #     )
#     #     el2.send_keys("alberto@mailinator.com")
#     #
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.Button").instance(1)')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.CLASS_NAME, "android.widget.Button")
#     #         )
#     #     )
#     #     el4.click()
#     #
#     # def test_TR_KATON_Meetings_HostControls_373(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #
#     #     el1 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el1.send_keys("alberto")
#     #
#     #
#     #     el2 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el2.send_keys("Test@123")
#     #
#     #
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Sign In").instance(1)')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     # Create button
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ACCESSIBILITY_ID, "Create")
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(9)')
#     #         )
#     #     )
#     #     el5.click()
#     #
#     #
#     #     el6 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.XPATH,
#     #              "//android.widget.ScrollView/android.widget.EditText[1]")
#     #         )
#     #     )
#     #     el6.send_keys("test")
#     #
#     #
#     #     el7 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el7.send_keys("leviskon@mailinator.com")
#     #
#     #
#     #     el8 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(4)')
#     #         )
#     #     )
#     #     el8.click()
#     #
#     #     el9 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Enable Host Controls")')
#     #         )
#     #     )
#     #     el9.click()
#     #
#     #     el10 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.CLASS_NAME, "android.widget.ScrollView")
#     #         )
#     #     )
#     #     el10.click()
#     #
#     # def test_TR_KATON_Meetings_HostControls_374(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #     el1 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el1.send_keys("alberto")
#     #
#     #     el2 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el2.send_keys("Test@123")
#     #
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Sign In").instance(1)')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     # Create button
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ACCESSIBILITY_ID, "Create")
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(9)')
#     #         )
#     #     )
#     #     el5.click()
#     #
#     #     el6 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.XPATH,
#     #              "//android.widget.ScrollView/android.widget.EditText[1]")
#     #         )
#     #     )
#     #     el6.send_keys("test")
#     #
#     #     el7 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el7.send_keys("leviskon@mailinator.com")
#     #
#     #     el8 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(4)')
#     #         )
#     #     )
#     #     el8.click()
#     #
#     #     el9 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Enable Host Controls")')
#     #         )
#     #     )
#     #     el9.click()
#     #
#     #     el10 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.CLASS_NAME, "android.widget.ScrollView")
#     #         )
#     #     )
#     #     el10.click()
#     #
#     # def test_TR_KATON_Meetings_Recurrence_383(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #     el1 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el1.send_keys("alberto")
#     #
#     #     # Password field
#     #     el2 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el2.send_keys("Test@123")
#     #
#     #
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Sign In").instance(1)')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ACCESSIBILITY_ID, "Create")
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(9)')
#     #         )
#     #     )
#     #     el5.click()
#     #
#     #
#     #     el6 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el6.send_keys("check")
#     #
#     #
#     #     el7 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el7.send_keys("leviskon@mailinator.com")
#     #
#     #
#     #     el8 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(4)')
#     #         )
#     #     )
#     #     el8.click()
#     #
#     #
#     #     el9 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().description("checkBox").instance(0)')
#     #         )
#     #     )
#     #     el9.click()
#     #
#     #
#     #     el9.click()
#     #
#     #
#     #     el10 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().description("checkBox").instance(0)')
#     #         )
#     #     )
#     #     el10.click()
#     #
#     # def test_TR_KATON_Meetings_Recurrence_384(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #     el1 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el1.send_keys("alberto")
#     #
#     #     el2 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el2.send_keys("Test@123")
#     #
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Sign In").instance(1)')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ACCESSIBILITY_ID, "Create")
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(9)')
#     #         )
#     #     )
#     #     el5.click()
#     #
#     #     el6 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el6.send_keys("check")
#     #
#     #     el7 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el7.send_keys("leviskon@mailinator.com")
#     #
#     #     el8 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(4)')
#     #         )
#     #     )
#     #     el8.click()
#     #
#     #
#     #     el9 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().description("checkBox").instance(0)')
#     #         )
#     #     )
#     #     el9.click()
#     #     el9.click()
#     #
#     #     el10 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().description("checkBox").instance(0)')
#     #         )
#     #     )
#     #     el10.click()
#     #
#     #
#     #     el11 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.Button").instance(4)')
#     #         )
#     #     )
#     #     el11.click()
#     #
#     #
#     #     el12 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(4)')
#     #         )
#     #     )
#     #     el12.click()
#     #
#     #     el13 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.Button").instance(4)')
#     #         )
#     #     )
#     #     el13.click()
#     #
#     #
#     #     el14 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(4)')
#     #         )
#     #     )
#     #     el14.click()
#     #
#     # def test_TR_KATON_Authentication_SignUp_425(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Don’t have an account? SignUp")')
#     #         )
#     #     )
#     #     el1.click()
#     #
#     #     el3 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el3.send_keys(
#     #         "wertyoytreqwertyuioiyertyuhvctuhgfdsertyuijhgfdswertyuikjvcdsawertyuikjbvcxzawertyuiokjhgfdsertasdftytrew"
#     #     )
#     #     el3.send_keys(
#     #         "wertyoytreqwertyuioiyertyuhvctuhgfdsertyuijhgfdswertyuikjvcdsawertyuikjbvcxzawertyuiokjhgfdsertasdftytrew"
#     #     )
#     #
#     #     el5 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el5.send_keys("a")
#     #
#     #
#     #     el6 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el6.send_keys("Priyaa")
#     #
#     #
#     #     el7 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("a")')
#     #         )
#     #     )
#     #     el7.send_keys(
#     #         "wertyuiojhbhjijndksoksklsiduygfvwbnwkedifuygdvbwnkeiuygfdvbqnkwodifugvdsbnmkodfiuygv "
#     #     )
#     #
#     #
#     #     el8 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     long_text = (
#     #         "rtyuihgfdsdfgkmkouyfdszxcvhjmnbvcxdrtyuikjnbvcxdrtyuijbvcxertyujnbcxesxfyujhbvcxsertyuijnbvcxsertyujbvcdsertyujm "
#     #         "rtyytrtyhjkkjikn"
#     #     )
#     #     el8.send_keys(long_text)
#     #     el8.send_keys(long_text)
#     #
#     # def test_TR_KATON_Authentication_SignUp_427(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #     el1 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el1.send_keys("alberto")
#     #
#     #     el2 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el2.send_keys("Test@123")
#     #
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(3)')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(36)')
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(2)')
#     #         )
#     #     )
#     #     el5.click()
#     #
#     #     el6 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.Button").instance(1)')
#     #         )
#     #     )
#     #     el6.click()
#     #
#     #
#     #     el7 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("alberto").instance(0)')
#     #         )
#     #     )
#     #     el7.send_keys(
#     #         "styuioihgiuhojsidhghwidjjowdbiwvdiwhdhiijwdedfguiwehdghiwhdoihwbedfocjb"
#     #     )
#     #
#     #
#     #     el8 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el8.send_keys("alberto")
#     #
#     #     el10 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el10.send_keys("a")
#     #
#     # def test_TR_KATON_Meetings_Recurrence_385(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #     el1 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el1.send_keys("alberto")
#     #
#     #     # Password
#     #     el2 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el2.send_keys("Test@123")
#     #
#     #
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Sign In").instance(1)')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ACCESSIBILITY_ID, "Create")
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Schedule Meeting")')
#     #         )
#     #     )
#     #     el5.click()
#     #
#     #     el6 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el6.send_keys("date picker")
#     #
#     #     el7 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el7.send_keys("leviskon@mailinator.com")
#     #
#     #     el8 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(4)')
#     #         )
#     #     )
#     #     el8.click()
#     #
#     #     el9 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().description("checkBox").instance(0)')
#     #         )
#     #     )
#     #     el9.click()
#     #
#     #     el10 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.Button").instance(5)')
#     #         )
#     #     )
#     #     el10.click()
#     #
#     #     for _ in range(3):
#     #         el_btn1 = wait.until(
#     #             EC.element_to_be_clickable(
#     #                 (AppiumBy.ANDROID_UIAUTOMATOR,
#     #                  'new UiSelector().className("android.widget.Button").instance(1)')
#     #             )
#     #         )
#     #         el_btn1.click()
#     #
#     #     el14 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.Button").instance(16)')
#     #         )
#     #     )
#     #     el14.click()
#     #
#     #
#     #     el15 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.Button").instance(35)')
#     #         )
#     #     )
#     #     el15.click()
#     #
#     # def test_KB_KBM_Meet_GM_912_376(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #
#     #     el1 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el1.send_keys("alberto")
#     #
#     #     # Password
#     #     el2 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el2.send_keys("Test@123")
#     #
#     #     # Sign In
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(3)')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     # 3-dots menu
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.ImageView").instance(4)')
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #     # Copy Meeting Code
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Copy Meeting Code")')
#     #         )
#     #     )
#     #     el5.click()
#     #
#     #     # Success Toast Message
#     #     el6 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Meeting Code copied to clipboard")')
#     #         )
#     #     )
#     #
#     # def test_KB_KBM_Sign_KBM_04_11(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el1.send_keys("alberto")
#     #
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el2.send_keys("Test@123")
#     #
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Sign In").instance(1)')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     # def test_KB_KBM_Sign_KBM_04_6(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.CLASS_NAME, "android.widget.ScrollView")
#     #         )
#     #     )
#     #     el1.click()
#     #
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Sign In").instance(0)')
#     #         )
#     #     )
#     #     el2.click()
#     #
#     # def test_KB_KBM_Sign_KBM_04_7(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el1.send_keys("Test@1234")
#     #
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(3)')
#     #         )
#     #     )
#     #     el2.click()
#     #
#     #     el3 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Username / Email is required")')
#     #         )
#     #     )
#     #
#     # def test_KB_KBM_Forg_KBM_14_15(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.CLASS_NAME, "android.widget.ScrollView")
#     #         )
#     #     )
#     #     el1.click()
#     #
#     #
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Forgot Username / Password?")')
#     #         )
#     #     )
#     #     el2.click()
#     #
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(1)')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     el4 = wait.until(
#     #         EC.presence_of_element_located(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Forgot Username / Password")')
#     #         )
#     #     )
#     #
#     # def test_KB_KBM_Forg_KBM_14_16(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Forgot Username / Password?")')
#     #         )
#     #     )
#     #     el1.click()
#     #
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.CLASS_NAME, "android.widget.EditText")
#     #         )
#     #     )
#     #     el2.send_keys("priya@mailinator.com")
#     #
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.Button").instance(0)')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     # def test_KB_KBM_Forg_KBM_14_20(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #     # Click on "Forgot Username / Password?"
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Forgot Username / Password?")')
#     #         )
#     #     )
#     #     el1.click()
#     #
#     #     # Enter registered email address
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.CLASS_NAME, "android.widget.EditText")
#     #         )
#     #     )
#     #     el2.send_keys("priya@mailinator.com")
#     #
#     #     # Click on Submit / Continue button
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.Button").instance(0)')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     # Enter OTP
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.CLASS_NAME, "android.widget.EditText")
#     #         )
#     #     )
#     #     el5.send_keys("5624")
#     #
#     # def test_KB_KBM_Forg_KBM_14_26(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #     # Click on "Forgot Username / Password?"
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Forgot Username / Password?")')
#     #         )
#     #     )
#     #     el1.click()
#     #
#     #     # Enter registered email address
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.CLASS_NAME, "android.widget.EditText")
#     #         )
#     #     )
#     #     el2.send_keys("priya@mailinator.com")
#     #
#     #     # Click on Submit / Continue button
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.Button").instance(0)')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     # Enter OTP
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.CLASS_NAME, "android.widget.EditText")
#     #         )
#     #     )
#     #     el4.send_keys("4594")
#     #
#     #     # Click Verify button
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Verify")')
#     #         )
#     #     )
#     #     el5.click()
#     #
#     #     # Enter New Password
#     #     el6 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el6.send_keys("Test@1234")
#     #
#     #     # Enter Confirm Password
#     #     el7 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el7.send_keys("Test@1234")
#     #
#     #     # Click Update Password
#     #     el8 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Update Password")')
#     #         )
#     #     )
#     #     el8.click()
#     #
#     # def test_KB_KBM_Rese_KBM_16_27(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #     # Click on "Forgot Username / Password?"
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Forgot Username / Password?")')
#     #         )
#     #     )
#     #     el1.click()
#     #
#     #     # Enter registered email address
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.CLASS_NAME, "android.widget.EditText")
#     #         )
#     #     )
#     #     el2.send_keys("priya@mailinator.com")
#     #
#     #     # Click on Submit / Continue button
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.Button").instance(0)')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     # Enter OTP
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.CLASS_NAME, "android.widget.EditText")
#     #         )
#     #     )
#     #     el4.send_keys("5624")
#     #
#     #     # Click Verify button
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Verify")')
#     #         )
#     #     )
#     #     el5.click()
#     #
#     #     # Enter New Password
#     #     el6 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el6.send_keys("Test@1234")
#     #
#     #     # Enter Confirm Password
#     #     el7 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el7.send_keys("Test@1234")
#     #
#     #     # Click Update Password
#     #     el8 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Update Password")')
#     #         )
#     #     )
#     #     el8.click()
#     #
#     # def test_KB_KBM_Rese_KBM_16_32(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Forgot Username / Password?")')
#     #         )
#     #     )
#     #     el1.click()
#     #
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.CLASS_NAME, "android.widget.EditText")
#     #         )
#     #     )
#     #     el2.send_keys("priya@mailinator.com")
#     #
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.XPATH,
#     #              "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.widget.Button")
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.CLASS_NAME, "android.widget.EditText")
#     #         )
#     #     )
#     #     el4.send_keys("2292")
#     #
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(2)')
#     #         )
#     #     )
#     #     el5.click()
#     #
#     #     el6 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el6.send_keys("Test@12345")
#     #
#     #     el7 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el7.send_keys("Test@123456")
#     #
#     #     el8 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(6)')
#     #         )
#     #     )
#     #     el8.click()
#     #
#     #     el9 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Passwords must match.")')
#     #         )
#     #     )
#     #     el9.click()
#     #
#     #
#     # def test_KB_KBM_Sign_KBM_91_36(self, mobile_v2):
#     #         self.driver = mobile_v2
#     #         wait = WebDriverWait(self.driver, 30)
#     #
#     #         # Enter Username
#     #         el1 = wait.until(
#     #             EC.element_to_be_clickable(
#     #                 (AppiumBy.ANDROID_UIAUTOMATOR,
#     #                  'new UiSelector().className("android.widget.EditText").instance(0)')
#     #             )
#     #         )
#     #         el1.send_keys("Priya")
#     #
#     #         # Enter Passwor
#     #         el2 = wait.until(
#     #             EC.element_to_be_clickable(
#     #                 (AppiumBy.ANDROID_UIAUTOMATOR,
#     #                  'new UiSelector().className("android.widget.EditText").instance(1)')
#     #             )
#     #         )
#     #         el2.send_keys("Test@1234")
#     #
#     #         # Click Sign In
#     #         el3 = wait.until(
#     #             EC.element_to_be_clickable(
#     #                 (AppiumBy.ANDROID_UIAUTOMATOR,
#     #                  'new UiSelector().text("Sign In").instance(1)')
#     #             )
#     #         )
#     #         el3.click()
#     #
#     #         # Click View (instance 46)
#     #         el4 = wait.until(
#     #             EC.element_to_be_clickable(
#     #                 (AppiumBy.ANDROID_UIAUTOMATOR,
#     #                  'new UiSelector().className("android.view.View").instance(46)')
#     #             )
#     #         )
#     #         el4.click()
#     #
#     #         # Click View (instance 9)
#     #         el5 = wait.until(
#     #             EC.element_to_be_clickable(
#     #                 (AppiumBy.ANDROID_UIAUTOMATOR,
#     #                  'new UiSelector().className("android.view.View").instance(9)')
#     #             )
#     #         )
#     #         el5.click()
#     #
#     #         # Click View (instance 3)
#     #         el6 = wait.until(
#     #             EC.element_to_be_clickable(
#     #                 (AppiumBy.ANDROID_UIAUTOMATOR,
#     #                  'new UiSelector().className("android.view.View").instance(3)')
#     #             )
#     #         )
#     #         el6.click()
#     #
#     #         # Click Sign Out
#     #         el7 = wait.until(
#     #             EC.element_to_be_clickable(
#     #                 (AppiumBy.ANDROID_UIAUTOMATOR,
#     #                  'new UiSelector().text("Sign Out")')
#     #             )
#     #         )
#     #         el7.click()
#     #
#     #         # Click ScrollView
#     #         el8 = wait.until(
#     #             EC.element_to_be_clickable(
#     #                 (AppiumBy.CLASS_NAME, "android.widget.ScrollView")
#     #             )
#     #         )
#     #         el8.click()
#     # def test_KB_KBM_Meet_GM_113_91(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #     # Enter Username
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el1.send_keys("Priya")
#     #
#     #     # Enter Password
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el2.send_keys("Test@1234")
#     #
#     #     # Click Login / Next
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(3)')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     # Click Create
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ACCESSIBILITY_ID, "Create")
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #     # Select Meeting Option
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(10)')
#     #         )
#     #     )
#     #     el5.click()
#     #
#     #     # Enter Meeting Name
#     #     el6 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el6.send_keys("test")
#     #
#     #     # Click Schedule
#     #     el7 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Schedule")')
#     #         )
#     #     )
#     #     el7.click()
#     #
#     #     # Confirm Schedule
#     #     el8 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(17)')
#     #         )
#     #     )
#     #     el8.click()
#     #
#     #     # Allow Permission (Foreground)
#     #     el9 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ID,
#     #              "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
#     #         )
#     #     )
#     #     el9.click()
#     #
#     #     # Allow Permission again (if prompted)
#     #     el10 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ID,
#     #              "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
#     #         )
#     #     )
#     #     el10.click()
#     #
#     #     el11 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Start Meeting")')
#     #         )
#     #     )
#     #     el11.click()
#     #
#     # def test_KB_KBM_Sett_GM_136_107(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #     # Enter Username
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el1.send_keys("Priya")
#     #
#     #     # Enter Password
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el2.send_keys("Test@1234")
#     #
#     #     # Click Sign In
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Sign In").instance(1)')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     # Click Settings Option
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(42)')
#     #         )
#     #     )
#     #     el4.click()
#     #
#     # def test_KB_KBM_Sett_GM_136_108(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #     # Enter Username
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el1.send_keys("Priya")
#     #
#     #     # Enter Password
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el2.send_keys("Test@1234")
#     #
#     #     # Click Sign In
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Sign In").instance(1)')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     # Click Settings
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(42)')
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #     # Click Sub Option
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(1)')
#     #         )
#     #     )
#     #     el5.click()
#     #
#     # def test_KB_KBM_Cale_GM_101_119(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #     # Enter Username
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el1.send_keys("Priya")
#     #
#     #     # Enter Password
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el2.send_keys("Test@1234")
#     #
#     #     # Click Login / Next
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(3)')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     # Open Calendar
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(12)')
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #     # Select Time 6:00
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("6:00")')
#     #         )
#     #     )
#     #     el5.click()
#     #     el5.click()
#     #
#     # def test_KB_KBM_Cale_GM_101_121(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #     # Enter Username
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el1.send_keys("Priya")
#     #
#     #     # Enter Password
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el2.send_keys("Test@1234")
#     #
#     #     # Click Sign In
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Sign In").instance(1)')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     # Select Time Slot
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("06:15 PM - 06:30 PM").instance(0)')
#     #         )
#     #     )
#     #     el4.click()
#     #
#     # def test_KB_KBM_Cale_GM_103_124(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #     # Enter Username
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el1.send_keys("Priya")
#     #
#     #     # Enter Password
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el2.send_keys("Test@1234")
#     #
#     #     # Click Sign In
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Sign In").instance(1)')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     # Open Calendar Icon
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.ImageView").instance(3)')
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #     # Click Today
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Today")')
#     #         )
#     #     )
#     #     el5.click()
#     #
#     #
#     #     el6 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("28 Jan, 2026")')
#     #         )
#     #     )
#     #     el6.click()
#     #
#     # def test_KB_KBM_Meet_GM_146_152(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #     # Enter Username
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el1.send_keys("Priya")
#     #
#     #     # Enter Password
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el2.send_keys("Test@1234")
#     #
#     #     # Click Sign In
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Sign In").instance(1)')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     # Open Settings
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(42)')
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ACCESSIBILITY_ID, "Push Notification")
#     #         )
#     #     )
#     #     el5.click()
#     #
#     # def test_KB_KBM_Meet_KBM_49_47(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #     # Enter Username
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el1.send_keys("Priya")
#     #
#     #     # Enter Password
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el2.send_keys("Test@1234")
#     #
#     #     # Click Sign In
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Sign In").instance(1)')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     # Click View (post login)
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(33)')
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #     # Click another View
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(9)')
#     #         )
#     #     )
#     #     el5.click()
#     #
#     #     # Allow permission – foreground only (1st time)
#     #     el6 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ID,
#     #              "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
#     #         )
#     #     )
#     #     el6.click()
#     #
#     #     # Allow permission – foreground only (2nd time)
#     #     el7 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ID,
#     #              "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
#     #         )
#     #     )
#     #     el7.click()
#     #
#     #     # Click Start Meeting
#     #     el8 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Start Meeting")')
#     #         )
#     #     )
#     #     el8.click()
#     #
#     #     # Click View (instance 23)
#     #     el9 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(23)')
#     #         )
#     #     )
#     #     el9.click()
#     #
#     #     # Click View (instance 23) again
#     #     el10 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(23)')
#     #         )
#     #     )
#     #     el10.click()
#     #
#     #     # Final View click
#     #     el11 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(3)')
#     #         )
#     #     )
#     #     el11.click()
#     #
#     # def test_KB_KBM_Sign_KBM_91_38(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #     # Enter Username
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el1.send_keys("Priya")
#     #
#     #     # Enter Passwor
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el2.send_keys("Test@1234")
#     #
#     #     # Click Sign In
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Sign In").instance(1)')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     # Click View (instance 46)
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(46)')
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #     # Click View (instance 9)
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(9)')
#     #         )
#     #     )
#     #     el5.click()
#     #
#     #     # Click View (instance 3)
#     #     el6 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(3)')
#     #         )
#     #     )
#     #     el6.click()
#     #
#     #     # Click Sign Out
#     #     el7 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Sign Out")')
#     #         )
#     #     )
#     #     el7.click()
#     #
#     #     # Click ScrollView
#     #     el8 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.CLASS_NAME, "android.widget.ScrollView")
#     #         )
#     #     )
#     #     el8.click()
#     #
#     # def test_KB_KBM_Home_KBM_18_40(self, mobile_v2):
#     #     self.driver = mobile_v2
#     #     wait = WebDriverWait(self.driver, 30)
#     #
#     #     # Enter Username
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el1.send_keys("Priya")
#     #
#     #     # Enter Password
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el2.send_keys("Test@1234")
#     #
#     #     # Click View (instance 8)
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(8)')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     # Click View (instance 3)
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(3)')
#     #         )
#     #     )
#     #     el4.click()
#     #
#     # def test_KB_KBM_Sett_GM_148_147(self, mobile_v2):
#     #     driver = mobile_v2
#     #     wait = WebDriverWait(driver, 30)
#     #
#     #     # Username
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el1.send_keys("Priya")
#     #
#     #     # Password
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el2.send_keys("Test@1234")
#     #
#     #     # Sign In
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Sign In").instance(1)')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     # View – instance 46
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(46)')
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #     # Button click
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.CLASS_NAME, "android.widget.Button")
#     #         )
#     #     )
#     #     el5.click()
#     #
#     #     # View – instance 47
#     #     el6 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(47)')
#     #         )
#     #     )
#     #     el6.click()
#     #
#     #     # View – instance 6
#     #     el7 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(6)')
#     #         )
#     #     )
#     #     el7.click()
#     #
#     #     # View – instance 2
#     #     el8 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(2)')
#     #         )
#     #     )
#     #     el8.click()
#     #
#     # def test_KB_KBM_Sear_GM_97_157(self, mobile_v2):
#     #     driver = mobile_v2
#     #     wait = WebDriverWait(driver, 30)
#     #
#     #     # Enter Username
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(0)')
#     #         )
#     #     )
#     #     el1.send_keys("Priya")
#     #
#     #     # Enter Password
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.widget.EditText").instance(1)')
#     #         )
#     #     )
#     #     el2.send_keys("Test@1234")
#     #
#     #     # Click Sign In
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().text("Sign In").instance(1)')
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     # Click Search (accessibility id)
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ACCESSIBILITY_ID, "Search")
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #     # Enter search text
#     #     el6 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.CLASS_NAME, "android.widget.EditText")
#     #         )
#     #     )
#     #     el6.send_keys("check")
#     #
#     #     # Click View – instance 4
#     #     el7 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(4)')
#     #         )
#     #     )
#     #     el7.click()
#     #
#     #     # Click View – instance 2
#     #     el8 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.ANDROID_UIAUTOMATOR,
#     #              'new UiSelector().className("android.view.View").instance(2)')
#     #         )
#     #     )
#     #     el8.click()
#
#     def test_KBM_04__Signin_Signin_6(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#         el1 = wait.until(
#             EC.element_to_be_clickable(
#                 (AppiumBy.ANDROID_UIAUTOMATOR,
#                  'new UiSelector().text("Forgot Username / Password?")')
#             )
#         )
#         el1.click()
#
#         el2 = wait.until(
#             EC.element_to_be_clickable(
#                 (AppiumBy.CLASS_NAME, "android.widget.ScrollView")
#             )
#         )
#         el2.click()
#
#     def test_KBM_04__Signin_Signin_11(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#         el1 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(0)'
#                 )
#             )
#         )
#         el1.send_keys("sathees")
#
#         el2 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(1)'
#                 )
#             )
#         )
#         el2.send_keys("test@123")
#
#         el3 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(7)'
#                 )
#             )
#         )
#         el3.click()
#
#     def test_KBM_14__Forgot_Password_OTP_16(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#         el1 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().text("Forgot Username / Password?")'
#                 )
#             )
#         )
#         el1.click()
#
#         el2 = wait.until(
#             EC.element_to_be_clickable(
#                 (AppiumBy.CLASS_NAME, "android.widget.EditText")
#             )
#         )
#         el2.send_keys("rakesh@mailinator.com")
#
#         el3 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().text("Send Code")'
#                 )
#             )
#         )
#         el3.click()
#
#         el4 = wait.until(
#             EC.element_to_be_clickable(
#                 (AppiumBy.CLASS_NAME, "android.widget.ScrollView")
#             )
#         )
#         el4.click()
#
#     def test_KBM_91__Signout_settings_36(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#         el1 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(0)'
#                 )
#             )
#         )
#         el1.send_keys("sathees")
#
#         el2 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(1)'
#                 )
#             )
#         )
#         el2.send_keys("test@123")
#
#         el3 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(7)'
#                 )
#             )
#         )
#         el3.click()
#
#         el4 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(13)'
#                 )
#             )
#         )
#         el4.click()
#
#         el5 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().text("Sign Out")'
#                 )
#             )
#         )
#         el5.click()
#
#         el6 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(3)'
#                 )
#             )
#         )
#         el6.click()
#
#         el7 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(3)'
#                 )
#             )
#         )
#         el7.click()
#
#     def test_GM_136__Settings_Account_104(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#         el1 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(0)'
#                 )
#             )
#         )
#         el1.send_keys("sathees")
#
#         el2 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(1)'
#                 )
#             )
#         )
#         el2.send_keys("test@123")
#
#         el3 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(7)'
#                 )
#             )
#         )
#         el3.click()
#
#         el4 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(13)'
#                 )
#             )
#         )
#         el4.click()
#
#         el5 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(38)'
#                 )
#             )
#         )
#         el5.click()
#
#     def test_GM_687__Settings_AppVersion_230(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#         el1 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(0)'
#                 )
#             )
#         )
#         el1.send_keys("sathees")
#
#         el2 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(1)'
#                 )
#             )
#         )
#         el2.send_keys("test@123")
#
#         el3 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(7)'
#                 )
#             )
#         )
#         el3.click()
#
#         el4 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(2)'
#                 )
#             )
#         )
#         el4.click()
#
#         el5 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(13)'
#                 )
#             )
#         )
#         el5.click()
#
#         el6 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().text("v2.0.6.5")'
#                 )
#             )
#         )
#         el6.click()
#
#     def test_KBM_49__Meeting_screen_End_call_42(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#         el1 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(0)'
#                 )
#             )
#         )
#         el1.send_keys("sathees")
#
#         el2 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(1)'
#                 )
#             )
#         )
#         el2.send_keys("test@123")
#
#         el3 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(7)'
#                 )
#             )
#         )
#         el3.click()
#
#         el4 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(74)'
#                 )
#             )
#         )
#         el4.click()
#
#         el5 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().text("Instant Meeting")'
#                 )
#             )
#         )
#         el5.click()
#
#         el6 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ID,
#                     "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
#                 )
#             )
#         )
#         el6.click()
#
#         el7 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ID,
#                     "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
#                 )
#             )
#         )
#         el7.click()
#
#         el8 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(29)'
#                 )
#             )
#         )
#         el8.click()
#
#     # def test_KBM_49__Meeting_screen_End_call_43(self, mobile_v2):
#     #     driver = mobile_v2
#     #     wait = WebDriverWait(driver, 30)
#     #
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.widget.EditText").instance(0)'
#     #             )
#     #         )
#     #     )
#     #     el1.send_keys("sathees")
#     #
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.widget.EditText").instance(1)'
#     #             )
#     #         )
#     #     )
#     #     el2.send_keys("test@123")
#     #
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(7)'
#     #             )
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(74)'
#     #             )
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().text("Instant Meeting")'
#     #             )
#     #         )
#     #     )
#     #     el5.click()
#     #
#     #     el6 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ID,
#     #                 "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
#     #             )
#     #         )
#     #     )
#     #     el6.click()
#     #
#     #     el7 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ID,
#     #                 "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
#     #             )
#     #         )
#     #     )
#     #     el7.click()
#     #
#     #     el8 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(29)'
#     #             )
#     #         )
#     #     )
#     #     el8.click()
#     #
#     #     el9 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(7)'
#     #             )
#     #         )
#     #     )
#     #     el9.click()
#     #
#     #     el10 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(7)'
#     #             )
#     #         )
#     #     )
#     #     el10.click()
#
#     def test_GM_148__Settings_Password_126(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#         el1 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(0)'
#                 )
#             )
#         )
#         el1.send_keys("sathees")
#
#         el2 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(1)'
#                 )
#             )
#         )
#         el2.send_keys("test@123")
#
#         el3 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(7)'
#                 )
#             )
#         )
#         el3.click()
#
#         el4 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(13)'
#                 )
#             )
#         )
#         el4.click()
#
#         el5 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().text("Change Password")'
#                 )
#             )
#         )
#         el5.click()
#
#         el6 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(3)'
#                 )
#             )
#         )
#         el6.click()
#
#     # def test_GM_146__Meeting_Videotitle_131(self, mobile_v2):
#     #     driver = mobile_v2
#     #     wait = WebDriverWait(driver, 30)
#     #
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.widget.EditText").instance(0)'
#     #             )
#     #         )
#     #     )
#     #     el1.send_keys("sathees")
#     #
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.widget.EditText").instance(1)'
#     #             )
#     #         )
#     #     )
#     #     el2.send_keys("test@123")
#     #
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(7)'
#     #             )
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(13)'
#     #             )
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(15)'
#     #             )
#     #         )
#     #     )
#     #     el5.click()
#     #
#     #     el6 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (AppiumBy.CLASS_NAME, "android.widget.ScrollView")
#     #         )
#     #     )
#     #     el6.click()
#
#     def test_GM_87__Meeting_Host_139(self, mobile_v2):
#         driver = mobile_v2
#
#         wait = WebDriverWait(driver, 30)
#
#         el1 = wait.until(
#
#             EC.element_to_be_clickable(
#
#                 (
#
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#
#                     'new UiSelector().className("android.widget.EditText").instance(0)'
#
#                 )
#
#             )
#
#         )
#
#         el1.send_keys("sathees")
#
#         el2 = wait.until(
#
#             EC.element_to_be_clickable(
#
#                 (
#
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#
#                     'new UiSelector().className("android.widget.EditText").instance(1)'
#
#                 )
#
#             )
#
#         )
#
#         el2.send_keys("test@123")
#
#         el3 = wait.until(
#
#             EC.element_to_be_clickable(
#
#                 (
#
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#
#                     'new UiSelector().className("android.view.View").instance(7)'
#
#                 )
#
#             )
#
#         )
#
#         el3.click()
#
#         el4 = wait.until(
#
#             EC.element_to_be_clickable(
#
#                 (
#
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#
#                     'new UiSelector().className("android.view.View").instance(74)'
#
#                 )
#
#             )
#
#         )
#
#         el4.click()
#
#         el5 = wait.until(
#
#             EC.element_to_be_clickable(
#
#                 (
#
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#
#                     'new UiSelector().text("Instant Meeting")'
#
#                 )
#
#             )
#
#         )
#
#         el5.click()
#
#         el6 = wait.until(
#
#             EC.element_to_be_clickable(
#
#                 (
#
#                     AppiumBy.ID,
#
#                     "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
#
#                 )
#
#             )
#
#         )
#
#         el6.click()
#
#         el7 = wait.until(
#
#             EC.element_to_be_clickable(
#
#                 (
#
#                     AppiumBy.ID,
#
#                     "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
#
#                 )
#
#             )
#
#         )
#
#         el7.click()
#
#         el8 = wait.until(
#
#             EC.element_to_be_clickable(
#
#                 (
#
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#
#                     'new UiSelector().className("android.view.View").instance(29)'
#
#                 )
#
#             )
#
#         )
#
#         el8.click()
#
#     def test_GM_1759__Authentication_Login_593(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#         el1 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(0)'
#                 )
#             )
#         )
#         el1.send_keys("rakesh@mailinator.com")
#
#         el2 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(1)'
#                 )
#             )
#         )
#         el2.send_keys("test@123")
#
#         el3 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(7)'
#                 )
#             )
#         )
#         el3.click()
#
#     def test_GM_2410__Tab_Bar_Navigation_Post_Login_Landing_851(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#         el1 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(0)'
#                 )
#             )
#         )
#         el1.send_keys("sathees")
#
#         el2 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(1)'
#                 )
#             )
#         )
#         el2.send_keys("test@123")
#
#         el3 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(7)'
#                 )
#             )
#         )
#         el3.click()
#
#     def test_GM_2410__Tab_Bar_Navigation_Tab_Bar_Visibility_852(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#         el1 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(0)'
#                 )
#             )
#         )
#         el1.send_keys("sathees")
#
#         el2 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(1)'
#                 )
#             )
#         )
#         el2.send_keys("test@123")
#
#         el3 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(7)'
#                 )
#             )
#         )
#         el3.click()
#
#         el4 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(77)'
#                 )
#             )
#         )
#         el4.click()
#
#     def test_GM_2410__Tab_Bar_Navigation_Contacts_Navigation_856(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#         el1 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(0)'
#                 )
#             )
#         )
#         el1.send_keys("sathees")
#
#         el2 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(1)'
#                 )
#             )
#         )
#         el2.send_keys("test@123")
#
#         el3 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(7)'
#                 )
#             )
#         )
#         el3.click()
#
#         el4 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(77)'
#                 )
#             )
#         )
#         el4.click()
#
#         el5 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(88)'
#                 )
#             )
#         )
#         el5.click()
#
#         el6 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(15)'
#                 )
#             )
#         )
#         el6.click()
#
#     def test_GM_2410__Tab_Bar_Navigation_Home_Navigation_855(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#         el1 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(0)'
#                 )
#             )
#         )
#         el1.send_keys("sathees")
#
#         el2 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(1)'
#                 )
#             )
#         )
#         el2.send_keys("test@123")
#
#         el3 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(7)'
#                 )
#             )
#         )
#         el3.click()
#
#         el4 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(77)'
#                 )
#             )
#         )
#         el4.click()
#
#         el5 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(88)'
#                 )
#             )
#         )
#         el5.click()
#
#         el6 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(15)'
#                 )
#             )
#         )
#         el6.click()
#
#         el7 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(62)'
#                 )
#             )
#         )
#         el7.click()
#
#     def test_GM_2410__Tab_Bar_Navigation_Home_Navigation_855(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#         el1 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(0)'
#                 )
#             )
#         )
#         el1.send_keys("sathees")
#
#         el2 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(1)'
#                 )
#             )
#         )
#         el2.send_keys("test@123")
#
#         el3 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(7)'
#                 )
#             )
#         )
#         el3.click()
#
#         el4 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(77)'
#                 )
#             )
#         )
#         el4.click()
#
#         el5 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(88)'
#                 )
#             )
#         )
#         el5.click()
#
#         el6 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(15)'
#                 )
#             )
#         )
#         el6.click()
#
#         el7 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(62)'
#                 )
#             )
#         )
#         el7.click()
#
#     # def test_GM_97__Search_Global_135(self, mobile_v2):
#     #     driver = mobile_v2
#     #     wait = WebDriverWait(driver, 30)
#     #
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.widget.EditText").instance(0)'
#     #             )
#     #         )
#     #     )
#     #     el1.send_keys("sathees")
#     #
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.widget.EditText").instance(1)'
#     #             )
#     #         )
#     #     )
#     #     el2.send_keys("test@123")
#     #
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(7)'
#     #             )
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(94)'
#     #             )
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.widget.EditText").instance(0)'
#     #             )
#     #         )
#     #     )
#     #     el5.send_keys("week")
#     #
#     #     el6 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(4)'
#     #             )
#     #         )
#     #     )
#     #     el6.click()
#     #
#     #     el7 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(7)'
#     #             )
#     #         )
#     #     )
#     #     el7.click()
#
#     def test_GM_2410__Tab_Bar_Navigation_Recordings_Navigation_857(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#         el1 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(0)'
#                 )
#             )
#         )
#         el1.send_keys("sathees")
#
#         el2 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(1)'
#                 )
#             )
#         )
#         el2.send_keys("test@123")
#
#         el3 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(7)'
#                 )
#             )
#         )
#         el3.click()
#
#         el4 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(13)'
#                 )
#             )
#         )
#         el4.click()
#
#         el5 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(9)'
#                 )
#             )
#         )
#         el5.click()
#
#         el6 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(3)'
#                 )
#             )
#         )
#         el6.click()
#
#     def test_GM_2410__Tab_Bar_Navigation_Calendar_Navigation_858(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#         el1 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(0)'
#                 )
#             )
#         )
#         el1.send_keys("sathees")
#         el1.send_keys("sathees")
#
#         el2 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(1)'
#                 )
#             )
#         )
#         el2.send_keys("test@123")
#
#         el3 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(7)'
#                 )
#             )
#         )
#         el3.click()
#
#         el4 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(89)'
#                 )
#             )
#         )
#         el4.click()
#
#         el5 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(14)'
#                 )
#             )
#         )
#         el5.click()
#
#     def test_GM_2410__Tab_Bar_Navigation_Plus_Icon_Action_Trigger_861(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#         el1 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(0)'
#                 )
#             )
#         )
#         el1.send_keys("sathees")
#
#         el2 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(1)'
#                 )
#             )
#         )
#         el2.send_keys("test@123")
#
#         el3 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(7)'
#                 )
#             )
#         )
#         el3.click()
#
#         el4 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(75)'
#                 )
#             )
#         )
#         el4.click()
#     #
#     # def test_GM_2415__Home_My_Meeting_Switch_Day_to_Week_View_871(self, mobile_v2):
#     #     driver = mobile_v2
#     #     wait = WebDriverWait(driver, 30)
#     #
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.widget.EditText").instance(0)'
#     #             )
#     #         )
#     #     )
#     #     el1.send_keys("sathees")
#     #
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.widget.EditText").instance(1)'
#     #             )
#     #         )
#     #     )
#     #     el2.send_keys("test@123")
#     #
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(7)'
#     #             )
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(99)'
#     #             )
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(20)'
#     #             )
#     #         )
#     #     )
#     #     el5.click()
#     #
#     #     el6 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().text("17")'
#     #             )
#     #         )
#     #     )
#     #     el6.click()
#     def test_GM_2409__Profile_Settings_Navigation_to_My_Account_899(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#         el1 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(0)'
#                 )
#             )
#         )
#         el1.send_keys("sathees")
#
#         el2 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(1)'
#                 )
#             )
#         )
#         el2.send_keys("test@123")
#
#         el3 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(7)'
#                 )
#             )
#         )
#         el3.click()
#
#         el4 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(13)'
#                 )
#             )
#         )
#         el4.click()
#
#         el5 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(5)'
#                 )
#             )
#         )
#         el5.click()
#
#         el6 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(3)'
#                 )
#             )
#         )
#         el6.click()
#
#     def test_GM_2409__Profile_Settings_Navigation_to_Edit_Profile_904(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#         el1 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(0)'
#                 )
#             )
#         )
#         el1.send_keys("sathees")
#
#         el2 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(1)'
#                 )
#             )
#         )
#         el2.send_keys("test@123")
#
#         el3 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(7)'
#                 )
#             )
#         )
#         el3.click()
#
#         el4 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(13)'
#                 )
#             )
#         )
#         el4.click()
#
#         el5 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(5)'
#                 )
#             )
#         )
#         el5.click()
#
#         el6 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(3)'
#                 )
#             )
#         )
#         el6.click()
#
#         el7 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ACCESSIBILITY_ID,
#                     "Action"
#                 )
#             )
#         )
#         el7.click()
#
#         el8 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(18)'
#                 )
#             )
#         )
#         el8.click()
#
#         el9 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.CLASS_NAME,
#                     "android.widget.ScrollView"
#                 )
#             )
#         )
#         el9.click()
#
#     def test_GM_2419__Recordings_Navigation_to_Recordings_Page_929(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#         el1 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(0)'
#                 )
#             )
#         )
#         el1.send_keys("sathees")
#
#         el2 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(1)'
#                 )
#             )
#         )
#         el2.send_keys("test@123")
#
#         el3 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(7)'
#                 )
#             )
#         )
#         el3.click()
#
#         el4 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(13)'
#                 )
#             )
#         )
#         el4.click()
#
#         el5 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(9)'
#                 )
#             )
#         )
#         el5.click()
#
#         el6 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(3)'
#                 )
#             )
#         )
#         el6.click()
#
#     def test_GM_2419__Recordings_Tabs_Visibility_930(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#         el1 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(0)'
#                 )
#             )
#         )
#         el1.send_keys("sathees")
#
#         el2 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(1)'
#                 )
#             )
#         )
#         el2.send_keys("test@123")
#
#         el3 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(7)'
#                 )
#             )
#         )
#         el3.click()
#
#         el4 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(13)'
#                 )
#             )
#         )
#         el4.click()
#
#         el5 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(9)'
#                 )
#             )
#         )
#         el5.click()
#
#         el6 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(3)'
#                 )
#             )
#         )
#         el6.click()
#
#         el7 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(6)'
#                 )
#             )
#         )
#         el7.click()
#
#         el8 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(3)'
#                 )
#             )
#         )
#         el8.click()
#
#     # def test_GM_2415__Calendar_Mobile_Today_Button_Navigation_Flow_997(self, mobile_v2):
#     #     driver = mobile_v2
#     #     wait = WebDriverWait(driver, 30)
#     #
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.widget.EditText").instance(0)'
#     #             )
#     #         )
#     #     )
#     #     el1.send_keys("sathees")
#     #
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.widget.EditText").instance(1)'
#     #             )
#     #         )
#     #     )
#     #     el2.send_keys("test@123")
#     #
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(7)'
#     #             )
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(98)'
#     #             )
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().text("18")'
#     #             )
#     #         )
#     #     )
#     #     el5.click()
#     #
#     #     el6 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(18)'
#     #             )
#     #         )
#     #     )
#     #     el6.click()
#
#     # def test_GM_2571__Calendar_Tablet_Today_Button_Navigation_Flow_1009(self, mobile_v2):
#     #     driver = mobile_v2
#     #     wait = WebDriverWait(driver, 30)
#     #
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.widget.EditText").instance(0)'
#     #             )
#     #         )
#     #     )
#     #     el1.send_keys("sathees")
#     #
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.widget.EditText").instance(1)'
#     #             )
#     #         )
#     #     )
#     #     el2.send_keys("test@123")
#     #
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(7)'
#     #             )
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(98)'
#     #             )
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().text("18")'
#     #             )
#     #         )
#     #     )
#     #     el5.click()
#     #
#     #     el6 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(18)'
#     #             )
#     #         )
#     #     )
#     #     el6.click()
#
#     # def test_GM_101__Calendar_Meetings_109(self, mobile_v2):
#     #     driver = mobile_v2
#     #     wait = WebDriverWait(driver, 30)
#     #
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.widget.EditText").instance(0)'
#     #             )
#     #         )
#     #     )
#     #     el1.send_keys("sathees")
#     #
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.widget.EditText").instance(1)'
#     #             )
#     #         )
#     #     )
#     #     el2.send_keys("test@123")
#     #
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(7)'
#     #             )
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(98)'
#     #             )
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(22)'
#     #             )
#     #         )
#     #     )
#     #     el5.click()
#
#     # def test_GM_103__Calendar_Navigation_113(self, mobile_v2):
#     #     driver = mobile_v2
#     #     wait = WebDriverWait(driver, 30)
#     #
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.widget.EditText").instance(0)'
#     #             )
#     #         )
#     #     )
#     #     el1.send_keys("sathees")
#     #
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.widget.EditText").instance(1)'
#     #             )
#     #         )
#     #     )
#     #     el2.send_keys("test@123")
#     #
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(7)'
#     #             )
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(98)'
#     #             )
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(29)'
#     #             )
#     #         )
#     #     )
#     #     el5.click()
#     #
#     #     el6 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().text("Today")'
#     #             )
#     #         )
#     #     )
#     #     el6.click()
#
#     def test_GM_2419__Recordings_Bookmarked_Tab_Listing_933(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#         el1 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(5)'
#                 )
#             )
#         )
#         el1.click()
#
#         el2 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(0)'
#                 )
#             )
#         )
#         el2.send_keys("sathees")
#
#         el3 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(1)'
#                 )
#             )
#         )
#         el3.send_keys("test@123")
#
#         el4 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(7)'
#                 )
#             )
#         )
#         el4.click()
#
#         el5 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(13)'
#                 )
#             )
#         )
#         el5.click()
#
#         el6 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(9)'
#                 )
#             )
#         )
#         el6.click()
#
#         el7 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(6)'
#                 )
#             )
#         )
#         el7.click()
#
#         el8 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(3)'
#                 )
#             )
#         )
#         el8.click()
#
#     # def test_GM_95__Meeting_Screen_Share_172(self, mobile_v2):
#     #     driver = mobile_v2
#     #     wait = WebDriverWait(driver, 30)
#     #
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.widget.EditText").instance(0)'
#     #             )
#     #         )
#     #     )
#     #     el1.send_keys("sathees")
#     #
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.widget.EditText").instance(1)'
#     #             )
#     #         )
#     #     )
#     #     el2.send_keys("test@123")
#     #
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(7)'
#     #             )
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(74)'
#     #             )
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().text("Instant Meeting")'
#     #             )
#     #         )
#     #     )
#     #     el5.click()
#     #
#     #     el6 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ID,
#     #                 'com.android.permissioncontroller:id/permission_allow_foreground_only_button'
#     #             )
#     #         )
#     #     )
#     #     el6.click()
#     #
#     #     el7 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ID,
#     #                 'com.android.permissioncontroller:id/permission_allow_foreground_only_button'
#     #             )
#     #         )
#     #     )
#     #     el7.click()
#     #
#     #     el8 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(27)'
#     #             )
#     #         )
#     #     )
#     #     el8.click()
#     #
#     #     el9 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().description("More Actions").instance(0)'
#     #             )
#     #         )
#     #     )
#     #     el9.click()
#     #
#     #     el10 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(4)'
#     #             )
#     #         )
#     #     )
#     #     el10.click()
#     #
#     #     el11 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(6)'
#     #             )
#     #         )
#     #     )
#     #     el11.click()
#     #
#     #     el12 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ID,
#     #                 'android:id/button1'
#     #             )
#     #         )
#     #     )
#     #     el12.click()
#
#     def test_GM_120__Meeting_Recording_149(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#         el1 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.XPATH,
#                     "//android.widget.ScrollView/android.widget.EditText[1]"
#                 )
#             )
#         )
#         el1.send_keys("sathees")
#
#         el2 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(1)'
#                 )
#             )
#         )
#         el2.send_keys("test@123")
#
#         el3 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.XPATH,
#                     "//android.widget.ScrollView/android.view.View[3]"
#                 )
#             )
#         )
#         el3.click()
#
#         el4 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(75)'
#                 )
#             )
#         )
#         el4.click()
#
#         el5 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(4)'
#                 )
#             )
#         )
#         el5.click()
#
#         el6 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(27)'
#                 )
#             )
#         )
#         el6.click()
#
#         el7 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(18)'
#                 )
#             )
#         )
#         el7.click()
#
#         el8 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(4)'
#                 )
#             )
#         )
#         el8.click()
#
#         el9 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().text("Continue")'
#                 )
#             )
#         )
#         el9.click()
#
#         el10 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(12)'
#                 )
#             )
#         )
#         el10.click()
#
#     def test_KBM_57__More_actions_copy_meeting_48(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#
#         el1 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(0)'
#                 )
#             )
#         )
#         el1.send_keys("sathees")
#
#
#         el2 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(1)'
#                 )
#             )
#         )
#         el2.send_keys("test@123")
#
#
#         el3 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(7)'
#                 )
#             )
#         )
#         el3.click()
#
#         el4 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(75)'
#                 )
#             )
#         )
#         el4.click()
#
#
#         el5 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().text("Instant Meeting")'
#                 )
#             )
#         )
#         el5.click()
#
#
#         el6 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(27)'
#                 )
#             )
#         )
#         el6.click()
#
#
#         el7 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ACCESSIBILITY_ID,
#                     "Info"
#                 )
#             )
#         )
#         el7.click()
#
#
#         el8 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().description("Copy Joining Info").instance(0)'
#                 )
#             )
#         )
#         el8.click()
#
#
#         el9 = wait.until(
#             EC.presence_of_element_located(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().text("Meeting ID copied to clipboard")'
#                 )
#             )
#         )
#
#         assert el9.is_displayed(), "Meeting ID copied to clipboard message is not displayed."
#
#     def test_KBM_45__Enable_disable_video_video_icon_54(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#         el1 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(0)'
#                 )
#             )
#         )
#         el1.send_keys("sathees")
#
#         el2 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(1)'
#                 )
#             )
#         )
#         el2.send_keys("test@123")
#
#         el3 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(7)'
#                 )
#             )
#         )
#         el3.click()
#
#         el4 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(75)'
#                 )
#             )
#         )
#         el4.click()
#
#         el5 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(4)'
#                 )
#             )
#         )
#         el5.click()
#
#         el6 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(23)'
#                 )
#             )
#         )
#         el6.click()
#
#     def test_KBM_43__Mute_unmute_audio_audio_icon_63(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#         el1 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(0)'
#                 )
#             )
#         )
#         el1.send_keys("sathes")
#
#         el2 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(0)'
#                 )
#             )
#         )
#         el2.send_keys("sathees")
#
#         el3 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(1)'
#                 )
#             )
#         )
#         el3.send_keys("test@123")
#
#         el4 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(7)'
#                 )
#             )
#         )
#         el4.click()
#
#         el5 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(74)'
#                 )
#             )
#         )
#         el5.click()
#
#         el6 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().text("Instant Meeting")'
#                 )
#             )
#         )
#         el6.click()
#
#         el7 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(21)'
#                 )
#             )
#         )
#         el7.click()
#
#     # def test_KBM_38__Meeting_screen_Meeting_screen_77(self, mobile_v2):
#     #     driver = mobile_v2
#     #     wait = WebDriverWait(driver, 30)
#     #
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.widget.EditText").instance(0)'
#     #             )
#     #         )
#     #     )
#     #     el1.send_keys("sathees")
#     #
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.widget.EditText").instance(1)'
#     #             )
#     #         )
#     #     )
#     #     el2.send_keys("test@123")
#     #
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(7)'
#     #             )
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(74)'
#     #             )
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(7)'
#     #             )
#     #         )
#     #     )
#     #     el5.click()
#     #
#     #     el6 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.widget.EditText").instance(0)'
#     #             )
#     #         )
#     #     )
#     #     el6.send_keys("title")
#     #
#     #     el7 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.XPATH,
#     #                 "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View"
#     #             )
#     #         )
#     #     )
#     #     el7.click()
#     #
#     #     el8 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(55)'
#     #             )
#     #         )
#     #     )
#     #     el8.click()
#     #
#     #     el9 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(17)'
#     #             )
#     #         )
#     #     )
#     #     el9.click()
#     #
#     #     el10 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.CLASS_NAME,
#     #                 "android.widget.ScrollView"
#     #             )
#     #         )
#     #     )
#     #     el10.click()
#     #
#     #     el11 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().text("Start Meeting")'
#     #             )
#     #         )
#     #     )
#     #     el11.click()
#     #
#     #     el12 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(12)'
#     #             )
#     #         )
#     #     )
#     #     el12.click()
#
#     def test_GM_113__Meeting_Management_Start_Meeting_Permissions_93(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#         el1 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(0)'
#                 )
#             )
#         )
#         el1.send_keys("sathees")
#
#         el2 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(1)'
#                 )
#             )
#         )
#         el2.send_keys("test@123")
#
#         el3 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(7)'
#                 )
#             )
#         )
#         el3.click()
#
#         el4 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(74)'
#                 )
#             )
#         )
#         el4.click()
#
#         el5 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().text("Instant Meeting")'
#                 )
#             )
#         )
#         el5.click()
#
#         el6 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ID,
#                     "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
#                 )
#             )
#         )
#         el6.click()
#
#         el7 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ID,
#                     "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
#                 )
#             )
#         )
#         el7.click()
#
#     def test_GM_75__Meeting_Activespeaker_140(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#         el1 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(0)'
#                 )
#             )
#         )
#         el1.send_keys("sathees")
#
#         el2 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(1)'
#                 )
#             )
#         )
#         el2.send_keys("test@123")
#
#         el3 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(7)'
#                 )
#             )
#         )
#         el3.click()
#
#         el4 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(74)'
#                 )
#             )
#         )
#         el4.click()
#
#         el5 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().text("Instant Meeting")'
#                 )
#             )
#         )
#         el5.click()
#
#         el6 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ID,
#                     "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
#                 )
#             )
#         )
#         el6.click()
#
#         el7 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ID,
#                     "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
#                 )
#             )
#         )
#         el7.click()
#
#         el8 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(18)'
#                 )
#             )
#         )
#         el8.click()
#
#         el9 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(4)'
#                 )
#             )
#         )
#         el9.click()
#
#     # def test_GM_143__Meeting_VideoView_122(self, mobile_v2):
#     #     driver = mobile_v2
#     #     wait = WebDriverWait(driver, 30)
#     #
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.widget.EditText").instance(0)'
#     #             )
#     #         )
#     #     )
#     #     el1.send_keys("sathees")
#     #
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.widget.EditText").instance(1)'
#     #             )
#     #         )
#     #     )
#     #     el2.send_keys("test@123")
#     #
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(7)'
#     #             )
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(74)'
#     #             )
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().text("Instant Meeting")'
#     #             )
#     #         )
#     #     )
#     #     el5.click()
#     #
#     #     el6 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ID,
#     #                 "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
#     #             )
#     #         )
#     #     )
#     #     el6.click()
#     #
#     #     el7 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ID,
#     #                 "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
#     #             )
#     #         )
#     #     )
#     #     el7.click()
#     #
#     #     el8 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(18)'
#     #             )
#     #         )
#     #     )
#     #     el8.click()
#     #
#     #     el9 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(4)'
#     #             )
#     #         )
#     #     )
#     #     el9.click()
#
#     # def test_GM_143__Meeting_VideoView_121(self, mobile_v2):
#     #     driver = mobile_v2
#     #     wait = WebDriverWait(driver, 30)
#     #
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.widget.EditText").instance(0)'
#     #             )
#     #         )
#     #     )
#     #     el1.send_keys("sathees")
#     #
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.widget.EditText").instance(1)'
#     #             )
#     #         )
#     #     )
#     #     el2.send_keys("test@123")
#     #
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(7)'
#     #             )
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(74)'
#     #             )
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().text("Instant Meeting")'
#     #             )
#     #         )
#     #     )
#     #     el5.click()
#     #
#     #     el6 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(18)'
#     #             )
#     #         )
#     #     )
#     #     el6.click()
#     #
#     #     el7 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(9)'
#     #             )
#     #         )
#     #     )
#     #     el7.click()
#
#     # def test_GM_711__Recording_Share_Recording_283(self, mobile_v2):
#     #     driver = mobile_v2
#     #     wait = WebDriverWait(driver, 30)
#     #
#     #
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.widget.EditText").instance(0)'
#     #             )
#     #         )
#     #     )
#     #     el1.send_keys("sathees")
#     #
#     #     # Password
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.widget.EditText").instance(1)'
#     #             )
#     #         )
#     #     )
#     #     el2.send_keys("test@123")
#     #
#     #     # Sign In
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(7)'
#     #             )
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     # Click element
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(13)'
#     #             )
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #     # Click element
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(9)'
#     #             )
#     #         )
#     #     )
#     #     el5.click()
#     #
#     #     # Click element
#     #     el6 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(19)'
#     #             )
#     #         )
#     #     )
#     #     el6.click()
#     #
#     #     # Click element
#     #     el7 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(36)'
#     #             )
#     #         )
#     #     )
#     #     el7.click()
#     #
#     #     # Click element
#     #     el8 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(10)'
#     #             )
#     #         )
#     #     )
#     #     el8.click()
#     #
#     #     # Click element
#     #     el9 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(21)'
#     #             )
#     #         )
#     #     )
#     #     el9.click()
#     #
#     # def test_GM_711__Recording_Share_Recording_287(self, mobile_v2):
#     #     driver = mobile_v2
#     #     wait = WebDriverWait(driver, 30)
#     #
#     #
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.widget.EditText").instance(0)'
#     #             )
#     #         )
#     #     )
#     #     el1.send_keys("sathees")
#     #
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.widget.EditText").instance(1)'
#     #             )
#     #         )
#     #     )
#     #     el2.send_keys("test@123")
#     #
#     #     # Sign In
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(7)'
#     #             )
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     # Click element
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(13)'
#     #             )
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #     # Click element
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(9)'
#     #             )
#     #         )
#     #     )
#     #     el5.click()
#     #
#     #     # Click element
#     #     el6 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(19)'
#     #             )
#     #         )
#     #     )
#     #     el6.click()
#     #
#     #     # Click element
#     #     el7 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(36)'
#     #             )
#     #         )
#     #     )
#     #     el7.click()
#     #
#     #     # Click element
#     #     el8 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(10)'
#     #             )
#     #         )
#     #     )
#     #     el8.click()
#     #
#     #
#     #     el9 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(21)'
#     #             )
#     #         )
#     #     )
#     #     el9.click()
#     #
#     # def test_GM_539__Meeting_Layout_401(self, mobile_v2):
#     #     driver = mobile_v2
#     #     wait = WebDriverWait(driver, 30)
#     #
#     #
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.widget.EditText").instance(0)'
#     #             )
#     #         )
#     #     )
#     #     el1.send_keys("sathees")
#     #
#     #
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.widget.EditText").instance(1)'
#     #             )
#     #         )
#     #     )
#     #     el2.send_keys("test@123")
#     #
#     #
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(7)'
#     #             )
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(74)'
#     #             )
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().text("Instant Meeting")'
#     #             )
#     #         )
#     #     )
#     #     el5.click()
#     #
#     #
#     #     el6 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ID,
#     #                 "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
#     #             )
#     #         )
#     #     )
#     #     el6.click()
#     #
#     #
#     #     el7 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ID,
#     #                 "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
#     #             )
#     #         )
#     #     )
#     #     el7.click()
#     #
#     #     # More Options
#     #     el8 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(27)'
#     #             )
#     #         )
#     #     )
#     #     el8.click()
#     #
#     #
#     #     el9 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().text("Meeting Layout")'
#     #             )
#     #         )
#     #     )
#     #     el9.click()
#     #
#     #
#     #     el10 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(7)'
#     #             )
#     #         )
#     #     )
#     #     el10.click()
#     #
#     # def test_GM_539__Meeting_Layout_402(self, mobile_v2):
#     #     driver = mobile_v2
#     #     wait = WebDriverWait(driver, 30)
#     #
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.widget.EditText").instance(0)'
#     #             )
#     #         )
#     #     )
#     #     el1.send_keys("sathees")
#     #
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.widget.EditText").instance(1)'
#     #             )
#     #         )
#     #     )
#     #     el2.send_keys("test@123")
#     #
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(7)'
#     #             )
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(74)'
#     #             )
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().text("Instant Meeting")'
#     #             )
#     #         )
#     #     )
#     #     el5.click()
#     #
#     #     el6 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ID,
#     #                 "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
#     #             )
#     #         )
#     #     )
#     #     el6.click()
#     #
#     #     el7 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ID,
#     #                 "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
#     #             )
#     #         )
#     #     )
#     #     el7.click()
#     #
#     #     # More Options
#     #     el8 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(27)'
#     #             )
#     #         )
#     #     )
#     #     el8.click()
#     #
#     #     el9 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().text("Meeting Layout")'
#     #             )
#     #         )
#     #     )
#     #     el9.click()
#     #
#     #     el10 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(7)'
#     #             )
#     #         )
#     #     )
#     #     el10.click()
#
#     # def test_GM_539__Meeting_Layout_403(self, mobile_v2):
#     #     driver = mobile_v2
#     #     wait = WebDriverWait(driver, 30)
#     #
#     #     el1 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.widget.EditText").instance(0)'
#     #             )
#     #         )
#     #     )
#     #     el1.send_keys("sathees")
#     #
#     #     el2 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.widget.EditText").instance(1)'
#     #             )
#     #         )
#     #     )
#     #     el2.send_keys("test@123")
#     #
#     #     el3 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(7)'
#     #             )
#     #         )
#     #     )
#     #     el3.click()
#     #
#     #     el4 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(74)'
#     #             )
#     #         )
#     #     )
#     #     el4.click()
#     #
#     #     el5 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().text("Instant Meeting")'
#     #             )
#     #         )
#     #     )
#     #     el5.click()
#     #
#     #     el6 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ID,
#     #                 "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
#     #             )
#     #         )
#     #     )
#     #     el6.click()
#     #
#     #     el7 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ID,
#     #                 "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
#     #             )
#     #         )
#     #     )
#     #     el7.click()
#     #
#     #     # More Options
#     #     el8 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(27)'
#     #             )
#     #         )
#     #     )
#     #     el8.click()
#     #
#     #     el9 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().text("Meeting Layout")'
#     #             )
#     #         )
#     #     )
#     #     el9.click()
#     #
#     #     el10 = wait.until(
#     #         EC.element_to_be_clickable(
#     #             (
#     #                 AppiumBy.ANDROID_UIAUTOMATOR,
#     #                 'new UiSelector().className("android.view.View").instance(7)'
#     #             )
#     #         )
#     #     )
#     #     el10.click()
#     def test_GM_2412__Home_FAB_Instant_Meeting_Navigation_796(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#
#         el1 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(0)'
#                 )
#             )
#         )
#         el1.send_keys("sathees")
#
#
#         el2 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(1)'
#                 )
#             )
#         )
#         el2.send_keys("test@123")
#
#         el3 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(7)'
#                 )
#             )
#         )
#         el3.click()
#
#         el4 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(74)'
#                 )
#             )
#         )
#         el4.click()
#
#
#         el5 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().text("Instant Meeting")'
#                 )
#             )
#         )
#         el5.click()
#
#
#         el6 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ID,
#                     "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
#                 )
#             )
#         )
#         el6.click()
#
#
#         el7 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ID,
#                     "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
#                 )
#             )
#         )
#         el7.click()
#
#     def test_GM_2412__Home_FAB_Schedule_Meeting_Navigation_797(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#         el1 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(0)'
#                 )
#             )
#         )
#         el1.send_keys("sathees")
#
#
#         el2 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(1)'
#                 )
#             )
#         )
#         el2.send_keys("test@123")
#
#         el3 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(7)'
#                 )
#             )
#         )
#         el3.click()
#
#         # Tap FAB
#         el4 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(74)'
#                 )
#             )
#         )
#         el4.click()
#
#
#         el5 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().text("Schedule Meeting")'
#                 )
#             )
#         )
#         el5.click()
#
#
#         el6 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.CLASS_NAME,
#                     "android.widget.ScrollView"
#                 )
#             )
#         )
#         el6.click()
#
#     def test_GM_2412__Home_FAB_Schedule_Event_Navigation_798(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#
#         el1 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(0)'
#                 )
#             )
#         )
#         el1.send_keys("sathees")
#
#
#         el2 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(1)'
#                 )
#             )
#         )
#         el2.send_keys("test@123")
#
#
#         el3 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(7)'
#                 )
#             )
#         )
#         el3.click()
#
#
#         el4 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(74)'
#                 )
#             )
#         )
#         el4.click()
#
#
#         el5 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().text("Schedule Event")'
#                 )
#             )
#         )
#         el5.click()
#
#
#         el6 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.CLASS_NAME,
#                     "android.widget.ScrollView"
#                 )
#             )
#         )
#         el6.click()
#
#     def test_GM_3218__Settings_Recordings_Access_from_Settings_1356(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#         el1 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(0)'
#                 )
#             )
#         )
#         el1.send_keys("sathees")
#
#         el2 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(1)'
#                 )
#             )
#         )
#         el2.send_keys("test@123")
#
#         el3 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.CLASS_NAME,
#                     "android.widget.ScrollView"
#                 )
#             )
#         )
#         el3.click()
#
#         el4 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(7)'
#                 )
#             )
#         )
#         el4.click()
#
#         el5 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(13)'
#                 )
#             )
#         )
#         el5.click()
#
#         el6 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(9)'
#                 )
#             )
#         )
#         el6.click()
#
#         el7 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(3)'
#                 )
#             )
#         )
#         el7.click()
#
#     def test_GM_104__JoinMeeting_MeetingCode_115(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#         el6 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(0)'
#                 )
#             )
#         )
#         el6.send_keys("sathees")
#
#         el7 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(1)'
#                 )
#             )
#         )
#         el7.send_keys("test@123")
#
#         el8 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(7)'
#                 )
#             )
#         )
#         el8.click()
#
#         el9 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.CLASS_NAME,
#                     "android.widget.EditText"
#                 )
#             )
#         )
#         el9.click()
#
#         el10 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().text("Join")'
#                 )
#             )
#         )
#         el10.click()
#
#     def test_GM_361__Invite_UI_Home_screen_184(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#         el1 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(0)'
#                 )
#             )
#         )
#         el1.send_keys("sathees")
#
#         el2 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(1)'
#                 )
#             )
#         )
#         el2.send_keys("test@123")
#
#         el3 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(7)'
#                 )
#             )
#         )
#         el3.click()
#
#         el4 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().text("Now").instance(1)'
#                 )
#             )
#         )
#         el4.click()
#
#     def test_GM_910__Meeting_Code_Validation_303(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#         el1 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(0)'
#                 )
#             )
#         )
#         el1.send_keys("sathees")
#
#         el2 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(1)'
#                 )
#             )
#         )
#         el2.send_keys("test@123")
#
#         el3 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(7)'
#                 )
#             )
#         )
#         el3.click()
#
#         el4 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.CLASS_NAME,
#                     "android.widget.EditText"
#                 )
#             )
#         )
#         el4.send_keys("ATUIOM")
#
#         el5 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().text("Join")'
#                 )
#             )
#         )
#         el5.click()
#
#         el7 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.CLASS_NAME,
#                     "android.widget.EditText"
#                 )
#             )
#         )
#         el7.send_keys("123456")
#
#         el8 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().text("Join")'
#                 )
#             )
#         )
#         el8.click()
#
#     def test_GM_1322__Streaming_Event_Create_Event_448(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#         el1 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(0)'
#                 )
#             )
#         )
#         el1.send_keys("sathees")
#
#         el2 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(1)'
#                 )
#             )
#         )
#         el2.send_keys("test@123")
#
#         el3 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(7)'
#                 )
#             )
#         )
#         el3.click()
#
#         el4 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(74)'
#                 )
#             )
#         )
#         el4.click()
#
#         el5 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().text("Schedule Event")'
#                 )
#             )
#         )
#         el5.click()
#
#         el6 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.CLASS_NAME,
#                     "android.widget.ScrollView"
#                 )
#             )
#         )
#         el6.click()
#
#     def test_GM_2412__Home_FAB_FAB_Visibility_794(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#         el1 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(0)'
#                 )
#             )
#         )
#         el1.send_keys("sathees")
#
#         el2 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(1)'
#                 )
#             )
#         )
#         el2.send_keys("test@123")
#
#         el3 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(7)'
#                 )
#             )
#         )
#         el3.click()
#
#         el4 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(74)'
#                 )
#             )
#         )
#         el4.click()
#
#     def test_GM_2412__Home_FAB_FAB_Expand_Options_795(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#         el1 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(0)'
#                 )
#             )
#         )
#         el1.send_keys("sathees")
#
#         el2 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.XPATH,
#                     "//android.widget.ScrollView/android.widget.EditText[2]"
#                 )
#             )
#         )
#         el2.send_keys("test@123")
#
#         el3 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(7)'
#                 )
#             )
#         )
#         el3.click()
#
#         el4 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(74)'
#                 )
#             )
#         )
#         el4.click()
#
#     def test_GM_2419__Recordings_All_Recordings_Listing_810(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#         el1 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(0)'
#                 )
#             )
#         )
#         el1.send_keys("sathees")
#
#         el2 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(1)'
#                 )
#             )
#         )
#         el2.send_keys("test@123")
#
#         el3 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(7)'
#                 )
#             )
#         )
#         el3.click()
#
#         el4 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(13)'
#                 )
#             )
#         )
#         el4.click()
#
#         el5 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(9)'
#                 )
#             )
#         )
#         el5.click()
#
#         el6 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(3)'
#                 )
#             )
#         )
#         el6.click()
#
#     def test_GM_1932__Localization_i18_Automatic_Detection_French_707(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#         el1 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(0)'
#                 )
#             )
#         )
#         el1.send_keys("sathees")
#
#         el2 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(1)'
#                 )
#             )
#         )
#         el2.send_keys("test@123")
#
#         el3 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(7)'
#                 )
#             )
#         )
#         el3.click()
#
#         el4 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(12)'
#                 )
#             )
#         )
#         el4.click()
#
#         el5 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(17)'
#                 )
#             )
#         )
#         el5.click()
#
#         el6 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(12)'
#                 )
#             )
#         )
#         el6.click()
#
#         el7 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.CLASS_NAME,
#                     "android.widget.ScrollView"
#                 )
#             )
#         )
#         el7.click()
#
#     def test_GM_2416__Meeting_Info_No_Navigation_Behavior_767(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#         el1 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(0)'
#                 )
#             )
#         )
#         el1.send_keys("sathees")
#
#         el2 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(1)'
#                 )
#             )
#         )
#         el2.send_keys("test@123")
#
#         el3 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(7)'
#                 )
#             )
#         )
#         el3.click()
#
#         el4 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.XPATH,
#                     "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[2]/android.view.View/android.view.View/android.view.View"
#                 )
#             )
#         )
#         el4.click()
#
#         el5 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.XPATH,
#                     "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[1]/android.view.View/android.view.View[4]/android.view.View[4]/android.view.View"
#                 )
#             )
#         )
#         el5.click()
#
#         el6 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(7)'
#                 )
#             )
#         )
#         el6.click()
#
#     def test_GM_2476__Meeting_and_Event_Header_Timer_Real_Time_Update_890(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#         el1 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(0)'
#                 )
#             )
#         )
#         el1.send_keys("sathees")
#
#         el2 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(1)'
#                 )
#             )
#         )
#         el2.send_keys("test@123")
#
#         el3 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(7)'
#                 )
#             )
#         )
#         el3.click()
#
#         el4 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(74)'
#                 )
#             )
#         )
#         el4.click()
#
#         el5 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().text("Instant Meeting")'
#                 )
#             )
#         )
#         el5.click()
#
#         el6 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ID,
#                     "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
#                 )
#             )
#         )
#         el6.click()
#
#         el7 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ID,
#                     "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
#                 )
#             )
#         )
#         el7.click()
#
#         el8 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(5)'
#                 )
#             )
#         )
#         el8.click()
#
#     def test_GM_2479__Meeting_Timer_Display_on_Meeting_Start_910(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#         el1 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(0)'
#                 )
#             )
#         )
#         el1.send_keys("sathees")
#
#         el2 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(1)'
#                 )
#             )
#         )
#         el2.send_keys("test@123")
#
#         el3 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(7)'
#                 )
#             )
#         )
#         el3.click()
#
#         el4 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(74)'
#                 )
#             )
#         )
#         el4.click()
#
#         el5 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().text("Instant Meeting")'
#                 )
#             )
#         )
#         el5.click()
#
#         el6 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(2)'
#                 )
#             )
#         )
#         el6.click()
#
#     def test_GM_2482__Meeting_Controls_Visibility_on_Meeting_Start_917(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#         el1 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(0)'
#                 )
#             )
#         )
#         el1.send_keys("sathees")
#
#         el2 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(1)'
#                 )
#             )
#         )
#         el2.send_keys("test@123")
#
#         el3 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(7)'
#                 )
#             )
#         )
#         el3.click()
#
#         el4 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(74)'
#                 )
#             )
#         )
#         el4.click()
#
#         el5 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().text("Instant Meeting")'
#                 )
#             )
#         )
#         el5.click()
#
#         el6 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(4)'
#                 )
#             )
#         )
#         el6.click()
#
#         el7 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(27)'
#                 )
#             )
#         )
#         el7.click()
#
#         el8 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(24)'
#                 )
#             )
#         )
#         el8.click()
#
#         el9 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.XPATH,
#                     "//android.view.ViewGroup/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View"
#                 )
#             )
#         )
#         el9.click()
#
#     def test_GM_2484__In_meeting_More_Settings_More_Settings_Visibility_in_Meeting_Controls_928(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#         el1 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(0)'
#                 )
#             )
#         )
#         el1.send_keys("sathees")
#
#         el2 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(1)'
#                 )
#             )
#         )
#         el2.send_keys("test@123")
#
#         el3 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(7)'
#                 )
#             )
#         )
#         el3.click()
#
#         el4 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(74)'
#                 )
#             )
#         )
#         el4.click()
#
#         el5 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().text("Instant Meeting")'
#                 )
#             )
#         )
#         el5.click()
#
#         el6 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(4)'
#                 )
#             )
#         )
#         el6.click()
#
#         el7 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(27)'
#                 )
#             )
#         )
#         el7.click()
#
#         el8 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(24)'
#                 )
#             )
#         )
#         el8.click()
#
#         el9 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.XPATH,
#                     "//android.view.ViewGroup/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View"
#                 )
#             )
#         )
#         el9.click()
#
#     def test_GM_2804__Participant_Panel_SEE_ALL_Connect_Flow_1021(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#         el1 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(0)'
#                 )
#             )
#         )
#         el1.send_keys("sathees")
#
#         el2 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(1)'
#                 )
#             )
#         )
#         el2.send_keys("test@123")
#
#         el3 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(7)'
#                 )
#             )
#         )
#         el3.click()
#
#         el4 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().text("See All")'
#                 )
#             )
#         )
#         el4.click()
#
#         el5 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(3)'
#                 )
#             )
#         )
#         el5.click()
#
#     def test_GM_3218__Settings_Recording_Tab_Placement_Validation_1333(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#         el1 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(0)'
#                 )
#             )
#         )
#         el1.send_keys("sathees")
#
#         el2 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(1)'
#                 )
#             )
#         )
#         el2.send_keys("test@123")
#
#         el3 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(7)'
#                 )
#             )
#         )
#         el3.click()
#
#         el4 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(13)'
#                 )
#             )
#         )
#         el4.click()
#
#         el5 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(9)'
#                 )
#             )
#         )
#         el5.click()
#
#         el6 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(3)'
#                 )
#             )
#         )
#         el6.click()
#
#     def test_GM_3218__Announcements_Announcement_List_Navigation_1334(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#         el1 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(0)'
#                 )
#             )
#         )
#         el1.send_keys("sathees")
#
#         el2 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(1)'
#                 )
#             )
#         )
#         el2.send_keys("test@123")
#
#         el3 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.XPATH,
#                     "//android.widget.ScrollView/android.view.View[3]"
#                 )
#             )
#         )
#         el3.click()
#
#         el4 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ACCESSIBILITY_ID,
#                     "Announcement"
#                 )
#             )
#         )
#         el4.click()
#
#         el5 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(3)'
#                 )
#             )
#         )
#         el5.click()
#
#     def test_GM_3218__Announcements_Bottom_Navigation_Search_Accessibility_1355(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#         el1 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(0)'
#                 )
#             )
#         )
#         el1.send_keys("sathees")
#
#         el2 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(1)'
#                 )
#             )
#         )
#         el2.send_keys("test@123")
#
#         el3 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(7)'
#                 )
#             )
#         )
#         el3.click()
#
#         el4 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(84)'
#                 )
#             )
#         )
#         el4.click()
#
#         el5 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(1)'
#                 )
#             )
#         )
#         el5.click()
#
#     def test_GM_3230__In_App_Review_Rate_Us_Button_Visibility_Validation_1217(self, mobile_v2):
#         driver = mobile_v2
#         wait = WebDriverWait(driver, 30)
#
#         el1 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(0)'
#                 )
#             )
#         )
#         el1.send_keys("sathees")
#
#         el2 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.EditText").instance(1)'
#                 )
#             )
#         )
#         el2.send_keys("test@123")
#
#         el3 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(7)'
#                 )
#             )
#         )
#         el3.click()
#
#         el4 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(13)'
#                 )
#             )
#         )
#         el4.click()
#
#         el5 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.view.View").instance(29)'
#                 )
#             )
#         )
#         el5.click()
#
#         el6 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().text("Settings")'
#                 )
#             )
#         )
#         el6.click()
#
#         el7 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().className("android.widget.RelativeLayout").instance(2)'
#                 )
#             )
#         )
#         el7.click()
#
#         el8 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ANDROID_UIAUTOMATOR,
#                     'new UiSelector().text("Notifications")'
#                 )
#             )
#         )
#         el8.click()
#
#         el9 = wait.until(
#             EC.element_to_be_clickable(
#                 (
#                     AppiumBy.ACCESSIBILITY_ID,
#                     "Back"
#                 )
#             )
#         )
#         el9.click()
    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Signin")
    @allure.description_html("""
    <h2>Verify user can navigate from Onboarding to Sign In screen</h2>

    <br>

    <u>Test Case Description</u>
    &nbsp;&nbsp;-&nbsp;&nbsp;
    Check whether the navigation from Onboarding to Sign In works.

    <br><br><br>

    <u>Expected Result</u>

    <br><br>

    User should be able to navigate to the login screen

    <br><br><br>

    Client
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    Katon Meet

    <br><br>

    Project
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    Katon Meet

    <br><br>
    """)
    def test_KBM_04__Signin_Signin_6(self, mobile_v2):
        driver = mobile_v2
        wait = WebDriverWait(driver, 30)

        el1 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(0)'
                )
            )
        )
        el1.send_keys("sathees")

        el2 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(1)'
                )
            )
        )
        el2.send_keys("test@1234")

        el3 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(7)'
                )
            )
        )
        el3.click()

        el4 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(22)'
                )
            )
        )
        el4.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Signin")
    @allure.description_html("""
        <h2>Verify successful login with valid credentials</h2>

        <br>

        <u>Test Case Description</u>
        &nbsp;&nbsp;-&nbsp;&nbsp;
        Check whether by entering the valid credentials.

        <br><br><br>

        <u>Expected Result</u>

        <br><br>

        User should be able to navigate to the home screen of the application

        <br><br><br>

        Client
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        Katon Meet

        <br><br>

        Project
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        Katon Meet

        <br><br>
        """)
    def test_KBM_04__Signin_Signin_11(self, mobile_v2):
        driver = mobile_v2
        wait = WebDriverWait(driver, 30)

        el1 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(0)'
                )
            )
        )
        el1.send_keys("sathees")

        el2 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(1)'
                )
            )
        )
        el2.send_keys("test@1234")

        el3 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(7)'
                )
            )
        )
        el3.click()

        el4 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(22)'
                )
            )
        )
        el4.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Signout")
    @allure.description_html("""
            <h2>Verify clicking "Signout" logs user out</h2>

            <br>

            <u>Test Case Description</u>
            &nbsp;&nbsp;-&nbsp;&nbsp;
            Check whether the user can able to logout when click on signout button on confirmation pop up.

            <br><br><br>

            <u>Expected Result</u>

            <br><br>

           User should be able to navigate back to the home screen

            <br><br><br>

            Client
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            Katon Meet

            <br><br>

            Project
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            Katon Meet

            <br><br>
            """)
    def test_KBM_91__Signout_Settings_35(self, mobile_v2):
        driver = mobile_v2
        wait = WebDriverWait(driver, 30)

        el1 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(0)'
                )
            )
        )
        el1.send_keys("sathees")

        el2 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(1)'
                )
            )
        )
        el2.send_keys("test@1234")

        el3 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(7)'
                )
            )
        )
        el3.click()

        el4 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(13)'
                )
            )
        )
        el4.click()

        el5 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(35)'
                )
            )
        )
        el5.click()

        el6 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().text("Sign Out")'
                )
            )
        )
        el6.click()

        el7 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.CLASS_NAME,
                    "android.widget.ScrollView"
                )
            )
        )
        el7.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Meeting")
    @allure.description_html("""
            <h2>Verify clicking leave meeting will ends call and navigates to Home screen</h2>

            <br>

            <u>Test Case Description</u>
            &nbsp;&nbsp;-&nbsp;&nbsp;
            Check whether the Participant disconnected and navigated to Home screen.

            <br><br><br>

            <u>Expected Result</u>

            <br><br>

          User should be able to leave the meeting and navigate back to home screen when click on leave meeting option

            <br><br><br>

            Client
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            Katon Meet

            <br><br>

            Project
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            Katon Meet

            <br><br>
            """)
    def test_KBM_49__Meeting_screen_End_call_41(self, mobile_v2):
        driver = mobile_v2
        wait = WebDriverWait(driver, 30)

        el1 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(0)'
                )
            )
        )
        el1.send_keys("sathees")

        el2 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(1)'
                )
            )
        )
        el2.send_keys("test@1234")

        el3 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(7)'
                )
            )
        )
        el3.click()

        el4 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(81)'
                )
            )
        )
        el4.click()

        el5 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().text("Instant Meeting")'
                )
            )
        )
        el5.click()

        el6 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ID,
                    "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
                )
            )
        )
        el6.click()

        el7 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ID,
                    "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
                )
            )
        )
        el7.click()

        el8 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(29)'
                )
            )
        )
        el8.click()

        el9 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(7)'
                )
            )
        )
        el9.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Meeting")
    @allure.description_html("""
                <h2>Verify that the meeting will end when click on end meeting for all option </h2>

                <br>

                <u>Test Case Description</u>
                &nbsp;&nbsp;-&nbsp;&nbsp;
                Check whether the meeting will end for all when click on end meeting for all option .

                <br><br><br>

                <u>Expected Result</u>

                <br><br>

              User should navigate back to the home screen when click on end meeting for all option 

                <br><br><br>

                Client
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                Katon Meet

                <br><br>

                Project
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                Katon Meet

                <br><br>
                """)
    def test_KBM_49__Meeting_screen_End_call_43(self, mobile_v2):
        driver = mobile_v2
        wait = WebDriverWait(driver, 30)

        el1 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(0)'
                )
            )
        )
        el1.send_keys("sathees")

        el2 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(1)'
                )
            )
        )
        el2.send_keys("test@1234")

        el3 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(7)'
                )
            )
        )
        el3.click()

        el4 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(81)'
                )
            )
        )
        el4.click()

        el5 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().text("Instant Meeting")'
                )
            )
        )
        el5.click()

        el6 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ID,
                    "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
                )
            )
        )
        el6.click()

        el7 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ID,
                    "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
                )
            )
        )
        el7.click()

        el8 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(29)'
                )
            )
        )
        el8.click()

        el9 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(7)'
                )
            )
        )
        el9.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Calendar")
    @allure.description_html("""
                    <h2>Verify that a user can view their calendar and see all upcoming meetings</h2>

                    <br>

                    <u>Test Case Description</u>
                    &nbsp;&nbsp;-&nbsp;&nbsp;
                    Check whether the application allows the user to view their calendar and see all upcoming meetings 
                    <br><br><br>

                    <u>Expected Result</u>

                    <br><br>

                  User should see all upcoming meetings displayed with correct title, start/end time, and a More Options menu.

                    <br><br><br>

                    Client
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    Katon Meet

                    <br><br>

                    Project
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    Katon Meet

                    <br><br>
                    """)
    def test_GM_101__Calendar_Meetings_107(self, mobile_v2):
        driver = mobile_v2
        wait = WebDriverWait(driver, 30)

        el1 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(0)'
                )
            )
        )
        el1.send_keys("sathees")

        el2 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(1)'
                )
            )
        )
        el2.send_keys("test@1234")

        el3 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(7)'
                )
            )
        )
        el3.click()

        el4 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(105)'
                )
            )
        )
        el4.click()

        el5 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(14)'
                )
            )
        )
        el5.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Calendar")
    @allure.description_html("""
                        <h2>Verify that the user can access the calendar and navigate back to today’s view using the "Today" button.</h2>

                        <br>

                        <u>Test Case Description</u>
                        &nbsp;&nbsp;-&nbsp;&nbsp;
                        Check whether the application allows the user to access the calendar and navigate back to today’s view using the "Today" button. 
                        <br><br><br>

                        <u>Expected Result</u>

                        <br><br>

                      User should see the calendar view navigate to the current day when the Today button is clicked..

                        <br><br><br>

                        Client
                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                        Katon Meet

                        <br><br>

                        Project
                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                        Katon Meet

                        <br><br>
                        """)
    def test_GM_103__Calendar_Navigation_111(self, mobile_v2):
        driver = mobile_v2
        wait = WebDriverWait(driver, 30)

        el1 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(0)'
                )
            )
        )
        el1.send_keys("sathees")

        el2 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(1)'
                )
            )
        )
        el2.send_keys("test@1234")

        el3 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(7)'
                )
            )
        )
        el3.click()

        el4 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(105)'
                )
            )
        )
        el4.click()

        el5 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().text("W")'
                )
            )
        )
        el5.click()

        el6 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().text("Today")'
                )
            )
        )
        el6.click()

        el7 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().text("T").instance(0)'
                )
            )
        )
        el7.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Meeting")
    @allure.description_html("""
                            <h2>Verify that the host's video tile is displayed in the center of the screen when the meeting launches</h2>

                            <br>

                            <u>Test Case Description</u>
                            &nbsp;&nbsp;-&nbsp;&nbsp;
                           Check whether the host's video tile is displayed in the center of the screen when the meeting launches.  
. 
                            <br><br><br>

                            <u>Expected Result</u>

                            <br><br>

                          User should be able to see the host's video tile displayed in the center of the screen  
.

                            <br><br><br>

                            Client
                            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                            Katon Meet

                            <br><br>

                            Project
                            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                            Katon Meet

                            <br><br>
                            """)
    def test_GM_75__Meeting_Activespeaker_138(self, mobile_v2):
        driver = mobile_v2
        wait = WebDriverWait(driver, 30)

        el1 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(0)'
                )
            )
        )
        el1.send_keys("sathees")

        el2 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(1)'
                )
            )
        )
        el2.send_keys("test@1234")

        el3 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(7)'
                )
            )
        )
        el3.click()

        el4 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(81)'
                )
            )
        )
        el4.click()

        el5 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(4)'
                )
            )
        )
        el5.click()

        el6 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ID,
                    "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
                )
            )
        )
        el6.click()

        el7 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ID,
                    "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
                )
            )
        )
        el7.click()

        el8 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(12)'
                )
            )
        )
        el8.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Forgot Password")
    @allure.description_html("""
                                <h2>Verify navigation to Forgot Password screen
                                <br>

                                <u>Test Case Description</u>
                                &nbsp;&nbsp;-&nbsp;&nbsp;
                              Check navigation from Sign In to Forgot Password screen.  
    . 
                                <br><br><br>

                                <u>Expected Result</u>

                                <br><br>

                              User should be able to navigate to the forgot password screen  
    .

                                <br><br><br>

                                Client
                                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                Katon Meet

                                <br><br>

                                Project
                                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                Katon Meet

                                <br><br>
                                """)
    def test_KBM_14__Forgot_Password_Forgot_password_screen_14(self, mobile_v2):
        driver = mobile_v2
        wait = WebDriverWait(driver, 30)

        el1 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().text("Forgot Username / Password?")'
                )
            )
        )
        el1.click()

        el2 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.CLASS_NAME,
                    "android.widget.ScrollView"
                )
            )
        )
        el2.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Meeting")
    @allure.description_html("""
                                   <h2>Verify that the user can successfully initiate an instant meeting when camera and microphone permissions are already granted.
                                   <br>

                                   <u>Test Case Description</u>
                                   &nbsp;&nbsp;-&nbsp;&nbsp;
                                Check whether the user is able to start an instant meeting when camera and microphone permissions are already granted  
       . 
                                   <br><br><br>

                                   <u>Expected Result</u>

                                   <br><br>

                                 User should be taken directly to the live meeting screen instantly.  
       .

                                   <br><br><br>

                                   Client
                                   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                   Katon Meet

                                   <br><br>

                                   Project
                                   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                   Katon Meet

                                   <br><br>
                                   """)
    def test_GM_716__Meeting_Permissions_236(self, mobile_v2):
        driver = mobile_v2
        wait = WebDriverWait(driver, 30)

        el1 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(0)'
                )
            )
        )
        el1.send_keys("sathees")

        el2 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(1)'
                )
            )
        )
        el2.send_keys("test@1234")

        el3 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(7)'
                )
            )
        )
        el3.click()

        el4 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(81)'
                )
            )
        )
        el4.click()

        el5 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().text("Instant Meeting")'
                )
            )
        )
        el5.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Meeting")
    @allure.description_html("""
                                      <h2>Verify turning video ON
                                      <br>

                                      <u>Test Case Description</u>
                                      &nbsp;&nbsp;-&nbsp;&nbsp;
                                   Check whether the user can able to turn on their video  
          . 
                                      <br><br><br>

                                      <u>Expected Result</u>

                                      <br><br>

                                    User should be able to start video during call  
          .

                                      <br><br><br>

                                      Client
                                      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                      Katon Meet

                                      <br><br>

                                      Project
                                      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                      Katon Meet

                                      <br><br>
                                      """)
    def test_KBM_45__Enable_disable_video_video_icon_52(self, mobile_v2):
        driver = mobile_v2
        wait = WebDriverWait(driver, 30)

        el1 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(0)'
                )
            )
        )
        el1.send_keys("sathees")

        el2 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(1)'
                )
            )
        )
        el2.send_keys("test@1234")

        el3 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(7)'
                )
            )
        )
        el3.click()

        el4 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(81)'
                )
            )
        )
        el4.click()

        el5 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().text("Instant Meeting")'
                )
            )
        )
        el5.click()

        el6 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(23)'
                )
            )
        )
        el6.click()

        el7 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(26)'
                )
            )
        )
        el7.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Meeting")
    @allure.description_html("""
                                        <h2>Verify mute functionality
                                        <br>

                                        <u>Test Case Description</u>
                                        &nbsp;&nbsp;-&nbsp;&nbsp;
                                     Check whether User should be able to mute audio during call  
            . 
                                        <br><br><br>

                                        <u>Expected Result</u>

                                        <br><br>

                                     User should be able to mute their audio and the other's audio has to be heard 
            .

                                        <br><br><br>

                                        Client
                                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                        Katon Meet

                                        <br><br>

                                        Project
                                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                        Katon Meet

                                        <br><br>
                                        """)
    def test_KBM_43__Mute_unmute_audio_audio_icon_61(self, mobile_v2):
        driver = mobile_v2
        wait = WebDriverWait(driver, 30)

        el1 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(0)'
                )
            )
        )
        el1.send_keys("sathees")

        el2 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(1)'
                )
            )
        )
        el2.send_keys("test@1234")

        el3 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(7)'
                )
            )
        )
        el3.click()

        el4 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(81)'
                )
            )
        )
        el4.click()

        el5 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().text("Instant Meeting")'
                )
            )
        )
        el5.click()

        el6 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(21)'
                )
            )
        )
        el6.click()

        el7 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(20)'
                )
            )
        )
        el7.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Meeting")
    @allure.description_html("""
                                          <h2>Verify users can send chat messages during call
                                          <br>

                                          <u>Test Case Description</u>
                                          &nbsp;&nbsp;-&nbsp;&nbsp;
                                       Check whether the user can able to send a message during the call 
              . 
                                          <br><br><br>

                                          <u>Expected Result</u>

                                          <br><br>

                                       User can able to send the message during the call 
              .

                                          <br><br><br>

                                          Client
                                          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                          Katon Meet

                                          <br><br>

                                          Project
                                          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                          Katon Meet

                                          <br><br>
                                          """)
    def test_KBM_53__Chat_chat_field_70(self, mobile_v2):
        driver = mobile_v2
        wait = WebDriverWait(driver, 30)

        el1 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(0)'
                )
            )
        )
        el1.send_keys("sathees")

        el2 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(1)'
                )
            )
        )
        el2.send_keys("test@1234")

        el3 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(7)'
                )
            )
        )
        el3.click()

        el4 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.XPATH,
                    "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[2]/android.view.View/android.view.View/android.view.View"
                )
            )
        )
        el4.click()

        el5 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().text("Instant Meeting")'
                )
            )
        )
        el5.click()

        el6 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(27)'
                )
            )
        )
        el6.click()

        el7 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().description("More Actions").instance(3)'
                )
            )
        )
        el7.click()

        el9 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.CLASS_NAME,
                    "android.widget.EditText"
                )
            )
        )
        el9.click()

        el10 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.CLASS_NAME,
                    "android.widget.EditText"
                )
            )
        )
        el10.send_keys("test")

        el11 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(11)'
                )
            )
        )
        el11.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Settings")
    @allure.description_html("""
                                             <h2>Verify that tapping the "Settings" button navigates the user to the dedicated settings page
                                             <br>

                                             <u>Test Case Description</u>
                                             &nbsp;&nbsp;-&nbsp;&nbsp;
                                         Check whether tapping the "Settings" button navigates the user to the dedicated settings page
                 . 
                                             <br><br><br>

                                             <u>Expected Result</u>

                                             <br><br>

                                          User should be able to navigate to the dedicated settings page by tapping the "Settings" button 
                 .

                                             <br><br><br>

                                             Client
                                             &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                             Katon Meet

                                             <br><br>

                                             Project
                                             &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                             Katon Meet

                                             <br><br>
                                             """)
    def test_GM_136__Settings_Account_102(self, mobile_v2):
        driver = mobile_v2
        wait = WebDriverWait(driver, 30)

        el1 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(0)'
                )
            )
        )
        el1.send_keys("sathees")

        el2 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(1)'
                )
            )
        )
        el2.send_keys("test@1234")

        el3 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(7)'
                )
            )
        )
        el3.click()

        el4 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(13)'
                )
            )
        )
        el4.click()

        el5 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.CLASS_NAME,
                    "android.widget.ScrollView"
                )
            )
        )
        el5.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Settings")
    @allure.description_html("""
                                                 <h2>Verify that tapping the "Change Password" menu item navigates the user to the dedicated Change Password page
                                                 <br>

                                                 <u>Test Case Description</u>
                                                 &nbsp;&nbsp;-&nbsp;&nbsp;
                                            Check that tapping the "Change Password" menu item navigates the user to the dedicated Change Password page
                     . 
                                                 <br><br><br>

                                                 <u>Expected Result</u>

                                                 <br><br>

                                             User should be able to tapping the "Change Password" menu item navigates the user to the dedicated Change Password page 
                     .

                                                 <br><br><br>

                                                 Client
                                                 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                                 Katon Meet

                                                 <br><br>

                                                 Project
                                                 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                                 Katon Meet

                                                 <br><br>
                                                 """)
    def test_GM_148__Settings_Password_124(self, mobile_v2):
        driver = mobile_v2
        wait = WebDriverWait(driver, 30)

        el1 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(0)'
                )
            )
        )
        el1.send_keys("sathees")

        el2 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(1)'
                )
            )
        )
        el2.send_keys("test@1234")

        el3 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(7)'
                )
            )
        )
        el3.click()

        el4 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(13)'
                )
            )
        )
        el4.click()

        el5 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.CLASS_NAME,
                    "android.widget.ScrollView"
                )
            )
        )
        el5.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Settings")
    @allure.description_html("""
                                                     <h2>Verify that the Settings page displays a notification toggle button
                                                     <br>

                                                     <u>Test Case Description</u>
                                                     &nbsp;&nbsp;-&nbsp;&nbsp;
                                                Check whether  the Settings page displays a notification toggle button
                         . 
                                                     <br><br><br>

                                                     <u>Expected Result</u>

                                                     <br><br>

                                                 User should be able to see Settings page displays a notification toggle button
                         .

                                                     <br><br><br>

                                                     Client
                                                     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                                     Katon Meet

                                                     <br><br>

                                                     Project
                                                     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                                     Katon Meet

                                                     <br><br>
                                                     """)
    def test_GM_146__Meeting_Videotitle_129(self, mobile_v2):
        driver = mobile_v2
        wait = WebDriverWait(driver, 30)

        el1 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(0)'
                )
            )
        )
        el1.send_keys("sathees")
        el1.send_keys("sathees")

        el2 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(1)'
                )
            )
        )
        el2.send_keys("test@1234")

        el3 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(7)'
                )
            )
        )
        el3.click()

        el4 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(13)'
                )
            )
        )
        el4.click()

        el5 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(15)'
                )
            )
        )
        el5.click()

        el6 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().text("Notifications may include alerts, sounds, and icon badges. These can be configured in Settings.")'
                )
            )
        )
        el6.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Captions")
    @allure.description_html("""
                                                         <h2>Verify that tapping the CC icon toggles captions on
                                                         <br>

                                                         <u>Test Case Description</u>
                                                         &nbsp;&nbsp;-&nbsp;&nbsp;
                                                    Check whether tapping the CC icon toggles captions on properly
                             . 
                                                         <br><br><br>

                                                         <u>Expected Result</u>

                                                         <br><br>

                                                     Captions are enabled and displayed on the video
                             .

                                                         <br><br><br>

                                                         Client
                                                         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                                         Katon Meet

                                                         <br><br>

                                                         Project
                                                         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                                         Katon Meet

                                                         <br><br>
                                                         """)
    def test_GM_1222__Captions_Toggle_354(self, mobile_v2):
        driver = mobile_v2
        wait = WebDriverWait(driver, 30)

        el1 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(0)'
                )
            )
        )
        el1.send_keys("sathees")

        el2 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(1)'
                )
            )
        )
        el2.send_keys("test@1234")

        el3 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(7)'
                )
            )
        )
        el3.click()

        el4 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(81)'
                )
            )
        )
        el4.click()

        el5 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(4)'
                )
            )
        )
        el5.click()

        el6 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ID,
                    "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
                )
            )
        )
        el6.click()

        el7 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ID,
                    "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
                )
            )
        )
        el7.click()

        el8 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(27)'
                )
            )
        )
        el8.click()

        el9 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(27)'
                )
            )
        )
        el9.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Captions")
    @allure.description_html("""
                                                             <h2>Verify that the user can select a caption language from the list
                                                             <br>

                                                             <u>Test Case Description</u>
                                                             &nbsp;&nbsp;-&nbsp;&nbsp;
                                                        Check whether the user can select a caption language from the list successfully
                                 . 
                                                             <br><br><br>

                                                             <u>Expected Result</u>

                                                             <br><br>

                                                         Selected caption language is applied to the video immediately
                                 .

                                                             <br><br><br>

                                                             Client
                                                             &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                                             Katon Meet

                                                             <br><br>

                                                             Project
                                                             &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                                             Katon Meet

                                                             <br><br>
                                                             """)
    def test_GM_1222__Captions_Toggle_359(self, mobile_v2):
        driver = mobile_v2
        wait = WebDriverWait(driver, 30)

        el1 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(0)'
                )
            )
        )
        el1.send_keys("sathees")

        el2 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(1)'
                )
            )
        )
        el2.send_keys("test@1234")

        el3 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(7)'
                )
            )
        )
        el3.click()

        el4 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(81)'
                )
            )
        )
        el4.click()

        el5 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(4)'
                )
            )
        )
        el5.click()

        el6 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ID,
                    "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
                )
            )
        )
        el6.click()

        el7 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ID,
                    "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
                )
            )
        )
        el7.click()

        el8 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(27)'
                )
            )
        )
        el8.click()

        el9 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(27)'
                )
            )
        )
        el9.click()

        el10 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(14)'
                )
            )
        )
        el10.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Host Controls")
    @allure.description_html("""
                                                             <h2>Verify the visibility of 'Host Controls' in the More Options panel
                                                             <br>

                                                             <u>Test Case Description</u>
                                                             &nbsp;&nbsp;-&nbsp;&nbsp;
                                                        Verify that the 'Host Controls' option is visible to the host user in the More Options panel during an active meeting.
                                 . 
                                                             <br><br><br>

                                                             <u>Expected Result</u>

                                                             <br><br>

                                                         Host Controls' option is visible in the More Options menu
                                 .

                                                             <br><br><br>

                                                             Client
                                                             &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                                             Katon Meet

                                                             <br><br>

                                                             Project
                                                             &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                                             Katon Meet

                                                             <br><br>
                                                             """)
    def test_GM_1366__Meeting_HostControls_390(self, mobile_v2):
        driver = mobile_v2
        wait = WebDriverWait(driver, 30)

        el1 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(0)'
                )
            )
        )
        el1.send_keys("sathees")

        el2 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(1)'
                )
            )
        )
        el2.send_keys("test@1234")

        el3 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(7)'
                )
            )
        )
        el3.click()
        el3.click()

        el4 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(81)'
                )
            )
        )
        el4.click()

        el5 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().text("Instant Meeting")'
                )
            )
        )
        el5.click()

        el6 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(27)'
                )
            )
        )
        el6.click()

        el7 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(24)'
                )
            )
        )
        el7.click()

        el8 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(7)'
                )
            )
        )
        el8.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Meeting Layout")
    @allure.description_html("""
                                                                <h2>Verify that the meeting launches in the default gallery view upon meeting start.
                                                                <br>

                                                                <u>Test Case Description</u>
                                                                &nbsp;&nbsp;-&nbsp;&nbsp;
                                                           Verify that the meeting launches in Gallery View by default for the host..
                                    . 
                                                                <br><br><br>

                                                                <u>Expected Result</u>

                                                                <br><br>

                                                            The meeting opens in the default view (Gallery View) without requiring manual selection.

                                    .

                                                                <br><br><br>

                                                                Client
                                                                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                                                Katon Meet

                                                                <br><br>

                                                                Project
                                                                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                                                Katon Meet

                                                                <br><br>
                                                                """)
    def test_GM_539__Meeting_Layout_403(self, mobile_v2):
        driver = mobile_v2
        wait = WebDriverWait(driver, 30)

        el1 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(0)'
                )
            )
        )
        el1.send_keys("sathees")

        el2 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(1)'
                )
            )
        )
        el2.send_keys("test@1234")

        el3 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(7)'
                )
            )
        )
        el3.click()

        el4 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(81)'
                )
            )
        )
        el4.click()

        el5 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(4)'
                )
            )
        )
        el5.click()

        el6 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(12)'
                )
            )
        )
        el6.click()

        el7 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(27)'
                )
            )
        )
        el7.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Meeting Layout")
    @allure.description_html("""
                                                                    <h2>Verify accessibility of the Layout option in the More Options menu..
                                                                    <br>

                                                                    <u>Test Case Description</u>
                                                                    &nbsp;&nbsp;-&nbsp;&nbsp;
                                                               Verify that the 'Layout' option is accessible via the meeting's More Options (three-dot) menu
                                        . 
                                                                    <br><br><br>

                                                                    <u>Expected Result</u>

                                                                    <br><br>

                                                               "The Layout option is visible and accessible in the More Options menu. Host can click on it without errors"

                                        .

                                                                    <br><br><br>

                                                                    Client
                                                                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                                                    Katon Meet

                                                                    <br><br>

                                                                    Project
                                                                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                                                    Katon Meet

                                                                    <br><br>
                                                                    """)
    def test_GM_539__Meeting_Layout_401(self, mobile_v2):
        driver = mobile_v2
        wait = WebDriverWait(driver, 30)

        el1 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(0)'
                )
            )
        )
        el1.send_keys("sathees")

        el2 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(1)'
                )
            )
        )
        el2.send_keys("test@1234")

        el3 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(7)'
                )
            )
        )
        el3.click()

        el4 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(81)'
                )
            )
        )
        el4.click()

        el5 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(4)'
                )
            )
        )
        el5.click()

        el6 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(12)'
                )
            )
        )
        el6.click()

        el7 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(27)'
                )
            )
        )
        el7.click()

        el8 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(30)'
                )
            )
        )
        el8.click()

        el9 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(13)'
                )
            )
        )
        el9.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Meeting Layout")
    @allure.description_html("""
                                                                       <h2>Verify availability of viewing modes (Gallery View, Spotlight View) in the Layout menu.
                                                                       <br>

                                                                       <u>Test Case Description</u>
                                                                       &nbsp;&nbsp;-&nbsp;&nbsp;
                                                                  Verify that the system provides 'Gallery View' and 'Spotlight View' options within the Layout menu.
                                           . 
                                                                       <br><br><br>

                                                                       <u>Expected Result</u>

                                                                       <br><br>

                                                                  "Both Gallery View and Spotlight View options are displayed and selectable in the Layout menu"


                                           .

                                                                       <br><br><br>

                                                                       Client
                                                                       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                                                       Katon Meet

                                                                       <br><br>

                                                                       Project
                                                                       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                                                       Katon Meet

                                                                       <br><br>
                                                                       """)
    def test_GM_539__Meeting_Layout_402(self, mobile_v2):
        driver = mobile_v2
        wait = WebDriverWait(driver, 30)

        el1 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(0)'
                )
            )
        )
        el1.send_keys("sathees")

        el2 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(1)'
                )
            )
        )
        el2.send_keys("test@1234")

        el3 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(7)'
                )
            )
        )
        el3.click()

        el4 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(81)'
                )
            )
        )
        el4.click()

        el5 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(4)'
                )
            )
        )
        el5.click()

        el6 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(12)'
                )
            )
        )
        el6.click()

        el7 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(27)'
                )
            )
        )
        el7.click()

        el8 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(30)'
                )
            )
        )
        el8.click()

        el9 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(13)'
                )
            )
        )
        el9.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Meeting Layout")
    @allure.description_html("""
                                                                           <h2>Verify the ability to toggle from Gallery View to Spotlight View.
                                                                           <br>

                                                                           <u>Test Case Description</u>
                                                                           &nbsp;&nbsp;-&nbsp;&nbsp;
                                                                      Verify the host can successfully switch from Gallery View to Spotlight View.
                                               . 
                                                                           <br><br><br>

                                                                           <u>Expected Result</u>

                                                                           <br><br>

                                                                      Clicking the toggle successfully switches the meeting from Gallery View to Spotlight View, updating the layout immediately
                                                                           <br><br><br>

                                                                           Client
                                                                           &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                                                           Katon Meet

                                                                           <br><br>

                                                                           Project
                                                                           &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                                                           Katon Meet

                                                                           <br><br>
                                                                           """)
    def test_GM_539__Meeting_Layout_410(self, mobile_v2):
        driver = mobile_v2
        wait = WebDriverWait(driver, 30)

        el1 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(0)'
                )
            )
        )
        el1.send_keys("sathees")

        el2 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(1)'
                )
            )
        )
        el2.send_keys("test@1234")

        el3 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(7)'
                )
            )
        )
        el3.click()

        el4 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(81)'
                )
            )
        )
        el4.click()

        el5 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(4)'
                )
            )
        )
        el5.click()

        el6 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(12)'
                )
            )
        )
        el6.click()

        el7 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(27)'
                )
            )
        )
        el7.click()

        el8 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(30)'
                )
            )
        )
        el8.click()

        el9 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(13)'
                )
            )
        )
        el9.click()
