import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_login(self): 
        
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin")
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click()
        time.sleep(5)
        
        # validasi
        expected_message = "Dashboard"
        actual_message = browser.find_element(By.ID,"menu_dashboard_index").text

        self.assertEqual(expected_message,actual_message)


if __name__ == "__main__": 
    unittest.main()