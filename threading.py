import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

import time
import threading

URL = 'https://zep.us/play/yaxGbJ'

options = webdriver.ChromeOptions()

options.add_argument("headless")

def bot_add(number):
    driver = webdriver.Chrome(executable_path='./chromedriver', options=options)

    driver.get(url=URL)

    wait = WebDriverWait(driver, 60)
    element = wait.until(EC.presence_of_element_located((By.XPATH, r'//*[@id="InitialSettingsModal"]/div/div/form/div[1]/div/div/div/input')))

    time.sleep(1)

    name_box = driver.find_element(By.XPATH, r'//*[@id="InitialSettingsModal"]/div/div/form/div[1]/div/div/div/input')

    name_box.send_keys(f'bot{number}')
    name_box.send_keys(Keys.RETURN)

    print(f'bot{number}')

    time.sleep(20)

    driver.close()

if __name__ == '__main__':
    start = time.perf_counter()
    threads = []
    for i in range(10):
        t = threading.Thread(target=bot_add, args=(i,))
        t.start()
        threads.append(t)
        
    for thread in threads:
        thread.join()
    finish = time.perf_counter()
 
    print(f'Finished in {round(finish-start, 2)} second(s)')
