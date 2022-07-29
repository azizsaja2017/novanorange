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
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/pim/viewMyDetails")
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin")
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click()
        time.sleep(5)
        browser.find_element(By.ID,"menu_pim_viewMyDetails").click()
        time.sleep(1)
        browser.find_element(By.ID,"btnSave").click()
        time.sleep(1)
        browser.find_element(By.ID,"personal_txtEmpFirstName").clear()
        time.sleep(1)
        browser.find_element(By.ID,"personal_txtEmpFirstName").send_keys("Ketaman")
        time.sleep(1)
        browser.find_element(By.ID,"personal_txtEmpMiddleName").clear()
        time.sleep(1)
        browser.find_element(By.ID,"personal_txtEmpMiddleName").send_keys("Asmoro")
        time.sleep(1)
        browser.find_element(By.ID,"personal_txtEmpLastName").clear()
        time.sleep(1)
        browser.find_element(By.ID,"personal_txtEmpLastName").send_keys("Abadi")
        time.sleep(1)
        browser.find_element(By.ID,"personal_txtEmployeeId").clear()
        time.sleep(1)
        browser.find_element(By.ID,"personal_txtEmployeeId").send_keys("268745")
        time.sleep(1)
        browser.find_element(By.ID,"personal_txtOtherID").clear()
        time.sleep(1)
        browser.find_element(By.ID,"personal_txtOtherID").send_keys("198784562")
        time.sleep(1)
        browser.find_element(By.ID,"personal_txtSINNo").clear()
        time.sleep(1)
        browser.find_element(By.ID,"personal_txtSINNo").send_keys("1985")
        time.sleep(1)
        browser.find_element(By.ID,"personal_optGender_2").click()
        time.sleep(1)




        # validasi
        expected_message = "My Info"
        actual_message = browser.find_element(By.XPATH,"//b[normalize-space()='My Info']").text

        self.assertEqual(expected_message,actual_message)
    

if __name__ == "__main__": 
    unittest.main()