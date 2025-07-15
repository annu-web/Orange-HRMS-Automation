import unittest
from selenium import webdriver
from chromedriver_py import binary_path
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import chrome
import pytest
import os

class TestBase(unittest.TestCase):
    
    def setUp(self):
        download_path=os.path.join(os.getcwd(),"Downloads")
        chrome_options = webdriver.ChromeOptions()
        p = {'download.default_directory':download_path}
        
        # chrome_options.add_experimental_option('prefs', p)
        # chrome_options.add_argument('headless')
        # chrome_options.headless = True
        # chrome_options.add_argument('window-size=1920x1080')
        service_object = Service(binary_path)
        self.driver = webdriver.Chrome(service=service_object, chrome_options=chrome_options)
        self.driver.maximize_window()


    def tearDown(self):
        self.driver.quit()

    if __name__=="__main__":
        unittest.main()
