from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date

class Test_HW2:
     #her test öncesi çağırılır
    def setup_method(self):
        self.driver =webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window
        self.driver.get("https://www.saucedemo.com/")
        self.folderPath=str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)
        #31.03.2023

    def teardown_method(self):
         self.driver.quit()
   
    @pytest.mark.parametrize("username,password",[("locked_out_user","secret_sauce")])
    def test_locked_user(self,username,password):

        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"),10)
        passwordInput = self.driver.find_element(By.ID,"password")
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-locked_user.png")
        assert errorMessage.text == "Epic sadface: Sorry, this user has been locked out."

    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_basket_item_number(self,username,password):
      
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"),10)
        passwordInput = self.driver.find_element(By.ID,"password")
        
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
      
        loginBtn = self.driver.find_element(By.ID,"login-button")
        
        loginBtn.click()

        sleep(2)
        item1=self.driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack")
        item1.click()
        sleep(2)
        item2=self.driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light")
        item2.click()

        basket=self.driver.find_element(By.CLASS_NAME,"shopping_cart_link")
        basket.click()
        sleep(2)

        numberOfItems=self.driver.find_elements(By.CLASS_NAME,"cart_item")

        assert len(numberOfItems)==2
        self.driver.save_screenshot(f"{self.folderPath}/test-basket-item-numbers.png")

        

    @pytest.mark.parametrize("username,password,firstname,lastname,postalcode",[("standard_user","secret_sauce","semih","hasal","00000")])
    def test_payment(self,username,password,firstname,lastname,postalcode):

        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"),10)
        passwordInput = self.driver.find_element(By.ID,"password")

        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
      
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(1)

        item1=self.driver.find_element(By.ID,"add-to-cart-sauce-labs-fleece-jacket")
        item1.click()

        basket=self.driver.find_element(By.CLASS_NAME,"shopping_cart_link")
        basket.click()
        sleep(1)
        checkout=self.driver.find_element(By.ID,"checkout")
        checkout.click()
        self.driver.save_screenshot(f"{self.folderPath}/personel-infos.png")
        
        self.waitForElementVisible((By.ID,"first-name"))
        firstnameInput = self.driver.find_element(By.ID,"first-name")
        self.waitForElementVisible((By.ID,"last-name"),10)
        lastnameInput = self.driver.find_element(By.ID,"last-name")
        self.waitForElementVisible((By.ID,"postal-code"),10)
        postalcodeInput = self.driver.find_element(By.ID,"postal-code")
        sleep(1)
        firstnameInput.send_keys(firstname)
        lastnameInput.send_keys(lastname)
        postalcodeInput.send_keys(postalcode)
        sleep(1)
        continueClick=self.driver.find_element(By.NAME,"continue")
        continueClick.click()
        self.driver.save_screenshot(f"{self.folderPath}/payment.png")
        sleep(1)
        finishClick=self.driver.find_element(By.NAME,"finish")
        finishClick.click()

        congratsMessage=self.driver.find_element(By.XPATH,"//*[@id='checkout_complete_container']/h2")
        self.driver.save_screenshot(f"{self.folderPath}/finish.png")
        assert congratsMessage.text == "Thank you for your order!"
       





    def test_add_remove(self):
        usernameInput = self.driver.find_element(By.ID,"user-name")
        usernameInput.send_keys("standard_user")
        passwordInput = self.driver.find_element(By.ID,"password")
        passwordInput.send_keys("secret_sauce")
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        self.waitForElementVisible((By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/a/div"))
        bikeLightAdd = self.driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light")
        bikeLightAdd.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-add1-remove.png")
        sleep(2)
        bikeLightRemove = self.driver.find_element(By.ID,"remove-sauce-labs-bike-light")
        bikeLightRemove.click()
        sleep(2)
        self.driver.save_screenshot(f"{self.folderPath}/test-add-remove2.png")
        addtoCart = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/button")

        assert addtoCart.text == "Add to cart"

    def waitForElementVisible(self,locator,timeout=5): 
         WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))