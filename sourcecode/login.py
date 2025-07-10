import os
import time
from BasePage import TestBase
from locators import LoginLocators
from Page import LoginPage
import unittest
from dotenv import load_dotenv

load_dotenv()

from selenium.common.exceptions import NoSuchElementException


class Login(TestBase):

    def setUp(self):
        super().setUp()
        self.login = LoginPage(self.driver)


    def test_able_login_with_valid_credentials(self):

        self.login.click(LoginLocators.L_usErname)
        time.sleep(2)

        self.login.send_text(LoginLocators.L_usErname, self.login.username)
        time.sleep(2)

        self.login.click(LoginLocators.L_pssword)
        time.sleep(2)

        self.login.send_text(LoginLocators.L_pssword, self.login.pswd)
        time.sleep(2)

        self.login.click(LoginLocators.L_loginbtn)
        time.sleep(2)
        
        # Verify dashboard title element is visible
        try:
            self.login.assert_elem_text_wait(LoginLocators.L_login_title,"Dashboard")
        except AssertionError as e:
            raise(AssertionError("User is unable to open login page."))
        

    def test_able_to_login_with_invalid_credentials(self):

        self.login.click(LoginLocators.L_usErname)
        time.sleep(2)

        self.login.send_text(LoginLocators.L_usErname, self.login.wrng_usrnme)
        time.sleep(2)

        self.login.click(LoginLocators.L_pssword)
        time.sleep(2)

        self.login.send_text(LoginLocators.L_pssword, self.login.wrng_pswd)
        time.sleep(2)

        self.login.click(LoginLocators.L_loginbtn)
        time.sleep(2)

         # Verify invalid credentials message is visible
        try:
            self.login.assert_elem_text_wait(LoginLocators.L_invalid_crds,"Invalid credentials")
        except AssertionError as e:
            raise(AssertionError("User is able to login with wrong creds"))
        


    def test_able_to_login_without_credentials(self):
        
        time.sleep(3)
        self.login.click(LoginLocators.L_loginbtn)
        time.sleep(2)
        try:
            self.login.assert_elem_text_wait(LoginLocators.L_reqrd_filds,"Required")
        except AssertionError as e:
            raise(AssertionError("User is able to login without creds"))

    def tearDown(self):
       time.sleep(2)
       super().tearDown()

    #    print("Browser closed successfully after test.")

    