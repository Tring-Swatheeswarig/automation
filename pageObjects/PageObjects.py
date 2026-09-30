import subprocess
import time
import string
import allure
from allure_commons.types import AttachmentType
# from appium.webdriver.common import touch_action
# import selenium
# from appium.webdriver.common.touch_action import TouchAction
from bs4 import element
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
# from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageObjects:
    title_logo_xpath = "//android.widget.ImageView[@resource-id='com.tringapps.jwp_poc.android.mobile:id/logo']"
    signup_button_xpath = "//android.widget.TextView[@text='SIGN UP']"
    create_acc_btn_xpath = "//android.widget.Button[@text='CREATE ACCOUNT']"
    enter_fullname_input_xpath = "//android.widget.EditText[@resource-id='com.tringapps.jwp_poc.android.mobile:id/fullNameSignUp']"
    enter_email_input_xpath = "//android.widget.EditText[@resource-id='com.tringapps.jwp_poc.android.mobile:id/emailSignUp']"
    enter_number_input_xpath = "//android.widget.EditText[@resource-id='com.tringapps.jwp_poc.android.mobile:id/phoneNumberSignUp']"
    enter_password_input_xpath = "//android.widget.EditText[@resource-id='com.tringapps.jwp_poc.android.mobile:id/passwordSignUp']"
    enter_cnf_pwd_input_xpath = "//android.widget.EditText[@resource-id='com.tringapps.jwp_poc.android.mobile:id/confirmPasswordSignUp']"
    next_btn_xpath = "//android.widget.Button[@text='NEXT']"
    get_started_btn_xpath = "//android.widget.Button[@text='GET STARTED']"
    pwd_eyeicon_disabled_xpath = "//android.widget.ImageView[@resource-id='com.tringapps.jwp_poc.android.mobile:id/eyeSignUp']"
    cnf_pwd_eyeicon_disabled_xpath = "//android.widget.ImageView[@resource-id='com.tringapps.jwp_poc.android.mobile:id/eyeSignUpConfirmPassword']"
    profile_desc_xpath = "//android.widget.TextView[@resource-id='com.tringapps.jwp_poc.android.mobile:id/readyToExperienceText']"
    country_code_xpath = "//android.widget.TextView[@resource-id='com.tringapps.jwp_poc.android.mobile:id/textView_selectedCountry']"
    country_flag_xpath = "//android.widget.ImageView[@resource-id='com.tringapps.jwp_poc.android.mobile:id/image_flag']"
    signinwith_email_xpath = "//android.widget.TextView[@text='SIGN IN WITH EMAIL']"
    signin_page_xpath = "//android.widget.TextView[@resource-id='com.tringapps.jwp_poc.android.mobile:id/signInText']"
    number_field_signin_xpath = "//android.widget.EditText[@text='Enter Email or Mobile No.']"
    password_field_signin_xpath = "//android.widget.EditText[@text='Enter password']"
    forgot_password_xpath = "//android.widget.TextView[@text='Forgot Password?']"
    signin_button_xpath = "//android.widget.Button[@text='SIGN IN']"
    signup_link_signinpage_xpath = "//android.widget.TextView[@text='Sign Up']"
    error_message_signin_xpath = "//*[@text='Enter valid credentials']"

    # from praveen
    onboarding_next_xpath = "//android.widget.Button[@resource-id='com.tringapps.jwp_poc.android.mobile:id/nextbtn']"
    signup_xpath = "//android.widget.TextView[@resource-id='com.tringapps.jwp_poc.android.mobile:id/nav_to_signUp']"
    first_name_field_xpath = "//android.widget.EditText[@text='Enter Full Name']"
    email_field_xpath = "//android.widget.EditText[@text='Enter Email']"
    password_field_xpath = "//android.widget.EditText[@resource-id='com.tringapps.jwp_poc.android.mobile:id/password']"
    conform_password_field_xpath = "//android.widget.EditText[@resource-id='com.tringapps.jwp_poc.android.mobile:id/confirmPasswordSignUp']"
    terms_acknowledge_xpath = "//android.widget.CheckBox[@resource-id='com.tringapps.jwp_poc.android.mobile:id/termsCheckbox']"
    signup_page_description_xpath = "//android.widget.TextView[@resource-id='com.tringapps.jwp_poc.android.mobile:id/ready_to_experience_text']"
    signin_link_xpath = "//android.widget.TextView[@text='Sign In']"
    signup_page_heading_xpath = "//android.widget.TextView[@text='Sign Up']"
    google_signin_xpath = "//android.widget.TextView[@text='SIGN IN WITH GOOGLE']"
    create_account_button_xpath = "//android.widget.Button[@resource-id='com.tringapps.jwp_poc.android.mobile:id/sign_up_button']"
    first_name_error_xpath = "//android.widget.TextView[@resource-id='com.tringapps.jwp_poc.android.mobile:id/textinput_error']"
    email_error_xpath = "//android.widget.TextView[@text='[This account already exists.]']"
    email_signin_button_xpath = "//android.widget.TextView[@text='SIGN IN WITH EMAIL']"
    forgetpassword_link_xpath = "//android.widget.TextView[@resource-id='com.tringapps.jwp_poc.android.mobile:id/forgot_password']"
    signup_link_xpath = "//android.widget.TextView[@resource-id='com.tringapps.jwp_poc.android.mobile:id/sign_up_link']"
    guest_xpath = "//android.widget.TextView[@resource-id='com.tringapps.jwp_poc.android.mobile:id/continue_as_guest']"
    # signin_button_xpath = "//android.widget.Button[@resource-id='com.tringapps.jwp_poc.android.mobile:id/sign_in_button']"
    home_page_xpath = "//android.widget.TextView[@resource-id='com.tringapps.jwp_poc.android.mobile:id/navigation_bar_item_large_label_view']"
    signin_email_xpath = "//android.widget.EditText[@resource-id='com.tringapps.jwp_poc.android.mobile:id/usernameSignIn']"
    signin_password_xpath = "//android.widget.EditText[@resource-id='com.tringapps.jwp_poc.android.mobile:id/passwordSignIn']"
    search_icon_xpath = "//android.widget.ImageView[@resource-id='com.tringapps.jwp_poc.android.mobile:id/search']"
    search_field_xpath = "//android.widget.TextView[@resource-id='com.tringapps.jwp_poc.android.mobile:id/search_title_text_view']"
    search_no_result_xpath = "//android.widget.TextView[@text='No search result available']"
    navigation_menu_xpath = "//android.widget.FrameLayout[@resource-id='com.tringapps.jwp_poc.android.mobile:id/bottom_navigation']"
    search_close_icon_xpath = "//android.widget.ImageView[@resource-id='android:id/search_close_btn']"
    search_result_xpath = "(//android.widget.TextView[contains(@text,'a')])[1]"
    profile_icon_xpath = "//android.widget.FrameLayout[@content-desc='Profile']"
    profile_screen_xpath = "//android.widget.TextView[@text='Profile']"
    search_field_home_xpath = "//android.widget.AutoCompleteTextView[@resource-id='android:id/search_src_text']"
    edit_profile_header_xpath = "//android.widget.TextView[@text='Edit Profile']"
    edit_profile_image_xpath = "//android.widget.ImageView[@resource-id='com.tringapps.jwp_poc.android.mobile:id/imageView']"
    edit_fullname_xpath = "//android.widget.EditText[@resource-id='com.tringapps.jwp_poc.android.mobile:id/full_name']"
    update_profile_button_xpath = "//android.widget.Button[@text='UPDATE PROFILE']"
    edit_icon_xpath = "//android.widget.ImageView[@resource-id='com.tringapps.jwp_poc.android.mobile:id/editButton']"
    account_export_data_xpath = "//android.widget.TextView[@text='Please Check your Email']"
    export_acc_data_xpath = "//android.widget.TextView[@text='Export Account Data']"
    password_export_data_screen_xpath = "//android.widget.EditText[@text='Enter password']"
    export_acc_data_btn_xpath = "//android.widget.Button[@text='EXPORT ACCOUNT DATA']"
    short_film_heading_xpath = "(//android.widget.TextView[@text = 'Short Films'])[1]"
    profile_page_xpath = "//android.widget.TextView[@text='Profile']"
    movies_page_xpath = "(//android.widget.TextView[@text='Movies'])[2]"
    short_video_page_xpath = "//android.widget.TextView[@text='Short Videos']"
    short_film_page_xpath = "//android.widget.TextView[@text='Short Films']"
    profile_edit_icon_xpath = "//android.widget.ImageView[@resource-id='com.tringapps.jwp_poc.android.mobile:id/editButton']"
    profile_full_name_xpath = "//android.widget.EditText[@resource-id='com.tringapps.jwp_poc.android.mobile:id/full_name']"
    update_profile_xpath = "//android.widget.Button[@resource-id='com.tringapps.jwp_poc.android.mobile:id/saveButton']"
    profie_name_display_xpath = "//android.widget.TextView[@resource-id='com.tringapps.jwp_poc.android.mobile:id/full_name']"
    profile_page_back_icon_xpath = "//android.widget.ImageButton[@displayed='true']"
    movie_page_heading_xpath = "//android.widget.TextView[@resource-id='com.tringapps.jwp_poc.android.mobile:id/title_text_view']"
    short_video_page_heading_xpath = "//android.widget.TextView[@resource-id='com.tringapps.jwp_poc.android.mobile:id/title_text_view']"
    signout_button_xpath = "//android.widget.TextView[@text='Sign Out']"
    homemenu_icon_xpath = "(//android.widget.ImageView[@resource-id='com.tringapps.jwp_poc.android.mobile:id/navigation_bar_item_icon_view'])[1]"
    moviemenu_icon_xpath = "(//android.widget.ImageView[@resource-id='com.tringapps.jwp_poc.android.mobile:id/navigation_bar_item_icon_view'])[2]"
    short_videosmenu_icon_xpath = "(//android.widget.ImageView[@resource-id='com.tringapps.jwp_poc.android.mobile:id/navigation_bar_item_icon_view'])[3]"
    short_filmsmenu_icon_xpath = "(//android.widget.ImageView[@resource-id='com.tringapps.jwp_poc.android.mobile:id/navigation_bar_item_icon_view'])[4]"
    email_profile_screen_xpath = "//android.widget.TextView[@resource-id='com.tringapps.jwp_poc.android.mobile:id/Email']"
    number_profile_screen_xpath = "//android.widget.TextView[@resource-id='com.tringapps.jwp_poc.android.mobile:id/phoneTextView']"
    download_video_text_xpathh = "//android.widget.TextView[@text='Downloaded Video']"
    subscription_details_text_xpath = "//android.widget.TextView[@text='Subscription Details']"
    change_password_text_xpath = "//android.widget.TextView[@text='Change Password']"
    delete_account_text_xpath = "//android.widget.TextView[@text='Delete Account']"
    old_password_field_xpath = "//android.widget.EditText[@text='Enter old password']"
    new_password_field_xpath = "//android.widget.EditText[@text='Enter new password']"
    cnfm_password_field_xpath = "//android.widget.EditText[@text='Re-Enter New password']"
    update_password_button_xpath = "//android.widget.Button[@text='UPDATE PASSWORD']"
    pwd_update_success_xpath = "//*[@text='Password changed successfully']"
    delete_account_btn_xpath = "//android.widget.Button[@text='DELETE ACCOUNT']"
    account_deleted_toaster_xpath = "//*[@text='Account deleted successfully']"
    continue_option_xpath = "//android.widget.Button[@text='CONTINUE']"
    mobilenum_signup_xpath = "//android.widget.EditText[@text='xxx xxx xxxx']"
    createpassword_signup_xpath = "(//android.widget.EditText[@text='Enter password'])[1]"
    checkbox_signup_xpath = "//android.widget.CheckBox[@resource-id='com.tringapps.jwp_poc.android.mobile:id/termsCheckbox']"
    firstcard_home_xpath = "(//android.widget.ImageView[@resource-id='com.tringapps.jwp_poc.android.mobile:id/image_view'])[1]"
    favourite_added_xpath = "//*[@text='Successfully added as Favorite']"
    favorite_removed_xpath = "//*[@text='Removed from Favorite']"
    favorite_btn_xpath = "//android.widget.Button[@resource-id='com.tringapps.jwp_poc.android.mobile:id/favorite_button']"



    def __init__(self, mobile):
        self.driver = mobile
        self.wait = WebDriverWait(self.driver, 30)

    def send_key(self, xpath, text):
        try:
            element = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, xpath)))
            element.click()
            element.clear()
            element.send_keys(text)
            self.driver.back()
        except NoSuchElementException:
            return False
        return True

    def click(self, xpath):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, xpath))).click()
        except NoSuchElementException:
            return False
        return True

    def doubleClick(self, xpath):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, xpath))).click()
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))).click()
        except NoSuchElementException:
            return False
        return True

    def presence(self, xpath):
        try:
            WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.XPATH, xpath)))
        except NoSuchElementException:
            return False
        return True

    def invisible(self, xpath):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.invisibility_of_element((By.XPATH, xpath)))
        except NoSuchElementException:
            return False
        return True

    def text_to_be_present(self, xpath, text):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.text_to_be_present_in_element((By.XPATH, xpath), text))
        except NoSuchElementException:
            return False
        return True

    def search_element(self, text):
        try:
            xpath = f"//*[text()='{text}']"
            element = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, xpath)))
            element.is_displayed()
        except (NoSuchElementException, TimeoutException):
            screen_size = self.driver.get_window_rect()
            a = screen_size['width'] / 2
            b = screen_size['height'] * .8
            c = screen_size['width'] / 2
            d = screen_size['height'] * .2
            command = f'adb shell input swipe {a} {b} {c} {d} {500}'
            subprocess.call(command, shell=True)
        self.search_element(text)
        return True

    # def scroll_to_element(self, searchele):
    #     try:
    #         web_driver_wait = WebDriverWait(self.driver, 5)
    #         element1 = web_driver_wait.until(EC.presence_of_element_located((By.XPATH, searchele)))
    #         web_driver_wait.until(EC.visibility_of(element1))
    #     except TimeoutException:
    #         screen_size = self.driver.get_window_rect()
    #         A = screen_size['width'] / 2
    #         B = screen_size['height'] * 9 / 10
    #         C = screen_size['width'] / 2
    #         D = screen_size['height'] / 20
    #         startPoint = {'x': A, 'y': B}
    #         endPoint = {'x': C, 'y': D}
    #         touch_action = TouchAction(self.driver)
    #         touch_action.long_press(**startPoint).move_to(**endPoint).release().perform()
    #         self.scroll_to_element(searchele)
    #     return True

    def launch_screen(self):
        try:
            WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, self.next_btn_xpath))).click()
            WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, self.next_btn_xpath))).click()
            WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, self.get_started_btn_xpath))).click()
        except NoSuchElementException:
            return False
        return True

    # def send_key(self, xpath, text):
    #     try:
    #         element = WebDriverWait(self.driver, 30).until(
    #             EC.presence_of_element_located((By.XPATH, xpath)))
    #         element.click()
    #         element.clear()
    #         element.send_keys(text)
    #         self.driver.back()
    #     except NoSuchElementException:
    #         return False
    #     return True

    # def click(self, xpath):
    #     try:
    #         WebDriverWait(self.driver, 30).until(
    #             EC.presence_of_element_located((By.XPATH, xpath))).click()
    #     except NoSuchElementException:
    #         return False
    #     return True

    # def doubleClick(self, xpath):
    #     try:
    #         WebDriverWait(self.driver, 30).until(
    #             EC.presence_of_element_located((By.XPATH, xpath))).click()
    #         WebDriverWait(self.driver, 10).until(
    #             EC.presence_of_element_located((By.XPATH, xpath))).click()
    #     except NoSuchElementException:
    #         return False
    #     return True

    # def presence(self, xpath):
    #     try:
    #         WebDriverWait(self.driver, 60).until(
    #             EC.presence_of_element_located((By.XPATH, xpath)))
    #     except NoSuchElementException:
    #         return False
    #     return True
    #
    # def invisible(self, xpath):
    #     try:
    #         WebDriverWait(self.driver, 30).until(
    #             EC.invisibility_of_element((By.XPATH, xpath)))
    #     except NoSuchElementException:
    #         return False
    #     return True
    #
    # def text_to_be_present(self, xpath, text):
    #     try:
    #         WebDriverWait(self.driver, 30).until(
    #             EC.text_to_be_present_in_element((By.XPATH, xpath), text))
    #     except NoSuchElementException:
    #         return False
    #     return True
    #
    # def search_element(self, text):
    #     try:
    #         xpath = f"//*[text()='{text}']"
    #         element = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, xpath)))
    #         element.is_displayed()
    #     except (NoSuchElementException, TimeoutException):
    #         screen_size = self.driver.get_window_rect()
    #         a = screen_size['width'] / 2
    #         b = screen_size['height'] * .8
    #         c = screen_size['width'] / 2
    #         d = screen_size['height'] * .2
    #         command = f'adb shell input swipe {a} {b} {c} {d} {500}'
    #         subprocess.call(command, shell=True)
    #     self.search_element(text)
    #     return True
    #
    # def scroll_to_element(self, searchele):
    #     try:
    #         web_driver_wait = WebDriverWait(self.driver, 5)
    #         element1 = web_driver_wait.until(EC.presence_of_element_located((By.XPATH, searchele)))
    #         web_driver_wait.until(EC.visibility_of(element1))
    #     except TimeoutException:
    #         screen_size = self.driver.get_window_rect()
    #         A = screen_size['width'] / 2
    #         B = screen_size['height'] * 9 / 10
    #         C = screen_size['width'] / 2
    #         D = screen_size['height'] / 20
    #         startPoint = {'x': A, 'y': B}
    #         endPoint = {'x': C, 'y': D}
    #         touch_action = TouchAction(self.driver)
    #         touch_action.long_press(**startPoint).move_to(**endPoint).release().perform()
    #         self.scroll_to_element(searchele)
    #     return True

    def get_text(self, xpath):
        try:
            element = self.wait.until(
                EC.presence_of_element_located((By.XPATH, xpath)))
            element_location = element.location
            text = element.text
            allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
        except NoSuchElementException:
            return False
        return text

    def verify_text(self, xpath, text):
        try:
            actual_text = self.get_text(xpath)
            l = len(actual_text)
            print(l)
            for i in actual_text:
                print(i)
            print("**********" + actual_text + "&&&&&&&&&&")
            print("**********" + actual_text + "*****" + text)
            if actual_text == text:
                return True
        except NoSuchElementException:
            return False

    @staticmethod
    def generate_random_valid_email():
        try:
            random_number = random.randrange(10000, 999999999)
            random_email = 'vikraman.aga+'.__add__(str(random_number)).__add__('@tringapps.com')
        except NoSuchElementException:
            return False
        return random_email

    @staticmethod
    def generate_random_number(N):
        try:
            minimum = pow(10, N - 1)
            maximum = pow(10, N) - 1
        except NoSuchElementException:
            return False
        return random.randint(minimum, maximum)

    @staticmethod
    def random_string(length):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for _ in range(length))

    @staticmethod
    def password_generator(length):
        """ Function that generates a password given a length """

        uppercase_loc = random.randint(1, 4)  # random location of lowercase
        symbol_loc = random.randint(5, 6)  # random location of symbols
        lowercase_loc = random.randint(7, 12)  # random location of uppercase

        password = ''  # empty string for password

        pool = string.ascii_letters + string.punctuation  # the selection of characters used

        for i in range(length):

            if i == uppercase_loc:  # this is to ensure there is at least one uppercase
                password += random.choice(string.ascii_uppercase)

            elif i == lowercase_loc:  # this is to ensure there is at least one uppercase
                password += random.choice(string.ascii_lowercase)

            elif i == symbol_loc:  # this is to ensure there is at least one symbol
                password += random.choice(string.punctuation)

            else:  # adds a random character from pool
                password += random.choice(pool)

        return password  # returns the string

    def update_password(self,oldpwd,newpwd):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, self.change_password_text_xpath))).click()
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, self.old_password_field_xpath))).send_keys(oldpwd)
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, self.new_password_field_xpath))).send_keys(newpwd)
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, self.cnfm_password_field_xpath))).send_keys(newpwd)
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, self.update_password_button_xpath))).click()
        except NoSuchElementException:
            return False
        return True

    def password_rechange(self,newpwd,oldpwd):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, self.change_password_text_xpath))).click()
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, self.old_password_field_xpath))).send_keys(newpwd)
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, self.new_password_field_xpath))).send_keys(oldpwd)
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, self.cnfm_password_field_xpath))).send_keys(oldpwd)
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, self.update_password_button_xpath))).click()
        except NoSuchElementException:
            return False
        return True
