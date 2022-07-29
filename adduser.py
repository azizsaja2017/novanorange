import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestAdduser(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_adduser(self): 
        
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/admin/viewSystemUsers")
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin")
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click()
        time.sleep(5)
        browser.find_element(By.ID,"menu_admin_viewAdminModule").click()
        time.sleep(1)
        browser.find_element(By.ID,"menu_admin_UserManagement").click()
        time.sleep(1)
        browser.find_element(By.ID,"btnAdd").click()
        time.sleep(1)
        browser.find_element(By.ID,"systemUser_employeeName_empName").send_keys("Ananya Dash")
        time.sleep(1)
        browser.find_element(By.ID,"systemUser_userName").send_keys("Dono Indro")
        time.sleep(1)
        browser.find_element(By.ID,"systemUser_password").send_keys("admin123456")
        time.sleep(1)
        browser.find_element(By.ID,"systemUser_confirmPassword").send_keys("admin123456")
        time.sleep(1)
        browser.find_element(By.ID,"btnSave").click()
        time.sleep(1)
        
        # validasi
        expected_message = "User Management"
        actual_message = browser.find_element(By.ID,"menu_admin_UserManagement").text

        self.assertEqual(expected_message,actual_message)
    

if __name__ == "__main__": 
    unittest.main()