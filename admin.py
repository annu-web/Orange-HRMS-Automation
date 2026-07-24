import time
from BasePage import TestBase
from locators import Adminlocators
from locators import Job_titlelocator
from Page import LoginPage
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv
import os
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import random
from selenium.webdriver.common.keys import Keys
import pytest
from PIL import Image



load_dotenv()

class Admin(TestBase):
   
   def setUp(self):
         super().setUp()
         self.login = LoginPage(self.driver)
         self.login.login()
         time.sleep(2)
         

   @pytest.mark.order("first")
   def test_able_to_add_admin_user(self):
       
         self.login.click(Adminlocators.Admin_btn)
         time.sleep(2)

         self.login.click(Adminlocators.add_btn)
         time.sleep(2)

         self.login.click(Adminlocators.User_slct_drpdwn)
         time.sleep(5)

         self.login.select_dropdown(Adminlocators.ESS_slct_btn)
         time.sleep(2)

         self.login.click(Adminlocators.EmpName)
         time.sleep(2)

         self.login.send_text(Adminlocators.EmpName, "j")
         time.sleep(2)

         self.login.select_dropdown(Adminlocators.Emp_name_slct)
         time.sleep(2)

         global text_1

         text_1 = chr(random.randint(ord('a'), ord('z')))+chr(random.randint(ord('a'), ord('z')))+chr(random.randint(ord('a'), ord('z')))+chr(random.randint(ord('a'), ord('z')))+chr(random.randint(ord('a'), ord('z')))

         self.login.send_keys(Adminlocators.admn_usrnme_slct, text_1)
         time.sleep(2)
      
         self.login.get_text(Adminlocators.admn_usrnme_slct)

         time.sleep(2)
   
         self.login.click(Adminlocators.Status_slct_drpdwn)

         self.login.select_dropdown(Adminlocators.disabled_slct_btn)
         time.sleep(2)

         self.login.send_text(Adminlocators.Admin_pswd, os.getenv("ADMIN_PASSWORD"))
         time.sleep(2)

         self.login.send_text(Adminlocators.Admin_confrm_pswd, os.getenv("ADMIN_CONFIRM_PASSWORD"))
         time.sleep(2)

         self.login.click(Adminlocators.Admin_sav_btn)
         time.sleep(2)

         try:
                self.login.assert_elem_text_wait(Adminlocators.add_success_msg, "Successfully Saved")
         except AssertionError as e:
                raise AssertionError("User is unable to add new admin user.")
    
   @pytest.mark.order("fourth")
   def test_user_able_to_delete_admin_user(self):
          
          self.login.click(Adminlocators.Admin_btn)
          time.sleep(2)

          self.login.click(Adminlocators.User_slct_drpdwn)
          time.sleep(5)

          self.login.select_dropdown(Adminlocators.ESS_slct_btn)
          time.sleep(2)

          self.login.click(Adminlocators.Status_slct_drpdwn)
          time.sleep(2)

          self.login.select_dropdown(Adminlocators.disabled_slct_btn)
          time.sleep(2)

          self.login.click(Adminlocators.Admin_search)
          time.sleep(2)

          self.login.click(Adminlocators.Admin_dlt_btn)
          time.sleep(2)

          self.login.click(Adminlocators.dlt_cnfrm_btn)
        

          try:
            self.login.assert_elem_text_wait(Adminlocators.success_msg, "Successfully Deleted")
          except AssertionError as e:
            raise AssertionError("User is unable to delete admin user.")
          
   @pytest.mark.order("fifth")
   def test_user_unable_to_add_admin_user_without_fields(self):
    
        self.login.click(Adminlocators.Admin_btn)
        time.sleep(2)

        self.login.click(Adminlocators.add_btn)
        time.sleep(2)

        self.login.click(Adminlocators.Admin_sav_btn)
        time.sleep(2)
        
        try:
            self.login.assert_elem_text_wait(Adminlocators.Admin_reqrd_btn, "Required")
            self.login.assert_elem_text_wait(Adminlocators.Admin_pswd_nt_mtch, "Passwords do not match")
        except AssertionError as e:
            raise AssertionError("User is unable to delete admin user.")
        
        
   @pytest.mark.order("second")
   def test_able_to_edit_admin_user(self):
        
        self.login.click(Adminlocators.Admin_btn)
        time.sleep(5)

        self.login.click(Adminlocators.User_slct_drpdwn)
        time.sleep(5)

        self.login.select_dropdown(Adminlocators.ESS_slct_btn)
        time.sleep(2)

        self.login.click(Adminlocators.Status_slct_drpdwn)
        time.sleep(2)

        self.login.select_dropdown(Adminlocators.disabled_slct_btn)
        time.sleep(2)

        self.login.click(Adminlocators.Admin_search)
        time.sleep(2)

        self.login.click(Adminlocators.Admin_edit_btn)
        time.sleep(2)

        self.login.clear_text_by_keys(Adminlocators.admn_usrnme_slct)
        time.sleep(2)

        self.login.send_text(Adminlocators.admn_usrnme_slct, os.getenv("RANDOM_TEXT"))
        time.sleep(2)
        
        self.login.click(Adminlocators.Admin_sav_btn)
        time.sleep(2)

        try:
            self.login.assert_elem_text_wait(Adminlocators.Edit_success_msg, "Successfully Updated")
            #self.login.assert_elem_text_wait(Adminlocators.Admin_pswd_nt_mtch, "Passwords do not match")
        except AssertionError as e:
            raise AssertionError("User is unable to delete admin user.") 
        

   @pytest.mark.order("third")
   def test_able_to_search_admin_user(self):
            
        self.login.click(Adminlocators.Admin_btn)
        time.sleep(2)

        self.login.click(Adminlocators.User_slct_drpdwn)
        time.sleep(5)

        self.login.select_dropdown(Adminlocators.ESS_slct_btn)
        time.sleep(2)

        self.login.click(Adminlocators.Status_slct_drpdwn)
        time.sleep(2)

        self.login.select_dropdown(Adminlocators.disabled_slct_btn)
        time.sleep(2)

        self.login.click(Adminlocators.Admin_search)
        time.sleep(2)

        try:
            self.login.assert_elem_text_wait(Adminlocators.Admn_user_role_verify, "ESS")
        except AssertionError as e:
            raise AssertionError("User is unable to search admin user.")  

   @pytest.mark.order("Sixth")
   def test_able_to_reset_admin_user(self):
            
        self.login.click(Adminlocators.Admin_btn)
        time.sleep(2)

        self.login.send_text(Adminlocators.admn_usrnme_slct, os.getenv("TEXT"))
        time.sleep(2)

        self.login.click(Adminlocators.Status_slct_drpdwn)
        time.sleep(2)

        self.login.select_dropdown(Adminlocators.disabled_slct_btn)
        time.sleep(2)

        self.login.click(Adminlocators.Admin_reset_btn)
        
        a = self.login.get_element_text(Adminlocators.Status_slct_drpdwn)

        print("status" +a)

        try:
            self.login.assert_elem_text_wait(Adminlocators.Status_slct_drpdwn, a)
        except AssertionError as e:
            raise AssertionError("User is unable to reset admin user.")   

   @pytest.mark.order("Seventh")
   def test_user_unable_to_search_invalid_username(self):

        self.login.click(Adminlocators.Admin_btn)
        time.sleep(2)

        random_1 =chr(random.randint(ord('a'), ord('z')))+chr(random.randint(ord('a'), ord('z')))+chr(random.randint(ord('a'), ord('z')))+chr(random.randint(ord('a'), ord('z')))+chr(random.randint(ord('a'), ord('z')))

        self.login.send_text(Adminlocators.admn_usrnme_slct, random_1)
        time.sleep(2)
        
        self.login.click(Adminlocators.Admin_search)
        time.sleep(2)

        try:
             self.login.assert_elem_text_wait(Adminlocators.No_info_found_msg,"No Records Found")
        except AssertionError as e:
            raise AssertionError("User is able to search admin user with non exist username.")   
        

   @pytest.mark.order("eigth")
   def test_user_unable_to_search_invalid_Empname(self):

      self.login.click(Adminlocators.Admin_btn)
      time.sleep(2)
      
      global text_3
      text_3 =chr(random.randint(ord('a'), ord('z')))+chr(random.randint(ord('a'), ord('z')))+chr(random.randint(ord('a'), ord('z')))+chr(random.randint(ord('a'), ord('z')))+chr(random.randint(ord('a'), ord('z')))

      self.login.send_text(Adminlocators.EmpName,text_3 )
      time.sleep(2)
  
      self.login.click(Adminlocators.Admin_search)
      time.sleep(2)

      try:
             self.login.assert_elem_text_wait(Adminlocators.Admn_invalid_srch,"Invalid")
      except AssertionError as e:
            raise AssertionError("User is able to search admin user with non exist username.")      
      
   @pytest.mark.order("nineth")
   def test_able_to_cancel_add_admin(self):
           
      self.login.click(Adminlocators.Admin_btn)
      time.sleep(2)
       
      self.login.click(Adminlocators.add_btn)
      time.sleep(2)

      self.login.click(Adminlocators.Admin_cancl_btn)

      try:
             self.login.is_visible(Adminlocators.add_btn)
      except AssertionError as e:      
            raise AssertionError("User is unable to click on cancel button.")
      
   @pytest.mark.order("tenth")
   def test_able_to_cancel_edit_admin(self):
           
      self.login.click(Adminlocators.Admin_btn)
      time.sleep(2)
       
      self.login.click(Adminlocators.Admin_edit_btn)
      time.sleep(2)

      self.login.click(Adminlocators.Admin_cancl_btn)

      try:
             self.login.is_visible(Adminlocators.add_btn)
      except AssertionError as e:      
            raise AssertionError("User is unable to click on edit cancel button.")
      

   @pytest.mark.order("tenth")
   def test_able_to_cancel_delete_admin(self):
           
      self.login.click(Adminlocators.Admin_btn)
      time.sleep(2)
      
      self.login.click(Adminlocators.User_slct_drpdwn)
      time.sleep(5)

      self.login.select_dropdown(Adminlocators.ESS_slct_btn)
      time.sleep(2)

      self.login.click(Adminlocators.Admin_search)
      time.sleep(2)
       
      self.login.click(Adminlocators.Admin_dlt_btn)
      time.sleep(2)

      self.login.click(Job_titlelocator.dlt_cncl_btn)
      time.sleep(2)

      try:
             self.login.is_visible(Adminlocators.add_btn)
      except AssertionError as e:      
            raise AssertionError("User is unable to click on edit cancel button.")
      
   @pytest.mark.order("eleventh")
   def test_able_to_get_pswd_mismatch_msg(self):
           
      self.login.click(Adminlocators.Admin_btn)
      time.sleep(2)
       
      self.login.click(Adminlocators.add_btn)
      time.sleep(2)

      self.login.send_text(Adminlocators.Admin_pswd,os.getenv("RANDOM_TEXT"))

      self.login.send_text(Adminlocators.Admin_confrm_pswd,os.getenv("TEXT"))

      try:
            self.login.assert_elem_text_wait(Adminlocators.Admin_pswd_nt_mtch, "Passwords do not match")
      except AssertionError as e:
            raise AssertionError("User is able to add mismatched admin pswd.")
      
   @pytest.mark.order("twelfth")
   def test_able_to_get_usrnme_exist_msg(self):
           
      self.login.click(Adminlocators.Admin_btn)
      time.sleep(2)
       
      self.login.click(Adminlocators.add_btn)
      time.sleep(2)

      self.login.send_text(Adminlocators.admn_usrnme_slct,os.getenv("USERNAME_1"))
      time.sleep(2)


      try:
            self.login.assert_elem_text_wait(Job_titlelocator.Alrdy_exist_msg, "Already exists")
      except AssertionError as e:
            raise AssertionError("User is unable to view already exist erro mesg for username field.")


   @pytest.mark.order("thirteenth")
   def test_able_to_add_pswd_while_edit(self):
           
      self.login.click(Adminlocators.Admin_btn)
      time.sleep(2)
       
      self.login.click(Adminlocators.Admin_edit_btn)
      time.sleep(2)

      self.login.click(Job_titlelocator.chnge_pswd_chckbx)
      time.sleep(2)

      self.login.send_text(Adminlocators.Admin_pswd,os.getenv("RANDOM_TEXT"))
      time.sleep(2)

      self.login.send_text(Adminlocators.Admin_confrm_pswd,os.getenv("TEXT"))
      time.sleep(2)

      try:
            self.login.assert_elem_text_wait(Adminlocators.Admin_pswd_nt_mtch, "Passwords do not match")
      except AssertionError as e:
            raise AssertionError("User is able to add mismatched admin pswd.") 
      
   @pytest.mark.order("fourteenth")
   def test_able_to_get_pswd_validation_while_edit(self):
           
      self.login.click(Adminlocators.Admin_btn)
      time.sleep(2)

      self.login.click(Adminlocators.Admin_edit_btn)
      time.sleep(2)

      self.login.click(Job_titlelocator.chnge_pswd_chckbx)
      time.sleep(2)

      self.login.click(Adminlocators.Admin_sav_btn)
      time.sleep(2)

      try:
            self.login.assert_elem_text_wait(Adminlocators.Admin_pswd_nt_mtch, "Passwords do not match")
      except AssertionError as e:
        raise AssertionError("User is able to add mismatched admin pswd.")

   def tearDown(self):
    super().tearDown()

  
   


