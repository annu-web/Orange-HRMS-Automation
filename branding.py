import os
import time
from BasePage import TestBase
from locators import branding
from locators import Adminlocators
from Page import LoginPage
import unittest
from dotenv import load_dotenv
from selenium.webdriver.support.color import Color
import pyautogui

load_dotenv()

class branding_page(TestBase):
    
    def setUp(self):
        super().setUp()
        self.login = LoginPage(self.driver)
        self.login.login()
        time.sleep(2)


    def test_able_to_publish_branding(self):
       
       self.login.click(Adminlocators.Admin_btn)
       time.sleep(2)

       self.login.click(branding.crprte_brndng_btn)
       time.sleep(2)

       self.login.click(branding.prmry_fnt_clr)
       time.sleep(2)

       self.login.clear_text_by_keys(branding.hex_clr_input_bx)
       time.sleep(2)

       self.login.send_text(branding.hex_clr_input_bx,"#52d852")
       time.sleep(4)

       style = self.login.get_attr(branding.prmry_fnt_clr_1,"style")

       a = str(style)

       b = a[47:]

       c = b.strip(";")

       self.assertEqual(c,"rgb(82, 216, 82)")  
       time.sleep(2)

       self.login.click(branding.scndry_fnt_clr)
       time.sleep(2)

       self.login.clear_text_by_keys(branding.hex_clr_input_bx)
       time.sleep(2)

       self.login.send_text(branding.hex_clr_input_bx,"#de28a7")
       time.sleep(2)

       
       style_1 = self.login.get_attr(branding.scndry_fnt_clr_1,"style")

       e = str(style_1)

       d = e[47:].strip(";")

       self.assertEqual(d,"rgb(222, 40, 167)")  
       time.sleep(2)

       self.login.click(branding.form_pg)
       time.sleep(2)

       self.login.click(branding.clint_logo_upld_btn)
       time.sleep(2)
           
       pyautogui.write(r"C:\PythonFolder\pythonProject\sourcecode\Screenshot\Screenshot 2025-07-11 114247 (1).png") #path of File
       time.sleep(2)
       pyautogui.press('enter')
       time.sleep(2)

       self.driver.execute_script("window.scrollBy(0,500)")

       self.login.click(branding.pblsh_btn)
       time.sleep(2)
    
       try:
         self.login.assert_elem_text_wait(Adminlocators.add_success_msg, "Successfully Saved")
       except AssertionError as e:
            raise AssertionError("corporate branding not published successfully.")
        






