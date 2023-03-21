from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com/")

driver.maximize_window()
#sleep(10)
input=driver.find_element(By.NAME,"q")
input.send_keys("kodlamaio")
searchbutton= driver.find_element(By.NAME,"btnK")
sleep(2)
searchbutton.click()
sleep(2)
firstResult= driver.find_element(By.XPATH,"//*[@id='rso']/div[1]/div/div/div/div/div/div/div/div[1]/a")
firstResult.click()

listOfCourses= driver.find_elements(By.CLASS_NAME,"course-listing")
print(f"kodlamaio sitesinde su anda {len(listOfCourses)}adet kurs var.")
while True:
    continue 
# HTML LOCATORS



#full xpath

# /html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a

#xpath
# //*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a

