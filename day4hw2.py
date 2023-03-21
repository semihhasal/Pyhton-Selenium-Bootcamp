from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By



class Test_saucedemo:
     def test_empty_username_password_login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")

        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID,"password")

        usernameInput.send_keys("")
        passwordInput.send_keys("")

        loginBtn = driver.find_element(By.ID,"login-button")

        loginBtn.click()
        errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username is required"
        print(f"TEST SONUCU: {testResult}")


     def test_empty_password_login(self):
         driver = webdriver.Chrome(ChromeDriverManager().install())
         driver.maximize_window()
         driver.get("https://www.saucedemo.com/")

         usernameInput = driver.find_element(By.ID, "user-name")
         passwordInput = driver.find_element(By.ID, "password")

         usernameInput.send_keys("1")
         passwordInput.send_keys("")

         loginBtn = driver.find_element(By.ID, "login-button")

         loginBtn.click()
         errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
         testResult = errorMessage.text == "Epic sadface: Password is required"
         print(f"TEST SONUCU: {testResult}")
     def test_locked_out_login(self):
         driver = webdriver.Chrome(ChromeDriverManager().install())
         driver.maximize_window()
         driver.get("https://www.saucedemo.com/")

         usernameInput = driver.find_element(By.ID, "user-name")
         passwordInput = driver.find_element(By.ID, "password")

         usernameInput.send_keys("locked_out_user")
         passwordInput.send_keys("secret_sauce")

         loginBtn = driver.find_element(By.ID, "login-button")

         loginBtn.click()
         errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
         testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
         print(f"TEST SONUCU: {testResult}")

     def test_empty_username_password_login_and_close(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")

        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")

        usernameInput.send_keys("")
        passwordInput.send_keys("")

        loginBtn = driver.find_element(By.ID, "login-button")

        loginBtn.click()
        error_button=driver.find_element(By.CLASS_NAME, "error-button")
        error_button.click()


     def test_successfull_login(self):
         driver = webdriver.Chrome(ChromeDriverManager().install())
         driver.maximize_window()
         driver.get("https://www.saucedemo.com/")

         usernameInput = driver.find_element(By.ID, "user-name")
         passwordInput = driver.find_element(By.ID, "password")

         usernameInput.send_keys("standard_user")
         passwordInput.send_keys("secret_sauce")

         loginBtn = driver.find_element(By.ID, "login-button")
         loginBtn.click()
         driver.get("https://www.saucedemo.com/inventory.html")

         sleep(3)
         productCount = driver.find_elements(By.CLASS_NAME, "inventory_item")
         print(f"Urun listesinde {len(productCount)} adet urun var")



         sleep(3)




testClass= Test_saucedemo()
testClass.test_empty_username_password_login()
testClass.test_empty_password_login()
testClass.test_locked_out_login()
testClass.test_empty_username_password_login_and_close()
testClass.test_successfull_login()


