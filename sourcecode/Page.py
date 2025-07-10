from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from locators import LoginLocators
from locators import Adminlocators
import time
import os
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
import random

class BasePage:
    """
    Base Page class that hold common elements
    and functionalities to all pages in app
    """
    def __init__(self, driver):
        self.driver = driver
        
    def do_click(self, by_locator):
        WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(by_locator)).click()
        
    def click(self, by_locator):
        WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(by_locator)).click()

    def get_attr_wait(self, by_locator,attribute):
        return WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(by_locator)).get_attribute(attribute)
    
    def get_attr(self, by_locator,attribute):
        attr= self.driver.find_element(*by_locator)
        return attr.get_attribute(attribute)
    
    def select_dropdown(self,by_locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator)).click()
   
    def get_text(self, by_locator):
        text=WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(by_locator)).text
        return text.lower()
    
    def explicit_wait(self,by_locator):
        WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(by_locator))

    
    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(by_locator))
        return element.text
    
    def get_text_no_low(self, by_locator):
        return WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(by_locator)).text
    
    def get_text_no_low_without_wait(self, by_locator):
        return self.driver.find_element(*by_locator).text
    
    def hover_to(self, by_locator,):
        element = WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()

    def assert_elem_text_wait(self, by_locator, elem_text):
        element = WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(by_locator))
        assert element.text.lower() == elem_text.lower()

    def assert_elem_text_wait_1(self, by_locator, elem_text):
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(by_locator))
        assert element.text.lower() == elem_text.lower()
      
    def assert_elem_text(self, by_locator, elem_text):
        element = self.driver.find_element(*by_locator)
        assert element.text.lower() == elem_text.lower()
        
    def assert_elem_get_attribute(self,by_locator,attribute,elem_text):
        element = self.driver.find_element(*by_locator).get_attribute(attribute)
        assert element.lower() == elem_text.lower()
        
    def assert_elem_in_get_attribute(self,by_locator,attribute,elem_text):
        element = self.driver.find_element(*by_locator).get_attribute(attribute)
        assert elem_text in element
        
    def assert_elem_get_attribute_wait(self,by_locator,attribute,elem_text):
        element = WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(by_locator)).get_attribute(attribute)
        assert element == elem_text 
        
    def assert_elem_in_get_attribute_wait(self,by_locator,attribute,elem_text):
        element = WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(by_locator)).get_attribute(attribute)
        assert elem_text in element

    def is_clickable(self, by_locator):
        return WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(by_locator))
    
    def is_visible(self, by_locator):
        return WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(by_locator))
    
    def is_not_display(self, by_locator):
        return WebDriverWait(self.driver, 30).until(EC.invisibility_of_element(by_locator))
    
    def clear_text(self, by_locator):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator)).clear()
    
    def is_display(self, by_locator):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator))
    
    def is_selected(self, by_locator):
        return WebDriverWait(self.driver, 40).until(EC.element_located_selection_state_to_be(by_locator))

    def send_text(self, by_locator, text):
        return WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
    
    def send_keys(self, by_locator, text):
        return WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
    
    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
    
    def select(self, by_locator,text):
        sele=(WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located(by_locator)))
        return sele.select_by_value(text)
    
    def select_option(self, *locator, option):
        """Select visible text from a dropdown"""
        select = Select(self.driver.find_element(*locator))
        select.select_by_visible_text(option)

    
    def select_text(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((by_locator, text)))
        self.click(by_locator)
        
    def Select_values_from_dropdown(self, by_locator, value):
        self.send_text(by_locator, value)
        for ele in by_locator:
            if ele.text == value:
                ele.click()
    
    def select_dynamic_drpdwn(self, by_locator1, by_locator2):
       WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((by_locator1)))
       self.click(by_locator2)

    def clear_text_by_keys(self, by_locator):
        Clear = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((by_locator)))
        Clear.send_keys(Keys.CONTROL + "a")
        Clear.send_keys(Keys.DELETE)

    def random(self):
        chr(random.randint(ord('a'), ord('z')))+chr(random.randint(ord('a'), ord('z')))+chr(random.randint(ord('a'), ord('z')))+chr(random.randint(ord('a'), ord('z')))+chr(random.randint(ord('a'), ord('z')))
          
    def wait_for_element_to_vanish(self,element: WebElement):
        is_displayed=element.is_displayed
        start_time=self.get_current_time_in_millis()
        time_interval_in_seconds= 5
        while is_displayed and not self.is_time_out(start_time,time_interval_in_seconds):
            is_displayed=element.is_displayed()
            
        return not is_displayed  

    
class  LoginPage(BasePage):
        
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(os.environ.get("BASE_URL"))
        self.username="Admin"
        self.pswd= "admin123"
        self.wrng_usrnme = "Akimj"
        self.wrng_pswd = "123"
      
        
    def login(self):
        self.send_text(LoginLocators.L_usErname,self.username)
        self.send_text(LoginLocators.L_pssword,self.pswd)
        self.click(LoginLocators.L_loginbtn)

        
    '''def logout(self):
        self.click(UpdateManifestLocators.admin_btn)
        self.click(LogoutLocators.logout_btn)'''
        


    