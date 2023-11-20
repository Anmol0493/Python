from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.gmail.com")

# email_input = driver.find_element(By.ID, "identifierId")
# email_input.send_keys("abcdefg96385200")
# time.sleep(1)
# email_input.send_keys(Keys.ENTER)
# time.sleep(3)

driver.find_element(By.ID, "identifierId").send_keys("abcdefg96385200")
driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span').click()
time.sleep(5)

driver.find_element(By.NAME, "Passwd").send_keys("zxcv@000")
driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span').click()
time.sleep(3)

# password_input = driver.find_element(By.NAME, "Passwd")
# password_input.send_keys("zxcv@000")
# time.sleep(1)
# password_input.send_keys(Keys.ENTER)
# time.sleep(3)

print("Gmail login has been successfully completed")  
time.sleep(25)
driver.close()