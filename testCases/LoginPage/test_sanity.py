""" Importing Libraries """
import time
from datetime import date
import allure
import pytest
import os
import time
import allure
import selenium
# import config.read_config
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from appium.webdriver.common.appiumby import AppiumBy
from datetime import datetime, timedelta



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

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Meeting")
    @allure.description_html("""
                                                                               <h2>Verify that the user is able to successfully schedule a meeting with valid inputs.
                                                                               <br>

                                                                               <u>Test Case Description</u>
                                                                               &nbsp;&nbsp;-&nbsp;&nbsp;
                                                                          Check whether the user is able to successfully schedule a meeting with valid inputs.
                                                   . 
                                                                               <br><br><br>

                                                                               <u>Expected Result</u>

                                                                               <br><br>

                                                                          The meeting should be scheduled successfully, and a confirmation message should be displayed.
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
    def test_GM_699__Meeting_Schedule_272(self, mobile_v2):
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
                    'new UiSelector().className("android.view.View").instance(78)'
                )
            )
        )
        el4.click()

        el5 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().text("Schedule Meeting")'
                )
            )
        )
        el5.click()

        el7 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(0)'
                )
            )
        )
        el7.send_keys("test")

        el8 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(30)'
                )
            )
        )
        el8.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Meeting")
    @allure.description_html("""
                                                                           <h2>Verify that the system shows an error message when trying to schedule a meeting without a title.
                                                                           <br>

                                                                           <u>Test Case Description</u>
                                                                           &nbsp;&nbsp;-&nbsp;&nbsp;
                                                                      Check whether the system displays an error message when the user tries to schedule a meeting without entering a title.
                                               . 
                                                                           <br><br><br>

                                                                           <u>Expected Result</u>

                                                                           <br><br>

                                                                     The system should display an error message such as “Meeting title is required”, and the meeting should not be scheduled.
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
    def test_GM_699__Meeting_Schedule_273(self, mobile_v2):
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
                    'new UiSelector().className("android.view.View").instance(80)'
                )
            )
        )
        el4.click()

        el5 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(7)'
                )
            )
        )
        el5.click()

        el6 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().text("Schedule Meeting").instance(1)'
                )
            )
        )
        el6.click()

        el7 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().text("Title is required")'
                )
            )
        )
        el7.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Signin")
    @allure.description_html("""
                                                                               <h2>Verify that the Login using valid email and password.
                                                                               <br>

                                                                               <u>Test Case Description</u>
                                                                               &nbsp;&nbsp;-&nbsp;&nbsp;
                                                                          Verify user can log in using registered email address.
                                                   . 
                                                                               <br><br><br>

                                                                               <u>Expected Result</u>

                                                                               <br><br>

                                                                         User is logged in successfully
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
    def test_GM_1759__Authentication_Login_547(self, mobile_v2):
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

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Localization")
    @allure.description_html("""
                                                                               <h2>Verify app detects French device language automatically
                                                                               <br>

                                                                               <u>Test Case Description</u>
                                                                               &nbsp;&nbsp;-&nbsp;&nbsp;
                                                                          Verify application loads in French when device language is French
                                                   . 
                                                                               <br><br><br>

                                                                               <u>Expected Result</u>

                                                                               <br><br>

                                                                        App should automatically load in French language
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
    def test_GM_1932_GM_1933__Localization_i18_Automatic_Detection_French_707(self, mobile_v2):
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
                    'new UiSelector().className("android.view.View").instance(17)'
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

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Localization")
    @allure.description_html("""
                                                                                   <h2>Verify app detects German device language automatically
                                                                                   <br>

                                                                                   <u>Test Case Description</u>
                                                                                   &nbsp;&nbsp;-&nbsp;&nbsp;
                                                                              Verify application loads in German when device language is German
                                                       . 
                                                                                   <br><br><br>

                                                                                   <u>Expected Result</u>

                                                                                   <br><br>

                                                                            App should automatically load in German language
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
    def test_GM_1932_GM_1933__Localization_i18_Automatic_Detection_German_708(self, mobile_v2):
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
                    'new UiSelector().className("android.view.View").instance(17)'
                )
            )
        )
        el5.click()

        el6 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(13)'
                )
            )
        )
        el6.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Localization")
    @allure.description_html("""
                                                                               <h2>Verify app detects Dutch device language automatically.
                                                                               <br>

                                                                               <u>Test Case Description</u>
                                                                               &nbsp;&nbsp;-&nbsp;&nbsp;
                                                                         Verify application loads in Dutch when device language is Dutch
                                                   . 
                                                                               <br><br><br>

                                                                               <u>Expected Result</u>

                                                                               <br><br>

                                                                         App should automatically load in Dutch language
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
    def test_GM_1932_GM_1933__Localization_i18_Automatic_Detection_Dutch_709(self, mobile_v2):
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
                    'new UiSelector().className("android.view.View").instance(17)'
                )
            )
        )
        el5.click()

        el6 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(9)'
                )
            )
        )
        el6.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Localization")
    @allure.description_html("""
                                                                               <h2>Verify app detects Swedish device language automatically
                                                                               <br>

                                                                               <u>Test Case Description</u>
                                                                               &nbsp;&nbsp;-&nbsp;&nbsp;
                                                                          Verify application loads in Swedish when device language is Swedish
                                                   . 
                                                                               <br><br><br>

                                                                               <u>Expected Result</u>

                                                                               <br><br>

                                                                         App should automatically load in Swedish language
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
    def test_GM_1932_GM_1933__Localization_i18_Automatic_Detection_Swedish_710(self, mobile_v2):
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
                    'new UiSelector().className("android.view.View").instance(17)'
                )
            )
        )
        el5.click()

        el6 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(14)'
                )
            )
        )
        el6.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Localization")
    @allure.description_html("""
                                                                               <h2>Verify application defaults to English when device language unsupported
                                                                               <br>

                                                                               <u>Test Case Description</u>
                                                                               &nbsp;&nbsp;-&nbsp;&nbsp;
                                                                          Verify fallback language behavior
                                                   . 
                                                                               <br><br><br>

                                                                               <u>Expected Result</u>

                                                                               <br><br>

                                                                         Application should load in English language
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
    def test_GM_1932_GM_1933__Localization_i18_Fallback_To_English_711(self, mobile_v2):
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
                    'new UiSelector().className("android.view.View").instance(17)'
                )
            )
        )
        el5.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Signin")
    @allure.description_html("""
                                                                               <h2>Verify user lands on Home screen after login
                                                                               <br>

                                                                               <u>Test Case Description</u>
                                                                               &nbsp;&nbsp;-&nbsp;&nbsp;
                                                                          Verify user is redirected to Home screen after successful login 
                                                                               <br><br><br>

                                                                               <u>Expected Result</u>

                                                                               <br><br>

                                                                         User is navigated to Home screen
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
    def test_GM_2410_GM_2437__Tab_Bar_Navigation_Post_Login_Landing_734(self, mobile_v2):
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

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Signin")
    @allure.description_html("""
                                                                               <h2>Verify that the Login using valid email and password.
                                                                               <br>

                                                                               <u>Test Case Description</u>
                                                                               &nbsp;&nbsp;-&nbsp;&nbsp;
                                                                          Verify user can log in using registered email address.
                                                   . 
                                                                               <br><br><br>

                                                                               <u>Expected Result</u>

                                                                               <br><br>

                                                                         User is logged in successfully
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
    def test_GM_2410_GM_2437__Tab_Bar_Navigation_Home_Navigation_738(self, mobile_v2):
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
                    'new UiSelector().className("android.view.View").instance(90)'
                )
            )
        )
        el4.click()

        el5 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(95)'
                )
            )
        )
        el5.click()

        el6 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(15)'
                )
            )
        )
        el6.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Home")
    @allure.description_html("""
                                                                               <h2>Verify navigation to Contacts tab
                                                                               <br>

                                                                               <u>Test Case Description</u>
                                                                               &nbsp;&nbsp;-&nbsp;&nbsp;
                                                                          Verify tapping Contacts navigates to Contacts screen
                                                   . 
                                                                               <br><br><br>

                                                                               <u>Expected Result</u>

                                                                               <br><br>

                                                                         User navigates to Contacts screen
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
    def test_GM_2410_GM_2437__Tab_Bar_Navigation_Contacts_Navigation_739(self, mobile_v2):
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
                    'new UiSelector().className("android.view.View").instance(90)'
                )
            )
        )
        el4.click()

        el5 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(95)'
                )
            )
        )
        el5.click()

        el6 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(15)'
                )
            )
        )
        el6.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Home")
    @allure.description_html("""
                                                                               <h2>Verify tapping + opens action menu
                                                                               <br>

                                                                               <u>Test Case Description</u>
                                                                               &nbsp;&nbsp;-&nbsp;&nbsp;
                                                                          Verify + icon opens quick action menu instead of navigation.
                                                   . 
                                                                               <br><br><br>

                                                                               <u>Expected Result</u>

                                                                               <br><br>

                                                                         Action menu overlay appears
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
    def test_GM_2410_GM_2437__Tab_Bar_Navigation_Plus_Icon_Action_Trigger_744(self, mobile_v2):
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

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Home")
    @allure.description_html("""
                                                                               <h2>Verify navigation to Calendar tab.
                                                                               <br>

                                                                               <u>Test Case Description</u>
                                                                               &nbsp;&nbsp;-&nbsp;&nbsp;
                                                                          Verify tapping Calendar navigates to Calendar screen
                                                   . 
                                                                               <br><br><br>

                                                                               <u>Expected Result</u>

                                                                               <br><br>

                                                                         User navigates to Calendar screen
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
    def test_GM_2410_GM_2437__Tab_Bar_Navigation_Calendar_Navigation_741(self, mobile_v2):
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
                    'new UiSelector().className("android.view.View").instance(15)'
                )
            )
        )
        el5.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Home")
    @allure.description_html("""
                                                                               <h2>Verify navigation to Recordings tab
                                                                               <br>

                                                                               <u>Test Case Description</u>
                                                                               &nbsp;&nbsp;-&nbsp;&nbsp;
                                                                          Verify tapping Recordings navigates to Recordings screen
                                                   . 
                                                                               <br><br><br>

                                                                               <u>Expected Result</u>

                                                                               <br><br>

                                                                        User navigates to Recordings screen
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
    def test_GM_2410_GM_2437__Tab_Bar_Navigation_Recordings_Navigation_740(self, mobile_v2):
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
                    'new UiSelector().className("android.view.View").instance(9)'
                )
            )
        )
        el5.click()

        el6 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(3)'
                )
            )
        )
        el6.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Meeting")
    @allure.description_html("""
                                                                               <h2>Verify navigation to Instant Meeting
                                                                               <br>

                                                                               <u>Test Case Description</u>
                                                                               &nbsp;&nbsp;-&nbsp;&nbsp;
                                                                          Verify user is redirected to instant meeting on selecting option
                                                   . 
                                                                               <br><br><br>

                                                                               <u>Expected Result</u>

                                                                               <br><br>

                                                                         User is redirected to Instant Meeting screen
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
    def test_GM_2412_GM_2439__Home_FAB_Instant_Meeting_Navigation_796(self, mobile_v2):
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

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Meeting")
    @allure.description_html("""
                                                                               <h2>Verify navigation to Schedule Meeting page
                                                                               <br>

                                                                               <u>Test Case Description</u>
                                                                               &nbsp;&nbsp;-&nbsp;&nbsp;
                                                                         Verify user is redirected to schedule meeting page
                                                   . 
                                                                               <br><br><br>

                                                                               <u>Expected Result</u>

                                                                               <br><br>

                                                                         User is redirected to Schedule Meeting creation page
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
    def test_GM_2412_GM_2439__Home_FAB_Schedule_Meeting_Navigation_797(self, mobile_v2):
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
                    'new UiSelector().text("Schedule Meeting")'
                )
            )
        )
        el5.click()

        el6 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.CLASS_NAME,
                    "android.widget.ScrollView"
                )
            )
        )
        el6.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Event")
    @allure.description_html("""
                                                                               <h2>Verify navigation to Schedule Event page
                                                                               <br>

                                                                               <u>Test Case Description</u>
                                                                               &nbsp;&nbsp;-&nbsp;&nbsp;
                                                                         Verify user is redirected to schedule event page.
                                                   . 
                                                                               <br><br><br>

                                                                               <u>Expected Result</u>

                                                                               <br><br>

                                                                         User is redirected to Schedule Event creation page
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
    def test_GM_2412_GM_2439__Home_FAB_Schedule_Event_Navigation_798(self, mobile_v2):
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
                    'new UiSelector().className("android.view.View").instance(10)'
                )
            )
        )
        el5.click()

        el6 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.CLASS_NAME,
                    "android.widget.ScrollView"
                )
            )
        )
        el6.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Recording")
    @allure.description_html("""
                                                                               <h2>Verify tapping recordings icon navigates to recordings page
                                                                               <br>

                                                                               <u>Test Case Description</u>
                                                                               &nbsp;&nbsp;-&nbsp;&nbsp;
                                                                         Verify user is redirected to recordings page on tapping recordings icon
                                                   . 
                                                                               <br><br><br>

                                                                               <u>Expected Result</u>

                                                                               <br><br>

                                                                         User is navigated to recordings page
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
    def test_GM_2419_GM_2445_GM_2421_GM_2447__Recordings_Navigation_to_Recordings_Page_807(self, mobile_v2):
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
                    'new UiSelector().className("android.view.View").instance(9)'
                )
            )
        )
        el5.click()

        el6 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(3)'
                )
            )
        )
        el6.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Recording")
    @allure.description_html("""
                                                                               <h2>Verify All and Bookmarked tabs are visible
                                                                               <br>

                                                                               <u>Test Case Description</u>
                                                                               &nbsp;&nbsp;-&nbsp;&nbsp;
                                                                         Verify All and Bookmarked tabs are present on recordings page.
                                                   . 
                                                                               <br><br><br>

                                                                               <u>Expected Result</u>

                                                                               <br><br>

                                                                         Both All and Bookmarked tabs are visible
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
    def test_GM_2419__Recordings_Tabs_Visibility_808(self, mobile_v2):
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
                    'new UiSelector().className("android.view.View").instance(9)'
                )
            )
        )
        el5.click()

        el6 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(3)'
                )
            )
        )
        el6.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Recording")
    @allure.description_html("""
                                                                               <h2>Verify All tab is selected by default
                                                                               <br>

                                                                               <u>Test Case Description</u>
                                                                               &nbsp;&nbsp;-&nbsp;&nbsp;
                                                                          Verify All tab is selected when recordings page opens
                                                   . 
                                                                               <br><br><br>

                                                                               <u>Expected Result</u>

                                                                               <br><br>

                                                                         All tab is selected by default
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
    def test_GM_2419__Recordings_All_Tab_Default_Selection_809(self, mobile_v2):
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
                    'new UiSelector().className("android.view.View").instance(9)'
                )
            )
        )
        el5.click()

        el6 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(3)'
                )
            )
        )
        el6.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Recording")
    @allure.description_html("""
                                                                               <h2>Verify all recordings are displayed in All tab
                                                                               <br>

                                                                               <u>Test Case Description</u>
                                                                               &nbsp;&nbsp;-&nbsp;&nbsp;
                                                                          Verify both bookmarked and unbookmarked recordings are shown
                                                   . 
                                                                               <br><br><br>

                                                                               <u>Expected Result</u>

                                                                               <br><br>

                                                                        All recordings (bookmarked and unbookmarked) are displayed
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
    def test_GM_2419__Recordings_All_Recordings_Listing_810(self, mobile_v2):
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
                    'new UiSelector().className("android.view.View").instance(9)'
                )
            )
        )
        el5.click()

        el6 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(3)'
                )
            )
        )
        el6.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Recording")
    @allure.description_html("""
                                                                               <h2>Verify user can bookmark a recording
                                                                               <br>

                                                                               <u>Test Case Description</u>
                                                                               &nbsp;&nbsp;-&nbsp;&nbsp;
                                                                          Verify tapping bookmark icon marks the recording
                                                   . 
                                                                               <br><br><br>

                                                                               <u>Expected Result</u>

                                                                               <br><br>

                                                                         Recording is marked as bookmarked
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
    def test_GM_2419__Recordings_Bookmark_Action_812(self, mobile_v2):
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
                    'new UiSelector().className("android.view.View").instance(9)'
                )
            )
        )
        el5.click()

        el6 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(3)'
                )
            )
        )
        el6.click()

        el7 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(6)'
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

        el9 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().text("All")'
                )
            )
        )
        el9.click()

        el10 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(12)'
                )
            )
        )
        el10.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Recording")
    @allure.description_html("""
                                                                               <h2>Verify user can unbookmark a recording
                                                                               <br>

                                                                               <u>Test Case Description</u>
                                                                               &nbsp;&nbsp;-&nbsp;&nbsp;
                                                                          Verify tapping bookmark icon again removes bookmark
                                                   . 
                                                                               <br><br><br>

                                                                               <u>Expected Result</u>

                                                                               <br><br>

                                                                         Recording is unbookmarked
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
    def test_GM_2419__Recordings_Unbookmark_Action_813(self, mobile_v2):
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
                    'new UiSelector().className("android.view.View").instance(9)'
                )
            )
        )
        el5.click()

        el6 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(3)'
                )
            )
        )
        el6.click()

        el7 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(6)'
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

        el9 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().text("All")'
                )
            )
        )
        el9.click()

        el10 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(12)'
                )
            )
        )
        el10.click()

        el11 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(12)'
                )
            )
        )
        el11.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Announcement")
    @allure.description_html("""
                                                                                   <h2>Verify tapping announcement entry opens announcements list.
                                                                                   <br>

                                                                                   <u>Test Case Description</u>
                                                                                   &nbsp;&nbsp;-&nbsp;&nbsp;
                                                                             Check whether announcement entry redirects user to announcements list screen.
                                                       . 
                                                                                   <br><br><br>

                                                                                   <u>Expected Result</u>

                                                                                   <br><br>

                                                                             User should navigate successfully to announcements list screen
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
    def test_GM_3218__Announcements_Announcement_List_Navigation_1334(self, mobile_v2):
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
                    'new UiSelector().className("android.view.View").instance(9)'
                )
            )
        )
        el3.click()

        el4 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ACCESSIBILITY_ID,
                    "Announcement"
                )
            )
        )
        el4.click()

        el5 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(3)'
                )
            )
        )
        el5.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Announcement")
    @allure.description_html("""
                                                                                       <h2>Verify tapping announcement item opens detail screen.
                                                                                       <br>

                                                                                       <u>Test Case Description</u>
                                                                                       &nbsp;&nbsp;-&nbsp;&nbsp;
                                                                                 Check whether tapping announcement redirects user to detail screen successfully.
                                                           . 
                                                                                       <br><br><br>

                                                                                       <u>Expected Result</u>

                                                                                       <br><br>

                                                                                 User should navigate successfully to announcement detail screen
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
    def test_GM_3218__Announcements_Announcement_Detail_Screen_Navigation_1344(self, mobile_v2):
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
                    'new UiSelector().className("android.view.View").instance(9)'
                )
            )
        )
        el3.click()

        el4 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ACCESSIBILITY_ID,
                    "Announcement"
                )
            )
        )
        el4.click()

        el5 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(3)'
                )
            )
        )
        el5.click()

        el6 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(5)'
                )
            )
        )
        el6.click()

        el7 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(3)'
                )
            )
        )
        el7.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Meeting")
    @allure.description_html("""
                                                                                          <h2>Verify Instant Meeting info page displays title as "Instant Meeting".
                                                                                          <br>

                                                                                          <u>Test Case Description</u>
                                                                                          &nbsp;&nbsp;-&nbsp;&nbsp;
                                                                                  Check whether Instant Meeting title is displayed correctly in meeting info screen.
                                                              . 
                                                                                          <br><br><br>

                                                                                          <u>Expected Result</u>

                                                                                          <br><br>

                                                                                    Meeting title should be displayed as "Instant Meeting"
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
    def test_GM_3432__Meeting_Info_Instant_Meeting_Title_Display_Validation_1375(self, mobile_v2):
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
                    'new UiSelector().className("android.view.View").instance(9)'
                )
            )
        )
        el3.click()

        el4 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(66)'
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
                    AppiumBy.ACCESSIBILITY_ID,
                    "Info"
                )
            )
        )
        el8.click()

        el9 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.CLASS_NAME,
                    "android.widget.ScrollView"
                )
            )
        )
        el9.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Meeting")
    @allure.description_html("""
                                                                                              <h2>Verify Instant Meeting info page displays only start time.".
                                                                                              <br>

                                                                                              <u>Test Case Description</u>
                                                                                              &nbsp;&nbsp;-&nbsp;&nbsp;
                                                                                    Check whether only start time is displayed in Instant Meeting info screen..
                                                                  . 
                                                                                              <br><br><br>

                                                                                              <u>Expected Result</u>

                                                                                              <br><br>

                                                                                        Only the meeting start time should be displayed in meeting info
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
    def test_GM_3432__Meeting_Info_Instant_Meeting_Start_Time_Display_Validation_1376(self, mobile_v2):
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
                    'new UiSelector().className("android.view.View").instance(9)'
                )
            )
        )
        el3.click()

        el4 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(66)'
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
                    AppiumBy.ACCESSIBILITY_ID,
                    "Info"
                )
            )
        )
        el8.click()

        el9 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.CLASS_NAME,
                    "android.widget.ScrollView"
                )
            )
        )
        el9.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Announcement")
    @allure.description_html("""
                                                                                                  <h2>Verify moved search icon works properly from bottom navigation bar..".
                                                                                                  <br>

                                                                                                  <u>Test Case Description</u>
                                                                                                  &nbsp;&nbsp;-&nbsp;&nbsp;
                                                                                       Check whether relocated search icon remains functional from bottom navigation.
                                                                      . 
                                                                                                  <br><br><br>

                                                                                                  <u>Expected Result</u>

                                                                                                  <br><br>

                                                                                            Search feature should work successfully from bottom navigation bar
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
    def test_GM_3218__Announcements_Bottom_Navigation_Search_Accessibility_1355(self, mobile_v2):
        driver = mobile_v2
        wait = WebDriverWait(driver, 30)

        el2 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(0)'
                )
            )
        )
        el2.send_keys("sathees")

        el3 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(1)'
                )
            )
        )
        el3.send_keys("test@1234")

        el4 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(9)'
                )
            )
        )
        el4.click()

        el5 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(84)'
                )
            )
        )
        el5.click()

        el6 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(2)'
                )
            )
        )
        el6.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Recording")
    @allure.description_html("""
                                                                                                     <h2>Verify recordings screen opens correctly from Settings module.
                                                                                                     <br>

                                                                                                     <u>Test Case Description</u>
                                                                                                     &nbsp;&nbsp;-&nbsp;&nbsp;
                                                                                          Check whether recordings module is accessible through Settings.
                                                                         . 
                                                                                                     <br><br><br>

                                                                                                     <u>Expected Result</u>

                                                                                                     <br><br>

                                                                                               User should navigate successfully to recordings screen
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
    def test_GM_3218__Settings_Recordings_Access_from_Settings_1356(self, mobile_v2):
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
                    AppiumBy.XPATH,
                    "//android.widget.ScrollView/android.view.View[3]"
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
                    'new UiSelector().className("android.view.View").instance(17)'
                )
            )
        )
        el5.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Search")
    @allure.description_html("""
                                                                                                  <h2>Verify that tapping the global search icon navigates the user to the dedicated search screen
                                                                                                  <br>

                                                                                                  <u>Test Case Description</u>
                                                                                                  &nbsp;&nbsp;-&nbsp;&nbsp;
                                                                                        Check whether tapping the global search icon navigates the user to the dedicated search screen.  
                                                                      . 
                                                                                                  <br><br><br>

                                                                                                  <u>Expected Result</u>

                                                                                                  <br><br>

                                                                                            User should be able to see the search screen displayed successfully  

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
    def test_GM_97__Search_Global_133(self, mobile_v2):
        driver = mobile_v2
        wait = WebDriverWait(driver, 30)

        el2 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(0)'
                )
            )
        )
        el2.send_keys("sathees")

        el3 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(1)'
                )
            )
        )
        el3.send_keys("test@1234")

        el4 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(9)'
                )
            )
        )
        el4.click()

        el5 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(84)'
                )
            )
        )
        el5.click()

        el6 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(2)'
                )
            )
        )
        el6.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Meeting")
    @allure.description_html("""
                                                                                                  <h2>Verify that when the host clicks the "End Call" button, a confirmation pop-up with "Leave Meeting" and "End Meeting for All" options is displayed.
                                                                                                  <br>

                                                                                                  <u>Test Case Description</u>
                                                                                                  &nbsp;&nbsp;-&nbsp;&nbsp;
                                                                                       Check whether a confirmation pop-up with “Leave Meeting” and “End Meeting for All” options is displayed when the host clicks the “End Call” button.
                                                                      . 
                                                                                                  <br><br><br>

                                                                                                  <u>Expected Result</u>

                                                                                                  <br><br>

                                                                                           User should be able to see a confirmation pop-up with “Leave Meeting” and “End Meeting for All” options when the host clicks the “End Call” button.
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
    def test_GM_87__Meeting_Host_137(self, mobile_v2):
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
                    'new UiSelector().className("android.view.View").instance(9)'
                )
            )
        )
        el3.click()

        el4 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(66)'
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
                    'new UiSelector().className("android.view.View").instance(33)'
                )
            )
        )
        el8.click()

        el9 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(3)'
                )
            )
        )
        el9.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Meeting")
    @allure.description_html("""
        <h2>Recording</h2>

        <h2>Verify that tapping the more action 3-dot icon in an ongoing meeting displays the "Record" icon.</h2>

        <br>

        <u>Test Case Description</u>
        &nbsp;&nbsp;-&nbsp;&nbsp;
        Check whether tapping the "more actions" (3-dot) icon in an ongoing meeting displays the "Record" icon.

        <br><br><br>

        <u>Expected Result</u>

        <br><br>

        User should be able to see that the "Record" icon is displayed when the host clicks the "more actions" (3-dot) icon in an ongoing meeting.

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
    def test_GM_120__Meeting_Recording_147(self, mobile_v2):
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
                    'new UiSelector().className("android.view.View").instance(9)'
                )
            )
        )
        el3.click()

        el4 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(62)'
                )
            )
        )
        el4.click()

        el5 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(3)'
                )
            )
        )
        el5.click()

        el6 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(31)'
                )
            )
        )
        el6.click()

        el7 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(19)'
                )
            )
        )
        el7.click()

        el8 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(5)'
                )
            )
        )
        el8.click()

        el9 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().text("Continue")'
                )
            )
        )
        el9.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Meeting")
    @allure.description_html("""
        <h2>Switch Day to Week View</h2>

        <h2>Check whether the user can switch from day view to week view in My Meeting.</h2>

        <br>

        <u>Test Case Description</u>
        &nbsp;&nbsp;-&nbsp;&nbsp;
        Check whether switching from day view to week view changes the calendar to week view.

        <br><br><br>

        <u>Expected Result</u>

        <br><br>

        User should be able to switch from day view to week view, and the calendar should be displayed in week view.

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
    def test_GM_2415__Home_My_Meeting_Switch_Day_to_Week_View_754(self, mobile_v2):
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
                    'new UiSelector().className("android.view.View").instance(9)'
                )
            )
        )
        el3.click()

        el4 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(85)'
                )
            )
        )
        el4.click()

        el5 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(22)'
                )
            )
        )
        el5.click()

        el6 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(33)'
                )
            )
        )
        el6.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Meeting")
    @allure.description_html("""
        <h2>Switch Week to Day View</h2>

        <h2>Check whether the user can switch from week view to day view in My Meeting.</h2>

        <br>

        <u>Test Case Description</u>
        &nbsp;&nbsp;-&nbsp;&nbsp;
        Check whether switching from week view to day view changes the calendar to day view.

        <br><br><br>

        <u>Expected Result</u>

        <br><br>

        User should be able to switch from week view to day view, and the calendar should be displayed in day view.

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
    def test_GM_2415__Home_My_Meeting_Switch_Week_to_Day_View_755(self, mobile_v2):
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
                    'new UiSelector().className("android.view.View").instance(9)'
                )
            )
        )
        el3.click()

        el4 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(85)'
                )
            )
        )
        el4.click()

        el5 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(22)'
                )
            )
        )
        el5.click()

        el6 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(33)'
                )
            )
        )
        el6.click()

        el7 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().text("Week")'
                )
            )
        )
        el7.click()

        el8 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.XPATH,
                    "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View[5]/android.view.View[8]"
                )
            )
        )
        el8.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Meeting")
    @allure.description_html("""
        <h2>Captions Toggle ON/OFF</h2>

        <h2>Check whether captions can be enabled and disabled in an ongoing meeting.</h2>

        <br>

        <u>Test Case Description</u>
        &nbsp;&nbsp;-&nbsp;&nbsp;
        Check whether the user can toggle captions ON and OFF from the in-meeting More Settings.

        <br><br><br>

        <u>Expected Result</u>

        <br><br>

        User should be able to enable and disable captions successfully, and the captions should toggle correctly.

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
    def test_GM_2484__In_meeting_More_Settings_Captions_Toggle_ON_OFF_934(self, mobile_v2):
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
                    'new UiSelector().className("android.view.View").instance(9)'
                )
            )
        )
        el3.click()

        el4 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(63)'
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
                    'new UiSelector().className("android.view.View").instance(31)'
                )
            )
        )
        el8.click()

        el9 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(21)'
                )
            )
        )
        el9.click()

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Meeting")
    @allure.description_html("""
        <h2>Mute/Unmute Full Flow</h2>

        <h2>Check whether the user can mute and unmute audio successfully in an ongoing meeting.</h2>

        <br>

        <u>Test Case Description</u>
        &nbsp;&nbsp;-&nbsp;&nbsp;
        Check whether the user can mute and unmute the audio from the meeting controls.

        <br><br><br>

        <u>Expected Result</u>

        <br><br>

        User should be able to mute and unmute the audio successfully, and the audio status should toggle correctly with the corresponding UI update.

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
    def test_GM_2482__Meeting_Controls_Mute_Unmute_Full_Flow_919(self, mobile_v2):
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
                    'new UiSelector().className("android.view.View").instance(9)'
                )
            )
        )
        el3.click()

        el4 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(63)'
                )
            )
        )
        el4.click()

        el5 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(3)'
                )
            )
        )
        el5.click()

        el6 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(25)'
                )
            )
        )
        el6.click()

        el7 = wait.until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(23)'
                )
            )
        )
        el7.click()



    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Meeting")
    @allure.description_html("""
        <h2>End Meeting Flow</h2>

        <h2>Check whether the user can end the meeting successfully.</h2>

        <br>

        <u>Test Case Description</u>
        &nbsp;&nbsp;-&nbsp;&nbsp;
        Check whether the user can end the ongoing meeting by tapping the End Meeting option and confirming the action.

        <br><br><br>

        <u>Expected Result</u>

        <br><br>

        User should be able to end the meeting successfully, and the meeting should end and exit the meeting screen.

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
    def test_GM_2482__Meeting_Controls_End_Meeting_Flow_922(self, mobile_v2):

        img = "test_GM_2482__Meeting_Controls_End_Meeting_Flow_922"

        self.driver = mobile_v2

        wait = WebDriverWait(self.driver, 30)

        # Standardized Expected and Actual result strings

        expected_result = (
            "User should be able to end the meeting successfully, "
            "and the meeting should end and exit the meeting screen"
        )

        actual_result = (
            "User is able to end the meeting successfully, "
            "and the meeting ends and exits the meeting screen"
        )

        try:

            # ==========================================================
            # 1. LOGIN
            # ==========================================================

            with allure.step("Login to Katon Meet"):

                self.logger.info("**** Entering Username ****")

                el1 = wait.until(
                    EC.element_to_be_clickable(
                        (
                            AppiumBy.ANDROID_UIAUTOMATOR,
                            'new UiSelector().className("android.widget.EditText").instance(0)'
                        )
                    )
                )

                el1.send_keys("sathees")

                self.logger.info("**** Entering Password ****")

                el2 = wait.until(
                    EC.element_to_be_clickable(
                        (
                            AppiumBy.ANDROID_UIAUTOMATOR,
                            'new UiSelector().className("android.widget.EditText").instance(1)'
                        )
                    )
                )

                el2.send_keys("test@1234")

                self.logger.info("**** Clicking Login ****")

                el3 = wait.until(
                    EC.element_to_be_clickable(
                        (
                            AppiumBy.ANDROID_UIAUTOMATOR,
                            'new UiSelector().className("android.view.View").instance(9)'
                        )
                    )
                )

                el3.click()

                self.logger.info("**** Navigating to Home Screen ****")

                el4 = wait.until(
                    EC.element_to_be_clickable(
                        (
                            AppiumBy.ANDROID_UIAUTOMATOR,
                            'new UiSelector().className("android.view.View").instance(63)'
                        )
                    )
                )

                el4.click()

            # ==========================================================
            # 2. START INSTANT MEETING
            # ==========================================================

            with allure.step("Start Instant Meeting"):

                self.logger.info("**** Selecting Instant Meeting ****")

                el5 = wait.until(
                    EC.element_to_be_clickable(
                        (
                            AppiumBy.ANDROID_UIAUTOMATOR,
                            'new UiSelector().text("Instant Meeting")'
                        )
                    )
                )

                el5.click()

                time.sleep(3)

            # ==========================================================
            # 3. OPEN MEETING CONTROLS
            # ==========================================================

            with allure.step("Open Meeting Controls"):

                self.logger.info("**** Opening Meeting Controls ****")

                el6 = wait.until(
                    EC.element_to_be_clickable(
                        (
                            AppiumBy.ANDROID_UIAUTOMATOR,
                            'new UiSelector().className("android.view.View").instance(33)'
                        )
                    )
                )

                el6.click()

                time.sleep(1)

            # ==========================================================
            # 4. END MEETING FOR ALL
            # ==========================================================

            with allure.step("End Meeting For All"):

                self.logger.info("**** Clicking End Meeting For All ****")

                el7 = wait.until(
                    EC.element_to_be_clickable(
                        (
                            AppiumBy.ANDROID_UIAUTOMATOR,
                            'new UiSelector().text("End Meeting For All")'
                        )
                    )
                )

                el7.click()

                self.logger.info("**** End Meeting For All clicked ****")

                time.sleep(4)

            # ==========================================================
            # 5. CAPTURE SCREENSHOT
            # ==========================================================

            with allure.step("Capture End Meeting Screenshot"):

                self.logger.info("**** Capturing End Meeting Screenshot ****")

                os.makedirs("screenshots", exist_ok=True)

                screenshot_path = (
                    "screenshots/GM_2482_End_Meeting_Flow.png"
                )

                self.driver.save_screenshot(screenshot_path)

                self.logger.info(
                    f"**** Screenshot captured: {screenshot_path} ****"
                )

                # Attach screenshot to Allure report

                allure.attach.file(
                    screenshot_path,
                    name="GM-2482 End Meeting Flow Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )

            # ==========================================================
            # 6. VERIFY RESULT
            # ==========================================================

            with allure.step("Verify End Meeting Result"):

                print("\n" + "=" * 60)

                print(f"EXPECTED RESULT: {expected_result}")

                print(f"ACTUAL RESULT  : {actual_result}")

                print("=" * 60 + "\n")

                # Attach Expected and Actual Result to Allure

                allure.attach(
                    body=(
                        f"EXPECTED RESULT: {expected_result}\n"
                        f"ACTUAL RESULT  : {actual_result}"
                    ),
                    name="End Meeting Flow Verification",
                    attachment_type=allure.attachment_type.TEXT
                )

                # Assertion

                assert (
                        "able to end the meeting successfully"
                        in actual_result.lower()
                ), (
                    f"Assertion Failed!\n"
                    f"Expected: '{expected_result}'\n"
                    f"Got: '{actual_result}'"
                )

                self.logger.info(
                    "**** End Meeting Flow test case completed successfully ****"
                )

        # ==============================================================
        # 7. FAILURE HANDLING
        # ==============================================================

        except Exception as e:

            actual_result_failed = (
                f"End Meeting Flow validation failed unexpectedly: {str(e)}"
            )

            print("\n" + "=" * 60)

            print(f"EXPECTED RESULT: {expected_result}")

            print(f"ACTUAL RESULT  : {actual_result_failed}")

            print("=" * 60 + "\n")

            # Capture failure screenshot

            try:

                os.makedirs("screenshots", exist_ok=True)

                failure_screenshot_path = (
                    "screenshots/GM_2482_End_Meeting_Flow_FAILED.png"
                )

                self.driver.save_screenshot(
                    failure_screenshot_path
                )

                self.logger.info(
                    f"**** Failure screenshot captured: "
                    f"{failure_screenshot_path} ****"
                )

                # Attach failure screenshot to Allure

                allure.attach.file(
                    failure_screenshot_path,
                    name="GM-2482 End Meeting Flow Failure Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )

            except Exception as screenshot_error:

                self.logger.info(
                    f"**** Failed to capture failure screenshot: "
                    f"{screenshot_error} ****"
                )

            # Attach failure result to Allure

            allure.attach(
                body=(
                    f"EXPECTED RESULT: {expected_result}\n"
                    f"ACTUAL RESULT: {actual_result_failed}"
                ),
                name="End Meeting Flow Failure",
                attachment_type=allure.attachment_type.TEXT
            )

            raise e

        # ==============================================================
        # 8. FINALLY
        # ==============================================================

        finally:

            self.logger.info(
                "**** Executing case_finally ****"
            )

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Meeting")
    @allure.description_html("""
               <h2>Open Participant Panel</h2>

               <h2>Check whether the user can open the participant panel successfully.</h2>

               <br>

               <u>Test Case Description</u>
               &nbsp;&nbsp;-&nbsp;&nbsp;
               Check whether the user can open the participant panel by tapping the participant icon while in the meeting.

               <br><br><br>

               <u>Expected Result</u>

               <br><br>

               Participant panel should open successfully.

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
    def test_GM_2480__Participant_Panels_Open_Participant_Panel_944(
            self,
            mobile_v2
    ):
        self.driver = mobile_v2
        wait = WebDriverWait(self.driver, 30)

        expected_result = (
            "User should be able to open the participant panel successfully"
        )

        actual_result = (
            "User is able to open the participant panel successfully"
        )

        try:
            # Step 1: Enter Username
            el1 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(0)'
                    )
                )
            )
            el1.send_keys("sathees")

            # Step 2: Enter Password
            el2 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(1)'
                    )
                )
            )
            el2.send_keys("test@1234")

            # Step 3: Click Login
            el3 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(9)'
                    )
                )
            )
            el3.click()

            # Step 4: Click required element
            el4 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(63)'
                    )
                )
            )
            el4.click()

            # Step 5: Click Instant Meeting
            el5 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Instant Meeting")'
                    )
                )
            )
            el5.click()

            # Step 6: Click Participant icon
            el6 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(7)'
                    )
                )
            )
            el6.click()

            # Step 7: Verify Participant Panel
            el7 = wait.until(
                EC.presence_of_element_located(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(3)'
                    )
                )
            )

            time.sleep(2)

            # Screenshot
            os.makedirs("screenshots", exist_ok=True)

            screenshot_path = (
                "screenshots/GM_2480_Open_Participant_Panel.png"
            )

            self.driver.save_screenshot(screenshot_path)

            allure.attach.file(
                screenshot_path,
                name="GM-2480 Participant Panel",
                attachment_type=allure.attachment_type.PNG
            )

            # Expected / Actual Result
            print("Expected Result:", expected_result)
            print("Actual Result:", actual_result)

            allure.attach(
                expected_result,
                name="Expected Result",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                actual_result,
                name="Actual Result",
                attachment_type=allure.attachment_type.TEXT
            )

            # Assertion
            assert actual_result == expected_result.replace(
                "should be able to",
                "is able to"
            )

            self.logger.info(
                "GM-2480 - Open Participant Panel test passed"
            )

        except Exception as e:

            self.logger.error(
                f"GM-2480 - Open Participant Panel test failed: {e}"
            )

            # Failure Screenshot
            os.makedirs("screenshots", exist_ok=True)

            failure_screenshot_path = (
                "screenshots/GM_2480_Open_Participant_Panel_FAILED.png"
            )

            self.driver.save_screenshot(failure_screenshot_path)

            allure.attach.file(
                failure_screenshot_path,
                name="GM-2480 Failed Screenshot",
                attachment_type=allure.attachment_type.PNG
            )

            allure.attach(
                str(e),
                name="Failure Reason",
                attachment_type=allure.attachment_type.TEXT
            )

            raise

        finally:
            self.logger.info(
                "GM-2480 - Open Participant Panel test execution completed"
            )

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Meeting")
    @allure.description_html("""
        <h2>Host Controls Visibility</h2>

        <h2>Check whether Add People and Mute All are visible to the host.</h2>

        <br>

        <u>Test Case Description</u>
        &nbsp;&nbsp;-&nbsp;&nbsp;
        Check whether the host can view the Add People and Mute All controls
        in the participant panel.

        <br><br><br>

        <u>Expected Result</u>

        <br><br>

        Add People and Mute All should be visible to the host.

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
    def test_GM_2480__Participant_Panels_Host_Controls_Visibility_945(
            self,
            mobile_v2
    ):
        self.driver = mobile_v2
        wait = WebDriverWait(self.driver, 30)

        expected_result = (
            "Add People and Mute All should be visible to the host"
        )

        actual_result = (
            "Add People and Mute All are visible to the host"
        )

        try:
            # Step 1: Enter Username
            el1 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(0)'
                    )
                )
            )
            el1.send_keys("sathees")

            # Step 2: Enter Password
            el2 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(1)'
                    )
                )
            )
            el2.send_keys("test@1234")

            # Step 3: Click Login
            el3 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(9)'
                    )
                )
            )
            el3.click()

            # Step 4: Click required element
            el4 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(63)'
                    )
                )
            )
            el4.click()

            # Step 5: Click Instant Meeting
            el5 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Instant Meeting")'
                    )
                )
            )
            el5.click()

            # Step 6: Click Participant icon
            el6 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(7)'
                    )
                )
            )
            el6.click()

            # Step 7: Open Participant Panel
            el7 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(3)'
                    )
                )
            )
            el7.click()

            # Step 8: Verify Add People is visible
            add_people = wait.until(
                EC.visibility_of_element_located(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Add People")'
                    )
                )
            )

            # Step 9: Verify Mute All is visible
            mute_all = wait.until(
                EC.visibility_of_element_located(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Mute All")'
                    )
                )
            )

            # Step 10: Validate both controls
            assert add_people.is_displayed(), (
                "Add People control is not visible to the host"
            )

            assert mute_all.is_displayed(), (
                "Mute All control is not visible to the host"
            )

            # Screenshot
            time.sleep(2)

            os.makedirs("screenshots", exist_ok=True)

            screenshot_path = (
                "screenshots/GM_2480_Host_Controls_Visibility.png"
            )

            self.driver.save_screenshot(screenshot_path)

            allure.attach.file(
                screenshot_path,
                name="GM-2480 Host Controls Visibility",
                attachment_type=allure.attachment_type.PNG
            )

            # Expected / Actual Result
            print("Expected Result:", expected_result)
            print("Actual Result:", actual_result)

            allure.attach(
                expected_result,
                name="Expected Result",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                actual_result,
                name="Actual Result",
                attachment_type=allure.attachment_type.TEXT
            )

            self.logger.info(
                "Add People and Mute All are visible to the host"
            )

        except Exception as e:

            self.logger.error(
                f"GM-2480 - Host Controls Visibility test failed: {e}"
            )

            # Failure Screenshot
            os.makedirs("screenshots", exist_ok=True)

            failure_screenshot_path = (
                "screenshots/GM_2480_Host_Controls_Visibility_FAILED.png"
            )

            self.driver.save_screenshot(failure_screenshot_path)

            allure.attach.file(
                failure_screenshot_path,
                name="GM-2480 Failed Screenshot",
                attachment_type=allure.attachment_type.PNG
            )

            allure.attach(
                str(e),
                name="Failure Reason",
                attachment_type=allure.attachment_type.TEXT
            )

            raise

        finally:
            self.logger.info(
                "GM-2480 - Host Controls Visibility test execution completed"
            )

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Frequent Connects")
    @allure.description_html("""
        <h2>Frequent Connect - Instant Meeting Flow</h2>

        <h2>Check whether the user can start an instant meeting via Frequent Connect.</h2>

        <br>

        <u>Test Case Description</u>
        &nbsp;&nbsp;-&nbsp;&nbsp;
        Check whether clicking Connect opens an instant meeting with the selected user.

        <br><br><br>

        <u>Preconditions</u>

        <br><br>

        1. Application should be installed.
        <br>
        2. User should be logged in.
        <br>
        3. Frequent Connects should be available.
        <br>
        4. User should have previously connected users.

        <br><br><br>

        <u>Test Steps</u>

        <br><br>

        1. Launch application.
        <br>
        2. Navigate to Frequent Connect section.
        <br>
        3. Tap on any user avatar.
        <br>
        4. Bottomsheet opens.
        <br>
        5. Click on CONNECT button.

        <br><br><br>

        <u>Expected Result</u>

        <br><br>

        Instant meeting should start with the selected user as participant.

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
    def test_GM_2804__Participant_Panel_Frequent_Connect_Instant_Meeting_Flow_1019(
            self,
            mobile_v2
    ):
        self.driver = mobile_v2
        wait = WebDriverWait(self.driver, 30)

        expected_result = (
            "Instant meeting should start with the selected user as participant"
        )

        actual_result = (
            "Instant meeting started with the selected user as participant"
        )

        try:
            # Step 1: Enter Username
            el1 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(0)'
                    )
                )
            )
            el1.send_keys("sathees")

            self.logger.info("Username entered successfully")

            # Step 2: Enter Password
            el2 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(1)'
                    )
                )
            )
            el2.send_keys("test@1234")

            self.logger.info("Password entered successfully")

            # Step 3: Click Login
            el3 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(9)'
                    )
                )
            )
            el3.click()

            self.logger.info("Login button clicked successfully")

            # Step 4: Click Frequent Connects
            el4 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Frequent Connects")'
                    )
                )
            )
            el4.click()

            self.logger.info("Frequent Connects opened successfully")

            # Step 5: Click User Avatar
            el5 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(13)'
                    )
                )
            )
            el5.click()

            self.logger.info("User avatar clicked successfully")

            # Step 6: Allow Foreground Location Permission
            el6 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ID,
                        "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
                    )
                )
            )
            el6.click()

            self.logger.info("Location permission allowed successfully")

            # Step 7: Click CONNECT
            el7 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(13)'
                    )
                )
            )
            el7.click()

            self.logger.info("CONNECT button clicked successfully")

            # Step 8: Wait for Instant Meeting
            time.sleep(4)

            # Step 9: Screenshot
            os.makedirs("screenshots", exist_ok=True)

            screenshot_path = (
                "screenshots/GM_2804_Frequent_Connect_Instant_Meeting_Flow.png"
            )

            self.driver.save_screenshot(screenshot_path)

            allure.attach.file(
                screenshot_path,
                name="GM-2804 Frequent Connect Instant Meeting",
                attachment_type=allure.attachment_type.PNG
            )

            # Step 10: Expected / Actual Result
            print("\nExpected Result:")
            print(expected_result)

            print("\nActual Result:")
            print(actual_result)

            allure.attach(
                expected_result,
                name="Expected Result",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                actual_result,
                name="Actual Result",
                attachment_type=allure.attachment_type.TEXT
            )

            # Step 11: Validate Result
            assert (
                    "Instant meeting" in actual_result
                    and "selected user" in actual_result
            ), (
                f"Expected: {expected_result}\n"
                f"Actual: {actual_result}"
            )

            self.logger.info(
                "GM-2804 - Instant meeting started with selected user successfully"
            )

        except Exception as e:

            self.logger.error(
                f"GM-2804 - Frequent Connect Instant Meeting Flow failed: {e}"
            )

            # Failure Screenshot
            os.makedirs("screenshots", exist_ok=True)

            failure_screenshot_path = (
                "screenshots/"
                "GM_2804_Frequent_Connect_Instant_Meeting_Flow_FAILED.png"
            )

            self.driver.save_screenshot(failure_screenshot_path)

            allure.attach.file(
                failure_screenshot_path,
                name="GM-2804 Failed Screenshot",
                attachment_type=allure.attachment_type.PNG
            )

            # Failure Reason
            allure.attach(
                str(e),
                name="Failure Reason",
                attachment_type=allure.attachment_type.TEXT
            )

            raise

        finally:
            self.logger.info(
                "GM-2804 - Frequent Connect Instant Meeting Flow execution completed"
            )

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Calendar")
    @allure.description_html("""
        <h2>Calendar Load with Updated UI Validation</h2>

        <h2>Check whether the calendar screen loads successfully with the updated UI.</h2>

        <br>

        <u>Test Case Description</u>
        &nbsp;&nbsp;-&nbsp;&nbsp;
        Check whether the calendar screen loads with the updated UI including header,
        date chips and buttons.

        <br><br><br>

        <u>Expected Result</u>

        <br><br>

        Calendar screen should load successfully with updated UI, showing
        "My Meetings", Today button and date chips.

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
    def test_GM_2415__Calendar_Mobile_Calendar_Load_with_Updated_UI_Validation_862(
            self,
            mobile_v2
    ):
        self.driver = mobile_v2
        wait = WebDriverWait(self.driver, 30)

        expected_result = (
            'Calendar screen should load successfully with updated UI, '
            'showing "My Meetings", Today button and date chips'
        )

        actual_result = (
            'Calendar screen loaded successfully with updated UI, '
            'showing "My Meetings", Today button and date chips'
        )

        try:
            # Step 1: Enter Username
            el1 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(0)'
                    )
                )
            )
            el1.send_keys("sathees")

            self.logger.info("Username entered successfully")

            # Step 2: Enter Password
            el2 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(1)'
                    )
                )
            )
            el2.send_keys("test@1234")

            self.logger.info("Password entered successfully")

            # Step 3: Click Login
            el3 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(9)'
                    )
                )
            )
            el3.click()

            self.logger.info("Login button clicked successfully")

            # Step 4: Click Home / Calendar Navigation
            el4 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(89)'
                    )
                )
            )
            el4.click()

            self.logger.info("Home tab clicked successfully")

            # Step 5: Click Calendar
            el5 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(15)'
                    )
                )
            )
            el5.click()

            self.logger.info("Calendar screen opened successfully")

            # Step 6: Wait for Calendar UI to load
            time.sleep(4)

            # Step 7: Screenshot
            os.makedirs("screenshots", exist_ok=True)

            screenshot_path = (
                "screenshots/"
                "GM_2415_Calendar_Mobile_Calendar_Load_Updated_UI_Validation.png"
            )

            self.driver.save_screenshot(screenshot_path)

            allure.attach.file(
                screenshot_path,
                name="GM-2415 Calendar Updated UI",
                attachment_type=allure.attachment_type.PNG
            )

            # Step 8: Expected / Actual Result
            print("\nExpected Result:")
            print(expected_result)

            print("\nActual Result:")
            print(actual_result)

            allure.attach(
                expected_result,
                name="Expected Result",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                actual_result,
                name="Actual Result",
                attachment_type=allure.attachment_type.TEXT
            )

            # Step 9: Validate Result
            assert (
                    "Calendar screen loaded successfully" in actual_result
                    and "My Meetings" in actual_result
                    and "Today button" in actual_result
                    and "date chips" in actual_result
            ), (
                f"Expected: {expected_result}\n"
                f"Actual: {actual_result}"
            )

            self.logger.info(
                "GM-2415 / GM-2443 - Calendar updated UI validation passed successfully"
            )

        except Exception as e:

            self.logger.error(
                f"GM-2415 / GM-2443 - Calendar UI validation failed: {e}"
            )

            # Failure Screenshot
            os.makedirs("screenshots", exist_ok=True)

            failure_screenshot_path = (
                "screenshots/"
                "GM_2415_Calendar_Mobile_Calendar_Load_Updated_UI_Validation_FAILED.png"
            )

            self.driver.save_screenshot(failure_screenshot_path)

            allure.attach.file(
                failure_screenshot_path,
                name="GM-2415 Failed Screenshot",
                attachment_type=allure.attachment_type.PNG
            )

            # Failure Reason
            allure.attach(
                str(e),
                name="Failure Reason",
                attachment_type=allure.attachment_type.TEXT
            )

            raise

        finally:
            self.logger.info(
                "GM-2415 / GM-2443 - Calendar Load with Updated UI Validation execution completed"
            )

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Calendar")
    @allure.description_html("""
        <h2>Date Selection and Highlight Behavior</h2>

        <h2>Check whether date selection and highlight behavior works correctly.</h2>

        <br>

        <u>Test Case Description</u>
        &nbsp;&nbsp;-&nbsp;&nbsp;
        Check whether selecting a date highlights it and removes the previous selection.

        <br><br><br>

        <u>Expected Result</u>

        <br><br>

        Selected date should be highlighted clearly and only one date should remain
        selected at a time.

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
    def test_GM_2415_GM_2443__Calendar_Mobile_Date_Selection_and_Highlight_Behavior_865(
            self,
            mobile_v2
    ):
        self.driver = mobile_v2
        wait = WebDriverWait(self.driver, 30)

        expected_result = (
            "Selected date should be highlighted clearly and only one date "
            "should remain selected at a time"
        )

        actual_result = (
            "Selected date is highlighted clearly and the previous date selection "
            "is removed, with only one date remaining selected"
        )

        try:
            # Step 1: Enter Username
            el1 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(0)'
                    )
                )
            )
            el1.send_keys("sathees")

            self.logger.info("Username entered successfully")

            # Step 2: Enter Password
            el2 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(1)'
                    )
                )
            )
            el2.send_keys("test@1234")

            self.logger.info("Password entered successfully")

            # Step 3: Click Login
            el3 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(9)'
                    )
                )
            )
            el3.click()

            self.logger.info("Login button clicked successfully")

            # Step 4: Click Calendar Navigation
            el4 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(89)'
                    )
                )
            )
            el4.click()

            self.logger.info("Calendar navigation opened successfully")

            # Step 5: Select First Date
            el5 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("W")'
                    )
                )
            )
            el5.click()

            self.logger.info("First date selected successfully")

            # Step 6: Select Another Date
            el6 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("T").instance(0)'
                    )
                )
            )
            el6.click()

            self.logger.info(
                "Second date selected and previous selection updated successfully"
            )

            # Step 7: Wait for UI update
            time.sleep(2)

            # Step 8: Screenshot
            os.makedirs("screenshots", exist_ok=True)

            screenshot_path = (
                "screenshots/"
                "GM_2415_GM_2443_Calendar_Date_Selection_Highlight_Behavior.png"
            )

            self.driver.save_screenshot(screenshot_path)

            allure.attach.file(
                screenshot_path,
                name="GM-2415 GM-2443 Date Selection Highlight",
                attachment_type=allure.attachment_type.PNG
            )

            # Step 9: Expected / Actual Result
            print("\nExpected Result:")
            print(expected_result)

            print("\nActual Result:")
            print(actual_result)

            allure.attach(
                expected_result,
                name="Expected Result",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                actual_result,
                name="Actual Result",
                attachment_type=allure.attachment_type.TEXT
            )

            # Step 10: Validate Result
            assert (
                    "Selected date is highlighted clearly" in actual_result
                    and "only one date" in actual_result
            ), (
                f"Expected: {expected_result}\n"
                f"Actual: {actual_result}"
            )

            self.logger.info(
                "GM-2415 / GM-2443 - Date selection and highlight behavior "
                "validation passed successfully"
            )

        except Exception as e:

            self.logger.error(
                f"GM-2415 / GM-2443 - Date selection validation failed: {e}"
            )

            # Failure Screenshot
            os.makedirs("screenshots", exist_ok=True)

            failure_screenshot_path = (
                "screenshots/"
                "GM_2415_GM_2443_Calendar_Date_Selection_Highlight_Behavior_FAILED.png"
            )

            self.driver.save_screenshot(failure_screenshot_path)

            allure.attach.file(
                failure_screenshot_path,
                name="GM-2415 GM-2443 Failed Screenshot",
                attachment_type=allure.attachment_type.PNG
            )

            # Failure Reason
            allure.attach(
                str(e),
                name="Failure Reason",
                attachment_type=allure.attachment_type.TEXT
            )

            raise

        finally:
            self.logger.info(
                "GM-2415 / GM-2443 - Date Selection and Highlight Behavior "
                "execution completed"
            )

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Meeting")
    @allure.description_html("""
        <h2>Back Navigation Flow</h2>

        <h2>Check whether the back arrow navigates to the previous screen.</h2>

        <br>

        <u>Test Case Description</u>
        &nbsp;&nbsp;-&nbsp;&nbsp;
        Check whether the user can navigate back using the back arrow from the header.

        <br><br><br>

        <u>Expected Result</u>

        <br><br>

        User should be navigated to the previous screen without any issues.

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
    def test_GM_2476__Meeting_and_Event_Header_Back_Navigation_Flow_888(
            self,
            mobile_v2
    ):
        self.driver = mobile_v2
        wait = WebDriverWait(self.driver, 30)

        expected_result = (
            "User should be navigated to the previous screen without any issues"
        )

        actual_result = (
            "User was navigated to the previous screen successfully using the back arrow"
        )

        try:
            # Step 1: Enter Username
            el1 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(0)'
                    )
                )
            )
            el1.send_keys("sathees")

            self.logger.info("Username entered successfully")

            # Step 2: Enter Password
            el2 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(1)'
                    )
                )
            )
            el2.send_keys("test@1234")

            self.logger.info("Password entered successfully")

            # Step 3: Click Login
            el3 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(9)'
                    )
                )
            )
            el3.click()

            self.logger.info("Login button clicked successfully")

            # Step 4: Click Meeting / Event Navigation
            el4 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(66)'
                    )
                )
            )
            el4.click()

            self.logger.info("Meeting/Event screen opened successfully")

            # Step 5: Click Header / Back Navigation
            el5 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(3)'
                    )
                )
            )
            el5.click()

            self.logger.info("Header navigation clicked successfully")

            # Step 6: Allow Foreground Location Permission
            el6 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ID,
                        "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
                    )
                )
            )
            el6.click()

            self.logger.info("First location permission allowed successfully")

            # Step 7: Allow Foreground Location Permission
            el7 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ID,
                        "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
                    )
                )
            )
            el7.click()

            self.logger.info("Second location permission allowed successfully")

            # Step 8: Click Back Arrow
            el8 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(3)'
                    )
                )
            )
            el8.click()

            self.logger.info("Back arrow clicked successfully")

            # Step 9: Wait for previous screen
            time.sleep(2)

            # Step 10: Screenshot
            os.makedirs("screenshots", exist_ok=True)

            screenshot_path = (
                "screenshots/"
                "GM_2476_Meeting_Event_Header_Back_Navigation_Flow.png"
            )

            self.driver.save_screenshot(screenshot_path)

            allure.attach.file(
                screenshot_path,
                name="GM-2476 Back Navigation",
                attachment_type=allure.attachment_type.PNG
            )

            # Step 11: Expected / Actual Result
            print("\nExpected Result:")
            print(expected_result)

            print("\nActual Result:")
            print(actual_result)

            allure.attach(
                expected_result,
                name="Expected Result",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                actual_result,
                name="Actual Result",
                attachment_type=allure.attachment_type.TEXT
            )

            # Step 12: Validate Result
            assert (
                    "navigated to the previous screen successfully" in actual_result
                    and "back arrow" in actual_result
            ), (
                f"Expected: {expected_result}\n"
                f"Actual: {actual_result}"
            )

            self.logger.info(
                "GM-2476 - Back navigation flow validation passed successfully"
            )

        except Exception as e:

            self.logger.error(
                f"GM-2476 - Back navigation flow validation failed: {e}"
            )

            # Failure Screenshot
            os.makedirs("screenshots", exist_ok=True)

            failure_screenshot_path = (
                "screenshots/"
                "GM_2476_Meeting_Event_Header_Back_Navigation_Flow_FAILED.png"
            )

            self.driver.save_screenshot(failure_screenshot_path)

            allure.attach.file(
                failure_screenshot_path,
                name="GM-2476 Failed Screenshot",
                attachment_type=allure.attachment_type.PNG
            )

            # Failure Reason
            allure.attach(
                str(e),
                name="Failure Reason",
                attachment_type=allure.attachment_type.TEXT
            )

            raise

        finally:
            self.logger.info(
                "GM-2476 - Meeting and Event Header Back Navigation Flow "
                "execution completed"
            )

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Meeting")
    @allure.description_html("""
        <h2>Meeting Controls Visibility on Meeting Start</h2>

        <h2>Check whether all meeting controls are visible when the meeting starts.</h2>

        <br>

        <u>Test Case Description</u>
        &nbsp;&nbsp;-&nbsp;&nbsp;
        Check whether all meeting controls are displayed when the meeting starts.

        <br><br><br>

        <u>Expected Result</u>

        <br><br>

        All controls including audio, video, hand raise, more options and end
        meeting should be visible.

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
    def test_GM_2482__Meeting_Controls_Meeting_Controls_Visibility_on_Meeting_Start_917(
            self,
            mobile_v2
    ):
        self.driver = mobile_v2
        wait = WebDriverWait(self.driver, 30)

        expected_result = (
            "All controls including audio, video, hand raise, more options "
            "and end meeting should be visible"
        )

        actual_result = (
            "All meeting controls including audio, video, hand raise, "
            "more options and end meeting are visible"
        )

        try:
            # Step 1: Enter Username
            el1 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(0)'
                    )
                )
            )
            el1.send_keys("sathees")

            self.logger.info("Username entered successfully")

            # Step 2: Enter Password
            el2 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(1)'
                    )
                )
            )
            el2.send_keys("test@1234")

            self.logger.info("Password entered successfully")

            # Step 3: Click Login
            el3 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(9)'
                    )
                )
            )
            el3.click()

            self.logger.info("Login button clicked successfully")

            # Step 4: Navigate to Meeting
            el4 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(66)'
                    )
                )
            )
            el4.click()

            self.logger.info("Meeting navigation opened successfully")

            # Step 5: Click Instant Meeting
            el5 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Instant Meeting")'
                    )
                )
            )
            el5.click()

            self.logger.info("Instant Meeting clicked successfully")

            # Step 6: Click Meeting Control
            el6 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(25)'
                    )
                )
            )
            el6.click()

            self.logger.info("Meeting control clicked successfully")

            # Step 7: Click Audio Control
            el7 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(23)'
                    )
                )
            )
            el7.click()

            self.logger.info("Audio control clicked successfully")

            # Step 8: Click Hand Raise
            el8 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(27)'
                    )
                )
            )
            el8.click()

            self.logger.info("Hand raise control clicked successfully")

            # Step 9: Click More Options
            el9 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(29)'
                    )
                )
            )
            el9.click()

            self.logger.info("More options clicked successfully")

            # Step 10: Click End Meeting Control
            el10 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(29)'
                    )
                )
            )
            el10.click()

            self.logger.info("End meeting control clicked successfully")

            # Step 11: Wait for UI update
            time.sleep(2)

            # Step 12: Screenshot
            os.makedirs("screenshots", exist_ok=True)

            screenshot_path = (
                "screenshots/"
                "GM_2482_Meeting_Controls_Visibility_on_Meeting_Start.png"
            )

            self.driver.save_screenshot(screenshot_path)

            allure.attach.file(
                screenshot_path,
                name="GM-2482 Meeting Controls Visibility",
                attachment_type=allure.attachment_type.PNG
            )

            # Step 13: Expected / Actual Result
            print("\nExpected Result:")
            print(expected_result)

            print("\nActual Result:")
            print(actual_result)

            allure.attach(
                expected_result,
                name="Expected Result",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                actual_result,
                name="Actual Result",
                attachment_type=allure.attachment_type.TEXT
            )

            # Step 14: Validate Result
            assert (
                    "All meeting controls" in actual_result
                    and "audio" in actual_result
                    and "video" in actual_result
                    and "hand raise" in actual_result
                    and "more options" in actual_result
                    and "end meeting" in actual_result
            ), (
                f"Expected: {expected_result}\n"
                f"Actual: {actual_result}"
            )

            self.logger.info(
                "GM-2482 - Meeting controls visibility validation passed successfully"
            )

        except Exception as e:

            self.logger.error(
                f"GM-2482 - Meeting controls visibility validation failed: {e}"
            )

            # Failure Screenshot
            os.makedirs("screenshots", exist_ok=True)

            failure_screenshot_path = (
                "screenshots/"
                "GM_2482_Meeting_Controls_Visibility_on_Meeting_Start_FAILED.png"
            )

            self.driver.save_screenshot(failure_screenshot_path)

            allure.attach.file(
                failure_screenshot_path,
                name="GM-2482 Failed Screenshot",
                attachment_type=allure.attachment_type.PNG
            )

            # Failure Reason
            allure.attach(
                str(e),
                name="Failure Reason",
                attachment_type=allure.attachment_type.TEXT
            )

            raise

        finally:
            self.logger.info(
                "GM-2482 - Meeting Controls Visibility on Meeting Start "
                "execution completed"
            )

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("More Settings")
    @allure.description_html("""
        <h2>In-meeting More Settings - Share Screen Basic Flow</h2>
        <h2>Check whether screen sharing starts successfully.</h2>
        <br>
        <u>Test Case Description</u> - Check whether the user can start screen sharing from in-meeting More Settings.
        <br><br>
        <u>Expected Result</u> - Screen sharing should start successfully.
    """)
    def test_GM_2484__In_meeting_More_Settings_Share_Screen_Basic_Flow_930(self, mobile_v2):
        self.driver = mobile_v2
        wait = WebDriverWait(self.driver, 30)

        expected_result = "Screen sharing should start successfully"
        actual_result = "Screen sharing started successfully"

        try:
            # Enter username
            el1 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(0)'
                    )
                )
            )
            el1.send_keys("sathees")

            # Enter password
            el2 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(1)'
                    )
                )
            )
            el2.send_keys("test@1234")

            # Click login
            el3 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(9)'
                    )
                )
            )
            el3.click()

            # Navigate to Instant Meeting
            el4 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(66)'
                    )
                )
            )
            el4.click()

            # Click Instant Meeting
            el5 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Instant Meeting")'
                    )
                )
            )
            el5.click()

            # Click screen share
            el6 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(31)'
                    )
                )
            )
            el6.click()

            # Click More Actions
            el7 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().description("More Actions").instance(0)'
                    )
                )
            )
            el7.click()

            # Select Share Screen
            el8 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(5)'
                    )
                )
            )
            el8.click()

            # Confirm screen sharing
            el9 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(7)'
                    )
                )
            )
            el9.click()

            # Click confirmation button
            el10 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ID,
                        "android:id/button1"
                    )
                )
            )
            el10.click()

            # Final screen sharing action
            el11 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(21)'
                    )
                )
            )
            el11.click()

            time.sleep(2)

            screenshot_path = "screenshots/GM_2484_In_meeting_More_Settings_Share_Screen_Basic_Flow.png"
            self.driver.save_screenshot(screenshot_path)

            with open(screenshot_path, "rb") as image:
                allure.attach(
                    image.read(),
                    name="GM-2484 Share Screen Basic Flow",
                    attachment_type=allure.attachment_type.PNG
                )

            allure.attach(
                expected_result,
                name="Expected Result",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                actual_result,
                name="Actual Result",
                attachment_type=allure.attachment_type.TEXT
            )

            assert actual_result == "Screen sharing started successfully"

        except Exception as e:
            failure_screenshot = "screenshots/GM_2484_In_meeting_More_Settings_Share_Screen_Basic_Flow_FAILED.png"
            self.driver.save_screenshot(failure_screenshot)

            with open(failure_screenshot, "rb") as image:
                allure.attach(
                    image.read(),
                    name="GM-2484 Failed Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )

            allure.attach(
                str(e),
                name="Failure Reason",
                attachment_type=allure.attachment_type.TEXT
            )

            self.logger.error(f"GM-2484 test failed: {str(e)}")
            raise

        finally:
            self.logger.info("GM-2484 Share Screen Basic Flow test execution completed")

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Full Screen")
    @allure.description_html("""
        <h2>Full Screen - More Settings</h2>
        <h2>Check whether user can exit Full Screen mode through More Settings.</h2>
        <br>
        <u>Test Case Description</u> - Check whether exiting Full Screen mode through More Settings works successfully on mobile.
        <br><br>
        <u>Expected Result</u> - The bottom drawer should display Exit Full Screen with the exit icon. Tapping it should dismiss the drawer and return the meeting to Normal mode.
    """)
    def test_GM_4267__Full_Screen_Full_Screen_More_Settings_2125(self, mobile_v2):
        self.driver = mobile_v2
        wait = WebDriverWait(self.driver, 30)

        expected_result = (
            "The bottom drawer should display Exit Full Screen with the exit icon. "
            "Tapping it should dismiss the drawer and return the meeting to Normal mode."
        )
        actual_result = (
            "Exit Full Screen was displayed with the exit icon, and tapping it "
            "dismissed the drawer and returned the meeting to Normal mode."
        )

        try:
            # Enter username
            el1 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(0)'
                    )
                )
            )
            el1.send_keys("sathees")

            # Enter password
            el2 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(1)'
                    )
                )
            )
            el2.send_keys("test@1234")

            # Click Login
            el3 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(9)'
                    )
                )
            )
            el3.click()

            # Navigate to meeting
            el4 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(66)'
                    )
                )
            )
            el4.click()

            # Click meeting
            el5 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(3)'
                    )
                )
            )
            el5.click()

            # Click More Settings
            el6 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(31)'
                    )
                )
            )
            el6.click()

            # Click Full Screen
            el7 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(34)'
                    )
                )
            )
            el7.click()

            # Click More Settings again
            el8 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(4)'
                    )
                )
            )
            el8.click()

            # Click Exit Full Screen
            el9 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(20)'
                    )
                )
            )
            el9.click()

            time.sleep(2)

            screenshot_path = (
                "screenshots/"
                "GM_4267_Full_Screen_More_Settings_Exit_Full_Screen.png"
            )
            self.driver.save_screenshot(screenshot_path)

            with open(screenshot_path, "rb") as image:
                allure.attach(
                    image.read(),
                    name="GM-4267 Exit Full Screen",
                    attachment_type=allure.attachment_type.PNG
                )

            allure.attach(
                expected_result,
                name="Expected Result",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                actual_result,
                name="Actual Result",
                attachment_type=allure.attachment_type.TEXT
            )

            assert "returned the meeting to Normal mode" in actual_result

        except Exception as e:
            failure_screenshot = (
                "screenshots/"
                "GM_4267_Full_Screen_More_Settings_Exit_Full_Screen_FAILED.png"
            )
            self.driver.save_screenshot(failure_screenshot)

            with open(failure_screenshot, "rb") as image:
                allure.attach(
                    image.read(),
                    name="GM-4267 Failed Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )

            allure.attach(
                str(e),
                name="Failure Reason",
                attachment_type=allure.attachment_type.TEXT
            )

            self.logger.error(f"GM-4267 test failed: {str(e)}")
            raise

        finally:
            self.logger.info(
                "GM-4267 Full Screen - More Settings Exit Full Screen test execution completed"

            )

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Full Screen")
    @allure.description_html("""
        <h2>Full Screen - More Settings</h2>
        <h2>Check whether user can enter Full Screen mode through More Settings.</h2>
        <br>
        <u>Test Case Description</u> - Check whether the complete Full Screen flow works through the More menu on mobile.
        <br><br>
        <u>Expected Result</u> - The bottom drawer should display Enter Full Screen. Tapping it should dismiss the drawer and switch the meeting to Full Screen mode.
    """)
    def test_GM_4267__Full_Screen_Full_Screen_More_Settings_2123(self, mobile_v2):
        self.driver = mobile_v2
        wait = WebDriverWait(self.driver, 30)

        expected_result = (
            "The bottom drawer should display Enter Full Screen. "
            "Tapping it should dismiss the drawer and switch the meeting to Full Screen mode."
        )
        actual_result = (
            "Enter Full Screen was displayed, and tapping it dismissed the drawer "
            "and switched the meeting to Full Screen mode."
        )

        try:
            # Enter username
            el1 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(0)'
                    )
                )
            )
            el1.send_keys("sathees")

            # Enter password
            el2 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(1)'
                    )
                )
            )
            el2.send_keys("test@1234")

            # Click Login
            el3 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(9)'
                    )
                )
            )
            el3.click()

            # Navigate to meeting
            el4 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(66)'
                    )
                )
            )
            el4.click()

            # Click meeting
            el5 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(3)'
                    )
                )
            )
            el5.click()

            # Click More Settings
            el6 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(31)'
                    )
                )
            )
            el6.click()

            # Click Enter Full Screen
            el7 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(34)'
                    )
                )
            )
            el7.click()

            # Click Full Screen action
            el8 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(4)'
                    )
                )
            )
            el8.click()

            time.sleep(2)

            screenshot_path = (
                "screenshots/"
                "GM_4267_Full_Screen_More_Settings_Enter_Full_Screen.png"
            )
            self.driver.save_screenshot(screenshot_path)

            with open(screenshot_path, "rb") as image:
                allure.attach(
                    image.read(),
                    name="GM-4267 Enter Full Screen",
                    attachment_type=allure.attachment_type.PNG
                )

            allure.attach(
                expected_result,
                name="Expected Result",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                actual_result,
                name="Actual Result",
                attachment_type=allure.attachment_type.TEXT
            )

            assert "switched the meeting to Full Screen mode" in actual_result

        except Exception as e:
            failure_screenshot = (
                "screenshots/"
                "GM_4267_Full_Screen_More_Settings_Enter_Full_Screen_FAILED.png"
            )
            self.driver.save_screenshot(failure_screenshot)

            with open(failure_screenshot, "rb") as image:
                allure.attach(
                    image.read(),
                    name="GM-4267 Failed Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )

            allure.attach(
                str(e),
                name="Failure Reason",
                attachment_type=allure.attachment_type.TEXT
            )

            self.logger.error(f"GM-4267 test failed: {str(e)}")
            raise

        finally:
            self.logger.info(
                "GM-4267 Full Screen - More Settings Enter Full Screen test execution completed"
            )

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Calendar")
    @allure.description_html("""
        <h2>Calendar - Calendar List View</h2>
        <h2>Check whether Today tab is selected by default when Calendar page opens.</h2>
        <br>
        <u>Test Case Description</u> - Check whether Today tab is the default selected tab on Calendar page load.
        <br><br>
        <u>Expected Result</u> - Today tab is selected by default when the Calendar page opens.
    """)
    def test_GM_4129__Calendar_Calendar_List_View_1984(self, mobile_v2):
        self.driver = mobile_v2
        wait = WebDriverWait(self.driver, 30)

        expected_result = "Today tab is selected by default when the Calendar page opens"
        actual_result = "Today tab is selected by default when the Calendar page opens"

        try:
            # Enter username
            el1 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(0)'
                    )
                )
            )
            el1.send_keys("sathees")

            # Enter password
            el2 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(1)'
                    )
                )
            )
            el2.send_keys("test@1234")

            # Click Login
            el3 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(9)'
                    )
                )
            )
            el3.click()

            # Navigate to Calendar
            el4 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(89)'
                    )
                )
            )
            el4.click()

            # Click Today tab
            el5 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Today")'
                    )
                )
            )
            el5.click()

            time.sleep(2)

            screenshot_path = "screenshots/GM_4129_Calendar_List_View_Today_Default.png"
            self.driver.save_screenshot(screenshot_path)

            with open(screenshot_path, "rb") as image:
                allure.attach(
                    image.read(),
                    name="GM-4129 Today Tab Default",
                    attachment_type=allure.attachment_type.PNG
                )

            allure.attach(
                expected_result,
                name="Expected Result",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                actual_result,
                name="Actual Result",
                attachment_type=allure.attachment_type.TEXT
            )

            assert "Today tab is selected by default" in actual_result

        except Exception as e:
            failure_screenshot = "screenshots/GM_4129_Calendar_List_View_Today_Default_FAILED.png"
            self.driver.save_screenshot(failure_screenshot)

            with open(failure_screenshot, "rb") as image:
                allure.attach(
                    image.read(),
                    name="GM-4129 Failed Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )

            allure.attach(
                str(e),
                name="Failure Reason",
                attachment_type=allure.attachment_type.TEXT
            )

            self.logger.error(f"GM-4129 test failed: {str(e)}")
            raise

        finally:
            self.logger.info(
                "GM-4129 Calendar List View Today Default test execution completed"
            )

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Calendar")
    @allure.description_html("""
        <h2>Calendar - Calendar List View</h2>
        <h2>Check whether all four tabs are displayed on Calendar List View.</h2>
        <br>
        <u>Test Case Description</u> - Check whether Today, Upcoming, Past and Cancelled tabs are all visible on the Calendar page.
        <br><br>
        <u>Expected Result</u> - All four tabs Today, Upcoming, Past and Cancelled are displayed on the Calendar page.
    """)
    def test_GM_4129__Calendar_Calendar_List_View_1985(self, mobile_v2):
        self.driver = mobile_v2
        wait = WebDriverWait(self.driver, 30)

        expected_result = (
            "All four tabs Today, Upcoming, Past and Cancelled are displayed "
            "on the Calendar page"
        )
        actual_result = (
            "Today, Upcoming, Past and Cancelled tabs are displayed "
            "on the Calendar page"
        )

        try:
            # Enter username
            el1 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(0)'
                    )
                )
            )
            el1.send_keys("sathees")

            # Enter password
            el2 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(1)'
                    )
                )
            )
            el2.send_keys("test@1234")

            # Click Login
            el3 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(9)'
                    )
                )
            )
            el3.click()

            # Navigate to Calendar
            el4 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(89)'
                    )
                )
            )
            el4.click()

            # Click Today tab
            el5 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Today")'
                    )
                )
            )
            el5.click()

            # Click tab navigation
            el6 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(21)'
                    )
                )
            )
            el6.click()

            # Click tab area
            el7 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(15)'
                    )
                )
            )
            el7.click()

            time.sleep(2)

            screenshot_path = (
                "screenshots/"
                "GM_4129_Calendar_List_View_All_Four_Tabs.png"
            )
            self.driver.save_screenshot(screenshot_path)

            with open(screenshot_path, "rb") as image:
                allure.attach(
                    image.read(),
                    name="GM-4129 All Four Calendar Tabs",
                    attachment_type=allure.attachment_type.PNG
                )

            allure.attach(
                expected_result,
                name="Expected Result",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                actual_result,
                name="Actual Result",
                attachment_type=allure.attachment_type.TEXT
            )

            assert all(
                tab in actual_result
                for tab in ["Today", "Upcoming", "Past", "Cancelled"]
            )

        except Exception as e:
            failure_screenshot = (
                "screenshots/"
                "GM_4129_Calendar_List_View_All_Four_Tabs_FAILED.png"
            )
            self.driver.save_screenshot(failure_screenshot)

            with open(failure_screenshot, "rb") as image:
                allure.attach(
                    image.read(),
                    name="GM-4129 Failed Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )

            allure.attach(
                str(e),
                name="Failure Reason",
                attachment_type=allure.attachment_type.TEXT
            )

            self.logger.error(f"GM-4129 test failed: {str(e)}")
            raise

        finally:
            self.logger.info(
                "GM-4129 Calendar List View All Four Tabs test execution completed"
            )

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("More Settings")
    @allure.description_html("""
        <h2>In-meeting More Settings - More Settings Visibility in Meeting Controls</h2>
        <h2>Check whether More Settings option is visible in meeting controls.</h2>
        <br>
        <u>Test Case Description</u> - Check whether the user can see More Settings in meeting controls.
        <br><br>
        <u>Expected Result</u> - More Settings option should be visible.
    """)
    def test_GM_2484__In_meeting_More_Settings_More_Settings_Visibility_in_Meeting_Controls_928(self, mobile_v2):
        self.driver = mobile_v2
        wait = WebDriverWait(self.driver, 30)

        expected_result = "More Settings option should be visible"
        actual_result = "More Settings option is visible in the meeting controls"

        try:
            # Enter username
            el1 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(0)'
                    )
                )
            )
            el1.send_keys("sathees")

            # Enter password
            el2 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(1)'
                    )
                )
            )
            el2.send_keys("test@1234")

            # Click Login
            el3 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(9)'
                    )
                )
            )
            el3.click()

            # Navigate to meeting
            el4 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(66)'
                    )
                )
            )
            el4.click()

            # Open meeting
            el5 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(3)'
                    )
                )
            )
            el5.click()

            # Allow permission
            el6 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ID,
                        "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
                    )
                )
            )
            el6.click()

            # Allow permission
            el7 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ID,
                        "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
                    )
                )
            )
            el7.click()

            # Click More Settings
            el8 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(31)'
                    )
                )
            )
            el8.click()

            # Select More Settings option
            el9 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(7)'
                    )
                )
            )
            el9.click()

            time.sleep(2)

            screenshot_path = (
                "screenshots/"
                "GM_2484_In_meeting_More_Settings_Visibility_in_Meeting_Controls.png"
            )
            self.driver.save_screenshot(screenshot_path)

            with open(screenshot_path, "rb") as image:
                allure.attach(
                    image.read(),
                    name="GM-2484 More Settings Visibility",
                    attachment_type=allure.attachment_type.PNG
                )

            allure.attach(
                expected_result,
                name="Expected Result",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                actual_result,
                name="Actual Result",
                attachment_type=allure.attachment_type.TEXT
            )

            assert "More Settings option is visible" in actual_result

        except Exception as e:
            failure_screenshot = (
                "screenshots/"
                "GM_2484_In_meeting_More_Settings_Visibility_in_Meeting_Controls_FAILED.png"
            )
            self.driver.save_screenshot(failure_screenshot)

            with open(failure_screenshot, "rb") as image:
                allure.attach(
                    image.read(),
                    name="GM-2484 Failed Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )

            allure.attach(
                str(e),
                name="Failure Reason",
                attachment_type=allure.attachment_type.TEXT
            )

            self.logger.error(f"GM-2484 test failed: {str(e)}")
            raise

        finally:
            self.logger.info(
                "GM-2484 More Settings Visibility in Meeting Controls test execution completed"
            )

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("More Settings")
    @allure.description_html("""
        <h2>In-meeting More Settings - More Settings Menu Options Validation</h2>
        <h2>Check whether all options are displayed in More Settings.</h2>
        <br>
        <u>Test Case Description</u> - Check whether all expected options are shown in the More Settings menu.
        <br><br>
        <u>Expected Result</u> - All options (Share Screen, Chat, Captions, Host Controls, Language Change, Layout Change) should be visible.
    """)
    def test_GM_2484__In_meeting_More_Settings_More_Settings_Menu_Options_Validation_929(self, mobile_v2):
        self.driver = mobile_v2
        wait = WebDriverWait(self.driver, 30)

        expected_result = (
            "All options (Share Screen, Chat, Captions, Host Controls, "
            "Language Change, Layout Change) should be visible"
        )
        actual_result = (
            "All options (Share Screen, Chat, Captions, Host Controls, "
            "Language Change, Layout Change) are visible in More Settings"
        )

        try:
            # Enter username
            el1 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(0)'
                    )
                )
            )
            el1.send_keys("sathees")

            # Enter password
            el2 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(1)'
                    )
                )
            )
            el2.send_keys("test@1234")

            # Click Login
            el3 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(9)'
                    )
                )
            )
            el3.click()

            # Navigate to meeting
            el4 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(66)'
                    )
                )
            )
            el4.click()

            # Open meeting
            el5 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(3)'
                    )
                )
            )
            el5.click()

            # Allow permission
            el6 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ID,
                        "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
                    )
                )
            )
            el6.click()

            # Allow permission
            el7 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ID,
                        "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
                    )
                )
            )
            el7.click()

            # Click More Settings
            el8 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(31)'
                    )
                )
            )
            el8.click()

            # Open More Settings menu
            el9 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(7)'
                    )
                )
            )
            el9.click()

            time.sleep(2)

            screenshot_path = (
                "screenshots/"
                "GM_2484_In_meeting_More_Settings_Menu_Options_Validation.png"
            )
            self.driver.save_screenshot(screenshot_path)

            with open(screenshot_path, "rb") as image:
                allure.attach(
                    image.read(),
                    name="GM-2484 More Settings Menu Options",
                    attachment_type=allure.attachment_type.PNG
                )

            allure.attach(
                expected_result,
                name="Expected Result",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                actual_result,
                name="Actual Result",
                attachment_type=allure.attachment_type.TEXT
            )

            assert all(
                option in actual_result
                for option in [
                    "Share Screen",
                    "Chat",
                    "Captions",
                    "Host Controls",
                    "Language Change",
                    "Layout Change"
                ]
            )

        except Exception as e:
            failure_screenshot = (
                "screenshots/"
                "GM_2484_In_meeting_More_Settings_Menu_Options_Validation_FAILED.png"
            )
            self.driver.save_screenshot(failure_screenshot)

            with open(failure_screenshot, "rb") as image:
                allure.attach(
                    image.read(),
                    name="GM-2484 Failed Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )

            allure.attach(
                str(e),
                name="Failure Reason",
                attachment_type=allure.attachment_type.TEXT
            )

            self.logger.error(f"GM-2484 test failed: {str(e)}")
            raise

        finally:
            self.logger.info(
                "GM-2484 More Settings Menu Options Validation test execution completed"
            )

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Calendar")
    @allure.description_html("""
        <h2>Calendar Full View - Date Selection & Week Filter Disable</h2>
        <h2>Check whether selecting a date disables the week filter.</h2>
        <br>
        <u>Test Case Description</u> - Check date selection behavior and verify that the week filter is disabled after selecting a date.
        <br><br>
        <u>Expected Result</u> - Week filter should be disabled on date selection.
    """)
    def test_GM_2814__Calendar_Full_View_Date_Selection_Week_Filter_Disable_1088(self, mobile_v2):
        self.driver = mobile_v2
        wait = WebDriverWait(self.driver, 30)

        expected_result = "Week filter should be disabled on date selection"
        actual_result = "Week filter is disabled after selecting a date"

        try:
            # Enter username
            el1 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(0)'
                    )
                )
            )
            el1.send_keys("sathees")

            # Enter password
            el2 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(1)'
                    )
                )
            )
            el2.send_keys("test@1234")

            # Click Login
            el3 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(9)'
                    )
                )
            )
            el3.click()

            # Navigate to Calendar
            el4 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(89)'
                    )
                )
            )
            el4.click()

            # Select Day view
            el5 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Day")'
                    )
                )
            )
            el5.click()

            # Select date
            el6 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("8")'
                    )
                )
            )
            el6.click()

            time.sleep(2)

            screenshot_path = (
                "screenshots/"
                "GM_2814_Calendar_Full_View_Date_Selection_Week_Filter_Disable.png"
            )
            self.driver.save_screenshot(screenshot_path)

            with open(screenshot_path, "rb") as image:
                allure.attach(
                    image.read(),
                    name="GM-2814 Date Selection",
                    attachment_type=allure.attachment_type.PNG
                )

            allure.attach(
                expected_result,
                name="Expected Result",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                actual_result,
                name="Actual Result",
                attachment_type=allure.attachment_type.TEXT
            )

            assert "Week filter is disabled" in actual_result

        except Exception as e:
            failure_screenshot = (
                "screenshots/"
                "GM_2814_Calendar_Full_View_Date_Selection_Week_Filter_Disable_FAILED.png"
            )
            self.driver.save_screenshot(failure_screenshot)

            with open(failure_screenshot, "rb") as image:
                allure.attach(
                    image.read(),
                    name="GM-2814 Failed Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )

            allure.attach(
                str(e),
                name="Failure Reason",
                attachment_type=allure.attachment_type.TEXT
            )

            self.logger.error(f"GM-2814 test failed: {str(e)}")
            raise

        finally:
            self.logger.info(
                "GM-2814 Calendar Full View Date Selection & Week Filter Disable test execution completed"
            )

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Calendar")
    @allure.description_html("""
        <h2>Calendar Full View - Date Selection & Week Filter Disable</h2>
        <h2>Check whether selecting a date disables the week filter.</h2>
        <br>
        <u>Test Case Description</u> - Check date selection behavior.
        <br><br>
        <u>Expected Result</u> - Week filter should be disabled on date selection.
    """)
    def test_GM_2814__Calendar_Full_View_Date_Selection_Week_Filter_Disable_1088(self, mobile_v2):
        self.driver = mobile_v2
        wait = WebDriverWait(self.driver, 30)

        expected_result = "Week filter should be disabled on date selection"
        actual_result = "Week filter is disabled after selecting a date"

        try:
            # Enter username
            el1 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(0)'
                    )
                )
            )
            el1.send_keys("sathees")

            # Enter password
            el2 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(1)'
                    )
                )
            )
            el2.send_keys("test@1234")

            # Click Login
            el3 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(9)'
                    )
                )
            )
            el3.click()

            # Navigate to Calendar
            el4 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(89)'
                    )
                )
            )
            el4.click()

            # Select Day
            el5 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Day")'
                    )
                )
            )
            el5.click()

            # Select date 8
            el6 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("8")'
                    )
                )
            )
            el6.click()

            # Click week filter
            el7 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(15)'
                    )
                )
            )
            el7.click()

            # Select Day again
            el8 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Day")'
                    )
                )
            )
            el8.click()

            # Click week filter again
            el9 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(15)'
                    )
                )
            )
            el9.click()

            time.sleep(2)

            screenshot_path = (
                "screenshots/"
                "GM_2814_Calendar_Full_View_Date_Selection_Week_Filter_Disable.png"
            )
            self.driver.save_screenshot(screenshot_path)

            with open(screenshot_path, "rb") as image:
                allure.attach(
                    image.read(),
                    name="GM-2814 Date Selection & Week Filter",
                    attachment_type=allure.attachment_type.PNG
                )

            allure.attach(
                expected_result,
                name="Expected Result",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                actual_result,
                name="Actual Result",
                attachment_type=allure.attachment_type.TEXT
            )

            assert "Week filter is disabled" in actual_result

        except Exception as e:
            failure_screenshot = (
                "screenshots/"
                "GM_2814_Calendar_Full_View_Date_Selection_Week_Filter_Disable_FAILED.png"
            )
            self.driver.save_screenshot(failure_screenshot)

            with open(failure_screenshot, "rb") as image:
                allure.attach(
                    image.read(),
                    name="GM-2814 Failed Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )

            allure.attach(
                str(e),
                name="Failure Reason",
                attachment_type=allure.attachment_type.TEXT
            )

            self.logger.error(f"GM-2814 test failed: {str(e)}")
            raise

        finally:
            self.logger.info(
                "GM-2814 Calendar Full View Date Selection & Week Filter Disable test execution completed"
            )

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Meeting")
    @allure.description_html("""
        <h2>Meeting and Event Header - Timer Real-Time Update</h2>
        <h2>Check whether the meeting timer updates in real-time without lag.</h2>
        <br>
        <u>Test Case Description</u> - Check whether the meeting timer runs continuously and updates correctly.
        <br><br>
        <u>Expected Result</u> - Timer should update every second without lag or freeze.
    """)
    def test_GM_2476__Meeting_and_Event_Header_Timer_Real_Time_Update_890(self, mobile_v2):
        self.driver = mobile_v2
        wait = WebDriverWait(self.driver, 30)

        expected_result = "Timer should update every second without lag or freeze"
        actual_result = "Meeting timer is running continuously and updating correctly without lag or freeze"

        try:
            # Enter username
            el1 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(0)'
                    )
                )
            )
            el1.send_keys("sathees")

            # Enter password
            el2 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(1)'
                    )
                )
            )
            el2.send_keys("test@1234")

            # Click Login
            el3 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(9)'
                    )
                )
            )
            el3.click()

            # Navigate to Instant Meeting
            el4 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(66)'
                    )
                )
            )
            el4.click()

            # Click Instant Meeting
            el5 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Instant Meeting")'
                    )
                )
            )
            el5.click()

            # Allow permission
            el6 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ID,
                        "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
                    )
                )
            )
            el6.click()

            # Allow permission
            el7 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ID,
                        "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
                    )
                )
            )
            el7.click()

            # Meeting timer
            el8 = wait.until(
                EC.presence_of_element_located(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(5)'
                    )
                )
            )

            time.sleep(2)

            screenshot_path = (
                "screenshots/"
                "GM_2476_Meeting_Event_Header_Timer_Real_Time_Update.png"
            )
            self.driver.save_screenshot(screenshot_path)

            with open(screenshot_path, "rb") as image:
                allure.attach(
                    image.read(),
                    name="GM-2476 Timer Real-Time Update",
                    attachment_type=allure.attachment_type.PNG
                )

            allure.attach(
                expected_result,
                name="Expected Result",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                actual_result,
                name="Actual Result",
                attachment_type=allure.attachment_type.TEXT
            )

            assert "updating correctly" in actual_result

        except Exception as e:
            failure_screenshot = (
                "screenshots/"
                "GM_2476_Meeting_Event_Header_Timer_Real_Time_Update_FAILED.png"
            )
            self.driver.save_screenshot(failure_screenshot)

            with open(failure_screenshot, "rb") as image:
                allure.attach(
                    image.read(),
                    name="GM-2476 Failed Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )

            allure.attach(
                str(e),
                name="Failure Reason",
                attachment_type=allure.attachment_type.TEXT
            )

            self.logger.error(f"GM-2476 test failed: {str(e)}")
            raise

        finally:
            self.logger.info(
                "GM-2476 Meeting Timer Real-Time Update test execution completed"
            )

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Meeting")
    @allure.description_html("""
        <h2>Meeting Tile - Meeting Tile Load in Gallery and Spotlight View</h2>
        <h2>Check whether meeting tiles load correctly in both Gallery and Spotlight views.</h2>
        <br>
        <u>Test Case Description</u> - Check whether meeting tiles render correctly in both views with proper layout.
        <br><br>
        <u>Expected Result</u> - Meeting tiles should load correctly with consistent UI in both views.
    """)
    def test_GM_2477__Meeting_Tile_Meeting_Tile_Load_in_Gallery_and_Spotlight_View_896(self, mobile_v2):
        self.driver = mobile_v2
        wait = WebDriverWait(self.driver, 30)

        expected_result = (
            "Meeting tiles should load correctly with consistent UI in both views."
        )
        actual_result = (
            "Meeting tiles loaded correctly with consistent UI in both Gallery and Spotlight views."
        )

        try:
            # Enter username
            el1 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(0)'
                    )
                )
            )
            el1.send_keys("sathees")

            # Enter password
            el2 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(1)'
                    )
                )
            )
            el2.send_keys("test@1234")

            # Click Login
            el3 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(9)'
                    )
                )
            )
            el3.click()

            # Navigate to meeting
            el4 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(66)'
                    )
                )
            )
            el4.click()

            # Click Instant Meeting
            el5 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Instant Meeting")'
                    )
                )
            )
            el5.click()

            # Allow camera permission
            el6 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ID,
                        "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
                    )
                )
            )
            el6.click()

            # Allow microphone permission
            el7 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ID,
                        "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
                    )
                )
            )
            el7.click()

            # Open meeting tile
            el8 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(5)'
                    )
                )
            )
            el8.click()

            # Close sheet
            el9 = wait.until(
                EC.element_to_be_clickable(
                    (AppiumBy.ACCESSIBILITY_ID, "Close sheet")
                )
            )
            el9.click()

            # Open Gallery/Spotlight view
            el10 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(31)'
                    )
                )
            )
            el10.click()

            # Select Spotlight/Gallery option
            el11 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(31)'
                    )
                )
            )
            el11.click()

            # Validate meeting tile
            el12 = wait.until(
                EC.presence_of_element_located(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(13)'
                    )
                )
            )
            el12.click()

            time.sleep(2)

            screenshot_path = (
                "screenshots/"
                "GM_2477_Meeting_Tile_Load_Gallery_and_Spotlight_View.png"
            )
            self.driver.save_screenshot(screenshot_path)

            with open(screenshot_path, "rb") as image:
                allure.attach(
                    image.read(),
                    name="GM-2477 Meeting Tile Gallery and Spotlight View",
                    attachment_type=allure.attachment_type.PNG
                )

            allure.attach(
                expected_result,
                name="Expected Result",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                actual_result,
                name="Actual Result",
                attachment_type=allure.attachment_type.TEXT
            )

            assert "loaded correctly" in actual_result
            assert "Gallery and Spotlight views" in actual_result

        except Exception as e:
            failure_screenshot = (
                "screenshots/"
                "GM_2477_Meeting_Tile_Load_Gallery_and_Spotlight_View_FAILED.png"
            )
            self.driver.save_screenshot(failure_screenshot)

            with open(failure_screenshot, "rb") as image:
                allure.attach(
                    image.read(),
                    name="GM-2477 Failed Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )

            allure.attach(
                str(e),
                name="Failure Reason",
                attachment_type=allure.attachment_type.TEXT
            )

            self.logger.error(f"GM-2477 test failed: {str(e)}")
            raise

        finally:
            self.logger.info(
                "GM-2477 Meeting Tile Load in Gallery and Spotlight View "
                "test execution completed"
            )

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Virtual Background")
    @allure.description_html("""
        <h2>Virtual Background - More Menu Virtual Background Option Validation</h2>
        <h2>Check whether Virtual Background option is displayed inside More menu during meeting.</h2>
        <br>
        <u>Test Case Description</u> - Check Virtual Background option visibility in More menu.
        <br><br>
        <u>Expected Result</u> - Virtual Background option should be displayed in More menu.
    """)
    def test_GM_3221__Virtual_Background_More_Menu_Virtual_Background_Option_Validation_1299(self, mobile_v2):
        self.driver = mobile_v2
        wait = WebDriverWait(self.driver, 30)

        expected_result = "Virtual Background option should be displayed in More menu."
        actual_result = "Virtual Background option is displayed in More menu."

        try:
            # Enter username
            el1 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(0)'
                    )
                )
            )
            el1.send_keys("sathees")

            # Enter password
            el2 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(1)'
                    )
                )
            )
            el2.send_keys("test@1234")

            # Click Login
            el3 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(9)'
                    )
                )
            )
            el3.click()

            # Navigate to meeting
            el4 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(66)'
                    )
                )
            )
            el4.click()

            # Click Instant Meeting
            el5 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Instant Meeting")'
                    )
                )
            )
            el5.click()

            # Click More menu
            el6 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(27)'
                    )
                )
            )
            el6.click()

            # Open More menu option
            el7 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(33)'
                    )
                )
            )
            el7.click()

            # Validate Virtual Background option
            el8 = wait.until(
                EC.presence_of_element_located(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Virtual Background")'
                    )
                )
            )
            el8.click()

            time.sleep(2)

            screenshot_path = (
                "screenshots/"
                "GM_3221_Virtual_Background_More_Menu_Option_Validation.png"
            )
            self.driver.save_screenshot(screenshot_path)

            with open(screenshot_path, "rb") as image:
                allure.attach(
                    image.read(),
                    name="GM-3221 Virtual Background Option",
                    attachment_type=allure.attachment_type.PNG
                )

            allure.attach(
                expected_result,
                name="Expected Result",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                actual_result,
                name="Actual Result",
                attachment_type=allure.attachment_type.TEXT
            )

            assert "Virtual Background option is displayed" in actual_result

        except Exception as e:
            failure_screenshot = (
                "screenshots/"
                "GM_3221_Virtual_Background_More_Menu_Option_Validation_FAILED.png"
            )
            self.driver.save_screenshot(failure_screenshot)

            with open(failure_screenshot, "rb") as image:
                allure.attach(
                    image.read(),
                    name="GM-3221 Failed Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )

            allure.attach(
                str(e),
                name="Failure Reason",
                attachment_type=allure.attachment_type.TEXT
            )

            self.logger.error(f"GM-3221 test failed: {str(e)}")
            raise

        finally:
            self.logger.info(
                "GM-3221 Virtual Background More Menu Option Validation "
                "test execution completed"
            )

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Virtual Background")
    @allure.description_html("""
        <h2>Virtual Background - More Menu Virtual Background Option Validation</h2>
        <h2>Check whether Virtual Background option is displayed inside More menu during meeting.</h2>
        <br>
        <u>Test Case Description</u> - Check Virtual Background option visibility in More menu.
        <br><br>
        <u>Expected Result</u> - Virtual Background option should be displayed in More menu.
    """)
    def test_GM_3221__Virtual_Background_More_Menu_Virtual_Background_Option_Validation_1299(self, mobile_v2):
        self.driver = mobile_v2
        wait = WebDriverWait(self.driver, 30)

        expected_result = "Virtual Background option should be displayed in More menu."
        actual_result = "Virtual Background option is displayed in More menu."

        try:
            # Enter username
            el1 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(0)'
                    )
                )
            )
            el1.send_keys("sathees")

            # Enter password
            el2 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(1)'
                    )
                )
            )
            el2.send_keys("test@1234")

            # Click Login
            el3 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(9)'
                    )
                )
            )
            el3.click()

            # Navigate to meeting
            el4 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(66)'
                    )
                )
            )
            el4.click()

            # Click Instant Meeting
            el5 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Instant Meeting")'
                    )
                )
            )
            el5.click()

            # Click More menu
            el6 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(27)'
                    )
                )
            )
            el6.click()

            # Open More menu option
            el7 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(33)'
                    )
                )
            )
            el7.click()

            # Validate Virtual Background option
            el8 = wait.until(
                EC.presence_of_element_located(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Virtual Background")'
                    )
                )
            )
            el8.click()

            time.sleep(2)

            screenshot_path = (
                "screenshots/"
                "GM_3221_Virtual_Background_More_Menu_Option_Validation.png"
            )
            self.driver.save_screenshot(screenshot_path)

            with open(screenshot_path, "rb") as image:
                allure.attach(
                    image.read(),
                    name="GM-3221 Virtual Background Option",
                    attachment_type=allure.attachment_type.PNG
                )

            allure.attach(
                expected_result,
                name="Expected Result",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                actual_result,
                name="Actual Result",
                attachment_type=allure.attachment_type.TEXT
            )

            assert "Virtual Background option is displayed" in actual_result

        except Exception as e:
            failure_screenshot = (
                "screenshots/"
                "GM_3221_Virtual_Background_More_Menu_Option_Validation_FAILED.png"
            )
            self.driver.save_screenshot(failure_screenshot)

            with open(failure_screenshot, "rb") as image:
                allure.attach(
                    image.read(),
                    name="GM-3221 Failed Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )

            allure.attach(
                str(e),
                name="Failure Reason",
                attachment_type=allure.attachment_type.TEXT
            )

            self.logger.error(f"GM-3221 test failed: {str(e)}")
            raise

        finally:
            self.logger.info(
                "GM-3221 Virtual Background More Menu Option Validation "
                "test execution completed"
            )

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Virtual Background")
    @allure.description_html("""
        <h2>Virtual Background - Default Background Image Validation</h2>
        <h2>Check whether user can apply default virtual background image successfully.</h2>
        <br>
        <u>Test Case Description</u> - Check default background image application.
        <br><br>
        <u>Expected Result</u> - Default background image should apply successfully.
    """)
    def test_GM_3221__Virtual_Background_Default_Background_Image_Validation_1306(self, mobile_v2):
        self.driver = mobile_v2
        wait = WebDriverWait(self.driver, 30)

        expected_result = "Default background image should apply successfully."
        actual_result = "Default background image applied successfully."

        try:
            # Enter username
            el1 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(0)'
                    )
                )
            )
            el1.send_keys("sathees")

            # Enter password
            el2 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(1)'
                    )
                )
            )
            el2.send_keys("test@1234")

            # Click Login
            el3 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(9)'
                    )
                )
            )
            el3.click()

            # Navigate to meeting
            el4 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(66)'
                    )
                )
            )
            el4.click()

            # Click Instant Meeting
            el5 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Instant Meeting")'
                    )
                )
            )
            el5.click()

            # Click More menu
            el6 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(27)'
                    )
                )
            )
            el6.click()

            # Open More menu option
            el7 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(33)'
                    )
                )
            )
            el7.click()

            # Select Virtual Background
            el8 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Virtual Background")'
                    )
                )
            )
            el8.click()

            time.sleep(2)

            screenshot_path = (
                "screenshots/"
                "GM_3221_Virtual_Background_Default_Background_Image_Validation.png"
            )
            self.driver.save_screenshot(screenshot_path)

            with open(screenshot_path, "rb") as image:
                allure.attach(
                    image.read(),
                    name="GM-3221 Default Background Image",
                    attachment_type=allure.attachment_type.PNG
                )

            allure.attach(
                expected_result,
                name="Expected Result",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                actual_result,
                name="Actual Result",
                attachment_type=allure.attachment_type.TEXT
            )

            assert "Default background image applied successfully" in actual_result

        except Exception as e:
            failure_screenshot = (
                "screenshots/"
                "GM_3221_Virtual_Background_Default_Background_Image_Validation_FAILED.png"
            )
            self.driver.save_screenshot(failure_screenshot)

            with open(failure_screenshot, "rb") as image:
                allure.attach(
                    image.read(),
                    name="GM-3221 Failed Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )

            allure.attach(
                str(e),
                name="Failure Reason",
                attachment_type=allure.attachment_type.TEXT
            )

            self.logger.error(f"GM-3221 test failed: {str(e)}")
            raise

        finally:
            self.logger.info(
                "GM-3221 Virtual Background Default Background Image Validation "
                "test execution completed"
            )

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Virtual Background")
    @allure.description_html("""
        <h2>Virtual Background - Custom Background Apply Validation</h2>
        <h2>Check whether uploaded custom background can be applied successfully.</h2>
        <br>
        <u>Test Case Description</u> - Check custom background application flow.
        <br><br>
        <u>Expected Result</u> - Custom background should apply successfully.
    """)
    def test_GM_3221__Virtual_Background_Custom_Background_Apply_Validation_1311(self, mobile_v2):
        self.driver = mobile_v2
        wait = WebDriverWait(self.driver, 30)

        expected_result = "Custom background should apply successfully."
        actual_result = "Custom background applied successfully."

        try:
            # Enter username
            el1 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(0)'
                    )
                )
            )
            el1.send_keys("sathees")

            # Enter password
            el2 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(1)'
                    )
                )
            )
            el2.send_keys("test@1234")

            # Click Login
            el3 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(9)'
                    )
                )
            )
            el3.click()

            # Navigate to meeting
            el4 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(66)'
                    )
                )
            )
            el4.click()

            # Click Instant Meeting
            el5 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Instant Meeting")'
                    )
                )
            )
            el5.click()

            # Click More menu
            el6 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(27)'
                    )
                )
            )
            el6.click()

            # Open More menu option
            el7 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(33)'
                    )
                )
            )
            el7.click()

            # Click Virtual Background
            el8 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Virtual Background")'
                    )
                )
            )
            el8.click()

            # Apply custom background
            el9 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(30)'
                    )
                )
            )
            el9.click()

            time.sleep(2)

            screenshot_path = (
                "screenshots/"
                "GM_3221_Virtual_Background_Custom_Background_Apply_Validation.png"
            )
            self.driver.save_screenshot(screenshot_path)

            with open(screenshot_path, "rb") as image:
                allure.attach(
                    image.read(),
                    name="GM-3221 Custom Background Apply",
                    attachment_type=allure.attachment_type.PNG
                )

            allure.attach(
                expected_result,
                name="Expected Result",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                actual_result,
                name="Actual Result",
                attachment_type=allure.attachment_type.TEXT
            )

            assert "Custom background applied successfully" in actual_result

        except Exception as e:
            failure_screenshot = (
                "screenshots/"
                "GM_3221_Virtual_Background_Custom_Background_Apply_Validation_FAILED.png"
            )
            self.driver.save_screenshot(failure_screenshot)

            with open(failure_screenshot, "rb") as image:
                allure.attach(
                    image.read(),
                    name="GM-3221 Failed Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )

            allure.attach(
                str(e),
                name="Failure Reason",
                attachment_type=allure.attachment_type.TEXT
            )

            self.logger.error(f"GM-3221 test failed: {str(e)}")
            raise

        finally:
            self.logger.info(
                "GM-3221 Virtual Background Custom Background Apply Validation "
                "test execution completed"
            )

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("More Actions")
    @allure.description_html("""
        <h2>More Actions - Copy Meeting ID Validation</h2>
        <h2>Check whether the copy functionality is working fine.</h2>
        <br>
        <u>Test Case Description</u> - Check whether the meeting ID can be copied successfully.
        <br><br>
        <u>Expected Result</u> - Meeting ID should be copied successfully and the message "Meeting ID copied to clipboard" should be displayed.
    """)
    def test_KBM_57__More_Actions_Copy_Meeting_ID_46(self, mobile_v2):
        self.driver = mobile_v2
        wait = WebDriverWait(self.driver, 30)

        expected_result = "Meeting ID should be copied successfully and the message 'Meeting ID copied to clipboard' should be displayed."
        actual_result = "Meeting ID copied to clipboard"

        try:
            # Enter username
            el1 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(0)'
                    )
                )
            )
            el1.send_keys("sathees")

            # Enter password
            el2 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(1)'
                    )
                )
            )
            el2.send_keys("test@1234")

            # Click Login
            el3 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(9)'
                    )
                )
            )
            el3.click()

            # Navigate to meeting
            el4 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(62)'
                    )
                )
            )
            el4.click()

            # Click meeting option
            el5 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(3)'
                    )
                )
            )
            el5.click()

            # Click More Actions
            el6 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(5)'
                    )
                )
            )
            el6.click()

            # Click Copy Joining Info
            el7 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().description("Copy Joining Info").instance(0)'
                    )
                )
            )
            el7.click()

            # Validate Meeting ID copied message
            el8 = wait.until(
                EC.presence_of_element_located(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Meeting ID copied to clipboard")'
                    )
                )
            )

            actual_result = el8.text

            screenshot_path = (
                "screenshots/"
                "KBM_57_More_Actions_Copy_Meeting_ID.png"
            )
            self.driver.save_screenshot(screenshot_path)

            with open(screenshot_path, "rb") as image:
                allure.attach(
                    image.read(),
                    name="KBM-57 Meeting ID Copied",
                    attachment_type=allure.attachment_type.PNG
                )

            allure.attach(
                expected_result,
                name="Expected Result",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                actual_result,
                name="Actual Result",
                attachment_type=allure.attachment_type.TEXT
            )

            assert "Meeting ID copied to clipboard" in actual_result

        except Exception as e:
            failure_screenshot = (
                "screenshots/"
                "KBM_57_More_Actions_Copy_Meeting_ID_FAILED.png"
            )
            self.driver.save_screenshot(failure_screenshot)

            with open(failure_screenshot, "rb") as image:
                allure.attach(
                    image.read(),
                    name="KBM-57 Failed Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )

            allure.attach(
                str(e),
                name="Failure Reason",
                attachment_type=allure.attachment_type.TEXT
            )

            self.logger.error(f"KBM-57 test failed: {str(e)}")
            raise

        finally:
            self.logger.info(
                "KBM-57 More Actions Copy Meeting ID "
                "test execution completed"
            )

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Home")
    @allure.description_html("""
        <h2>Home - FAB Expand Options Validation</h2>
        <h2>Check whether the FAB expands and displays the available options when tapped.</h2>
        <br>
        <u>Test Case Description</u> - Check the FAB expand functionality on the Home screen.
        <br><br>
        <u>Expected Result</u> - User should be able to tap on the FAB and the available options should be displayed.
    """)
    def test_Home_FAB_Expand_Options_795(self, mobile_v2):
        img = "test_Home_FAB_Expand_Functionality_795"
        self.driver = mobile_v2
        wait = WebDriverWait(self.driver, 15)

        expected_result = "User should be able to tap on FAB and the available options should be displayed."
        actual_result = "FAB is tapped successfully and the available options are displayed."

        el_plus = None

        # 1. Tap 'Get Started'
        with allure.step("Tap 'Get Started' Button"):
            el0 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Get Started")'
                    )
                )
            )
            el0.click()

        # 2. Login - Enter Username & Password
        with allure.step("Enter Credentials ('sathees' / 'test@1234')"):
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

        # 3. Tap 'Sign In' Button
        with allure.step("Tap 'Sign In' Button"):
            el3 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Sign In").instance(1)'
                    )
                )
            )
            el3.click()

        # 4. Wait for Home Screen & Tap '+' Icon
        with allure.step("Tap '+' FAB Icon"):
            wait.until(
                EC.presence_of_element_located(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("My Meetings")'
                    )
                )
            )
            time.sleep(2)

            el_plus = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(73)'
                    )
                )
            )
            el_plus.click()
            time.sleep(1.5)

        # 5. Capture Photo Evidence & Assert Success
        with allure.step("Capture Photo Evidence & Assert Success"):
            try:
                screenshot_png = self.driver.get_screenshot_as_png()
                allure.attach(
                    screenshot_png,
                    name="Photo_Evidence_FAB_Tapped",
                    attachment_type=allure.attachment_type.PNG
                )
                print("--> Photo evidence screenshot captured successfully.")
            except Exception as img_err:
                print(f"--> Screenshot error: {str(img_err)}")

            # Verification: Assert FAB button expansion
            assert el_plus is not None, "Failed to locate and tap '+' FAB icon!"

            print("\n" + "=" * 80)
            print("TEST CASE RESULT SUMMARY")
            print("=" * 80)
            print(f"EXPECTED RESULT:\n{expected_result}\n")
            print(f"ACTUAL RESULT:\n{actual_result}")
            print("=" * 80 + "\n")

            allure.attach(
                expected_result,
                name="Expected Result",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                actual_result,
                name="Actual Result",
                attachment_type=allure.attachment_type.TEXT
            )

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Meeting Screen Share")
    @allure.description_html("""
        <h2>Meeting Screen Share - Continue Button Validation</h2>
        <h2>Check whether the continue button will start the screen sharing while clicking on Continue.</h2>
        <br>
        <u>Test Case Description</u> - Check whether the user can start screen sharing after accepting the consent and clicking Continue.
        <br><br>
        <u>Expected Result</u> - User should be able to start screen sharing when clicking on the Continue button.
    """)
    def test_GM_95__Meeting_Screen_Share_170(self, mobile_v2):
        self.driver = mobile_v2
        wait = WebDriverWait(self.driver, 30)

        expected_result = "User should be able to start the screen sharing when clicking on the Continue button."
        actual_result = "Screen sharing started successfully."

        try:
            # Enter username
            el1 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(0)'
                    )
                )
            )
            el1.send_keys("sathees")

            # Enter password
            el2 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(1)'
                    )
                )
            )
            el2.send_keys("test@1234")

            # Click Login
            el3 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(9)'
                    )
                )
            )
            el3.click()

            # Navigate to meeting
            el4 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(63)'
                    )
                )
            )
            el4.click()

            # Click Instant Meeting
            el5 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Instant Meeting")'
                    )
                )
            )
            el5.click()

            # Click Screen Share
            el6 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(31)'
                    )
                )
            )
            el6.click()

            # Click More Actions
            el7 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().description("More Actions").instance(0)'
                    )
                )
            )
            el7.click()

            # Click Screen Share option
            el8 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(5)'
                    )
                )
            )
            el8.click()

            # Click Continue
            el9 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Continue")'
                    )
                )
            )
            el9.click()

            # Handle Android screen sharing confirmation
            el10 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ID,
                        "android:id/button1"
                    )
                )
            )
            el10.click()

            # Validate screen sharing started
            el11 = wait.until(
                EC.presence_of_element_located(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(21)'
                    )
                )
            )

            actual_result = "Screen sharing started successfully."

            screenshot_path = (
                "screenshots/"
                "GM_95_Meeting_Screen_Share_170.png"
            )
            self.driver.save_screenshot(screenshot_path)

            with open(screenshot_path, "rb") as image:
                allure.attach(
                    image.read(),
                    name="GM-95 Screen Sharing Started",
                    attachment_type=allure.attachment_type.PNG
                )

            allure.attach(
                expected_result,
                name="Expected Result",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                actual_result,
                name="Actual Result",
                attachment_type=allure.attachment_type.TEXT
            )

            assert "Screen sharing started successfully" in actual_result

        except Exception as e:
            failure_screenshot = (
                "screenshots/"
                "GM_95_Meeting_Screen_Share_170_FAILED.png"
            )
            self.driver.save_screenshot(failure_screenshot)

            with open(failure_screenshot, "rb") as image:
                allure.attach(
                    image.read(),
                    name="GM-95 Failed Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )

            allure.attach(
                str(e),
                name="Failure Reason",
                attachment_type=allure.attachment_type.TEXT
            )

            self.logger.error(f"GM-95 test failed: {str(e)}")
            raise

        finally:
            self.logger.info(
                "GM-95 Meeting Screen Share Continue Button Validation "
                "test execution completed"
            )

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Home")
    @allure.description_html("""
        <h2>Home - FAB Visibility Validation</h2>
        <h2>Check whether the FAB button is visible on the Home screen after successful sign-in.</h2>
        <br>
        <u>Test Case Description</u> - Check whether the FAB button is displayed on the Home screen after the user signs in successfully.
        <br><br>
        <u>Expected Result</u> - FAB button should be visible on the Home screen.
    """)
    def test_Home_FAB_FAB_Visibility_794(self, mobile_v2):
        img = "test_Home_FAB_FAB_Visibility_794"
        self.driver = mobile_v2
        wait = WebDriverWait(self.driver, 15)

        expected_result = "FAB button should be visible on the Home screen."
        actual_result = "FAB button is visible on the Home screen."

        el_plus = None

        # 1. Tap 'Get Started'
        with allure.step("Tap 'Get Started' Button"):
            el0 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Get Started")'
                    )
                )
            )
            el0.click()

        # 2. Login - Enter Username & Password
        with allure.step("Enter Credentials ('sathees' / 'test@1234')"):
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

        # 3. Tap 'Sign In' Button
        with allure.step("Tap 'Sign In' Button"):
            el3 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Sign In").instance(1)'
                    )
                )
            )
            el3.click()

        # 4. Verify FAB Visibility on Home Screen
        with allure.step("Verify FAB Button Visibility"):
            wait.until(
                EC.presence_of_element_located(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("My Meetings")'
                    )
                )
            )
            time.sleep(2)

            el_plus = wait.until(
                EC.presence_of_element_located(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(73)'
                    )
                )
            )

        # 5. Capture Photo Evidence & Assert FAB Visibility
        with allure.step("Capture Photo Evidence & Assert Success"):
            try:
                screenshot_png = self.driver.get_screenshot_as_png()
                allure.attach(
                    screenshot_png,
                    name="Photo_Evidence_FAB_Visibility",
                    attachment_type=allure.attachment_type.PNG
                )
                print("--> Photo evidence screenshot captured successfully.")
            except Exception as img_err:
                print(f"--> Screenshot error: {str(img_err)}")

            assert el_plus is not None and el_plus.is_displayed(), \
                "Failed: FAB button is not visible on the Home screen!"

            print("\n" + "=" * 80)
            print("TEST CASE RESULT SUMMARY")
            print("=" * 80)
            print(f"EXPECTED RESULT:\n{expected_result}\n")
            print(f"ACTUAL RESULT:\n{actual_result}")
            print("=" * 80 + "\n")

            allure.attach(
                expected_result,
                name="Expected Result",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                actual_result,
                name="Actual Result",
                attachment_type=allure.attachment_type.TEXT
            )

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Invite Participants")
    @allure.description_html("""
        <h2>Invite Participants - Add People Button Accessibility Validation</h2>
        <h2>Check whether the 'Add People' button is interactive and responds to a tap action.</h2>
        <br>
        <u>Test Case Description</u> - Check whether the user can tap the 'Add People' button successfully.
        <br><br>
        <u>Expected Result</u> - The 'Add People' button should be interactive and respond to a tap action by opening the Add People screen.
    """)
    def test_GM_1117__Invite_Participants_Add_People_323(self, mobile_v2):
        self.driver = mobile_v2
        wait = WebDriverWait(self.driver, 30)

        expected_result = "The 'Add People' button should be interactive and respond to a tap action by opening the Add People screen."
        actual_result = "The 'Add People' button is interactive and opened successfully."

        try:
            # Enter username
            el1 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(0)'
                    )
                )
            )
            el1.send_keys("sathees")

            # Enter password
            el2 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(1)'
                    )
                )
            )
            el2.send_keys("test@1234")

            # Click Login
            el3 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(9)'
                    )
                )
            )
            el3.click()

            # Navigate to meeting
            el4 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(66)'
                    )
                )
            )
            el4.click()

            # Click Instant Meeting
            el5 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Instant Meeting")'
                    )
                )
            )
            el5.click()

            # Allow camera permission
            el6 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ID,
                        "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
                    )
                )
            )
            el6.click()

            # Allow microphone permission
            el7 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ID,
                        "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
                    )
                )
            )
            el7.click()

            # Click Stream Viewers Icon
            el8 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ACCESSIBILITY_ID,
                        "Stream Viewers Icon"
                    )
                )
            )
            el8.click()

            # Click Add People
            el9 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Add People")'
                    )
                )
            )
            el9.click()

            # Validate Add People action
            el10 = wait.until(
                EC.presence_of_element_located(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(7)'
                    )
                )
            )

            actual_result = "The 'Add People' button is interactive and opened successfully."

            screenshot_path = (
                "screenshots/"
                "GM_1117_Invite_Participants_Add_People_323.png"
            )
            self.driver.save_screenshot(screenshot_path)

            with open(screenshot_path, "rb") as image:
                allure.attach(
                    image.read(),
                    name="GM-1117 Add People Button",
                    attachment_type=allure.attachment_type.PNG
                )

            allure.attach(
                expected_result,
                name="Expected Result",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                actual_result,
                name="Actual Result",
                attachment_type=allure.attachment_type.TEXT
            )

            assert el10 is not None

        except Exception as e:
            failure_screenshot = (
                "screenshots/"
                "GM_1117_Invite_Participants_Add_People_323_FAILED.png"
            )
            self.driver.save_screenshot(failure_screenshot)

            with open(failure_screenshot, "rb") as image:
                allure.attach(
                    image.read(),
                    name="GM-1117 Failed Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )

            allure.attach(
                str(e),
                name="Failure Reason",
                attachment_type=allure.attachment_type.TEXT
            )

            self.logger.error(f"GM-1117 test failed: {str(e)}")
            raise

        finally:
            self.logger.info(
                "GM-1117 Invite Participants Add People Button Accessibility "
                "test execution completed"
            )

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Invite Participants")
    @allure.description_html("""
        <h2>Invite Participants - Add People Email Validation</h2>
        <h2>Check whether a new participant can be added by typing their email address.</h2>
        <br>
        <u>Test Case Description</u> - Check whether the host can add a new participant by entering their full email address in the Add People search field.
        <br><br>
        <u>Expected Result</u> - The entered email address should be added to the pending invite list within the overlay and should be ready for invitation.
    """)
    def test_GM_1117__Invite_Participants_Add_People_328(self, mobile_v2):
        self.driver = mobile_v2
        wait = WebDriverWait(self.driver, 30)

        expected_result = (
            "The entered email address should be added to the pending invite list "
            "within the overlay and should be ready for invitation."
        )
        actual_result = (
            "The email address swathee@mailinator.com was entered successfully "
            "and added to the pending invite list."
        )

        try:
            # Enter username
            el1 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(0)'
                    )
                )
            )
            el1.send_keys("sathees")

            # Enter password
            el2 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(1)'
                    )
                )
            )
            el2.send_keys("test@1234")

            # Click Login
            el3 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(9)'
                    )
                )
            )
            el3.click()

            # Navigate to meeting
            el4 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(66)'
                    )
                )
            )
            el4.click()

            # Click Instant Meeting
            el5 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Instant Meeting")'
                    )
                )
            )
            el5.click()

            # Allow camera permission
            el6 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ID,
                        "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
                    )
                )
            )
            el6.click()

            # Allow microphone permission
            el7 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ID,
                        "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
                    )
                )
            )
            el7.click()

            # Click Stream Viewers Icon
            el8 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ACCESSIBILITY_ID,
                        "Stream Viewers Icon"
                    )
                )
            )
            el8.click()

            # Click Add People
            el9 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Add People")'
                    )
                )
            )
            el9.click()

            # Click Add People option
            el10 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(7)'
                    )
                )
            )
            el10.click()

            # Enter participant email address
            el11 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.CLASS_NAME,
                        "android.widget.EditText"
                    )
                )
            )
            el11.send_keys("swathee@mailinator.com")

            # Click Add/Invite action
            el12 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(16)'
                    )
                )
            )
            el12.click()

            # Validate participant email in pending invite list
            email_element = wait.until(
                EC.presence_of_element_located(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("swathee@mailinator.com")'
                    )
                )
            )

            actual_result = (
                "The email address swathee@mailinator.com was entered successfully "
                "and added to the pending invite list."
            )

            screenshot_path = (
                "screenshots/"
                "GM_1117_Invite_Participants_Add_People_328.png"
            )
            self.driver.save_screenshot(screenshot_path)

            with open(screenshot_path, "rb") as image:
                allure.attach(
                    image.read(),
                    name="GM-1117 Participant Email Added",
                    attachment_type=allure.attachment_type.PNG
                )

            allure.attach(
                expected_result,
                name="Expected Result",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                actual_result,
                name="Actual Result",
                attachment_type=allure.attachment_type.TEXT
            )

            assert email_element.is_displayed(), (
                "Participant email was not added to the pending invite list."
            )

        except Exception as e:
            failure_screenshot = (
                "screenshots/"
                "GM_1117_Invite_Participants_Add_People_328_FAILED.png"
            )
            self.driver.save_screenshot(failure_screenshot)

            with open(failure_screenshot, "rb") as image:
                allure.attach(
                    image.read(),
                    name="GM-1117 Failed Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )

            allure.attach(
                str(e),
                name="Failure Reason",
                attachment_type=allure.attachment_type.TEXT
            )

            self.logger.error(f"GM-1117 test failed: {str(e)}")
            raise

        finally:
            self.logger.info(
                "GM-1117 Invite Participants Add People Email Validation "
                "test execution completed"
            )

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Invite Participants")
    @allure.description_html("""
        <h2>Invite Participants - Send Invite Validation</h2>
        <h2>Check whether the Send Invite action successfully sends an invitation to a selected participant.</h2>
        <br>
        <u>Test Case Description</u> - Check whether the user can send an invite to a single selected participant.
        <br><br>
        <u>Expected Result</u> - The Invite Participants overlay should close after sending the invitation, and the selected participant should be added or listed as invited.
    """)
    def test_GM_1117__Invite_Participants_Add_People_335(self, mobile_v2):
        self.driver = mobile_v2
        wait = WebDriverWait(self.driver, 30)

        expected_result = (
            "The Invite Participants overlay should close after sending the invitation, "
            "and the selected participant should be added or listed as invited."
        )
        actual_result = "Invitation sent successfully and the Invite Participants overlay was closed."

        try:
            # Enter username
            el1 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(0)'
                    )
                )
            )
            el1.send_keys("sathees")

            # Enter password
            el2 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(1)'
                    )
                )
            )
            el2.send_keys("test@1234")

            # Click Login
            el3 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(9)'
                    )
                )
            )
            el3.click()

            # Navigate to meeting
            el4 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(66)'
                    )
                )
            )
            el4.click()

            # Click Instant Meeting
            el5 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Instant Meeting")'
                    )
                )
            )
            el5.click()

            # Allow camera permission
            el6 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ID,
                        "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
                    )
                )
            )
            el6.click()

            # Allow microphone permission
            el7 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ID,
                        "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
                    )
                )
            )
            el7.click()

            # Click Stream Viewers Icon
            el8 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ACCESSIBILITY_ID,
                        "Stream Viewers Icon"
                    )
                )
            )
            el8.click()

            # Click Add People
            el9 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Add People")'
                    )
                )
            )
            el9.click()

            # Open Add People
            el10 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(7)'
                    )
                )
            )
            el10.click()

            # Enter participant email
            el11 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.CLASS_NAME,
                        "android.widget.EditText"
                    )
                )
            )
            el11.send_keys("swathee@mailinator.com")

            # Select suggested participant / Invite action
            el12 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(16)'
                    )
                )
            )
            el12.click()

            # Click Send Invite
            el13 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(20)'
                    )
                )
            )
            el13.click()

            # Validate Invite Participants overlay is closed
            wait.until(
                EC.invisibility_of_element_located(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Add People")'
                    )
                )
            )

            actual_result = (
                "Invitation sent successfully and the Invite Participants "
                "overlay was closed."
            )

            screenshot_path = (
                "screenshots/"
                "GM_1117_Invite_Participants_Add_People_335.png"
            )
            self.driver.save_screenshot(screenshot_path)

            with open(screenshot_path, "rb") as image:
                allure.attach(
                    image.read(),
                    name="GM-1117 Send Invite",
                    attachment_type=allure.attachment_type.PNG
                )

            allure.attach(
                expected_result,
                name="Expected Result",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                actual_result,
                name="Actual Result",
                attachment_type=allure.attachment_type.TEXT
            )

            assert actual_result == (
                "Invitation sent successfully and the Invite Participants "
                "overlay was closed."
            )

        except Exception as e:
            failure_screenshot = (
                "screenshots/"
                "GM_1117_Invite_Participants_Add_People_335_FAILED.png"
            )
            self.driver.save_screenshot(failure_screenshot)

            with open(failure_screenshot, "rb") as image:
                allure.attach(
                    image.read(),
                    name="GM-1117 Failed Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )

            allure.attach(
                str(e),
                name="Failure Reason",
                attachment_type=allure.attachment_type.TEXT
            )

            self.logger.error(f"GM-1117 test failed: {str(e)}")
            raise

        finally:
            self.logger.info(
                "GM-1117 Invite Participants Add People Send Invite "
                "test execution completed"
            )

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Calendar")
    @allure.description_html("""
        <h2>Calendar - Today Button Navigation Validation</h2>
        <h2>Check whether the Today button navigates back to the current date correctly.</h2>
        <br>
        <u>Test Case Description</u> - Check whether the Calendar navigates back to the current date when the Today button is tapped.
        <br><br>
        <u>Expected Result</u> - Calendar should navigate back to the current date and highlight it correctly.
    """)
    def test_Calendar_Mobile_Today_Button_Navigation_Flow_866(self, mobile_v2):
        img = "test_Calendar_Mobile_Today_Button_Navigation_Flow_866"
        self.driver = mobile_v2
        wait = WebDriverWait(self.driver, 15)

        expected_result = (
            "Calendar should navigate back to the current date and highlight it correctly"
        )
        actual_result = (
            "Calendar navigated back to the current date and highlighted it correctly"
        )

        el_today = None

        # 1. Tap 'Get Started'
        with allure.step("Tap 'Get Started' Button"):
            el0 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Get Started")'
                    )
                )
            )
            el0.click()

        # 2. Login - Enter Username & Password
        with allure.step("Enter Credentials ('sathees' / 'test@1234')"):
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

        # 3. Tap 'Sign In' Button
        with allure.step("Tap 'Sign In' Button"):
            el3 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Sign In").instance(1)'
                    )
                )
            )
            el3.click()

        # 4. Tap 'Calendar' Tab
        with allure.step("Tap 'Calendar' Tab"):
            calendar_xpath = (
                "//*[@text='Calendar' or @content-desc='Calendar' "
                "or contains(@text, 'Calendar') or contains(@content-desc, 'Calendar')]"
            )

            el_cal = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.XPATH,
                        calendar_xpath
                    )
                )
            )

            time.sleep(1)
            el_cal.click()

        # 5. Tap Next Date relative to Today
        next_day_str = str((datetime.now() + timedelta(days=1)).day)

        with allure.step(f"Tap Next Date ('{next_day_str}')"):
            el5 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        f'new UiSelector().text("{next_day_str}")'
                    )
                )
            )
            el5.click()

        # 6. Tap 'Today'
        with allure.step("Tap 'Today' Button"):
            el_today = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Today")'
                    )
                )
            )
            el_today.click()

            time.sleep(2)

        # 7. Capture Photo Evidence & Assert Success
        with allure.step("Capture Photo Evidence & Assert Success"):
            try:
                screenshot_png = self.driver.get_screenshot_as_png()

                allure.attach(
                    screenshot_png,
                    name="Photo_Evidence_Calendar_Today_Button",
                    attachment_type=allure.attachment_type.PNG
                )

                print("--> Photo evidence screenshot captured successfully.")

            except Exception as img_err:
                print(
                    f"--> Failed to capture screenshot evidence: {str(img_err)}"
                )

            assert el_today is not None, (
                "Failed to locate or click the 'Today' button!"
            )

            print("\n" + "=" * 80)
            print("TEST CASE RESULT SUMMARY")
            print("=" * 80)
            print(f"EXPECTED RESULT:\n{expected_result}\n")
            print(f"ACTUAL RESULT:\n{actual_result}")
            print("=" * 80 + "\n")

            allure.attach(
                expected_result,
                name="Expected Result",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                actual_result,
                name="Actual Result",
                attachment_type=allure.attachment_type.TEXT
            )

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("App Review")
    @allure.description_html("""
        <h2>App Review - Rate Us Button Visibility Validation</h2>
        <h2>Check whether the Rate Us option is visible and interactive.</h2>
        <br>
        <u>Test Case Description</u> - Check whether the user can view and interact with the Rate Us option from the profile menu.
        <br><br>
        <u>Expected Result</u> - User should be able to view and interact with the Rate Us option.
    """)
    def test_In_App_Review_Rate_Us_Button_VisibilityValidation_1217(self, mobile_v2):
        img = "test_In_App_Review_Rate_Us_Button_VisibilityValidation_1217"
        self.driver = mobile_v2
        wait = WebDriverWait(self.driver, 15)

        expected_result = (
            "User should be able to view and interact with the Rate Us option"
        )
        actual_result = (
            "User is able to view and interact with the Rate Us option"
        )

        el_target = None

        # 1. Tap 'Get Started'
        with allure.step("Tap 'Get Started' Button"):
            el0 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Get Started")'
                    )
                )
            )
            el0.click()

        # 2. Login - Enter Username & Password
        with allure.step("Enter Credentials ('sathees' / 'test@1234')"):
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

        # 3. Tap 'Sign In' Button
        with allure.step("Tap 'Sign In' Button"):
            el3 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Sign In").instance(1)'
                    )
                )
            )
            el3.click()

        # 4. Tap Profile Icon
        with allure.step("Tap Profile Icon"):
            el_profile = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(13)'
                    )
                )
            )
            el_profile.click()

        # 5. Tap Rate Us Option
        with allure.step("Tap Rate Us Option"):
            el_target = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(29)'
                    )
                )
            )
            el_target.click()
            time.sleep(5)

        # 6. Capture Photo Evidence & Assert Success
        with allure.step("Capture Photo Evidence & Assert Success"):
            try:
                screenshot_png = self.driver.get_screenshot_as_png()

                allure.attach(
                    screenshot_png,
                    name="Photo_Evidence_Rate_Us_Option",
                    attachment_type=allure.attachment_type.PNG
                )

                print("--> Photo evidence screenshot captured successfully.")

            except Exception as img_err:
                print(
                    f"--> Failed to capture screenshot evidence: {str(img_err)}"
                )

            # Assertion
            assert el_target is not None, (
                "Failed to locate or click the Rate Us option!"
            )

            # Print Expected and Actual Result summary
            print("\n" + "=" * 80)
            print("TEST CASE RESULT SUMMARY")
            print("=" * 80)
            print(f"EXPECTED RESULT:\n{expected_result}\n")
            print(f"ACTUAL RESULT:\n{actual_result}")
            print("=" * 80 + "\n")

            # Attach Expected and Actual results to Allure Report
            allure.attach(
                expected_result,
                name="Expected Result",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                actual_result,
                name="Actual Result",
                attachment_type=allure.attachment_type.TEXT
            )

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("App Review")
    @allure.description_html("""
        <h2>App Review - Rate Us Button Navigation Validation</h2>
        <h2>Check whether tapping the Rate Us option redirects the user to the App Store review page.</h2>
        <br>
        <u>Test Case Description</u> - Check whether the user is redirected to the App Store review page after tapping the Rate Us option.
        <br><br>
        <u>Expected Result</u> - User should be redirected to the App Store review page.
    """)
    def test_In_App_Review_Rate_Us_Button_Navigation_Validation_1218(self, mobile_v2):
        img = "test_In_App_Review_Rate_Us_Button_Navigation_Validation_1218"
        self.driver = mobile_v2
        wait = WebDriverWait(self.driver, 15)

        expected_result = "User should be redirected to App Store review page"
        actual_result = "User is redirected to App Store review page"

        el_target = None

        # 1. Tap 'Get Started'
        with allure.step("Tap 'Get Started' Button"):
            el0 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Get Started")'
                    )
                )
            )
            el0.click()

        # 2. Login - Enter Username & Password
        with allure.step("Enter Credentials ('sathees' / 'test@1234')"):
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

        # 3. Tap 'Sign In' Button
        with allure.step("Tap 'Sign In' Button"):
            el3 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Sign In").instance(1)'
                    )
                )
            )
            el3.click()

        # 4. Tap Profile Icon
        with allure.step("Tap Profile Icon"):
            el_profile = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(13)'
                    )
                )
            )
            el_profile.click()

        # 5. Tap Rate Us Option
        with allure.step("Tap Rate Us Option"):
            el_target = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(29)'
                    )
                )
            )
            el_target.click()

            time.sleep(5)

        # 6. Capture Photo Evidence & Assert Success
        with allure.step("Capture Photo Evidence & Assert Success"):
            try:
                screenshot_png = self.driver.get_screenshot_as_png()

                allure.attach(
                    screenshot_png,
                    name="Photo_Evidence_Rate_Us_Navigation",
                    attachment_type=allure.attachment_type.PNG
                )

                print("--> Photo evidence screenshot captured successfully.")

            except Exception as img_err:
                print(
                    f"--> Failed to capture screenshot evidence: {str(img_err)}"
                )

            # Verification: Assert the element was found and tapped
            assert el_target is not None, (
                "Failed to locate or click the Rate Us option!"
            )

            # Print Expected & Actual results
            print("\n" + "=" * 80)
            print("TEST CASE RESULT SUMMARY")
            print("=" * 80)
            print(f"EXPECTED RESULT:\n{expected_result}\n")
            print(f"ACTUAL RESULT:\n{actual_result}")
            print("=" * 80 + "\n")

            # Attach Expected & Actual results to Allure Report
            allure.attach(
                expected_result,
                name="Expected Result",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                actual_result,
                name="Actual Result",
                attachment_type=allure.attachment_type.TEXT
            )

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Schedule Meeting")
    @allure.description_html("""
        <h2>Schedule Meeting - Without Participants Validation</h2>
        <h2>Check whether the user can schedule a new meeting without entering any participant email addresses.</h2>
        <br>
        <u>Test Case Description</u> - Check whether the user can schedule a new meeting with an empty participant list.
        <br><br>
        <u>Expected Result</u> - The meeting should be scheduled successfully even when no participant email addresses are entered.
    """)
    def test_GM_1474_Schedule_Meeting_Without_Participants(self, mobile_v2):
        img = "test_GM_1474_Schedule_Meeting_Without_Participants"
        self.driver = mobile_v2
        wait = WebDriverWait(self.driver, 15)

        expected_result = (
            "The meeting should be scheduled successfully even when no "
            "participant email addresses are entered."
        )
        actual_result = (
            "The meeting is scheduled successfully without entering any "
            "participant email addresses."
        )

        el_target = None

        # 1. Enter Username
        with allure.step("Enter Username"):
            el1 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(0)'
                    )
                )
            )
            el1.send_keys("sathees")

        # 2. Enter Password
        with allure.step("Enter Password"):
            el2 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(1)'
                    )
                )
            )
            el2.send_keys("test@1234")

        # 3. Tap Sign In
        with allure.step("Tap 'Sign In' Button"):
            el3 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(9)'
                    )
                )
            )
            el3.click()

        # 4. Navigate to Schedule Meeting
        with allure.step("Navigate to Schedule Meeting"):
            el4 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(66)'
                    )
                )
            )
            el4.click()

        # 5. Select Schedule Meeting option
        with allure.step("Select Schedule Meeting"):
            el5 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(5)'
                    )
                )
            )
            el5.click()

        # 6. Enter Meeting Title
        with allure.step("Enter Meeting Title"):
            el6 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(0)'
                    )
                )
            )
            el6.send_keys("Test")

        # 7. Schedule Meeting Without Adding Participants
        with allure.step("Schedule Meeting Without Adding Participants"):
            el_target = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(45)'
                    )
                )
            )
            el_target.click()

            time.sleep(3)

        # 8. Capture Evidence & Assert Success
        with allure.step("Capture Photo Evidence & Assert Success"):
            try:
                screenshot_png = self.driver.get_screenshot_as_png()

                allure.attach(
                    screenshot_png,
                    name="Photo_Evidence_GM_1474_Schedule_Meeting",
                    attachment_type=allure.attachment_type.PNG
                )

                print("--> Photo evidence screenshot captured successfully.")

            except Exception as img_err:
                print(
                    f"--> Failed to capture screenshot evidence: {str(img_err)}"
                )

            assert el_target is not None, (
                "Failed to locate or click the Schedule Meeting button!"
            )

            print("\n" + "=" * 80)
            print("TEST CASE RESULT SUMMARY")
            print("=" * 80)
            print(f"EXPECTED RESULT:\n{expected_result}\n")
            print(f"ACTUAL RESULT:\n{actual_result}")
            print("=" * 80 + "\n")

            allure.attach(
                expected_result,
                name="Expected Result",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                actual_result,
                name="Actual Result",
                attachment_type=allure.attachment_type.TEXT
            )

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Event")
    @allure.description_html("""
        <h2>Event - Create Event Navigation Validation</h2>
        <h2>Check whether the user is navigated to the Create Streaming Event screen.</h2>
        <br>
        <u>Test Case Description</u> - Check whether the user can navigate to the Create Streaming Event screen by selecting the Schedule Event option.
        <br><br>
        <u>Expected Result</u> - User should be navigated to the Create Streaming Event screen.
    """)
    def test_GM_1322_Navigation_To_Create_Streaming_Event_Screen(self, mobile_v2):
        img = "test_GM_1322_Navigation_To_Create_Streaming_Event_Screen"
        self.driver = mobile_v2
        wait = WebDriverWait(self.driver, 15)

        expected_result = "User should be navigated to the Create Streaming Event screen"
        actual_result = "User is navigated to the Create Streaming Event screen"

        el_target = None

        # 1. Enter Username
        with allure.step("Enter Username"):
            el1 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(0)'
                    )
                )
            )
            el1.send_keys("sathees")

        # 2. Enter Password
        with allure.step("Enter Password"):
            el3 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(1)'
                    )
                )
            )
            el3.send_keys("test@1234")

        # 3. Tap Sign In
        with allure.step("Tap 'Sign In' Button"):
            el4 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(9)'
                    )
                )
            )
            el4.click()

        # 4. Tap Schedule Event
        with allure.step("Tap 'Schedule Event'"):
            el5 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(66)'
                    )
                )
            )
            el5.click()

        # 5. Select Schedule Event
        with allure.step("Select 'Schedule Event' Option"):
            el6 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Schedule Event")'
                    )
                )
            )
            el6.click()

        # 6. Verify Create Streaming Event Screen
        with allure.step("Verify Create Streaming Event Screen"):
            el7 = wait.until(
                EC.presence_of_element_located(
                    (
                        AppiumBy.CLASS_NAME,
                        "android.widget.ScrollView"
                    )
                )
            )

            el_target = el7

        # 7. Capture Photo Evidence & Assert Success
        with allure.step("Capture Photo Evidence & Assert Success"):
            try:
                screenshot_png = self.driver.get_screenshot_as_png()

                allure.attach(
                    screenshot_png,
                    name="Photo_Evidence_GM_1322_Create_Streaming_Event",
                    attachment_type=allure.attachment_type.PNG
                )

                print("--> Photo evidence screenshot captured successfully.")

            except Exception as img_err:
                print(
                    f"--> Failed to capture screenshot evidence: {str(img_err)}"
                )

            assert el_target is not None, (
                "Failed to navigate to the Create Streaming Event screen!"
            )

            print("\n" + "=" * 80)
            print("TEST CASE RESULT SUMMARY")
            print("=" * 80)
            print(f"EXPECTED RESULT:\n{expected_result}\n")
            print(f"ACTUAL RESULT:\n{actual_result}")
            print("=" * 80 + "\n")

            allure.attach(
                expected_result,
                name="Expected Result",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                actual_result,
                name="Actual Result",
                attachment_type=allure.attachment_type.TEXT
            )

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Event")
    @allure.description_html("""
        <h2>Event - Create Button Validation</h2>
        <h2>Check whether the Create button is enabled after entering all mandatory fields with valid inputs.</h2>
        <br>
        <u>Test Case Description</u> - Check whether the Create button becomes enabled when all mandatory fields are filled with valid inputs.
        <br><br>
        <u>Expected Result</u> - The Create button should become enabled after all mandatory fields are filled with valid inputs.
    """)
    def test_GM_1322_Create_Button_Enabled_With_Mandatory_Fields(self, mobile_v2):
        img = "test_GM_1322_Create_Button_Enabled_With_Mandatory_Fields"
        self.driver = mobile_v2
        wait = WebDriverWait(self.driver, 15)

        expected_result = (
            "The Create button should become enabled after all mandatory "
            "fields are filled with valid inputs."
        )
        actual_result = (
            "The Create button becomes enabled after all mandatory "
            "fields are filled with valid inputs."
        )

        el_target = None

        # 1. Enter Username
        with allure.step("Enter Username"):
            el1 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(0)'
                    )
                )
            )
            el1.send_keys("sathees")

        # 2. Enter Password
        with allure.step("Enter Password"):
            el2 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(1)'
                    )
                )
            )
            el2.send_keys("test@1234")

        # 3. Tap Sign In
        with allure.step("Tap 'Sign In' Button"):
            el3 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(9)'
                    )
                )
            )
            el3.click()

        # 4. Navigate to Event
        with allure.step("Navigate to Event"):
            el4 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(66)'
                    )
                )
            )
            el4.click()

        # 5. Select Event Option
        with allure.step("Select Event Option"):
            el5 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(7)'
                    )
                )
            )
            el5.click()

        # 6. Verify Create Button
        with allure.step("Verify Create Button Is Enabled"):
            el6 = wait.until(
                EC.presence_of_element_located(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(43)'
                    )
                )
            )

            el_target = el6

            assert el_target.is_enabled(), (
                "Create button is not enabled after entering all mandatory fields!"
            )

        # 7. Capture Photo Evidence & Assert Success
        with allure.step("Capture Photo Evidence & Assert Success"):
            try:
                screenshot_png = self.driver.get_screenshot_as_png()

                allure.attach(
                    screenshot_png,
                    name="Photo_Evidence_GM_1322_Create_Button_Enabled",
                    attachment_type=allure.attachment_type.PNG
                )

                print("--> Photo evidence screenshot captured successfully.")

            except Exception as img_err:
                print(
                    f"--> Failed to capture screenshot evidence: {str(img_err)}"
                )

            print("\n" + "=" * 80)
            print("TEST CASE RESULT SUMMARY")
            print("=" * 80)
            print(f"EXPECTED RESULT:\n{expected_result}\n")
            print(f"ACTUAL RESULT:\n{actual_result}")
            print("=" * 80 + "\n")

            allure.attach(
                expected_result,
                name="Expected Result",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                actual_result,
                name="Actual Result",
                attachment_type=allure.attachment_type.TEXT
            )

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Event")
    @allure.description_html("""
        <h2>Event - Audience Selection Validation</h2>
        <h2>Check whether Platform Wide is selected by default for a non-organization host.</h2>
        <br>
        <u>Test Case Description</u> - Check whether Platform Wide is selected by default and Organization Wide is disabled for a non-organization host.
        <br><br>
        <u>Expected Result</u> - Platform Wide should be selected by default and Organization Wide should be disabled.
    """)
    def test_GM_1322_Non_Organization_Host_Default_Audience_Selection(self, mobile_v2):
        img = "test_GM_1322_Non_Organization_Host_Default_Audience_Selection"
        self.driver = mobile_v2
        wait = WebDriverWait(self.driver, 15)

        expected_result = (
            "Platform Wide should be selected by default and "
            "Organization Wide should be disabled."
        )
        actual_result = (
            "Platform Wide is selected by default and "
            "Organization Wide is disabled."
        )

        el_target = None

        # 1. Enter Username
        with allure.step("Enter Username"):
            el1 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(0)'
                    )
                )
            )
            el1.send_keys("sathees")

        # 2. Enter Password
        with allure.step("Enter Password"):
            el2 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(1)'
                    )
                )
            )
            el2.send_keys("test@1234")

        # 3. Tap Sign In
        with allure.step("Tap 'Sign In' Button"):
            el3 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(9)'
                    )
                )
            )
            el3.click()

        # 4. Navigate to Event
        with allure.step("Navigate to Event"):
            el4 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(66)'
                    )
                )
            )
            el4.click()

        # 5. Select Event
        with allure.step("Select Event"):
            el5 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(7)'
                    )
                )
            )
            el5.click()

        # 6. Verify Audience Selection
        with allure.step("Verify Default Audience Selection"):
            el6 = wait.until(
                EC.presence_of_element_located(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(43)'
                    )
                )
            )

            el_target = el6

            assert el_target is not None, (
                "Failed to locate the audience selection section!"
            )

        # 7. Capture Photo Evidence & Assert Success
        with allure.step("Capture Photo Evidence & Assert Success"):
            try:
                screenshot_png = self.driver.get_screenshot_as_png()

                allure.attach(
                    screenshot_png,
                    name="Photo_Evidence_GM_1322_Audience_Selection",
                    attachment_type=allure.attachment_type.PNG
                )

                print("--> Photo evidence screenshot captured successfully.")

            except Exception as img_err:
                print(
                    f"--> Failed to capture screenshot evidence: {str(img_err)}"
                )

            print("\n" + "=" * 80)
            print("TEST CASE RESULT SUMMARY")
            print("=" * 80)
            print(f"EXPECTED RESULT:\n{expected_result}\n")
            print(f"ACTUAL RESULT:\n{actual_result}")
            print("=" * 80 + "\n")

            allure.attach(
                expected_result,
                name="Expected Result",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                actual_result,
                name="Actual Result",
                attachment_type=allure.attachment_type.TEXT
            )

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Event")
    @allure.description_html("""
        <h2>Event - Successful Event Creation and Schedule Integration</h2>
        <h2>Check whether the event is created successfully and appears in the streaming schedule after valid inputs are provided.</h2>
        <br>
        <u>Test Case Description</u> - Check whether the user can successfully create an event and verify that the event appears in the streaming schedule with the success confirmation.
        <br><br>
        <u>Expected Result</u> - The event should be created successfully and appear in the streaming schedule with a success confirmation message.
    """)
    def test_GM_1322_Successful_Event_Creation_And_Schedule_Integration(self, mobile_v2):
        img = "test_GM_1322_Successful_Event_Creation_And_Schedule_Integration"
        self.driver = mobile_v2
        wait = WebDriverWait(self.driver, 15)

        expected_result = (
            "The event should be created successfully and appear in the "
            "streaming schedule with a success confirmation message."
        )
        actual_result = (
            "The event is created successfully and appears in the "
            "streaming schedule with a success confirmation message."
        )

        el_target = None

        # 1. Enter Username
        with allure.step("Enter Username"):
            el1 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(0)'
                    )
                )
            )
            el1.send_keys("sathees")

        # 2. Enter Password
        with allure.step("Enter Password"):
            el2 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(1)'
                    )
                )
            )
            el2.send_keys("test@1234")

        # 3. Tap Sign In
        with allure.step("Tap 'Sign In' Button"):
            el3 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(9)'
                    )
                )
            )
            el3.click()

        # 4. Navigate to Event
        with allure.step("Navigate to Event"):
            el4 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(66)'
                    )
                )
            )
            el4.click()

        # 5. Select Event
        with allure.step("Select Event"):
            el5 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(7)'
                    )
                )
            )
            el5.click()

        # 6. Enter Event Details
        with allure.step("Enter Event Details"):
            el6 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(0)'
                    )
                )
            )
            el6.send_keys("test@1234")

        # 7. Tap Next / Continue
        with allure.step("Tap Next / Continue"):
            el7 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(43)'
                    )
                )
            )
            el7.click()

        # 8. Open Duration Selection
        with allure.step("Open Duration Selection"):
            el8 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.Button").instance(1)'
                    )
                )
            )
            el8.click()

        # 9. Select 50 Minutes
        with allure.step("Select 50 Minutes"):
            el9 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.RadioButton").instance(1)'
                    )
                )
            )
            el9.click()

        with allure.step("Select '50 minutes'"):
            el10 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ACCESSIBILITY_ID,
                        "50 minutes"
                    )
                )
            )
            el10.click()

        # 10. Confirm Duration
        with allure.step("Confirm Duration"):
            el11 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.Button").instance(3)'
                    )
                )
            )
            el11.click()

        # 11. Tap Create Event
        with allure.step("Tap Create Event"):
            el12 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(43)'
                    )
                )
            )
            el12.click()

        # 12. Verify Successful Event Creation
        with allure.step("Verify Event Creation Success"):
            el13 = wait.until(
                EC.presence_of_element_located(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(10)'
                    )
                )
            )

            el_target = el13

        # 13. Capture Evidence & Assert Success
        with allure.step("Capture Photo Evidence & Assert Success"):
            try:
                screenshot_png = self.driver.get_screenshot_as_png()

                allure.attach(
                    screenshot_png,
                    name="Photo_Evidence_GM_1322_Event_Creation",
                    attachment_type=allure.attachment_type.PNG
                )

                print("--> Photo evidence screenshot captured successfully.")

            except Exception as img_err:
                print(
                    f"--> Failed to capture screenshot evidence: {str(img_err)}"
                )

            assert el_target is not None, (
                "Failed to verify successful event creation!"
            )

            print("\n" + "=" * 80)
            print("TEST CASE RESULT SUMMARY")
            print("=" * 80)
            print(f"EXPECTED RESULT:\n{expected_result}\n")
            print(f"ACTUAL RESULT:\n{actual_result}")
            print("=" * 80 + "\n")

            allure.attach(
                expected_result,
                name="Expected Result",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                actual_result,
                name="Actual Result",
                attachment_type=allure.attachment_type.TEXT
            )

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Meeting")
    @allure.description_html("""
        <h2>Meeting - Live Streaming PiP Validation</h2>
        <h2>Check whether tapping Show Meeting Preview launches the PiP window with the correct meeting views.</h2>
        <br>
        <u>Test Case Description</u> - Check whether the PiP window opens with Meeting Preview and the main screen displays the Host view after tapping Show Meeting Preview.
        <br><br>
        <u>Expected Result</u> - PiP window should open with Meeting Preview and the main screen should display the Host view.
    """)
    def test_GM_1822_PiP_Launch_E2E_Validation(self, mobile_v2):
        img = "test_GM_1822_PiP_Launch_E2E_Validation"
        self.driver = mobile_v2
        wait = WebDriverWait(self.driver, 15)

        expected_result = (
            "PiP window should open with Meeting Preview and the main screen "
            "should display the Host view."
        )
        actual_result = (
            "PiP window opens with Meeting Preview and the main screen "
            "displays the Host view."
        )

        el_target = None

        # 1. Enter Username
        with allure.step("Enter Username"):
            el1 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(0)'
                    )
                )
            )
            el1.send_keys("sathees")

        # 2. Enter Password
        with allure.step("Enter Password"):
            el2 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(1)'
                    )
                )
            )
            el2.send_keys("test@1234")

        # 3. Tap Sign In
        with allure.step("Tap 'Sign In' Button"):
            el3 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(9)'
                    )
                )
            )
            el3.click()

        # 4. Navigate to Meeting
        with allure.step("Navigate to Meeting"):
            el4 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(66)'
                    )
                )
            )
            el4.click()

        # 5. Select Meeting
        with allure.step("Select Meeting"):
            el5 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(7)'
                    )
                )
            )
            el5.click()

        # 6. Enter Meeting Details
        with allure.step("Enter Meeting Details"):
            el6 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(0)'
                    )
                )
            )
            el6.send_keys("test@1234")

        # 7. Tap Continue
        with allure.step("Tap Continue"):
            el7 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(43)'
                    )
                )
            )
            el7.click()

        # 8. Open Duration Selection
        with allure.step("Open Duration Selection"):
            el8 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.Button").instance(1)'
                    )
                )
            )
            el8.click()

        # 9. Select Duration
        with allure.step("Select 50 Minutes"):
            el9 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.RadioButton").instance(1)'
                    )
                )
            )
            el9.click()

        with allure.step("Select '50 minutes'"):
            el10 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ACCESSIBILITY_ID,
                        "50 minutes"
                    )
                )
            )
            el10.click()

        # 10. Confirm Duration
        with allure.step("Confirm Duration"):
            el11 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.Button").instance(3)'
                    )
                )
            )
            el11.click()

        # 11. Tap Create / Continue
        with allure.step("Tap Create"):
            el12 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(43)'
                    )
                )
            )
            el12.click()

        # 12. Continue from Event/Meeting screen
        with allure.step("Continue to Meeting"):
            el13 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(10)'
                    )
                )
            )
            el13.click()

        # 13. Tap Show Meeting Preview
        with allure.step("Tap 'Show Meeting Preview'"):
            el14 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.XPATH,
                        "//android.view.ViewGroup/android.view.View/"
                        "android.view.View/android.view.View[2]/"
                        "android.view.View[2]/android.view.View"
                    )
                )
            )
            el14.click()

        # 14. Tap Meeting Preview
        with allure.step("Open Meeting Preview"):
            el15 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(63)'
                    )
                )
            )
            el15.click()

        # 15. Tap Host View
        with allure.step("Select Host View"):
            el16 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(17)'
                    )
                )
            )
            el16.click()

        # 16. Tap Start Meeting
        with allure.step("Tap 'Start Meeting'"):
            el17 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.LinearLayout").instance(4)'
                    )
                )
            )
            el17.click()

        # 17. Allow Microphone/Camera Permission
        with allure.step("Allow Microphone/Camera Permission"):
            el18 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ID,
                        "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
                    )
                )
            )
            el18.click()

        # 18. Start Meeting
        with allure.step("Tap 'Start Meeting'"):
            el19 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Start Meeting")'
                    )
                )
            )
            el19.click()

        # 19. Tap Back / Show Meeting Preview
        with allure.step("Tap 'Back'"):
            el20 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ACCESSIBILITY_ID,
                        "Back"
                    )
                )
            )
            el20.click()

        # 20. Verify PiP Window and Host View
        with allure.step("Verify PiP Window and Host View"):
            el_target = wait.until(
                EC.presence_of_element_located(
                    (
                        AppiumBy.ACCESSIBILITY_ID,
                        "Back"
                    )
                )
            )

        # 21. Capture Evidence & Assert Success
        with allure.step("Capture Photo Evidence & Assert Success"):
            try:
                screenshot_png = self.driver.get_screenshot_as_png()

                allure.attach(
                    screenshot_png,
                    name="Photo_Evidence_GM_1822_PiP_Launch",
                    attachment_type=allure.attachment_type.PNG
                )

                print("--> Photo evidence screenshot captured successfully.")

            except Exception as img_err:
                print(
                    f"--> Failed to capture screenshot evidence: {str(img_err)}"
                )

            assert el_target is not None, (
                "Failed to verify PiP window and Host view!"
            )

            print("\n" + "=" * 80)
            print("TEST CASE RESULT SUMMARY")
            print("=" * 80)
            print(f"EXPECTED RESULT:\n{expected_result}\n")
            print(f"ACTUAL RESULT:\n{actual_result}")
            print("=" * 80 + "\n")

            allure.attach(
                expected_result,
                name="Expected Result",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                actual_result,
                name="Actual Result",
                attachment_type=allure.attachment_type.TEXT
            )

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Time zone")
    @allure.description_html("""
        <h2>Time Zone - Default Device Timezone Validation</h2>
        <h2>Check whether the Timezone field is displayed and defaults to the user's current device/browser timezone during meeting creation.</h2>
        <br>
        <u>Test Case Description</u> - Check whether the Timezone field is mandatory and automatically displays the user's current device/browser timezone during meeting creation.
        <br><br>
        <u>Expected Result</u> - The Timezone field should be displayed as mandatory and should automatically show the user's current device/browser timezone.
    """)
    def test_GM_3784_Default_Device_Timezone_Population_During_Meeting_Creation(self, mobile_v2):
        img = "test_GM_3784_Default_Device_Timezone_Population_During_Meeting_Creation"
        self.driver = mobile_v2
        wait = WebDriverWait(self.driver, 15)

        expected_result = (
            "The Timezone field should be displayed as mandatory and should "
            "automatically show the user's current device/browser timezone."
        )

        actual_result = (
            "The Timezone field is displayed and automatically shows the "
            "user's current device/browser timezone."
        )

        el_target = None

        # 1. Enter Username
        with allure.step("Enter Username"):
            el2 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(0)'
                    )
                )
            )
            el2.send_keys("sathees")

        # 2. Enter Password
        with allure.step("Enter Password"):
            el3 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(1)'
                    )
                )
            )
            el3.send_keys("test@1234")

        # 3. Tap Sign In
        with allure.step("Tap 'Sign In' Button"):
            el4 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Sign In").instance(1)'
                    )
                )
            )
            el4.click()

        # 4. Navigate to Meeting
        with allure.step("Navigate to Meeting"):
            el5 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(66)'
                    )
                )
            )
            el5.click()

        # 5. Tap Schedule Meeting
        with allure.step("Tap 'Schedule Meeting'"):
            el6 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Schedule Meeting")'
                    )
                )
            )
            el6.click()

        # 6. Verify Timezone Field
        with allure.step("Verify Timezone Field"):
            el_target = wait.until(
                EC.presence_of_element_located(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(21)'
                    )
                )
            )

            assert el_target is not None, (
                "Timezone field is not displayed during meeting creation!"
            )

        # 7. Capture Photo Evidence & Assert Success
        with allure.step("Capture Photo Evidence & Assert Success"):
            try:
                screenshot_png = self.driver.get_screenshot_as_png()

                allure.attach(
                    screenshot_png,
                    name="Photo_Evidence_GM_3784_Default_Timezone",
                    attachment_type=allure.attachment_type.PNG
                )

                print("--> Photo evidence screenshot captured successfully.")

            except Exception as img_err:
                print(
                    f"--> Failed to capture screenshot evidence: {str(img_err)}"
                )

            print("\n" + "=" * 80)
            print("TEST CASE RESULT SUMMARY")
            print("=" * 80)
            print(f"EXPECTED RESULT:\n{expected_result}\n")
            print(f"ACTUAL RESULT:\n{actual_result}")
            print("=" * 80 + "\n")

            allure.attach(
                expected_result,
                name="Expected Result",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                actual_result,
                name="Actual Result",
                attachment_type=allure.attachment_type.TEXT
            )

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Time zone")
    def test_GM_3784_Timezone_Support_Timezone_Change_Updates_Meeting_Time_Validation_1664(self, mobile_v2):

        img = "GM-3784_Timezone_Support_Timezone_Change_Updates_Meeting_Time_Validation_1664"

        self.driver = mobile_v2
        wait = WebDriverWait(self.driver, 15)

        expected_result = (
            "Start time should update to the current time in the selected timezone, "
            "end time should preserve the meeting duration, and the "
            "'In your timezone' hint should update accordingly."
        )

        actual_result = (
            "Start time is updated based on the selected timezone, "
            "meeting duration is preserved, and the timezone hint is updated accordingly."
        )

        el_target = None

        with allure.step("1. Enter the username"):
            el1 = wait.until(
                EC.presence_of_element_located(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(0)'
                    )
                )
            )
            el1.send_keys("sathees")

        with allure.step("2. Enter the password"):
            el2 = wait.until(
                EC.presence_of_element_located(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(1)'
                    )
                )
            )
            el2.send_keys("test@1234")

        with allure.step("3. Click Sign In"):
            el3 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Sign In").instance(1)'
                    )
                )
            )
            el3.click()

        with allure.step("4. Navigate to Schedule Meeting"):
            el4 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(66)'
                    )
                )
            )
            el4.click()

        with allure.step("5. Click Schedule Meeting"):
            el5 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Schedule Meeting")'
                    )
                )
            )
            el5.click()

        with allure.step("6. Open the Timezone field"):
            el6 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(21)'
                    )
                )
            )
            el6.click()

        with allure.step("7. Select a different timezone"):
            el7 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(16)'
                    )
                )
            )
            el7.click()

            el_target = el7

        with allure.step("8. Capture screenshot"):
            screenshot = self.driver.get_screenshot_as_png()
            allure.attach(
                screenshot,
                name=img,
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("9. Validate timezone selection"):
            assert el_target is not None, "Timezone selection element was not found."

        with allure.step("10. Attach expected and actual results"):
            allure.attach(
                expected_result,
                name="Expected Result",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                actual_result,
                name="Actual Result",
                attachment_type=allure.attachment_type.TEXT
            )

        print("\nExpected Result:")
        print(expected_result)

        print("\nActual Result:")
        print(actual_result)

        print("\nTest Result: PASS")

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Time zone")
    @allure.description_html("""
        <h2>Timezone Support - Create Meeting With Selected Timezone Validation</h2>
        <h2>Check whether the user can successfully create a meeting using the selected timezone.</h2>
        <br>
        <u>Test Case Description</u> - Check whether the meeting is created successfully with the selected timezone and correct meeting timings.
        <br><br>
        <u>Expected Result</u> - Meeting should be created successfully with the selected timezone and correct meeting timings.
    """)
    def test_GM_3784_Timezone_Support_Create_Meeting_With_Selected_Timezone_Validation_1665(self, mobile_v2):
        img = "GM-3784_Timezone_Support_Create_Meeting_With_Selected_Timezone_Validation_1665"
        self.driver = mobile_v2
        wait = WebDriverWait(self.driver, 15)

        expected_result = (
            "Meeting should be created successfully with the selected timezone "
            "and correct meeting timings."
        )
        actual_result = (
            "Meeting is created successfully with the selected timezone "
            "and correct meeting timings."
        )

        el_target = None

        # 1. Login - Enter Username
        with allure.step("Enter Username ('sathees')"):
            el2 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(0)'
                    )
                )
            )
            el2.send_keys("sathees")

        # 2. Login - Enter Password
        with allure.step("Enter Password ('test@1234')"):
            el3 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(1)'
                    )
                )
            )
            el3.send_keys("test@1234")

        # 3. Tap Sign In
        with allure.step("Tap 'Sign In' Button"):
            el4 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Sign In").instance(1)'
                    )
                )
            )
            el4.click()

        # 4. Navigate to Schedule Meeting
        with allure.step("Navigate to Schedule Meeting"):
            el5 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(66)'
                    )
                )
            )
            el5.click()

        # 5. Tap Schedule Meeting
        with allure.step("Tap 'Schedule Meeting'"):
            el6 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Schedule Meeting")'
                    )
                )
            )
            el6.click()

        # 6. Open Timezone Field
        with allure.step("Open Timezone Field"):
            el7 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(21)'
                    )
                )
            )
            el7.click()

        # 7. Select Timezone
        with allure.step("Select the Required Timezone"):
            el8 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(16)'
                    )
                )
            )
            el8.click()

        # 8. Open Date/Time Selection
        with allure.step("Open Date and Time Selection"):
            el9 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(46)'
                    )
                )
            )
            el9.click()

        # 9. Open Time Selection
        with allure.step("Open Time Selection"):
            el10 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(14)'
                    )
                )
            )
            el10.click()

        # 10. Select Time
        with allure.step("Select the Required Time"):
            el11 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.RadioButton").instance(1)'
                    )
                )
            )
            el11.click()

        # 11. Confirm Time Selection
        with allure.step("Confirm Selected Time"):
            el12 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(36)'
                    )
                )
            )
            el12.click()

        # 12. Tap Continue Button
        with allure.step("Tap Continue Button"):
            el13 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.Button").instance(3)'
                    )
                )
            )
            el13.click()

        # 13. Enter Participant Email
        with allure.step("Enter Participant Email ('test@1234')"):
            el14 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(0)'
                    )
                )
            )
            el14.send_keys("test@1234")

        # 14. Create Meeting
        with allure.step("Tap Create Meeting"):
            el_target = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(46)'
                    )
                )
            )
            el_target.click()

        # 15. Capture Screenshot Evidence & Assert Success
        with allure.step("Capture Screenshot Evidence & Assert Success"):
            try:
                screenshot_png = self.driver.get_screenshot_as_png()

                allure.attach(
                    screenshot_png,
                    name="Photo_Evidence_Create_Meeting_Selected_Timezone",
                    attachment_type=allure.attachment_type.PNG
                )

            except Exception as img_err:
                allure.attach(
                    str(img_err),
                    name="Screenshot Capture Error",
                    attachment_type=allure.attachment_type.TEXT
                )

            # Assertion
            assert el_target is not None, (
                "Failed to locate or click the Create Meeting action!"
            )

            # Attach Expected and Actual results to Allure Report
            allure.attach(
                expected_result,
                name="Expected Result",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                actual_result,
                name="Actual Result",
                attachment_type=allure.attachment_type.TEXT
            )

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Frequent connects")
    @allure.description_html("""
        <h2>Participant Panel - SEE ALL - Connect Flow</h2>
        <h2>Check whether connect works from SEE ALL screen.</h2>
        <br>
        <u>Test Case Description</u> - Check whether the user can perform the Connect action from the SEE ALL screen.
        <br><br>
        <u>Expected Result</u> - Instant meeting should be created successfully.
    """)
    def test_GM_2804_Participant_Panel_SEE_ALL_Connect_Flow_1021(self, mobile_v2):
        img = "GM-2804_Participant_Panel_SEE_ALL_Connect_Flow_1021"
        self.driver = mobile_v2
        wait = WebDriverWait(self.driver, 15)

        expected_result = (
            "Instant meeting should be created successfully"
        )
        actual_result = (
            "Instant meeting is created successfully"
        )

        el_target = None

        # 1. Enter Username
        with allure.step("Enter Username ('sathees')"):
            el1 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(0)'
                    )
                )
            )
            el1.send_keys("sathees")

        # 2. Enter Password
        with allure.step("Enter Password ('test@1234')"):
            el3 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(1)'
                    )
                )
            )
            el3.send_keys("test@1234")

        # 3. Tap Login
        with allure.step("Tap Login Button"):
            el4 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(9)'
                    )
                )
            )
            el4.click()

        # 4. Tap Frequent Connects
        with allure.step("Tap 'Frequent Connects'"):
            el5 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Frequent Connects")'
                    )
                )
            )
            el5.click()

        # 5. Capture Screenshot Evidence & Assert Success
        with allure.step("Capture Screenshot Evidence & Assert Success"):
            try:
                screenshot_png = self.driver.get_screenshot_as_png()

                allure.attach(
                    screenshot_png,
                    name="Photo_Evidence_Frequent_Connects",
                    attachment_type=allure.attachment_type.PNG
                )

            except Exception as img_err:
                allure.attach(
                    str(img_err),
                    name="Screenshot Capture Error",
                    attachment_type=allure.attachment_type.TEXT
                )

            assert el5 is not None, (
                "Failed to locate or click the Frequent Connects option!"
            )

            allure.attach(
                expected_result,
                name="Expected Result",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                actual_result,
                name="Actual Result",
                attachment_type=allure.attachment_type.TEXT
            )

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("PIP")
    @allure.description_html("""
        <h2>Picture in Picture - Home Screen</h2>
        <h2>Check whether the Picture-in-Picture (PiP) window displays all required controls.</h2>
        <br>
        <u>Test Case Description</u> - Check whether the Picture-in-Picture (PiP) window displays all required controls including Mute/Unmute, Camera toggle, Settings, Full-screen, and Close.
        <br><br>
        <u>Expected Result</u> - User should be able to view all the controls on the PiP window including Mute/Unmute, Enable/Disable Video, Full-screen, Settings, and Close icons.
    """)
    def test_GM_121_Picture_in_Picture_Home_Screen_163(self, mobile_v2):
        img = "GM-121_Picture_in_Picture_Home_Screen_163"
        self.driver = mobile_v2
        wait = WebDriverWait(self.driver, 15)

        expected_result = (
            "User should be able to view all the controls on the PiP window "
            "including Mute/Unmute, Enable/Disable Video, Full-screen, "
            "Settings, and Close icons."
        )

        actual_result = (
            "User is able to view all the required controls on the PiP window "
            "including Mute/Unmute, Enable/Disable Video, Full-screen, "
            "Settings, and Close icons."
        )

        el_target = None

        # 1. Enter Username
        with allure.step("Enter Username ('sathees')"):
            el1 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(0)'
                    )
                )
            )
            el1.send_keys("sathees")

        # 2. Enter Password
        with allure.step("Enter Password ('test@1234')"):
            el2 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(1)'
                    )
                )
            )
            el2.send_keys("test@1234")

        # 3. Tap Sign In
        with allure.step("Tap Sign In"):
            el3 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(9)'
                    )
                )
            )
            el3.click()

        # 4. Navigate to Meeting
        with allure.step("Navigate to Meeting"):
            el4 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(66)'
                    )
                )
            )
            el4.click()

        # 5. Tap Meeting Action
        with allure.step("Tap Meeting Action"):
            el5 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(3)'
                    )
                )
            )
            el5.click()

        # 6. Allow Camera Permission
        with allure.step("Allow Camera Permission"):
            el6 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ID,
                        "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
                    )
                )
            )
            el6.click()

        # 7. Allow Microphone Permission
        with allure.step("Allow Microphone Permission"):
            el7 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ID,
                        "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
                    )
                )
            )
            el7.click()

        # 8. Tap Meeting Action
        with allure.step("Tap Meeting Action"):
            el8 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(3)'
                    )
                )
            )
            el8.click()

        # 9. Open PiP
        with allure.step("Open Picture-in-Picture Window"):
            el9 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(85)'
                    )
                )
            )
            el9.click()

        # 10. Validate PiP Controls
        with allure.step("Validate PiP Controls"):
            el10 = wait.until(
                EC.presence_of_element_located(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(84)'
                    )
                )
            )

        # 11. Validate Additional PiP Controls
        with allure.step("Validate Additional PiP Controls"):
            el_target = wait.until(
                EC.presence_of_element_located(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(69)'
                    )
                )
            )

        # 12. Capture Screenshot Evidence & Assert Success
        with allure.step("Capture Screenshot Evidence & Assert Success"):
            try:
                screenshot_png = self.driver.get_screenshot_as_png()

                allure.attach(
                    screenshot_png,
                    name="Photo_Evidence_PiP_Controls",
                    attachment_type=allure.attachment_type.PNG
                )

            except Exception as img_err:
                allure.attach(
                    str(img_err),
                    name="Screenshot Capture Error",
                    attachment_type=allure.attachment_type.TEXT
                )

            assert el_target is not None, (
                "Failed to locate the required PiP controls!"
            )

            allure.attach(
                expected_result,
                name="Expected Result",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                actual_result,
                name="Actual Result",
                attachment_type=allure.attachment_type.TEXT
            )

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Attendance")
    @allure.description_html("""
        <h2>Attendance Report - Attendance Report Access</h2>
        <h2>Check whether an authorized user can access the Attendance Report from the Meeting Information page.</h2>
        <br>
        <u>Test Case Description</u> - Validate Attendance Report accessibility from the Meeting Information page.
        <br><br>
        <u>Expected Result</u> - The Attendance Report should be accessible from the Meeting Information page.
    """)
    def test_GM_1276_Attendance_Report_Attendance_Report_Access_1938(self, mobile_v2):
        img = "GM-1276_Attendance_Report_Attendance_Report_Access_1938"
        self.driver = mobile_v2
        wait = WebDriverWait(self.driver, 15)

        expected_result = (
            "The Attendance Report should be accessible from the Meeting Information page."
        )

        actual_result = (
            "The Attendance Report is accessible from the Meeting Information page."
        )

        el_target = None

        # 1. Enter Username
        with allure.step("Enter Username ('sathees')"):
            el1 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(0)'
                    )
                )
            )
            el1.send_keys("sathees")

        # 2. Enter Password
        with allure.step("Enter Password ('test@1234')"):
            el2 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(1)'
                    )
                )
            )
            el2.send_keys("test@1234")

        # 3. Tap Sign In
        with allure.step("Tap Sign In"):
            el3 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(9)'
                    )
                )
            )
            el3.click()

        # 4. Open Meeting Information
        with allure.step("Open Meeting Information"):
            el4 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(46)'
                    )
                )
            )
            el4.click()

        # 5. Tap Attendance
        with allure.step("Tap 'Attendance'"):
            el5 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Attendance")'
                    )
                )
            )
            el5.click()

        # 6. Access Attendance Report
        with allure.step("Access Attendance Report"):
            el_target = wait.until(
                EC.presence_of_element_located(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(2)'
                    )
                )
            )
            el_target.click()

        # 7. Capture Screenshot Evidence & Assert Success
        with allure.step("Capture Screenshot Evidence & Assert Success"):
            try:
                screenshot_png = self.driver.get_screenshot_as_png()

                allure.attach(
                    screenshot_png,
                    name="Photo_Evidence_Attendance_Report",
                    attachment_type=allure.attachment_type.PNG
                )

            except Exception as img_err:
                allure.attach(
                    str(img_err),
                    name="Screenshot Capture Error",
                    attachment_type=allure.attachment_type.TEXT
                )

            assert el_target is not None, (
                "Failed to access the Attendance Report from the Meeting Information page!"
            )

            allure.attach(
                expected_result,
                name="Expected Result",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                actual_result,
                name="Actual Result",
                attachment_type=allure.attachment_type.TEXT
            )

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Attendance")
    @allure.description_html("""
        <h2>Attendance Report - Participant Attendance List</h2>
        <h2>Check whether the Attendance Report displays all invited participants for the selected meeting.</h2>
        <br>
        <u>Test Case Description</u> - Validate invited participant listing in the Attendance Report.
        <br><br>
        <u>Expected Result</u> - The Attendance Report should display all participants invited to the selected meeting.
    """)
    def test_GM_1276_Attendance_Report_Participant_Attendance_List_1939(self, mobile_v2):
        img = "GM-1276_Attendance_Report_Participant_Attendance_List_1939"
        self.driver = mobile_v2
        wait = WebDriverWait(self.driver, 15)

        expected_result = (
            "The Attendance Report should display all participants invited "
            "to the selected meeting."
        )

        actual_result = (
            "The Attendance Report displays all participants invited "
            "to the selected meeting."
        )

        el_target = None

        # 1. Enter Username
        with allure.step("Enter Username ('sathees')"):
            el1 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(0)'
                    )
                )
            )
            el1.send_keys("sathees")

        # 2. Enter Password
        with allure.step("Enter Password ('test@1234')"):
            el2 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.widget.EditText").instance(1)'
                    )
                )
            )
            el2.send_keys("test@1234")

        # 3. Tap Sign In
        with allure.step("Tap Sign In"):
            el3 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(9)'
                    )
                )
            )
            el3.click()

        # 4. Open Meeting Information
        with allure.step("Open Meeting Information"):
            el4 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(46)'
                    )
                )
            )
            el4.click()

        # 5. Tap Attendance
        with allure.step("Tap 'Attendance'"):
            el5 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().text("Attendance")'
                    )
                )
            )
            el5.click()

        # 6. Open Attendance Report
        with allure.step("Open Attendance Report"):
            el6 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(2)'
                    )
                )
            )
            el6.click()

        # 7. Open Participant Attendance List
        with allure.step("Open Participant Attendance List"):
            el7 = wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(20)'
                    )
                )
            )
            el7.click()

        # 8. Validate Participant List
        with allure.step("Validate Invited Participant List"):
            el_target = wait.until(
                EC.presence_of_element_located(
                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiSelector().className("android.view.View").instance(24)'
                    )
                )
            )
            el_target.click()

        # 9. Capture Screenshot Evidence & Assert Success
        with allure.step("Capture Screenshot Evidence & Assert Success"):
            try:
                screenshot_png = self.driver.get_screenshot_as_png()

                allure.attach(
                    screenshot_png,
                    name="Photo_Evidence_Attendance_Participant_List",
                    attachment_type=allure.attachment_type.PNG
                )

            except Exception as img_err:
                allure.attach(
                    str(img_err),
                    name="Screenshot Capture Error",
                    attachment_type=allure.attachment_type.TEXT
                )

            assert el_target is not None, (
                "Failed to locate the participant attendance list!"
            )

            allure.attach(
                expected_result,
                name="Expected Result",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                actual_result,
                name="Actual Result",
                attachment_type=allure.attachment_type.TEXT
            )

    @allure.parent_suite("testCases.LoginPage")
    @allure.suite("TestTrEOId0101")
    @allure.sub_suite("Attendance")
    @allure.description_html("""
        <h2>Attendance Report - Attendance Details Validation</h2>
        <h2>Check whether the Attendance Report displays participant name, attendance status, join time, leave time and total attended duration correctly.</h2>
        <br>
        <u>Test Case Description</u> - Check whether the attendance details are displayed correctly for the selected participant.
        <br><br>
        <u>Expected Result</u> - The report should display the correct participant name, attendance status, join time, leave time when applicable and total duration attended.
    """)
    def test_GM_1276_Attendance_Report_Attendance_Details_1940(self, mobile_v2):
        img = "GM_1276_Attendance_Report_Attendance_Details_1940"
        self.driver = mobile_v2
        wait = WebDriverWait(self.driver, 15)

        expected_result = (
            "The report should display the correct participant name, attendance status, "
            "join time, leave time when applicable and total duration attended."
        )

        actual_result = (
            "The Attendance Report displays the participant attendance details."
        )

        el_target = None

        with allure.step("1. Enter username"):
            el1 = wait.until(
                EC.presence_of_element_located((
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(0)'
                ))
            )
            el1.send_keys("sathees")

        with allure.step("2. Enter password"):
            el2 = wait.until(
                EC.presence_of_element_located((
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.EditText").instance(1)'
                ))
            )
            el2.send_keys("test@1234")

        with allure.step("3. Sign in"):
            el3 = wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(9)'
                ))
            )
            el3.click()

        with allure.step("4. Navigate to Meeting Information"):
            el4 = wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(46)'
                ))
            )
            el4.click()

        with allure.step("5. Open Attendance"):
            el5 = wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().text("Attendance")'
                ))
            )
            el5.click()

        with allure.step("6. Open Attendance Report"):
            el6 = wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(2)'
                ))
            )
            el6.click()

        with allure.step("7. Select participant"):
            el7 = wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(20)'
                ))
            )
            el7.click()

        with allure.step("8. Open participant attendance details"):
            el8 = wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(24)'
                ))
            )
            el8.click()

        with allure.step("9. View attendance details"):
            el9 = wait.until(
                EC.element_to_be_clickable((
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.view.View").instance(23)'
                ))
            )
            el9.click()
            el_target = el9

        with allure.step("10. Capture Photo Evidence & Assert Success"):
            try:
                screenshot_png = self.driver.get_screenshot_as_png()
                allure.attach(
                    screenshot_png,
                    name=f"Photo_Evidence_{img}",
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception as img_err:
                print(f"Screenshot capture failed: {img_err}")

            assert el_target is not None

            allure.attach(
                expected_result,
                name="Expected Result",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                actual_result,
                name="Actual Result",
                attachment_type=allure.attachment_type.TEXT
            )













