import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestAddEmployee(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_addemployee(self): 
        
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/pim/viewEmployeeList")
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin")
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click()
        time.sleep(5)
        browser.find_element(By.ID,"menu_pim_viewPimModule").click()
        time.sleep(1)
        browser.find_element(By.ID,"menu_pim_viewEmployeeList").click()
        time.sleep(1)
        browser.find_element(By.ID,"btnAdd").click()
        time.sleep(1)
        browser.find_element(By.ID,"firstName").send_keys("Didik")
        time.sleep(1)
        browser.find_element(By.ID,"lastName").send_keys("Haryadi")
        time.sleep(1)
        browser.find_element(By.ID,"chkLogin").click()
        time.sleep(1)
        browser.find_element(By.ID,"user_name").send_keys("DidikHar212")
        time.sleep(1)
        browser.find_element(By.ID,"user_password").send_keys("adminku123")
        time.sleep(1)
        browser.find_element(By.ID,"re_password").send_keys("adminku123")
        time.sleep(1)
        browser.find_element(By.ID,"btnSave").click()
        time.sleep(1)
        
        # validasi
        expected_message = "Employee List"
        actual_message = browser.find_element(By.ID,"menu_pim_viewEmployeeList").text

        self.assertEqual(expected_message,actual_message)
    

if __name__ == "__main__": 
    unittest.main()