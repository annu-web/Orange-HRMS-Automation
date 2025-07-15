import time
from BasePage import TestBase
from locators import Job_titlelocator
from locators import Adminlocators
from Page import LoginPage
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import random
from selenium.webdriver.common.keys import Keys
import os
import pyautogui

load_dotenv()

class Title_pge(TestBase):
    
    def setUp(self):
        super().setUp()
        self.login = LoginPage(self.driver)
        self.login.login()
        time.sleep(2)

    def test_able_to_open_job_page_title(self):

        self.login.click(Adminlocators.Admin_btn)
        time.sleep(2)

        self.login.click(Job_titlelocator.Job_btn)
        time.sleep(2)
        
        self.login.click(Job_titlelocator.job_title_txt)
        time.sleep(2)

        try:
            self.login.click(Job_titlelocator.job_title_ele)
        except AssertionError as e:
            raise AssertionError("Unable to click on Job Title page.")
          
        time.sleep(2)
        
    def user_able_to_open_add_job_titles_page(self):

        self.login.click(Adminlocators.Admin_btn)
        time.sleep(2)

        self.login.click(Job_titlelocator.Job_btn)
        time.sleep(2)
        
        self.login.click(Job_titlelocator.job_title_txt)
        time.sleep(2)

        self.login.click(Job_titlelocator.job_add_btn)
        time.sleep(2)

        try:
            self.login.click(Job_titlelocator.add_jb_ttle_txt)
        except AssertionError as e:
            raise AssertionError("Unable to click on add button of  Job Title page.")
        
        time.sleep(2)

    def user_able_to_add_title(self):

        self.login.click(Adminlocators.Admin_btn)
        time.sleep(2)

        self.login.click(Job_titlelocator.Job_btn)
        time.sleep(2)
        
        self.login.click(Job_titlelocator.job_title_txt)
        time.sleep(2)

        self.login.click(Job_titlelocator.job_add_btn)
        time.sleep(2)
        
        text_1 = chr(random.randint(ord('a'), ord('z'))) + chr(random.randint(ord('a'), ord('z'))) + chr(random.randint(ord('a'), ord('z')))

        self.login.send_text(Job_titlelocator.jb_ttle_entry, text_1)
        time.sleep(2)

        self.login.send_text(Job_titlelocator.jb_descrptn_entry, os.getenv("JOB_DESCRIPTION"))
        time.sleep(2)

        self.login.send_text(Job_titlelocator.add_nte_btn,os.getenv("ADD_NOTE"))
        time.sleep(2)

        self.login.click(Job_titlelocator.ttle_upload_fle)
        time.sleep(10) 
        pyautogui.write(r"C:\PythonFolder\pythonProject\sourcecode\Test data\job_dscptn_file.txt") #path of File
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(4)

        self.login.click(Job_titlelocator.jb_ttle_sve_btn)
        time.sleep(2)

        try:
            self.login.assert_elem_text_wait(Adminlocators.add_success_msg, "Successfully Saved")
        except AssertionError as e:
            raise AssertionError("Job title is not added successfully.")
        
        time.sleep(4)

    def test_able_to_add_without_fields(self):

        self.login.click(Adminlocators.Admin_btn)
        time.sleep(2)
        self.login.click(Job_titlelocator.Job_btn)
        time.sleep(2)
        self.login.click(Job_titlelocator.job_title_txt)
        time.sleep(2)
        self.login.click(Job_titlelocator.job_add_btn)
        time.sleep(2)
        self.login.click(Job_titlelocator.jb_ttle_sve_btn)
        time.sleep(2)

        try:
            self.login.assert_elem_text_wait(Job_titlelocator.jb_rqrd_btn, "Required")
        except AssertionError as e:
            raise AssertionError("User is unable to add job title without required fields.")
        

    def test_user_able_to_edit_job_title(self):

        self.login.click(Adminlocators.Admin_btn)
        time.sleep(2)

        self.login.click(Job_titlelocator.Job_btn)
        time.sleep(2)
        
        self.login.click(Job_titlelocator.job_title_txt)
        time.sleep(2)

        self.login.click(Adminlocators.Admin_edit_btn)
        time.sleep(2)

        self.login.click(Job_titlelocator.jb_ttle_sve_btn)
        time.sleep(2)

        try:
          self.login.assert_elem_text_wait(Adminlocators.Edit_success_msg, "Successfully Updated")
        except AssertionError as e:
            raise AssertionError("User is unable to edit job title")
        

    def test_user_able_to_delete_job_title(self):

        self.login.click(Adminlocators.Admin_btn)
        time.sleep(2)

        self.login.click(Job_titlelocator.Job_btn)
        time.sleep(2)
        
        self.login.click(Job_titlelocator.job_title_txt)
        time.sleep(2)

        self.login.click(Adminlocators.Admin_dlt_btn)
        time.sleep(2)

        self.login.click(Adminlocators.dlt_cnfrm_btn)
        time.sleep(2)

        try:
          self.login.assert_elem_text_wait(Adminlocators.success_msg, "Successfully Deleted")
        except AssertionError as e:
            raise AssertionError("User is unable to delete job title")
        

    def  test_able_to_cancel_add_job_title(self):

        self.login.click(Adminlocators.Admin_btn)
        time.sleep(2)

        self.login.click(Job_titlelocator.Job_btn)
        time.sleep(2)

        self.login.click(Job_titlelocator.job_title_txt)
        time.sleep(2)

        self.login.click(Job_titlelocator.job_add_btn)
        time.sleep(2)

        self.login.click(Adminlocators.Admin_cancl_btn)
        time.sleep(2)

        try:
          self.login.is_visible(Job_titlelocator.job_title_ele)
        except AssertionError as e:
            raise AssertionError("User is unable to delete job title")
        
    def  test_able_to_cancel_edit_job_title(self):

        self.login.click(Adminlocators.Admin_btn)
        time.sleep(2)

        self.login.click(Job_titlelocator.Job_btn)
        time.sleep(2)

        self.login.click(Job_titlelocator.job_title_txt)
        time.sleep(2)

        self.login.click(Adminlocators.Admin_edit_btn)
        time.sleep(2)

        self.login.click(Adminlocators.Admin_cancl_btn)
        time.sleep(2)

        try:
          self.login.is_visible(Job_titlelocator.job_title_ele)
        except AssertionError as e:
            raise AssertionError("User is unable to delete job title")
        

    def  test_able_to_cancel_delete_job_title(self):

        self.login.click(Adminlocators.Admin_btn)
        time.sleep(2)

        self.login.click(Job_titlelocator.Job_btn)
        time.sleep(2)

        self.login.click(Job_titlelocator.job_title_txt)
        time.sleep(2)

        self.login.click(Adminlocators.Admin_dlt_btn)
        time.sleep(2)

        self.login.click(Job_titlelocator.dlt_cncl_btn)
        time.sleep(2)

        try:
          self.login.is_visible(Job_titlelocator.job_title_ele)
        except AssertionError as e:
            raise AssertionError("User is unable to delete job title")
        
        
    def  test_able_to_select_all_job_checkboxes(self):
       
     self.login.click(Adminlocators.Admin_btn)
     time.sleep(2)

     self.login.click(Job_titlelocator.Job_btn)
     time.sleep(2)

     self.login.click(Job_titlelocator.job_title_txt)
     time.sleep(2)

     self.login.click(Job_titlelocator.jb_ttle_checkbox)

     time.sleep(2)

     checkboxes = self.login.driver.find_elements(By.XPATH,"//input[@type='checkbox']")
        #self.login.get_attr(Job_titlelocator.jb_ttle_chckboxes,)
 
     for checkbx in checkboxes:
           
        if checkbx.is_selected():
         
         print("checkbox is already selected.")
     else:
        print("checkbox is selected.")

     self.driver.save_screenshot("C:\PythonFolder\pythonProject\sourcecode\Test data\ss2.png")
     

    def test_able_delete_all_job_title_Atonce(self):
       
      self.login.click(Adminlocators.Admin_btn)
      time.sleep(2)

      self.login.click(Job_titlelocator.Job_btn)
      time.sleep(2)

      self.login.click(Job_titlelocator.job_title_txt)
      time.sleep(2)

      self.login.click(Job_titlelocator.jb_ttle_checkbox)
      time.sleep(2)

      checkboxes = self.login.driver.find_elements(By.XPATH,"//input[@type='checkbox']")
 
      for checkbx in checkboxes:
           
        if checkbx.is_selected():
         print("checkbox is already selected.")
        else:
         print("checkbox is selected.")

    #   self.login.click(Job_titlelocator.dlt_selected_chckboxs)
    #   time.sleep(2)

    #   self.login.click(Adminlocators.dlt_cnfrm_btn)
    #   time.sleep(2)

    #   try:
    #     self.login.is_visible(Adminlocators.Admin_dlt_btn)
    #   except AssertionError as e:
    #         raise AssertionError("User is unable to delete all selected job title")

    def tearDown(self):
       time.sleep(2)
       super().tearDown()





        