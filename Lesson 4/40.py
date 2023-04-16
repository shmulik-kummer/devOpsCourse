from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("file:///home/kummer/Documents/DevOps Course/tip_calc/index.html")
billamt = driver.find_element(by="id", value="billamt")
billamt.send_keys(200)
s = driver.find_element(by="xpath", value="//*[@id=\"serviceQual\"]/option[5]")
s.click()
music = driver.find_element(by="id", value="music")
peopleamt = driver.find_element(by="id", value="peopleamt")
peopleamt.send_keys("4")
music.send_keys("5")
driver.find_element(by="id", value="calculate").click()
expected = "21.25"
actual = driver.find_element(by="id", value="tip").text
print(actual)
assert expected == actual
sleep(2)
driver.close()
