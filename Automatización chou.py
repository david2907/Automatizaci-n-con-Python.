from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(8)

search_box = driver.find_element("name", "username")
search_box.send_keys("Admin")
time.sleep(3)

clave_box =driver.find_element("name","password")
clave_box.send_keys("admin123")
clave_box.send_keys(Keys.ENTER)
time.sleep(20)

no_of_jobs = int(wd.find_element(By.CSS_SELECTOR, 'href=/web/index.php/recruitment/viewRecruitmentModule')).click()







