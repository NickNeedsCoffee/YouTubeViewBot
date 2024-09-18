
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

URL = str(input('Enter the video URL >> '))
DRIVERS = int(input('Number of Drivers(Windows) >>'))
driver = []
BreakRate = 10 #sec
RefRate = 11.0 #sec
cService = webdriver.ChromeService(executable_path='C:\Program Files (x86)\ChromeDriver\chromedriver.exe')

for i in range(DRIVERS):
    driver.append(webdriver.Chrome(service = cService))
    driver[i].get(URL)
    action = ActionChains(driver[i])
    action.send_keys(Keys.SPACE)
    action.perform()

while True:
    time.sleep(RefRate)
    for j in range(DRIVERS):
        driver[j].refresh()
        action = ActionChains(driver[j])
        action.send_keys(Keys.SPACE)
        action.perform()