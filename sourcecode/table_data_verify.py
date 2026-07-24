import time
from Page import LoginPage
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
import random
from BasePage import TestBase


class table_verify(TestBase):
       
       def setUp(self):
         super().setUp()
         self.login = LoginPage(self.driver)
         self.login.login()
         time.sleep(2)

       def test_verify_table_data(self):
           
           table = self.login.driver.find_element(By.XPATH,"//table[@id='userTable']")

           text_1 = chr(random.randint(ord('a'), ord('z'))) + chr(random.randint(ord('a'), ord('z'))) + chr(random.randint(ord('a'), ord('z')))

           for data in table:
               
               print(data)


       def tearDown(self):
        time.sleep(2)
        super().tearDown()
               
               

                   
               


