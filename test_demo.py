from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains


class Test_DemoClass:
     #her test öncesi çağırılır
    def setup_method(self):
        self.driver =webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window
        self.driver.get("https://www.saucedemo.com/")

    #her testten sonra çağırılır
    def teardown_method(self):
         self.driver.quit()
    def test_demoFunc(self):
        # 3A Act Arrange Assert
         text="Hello"
         assert text == "Hello"
   
    def test_demo2(self):
         assert True
   
    
    def test_invalid_login(self):
      
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        # en fazla 5 saniye olacak şekilde user-name id'li elementin görünmesini bekle
        usernameInput = self.driver.find_element(By.ID, "user-name")
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput = self.driver.find_element(By.ID,"password")
        
        usernameInput.send_keys("1")
        passwordInput.send_keys("1")
      
        loginBtn = self.driver.find_element(By.ID,"login-button")
        
        loginBtn.click()

        errorMessage =self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
       
     