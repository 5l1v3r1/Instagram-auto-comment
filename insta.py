from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.instagram.com')
sleep(1)
driver.find_element_by_name('username').send_keys('usernone')  #enter your insta acc
driver.find_element_by_name('password').send_keys('pass123') #enter your insta acc 
#note no two factor authentication is on when automation goes create another insta acc
sleep(1)
driver.find_element_by_xpath("//button[@type='submit']").click()
sleep(3)
driver.get("https://www.instagram.com/p/CiRXFqzvOi-/?utm_source=ig_web_copy_link") #replace with your needed post url
sleep(2)
driver.find_element(By.XPATH,'//*[@class ="_aao9"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aao9"]//textarea').send_keys("amazing") #change text to your required and do in below also
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aao9"]//button[@type="submit"]').click()

sleep(7)

driver.find_element(By.XPATH,'//*[@class ="_aao9"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aao9"]//textarea').send_keys("progress")
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aao9"]//button[@type="submit"]').click()

sleep(7)

driver.find_element(By.XPATH,'//*[@class ="_aao9"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aao9"]//textarea').send_keys("trying to new idea")
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aao9"]//button[@type="submit"]').click()

sleep(7)

driver.find_element(By.XPATH,'//*[@class ="_aao9"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aao9"]//textarea').send_keys("amazing")
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aao9"]//button[@type="submit"]').click()

sleep(8)

driver.find_element(By.XPATH,'//*[@class ="_aao9"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aao9"]//textarea').send_keys("fabulous")
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aao9"]//button[@type="submit"]').click()

sleep(8)

driver.find_element(By.XPATH,'//*[@class ="_aao9"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aao9"]//textarea').send_keys("superb")
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aao9"]//button[@type="submit"]').click()

sleep(8)

driver.find_element(By.XPATH,'//*[@class ="_aao9"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aao9"]//textarea').send_keys("excellent")
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aao9"]//button[@type="submit"]').click()

sleep(8)

driver.find_element(By.XPATH,'//*[@class ="_aao9"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aao9"]//textarea').send_keys("marvelous")
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aao9"]//button[@type="submit"]').click()

sleep(8)

driver.find_element(By.XPATH,'//*[@class ="_aao9"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aao9"]//textarea').send_keys("awesome")
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aao9"]//button[@type="submit"]').click()

sleep(7)

driver.find_element(By.XPATH,'//*[@class ="_aao9"]//textarea').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aao9"]//textarea').send_keys("excellent")
sleep(1)
driver.find_element(By.XPATH,'//*[@class ="_aao9"]//button[@type="submit"]').click()

sleep(30)




