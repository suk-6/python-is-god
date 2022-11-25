# Developed by Woosuk

import time
import openpyxl
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://www.realtyprice.kr:447/notice/town/searchOpinion.htm")

elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="sido"]/option[9]')))
driver.find_element_by_xpath('//*[@id="sido"]/option[9]').click()

elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="sigungu"]/option[34]')))
driver.find_element_by_xpath('//*[@id="sigungu"]/option[34]').click()


elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="initialword"]/option[5]')))
driver.find_element_by_xpath('//*[@id="initialword"]/option[5]').click()


elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="road"]/option[61]')))
driver.find_element_by_xpath('//*[@id="road"]/option[61]').click()


elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="apt"]/option[3]')))
driver.find_element_by_xpath('//*[@id="apt"]/option[3]').click()

elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="dong"]/option[1]')))

dongval = 2
dong1 = '#dong > option:nth-child(' + str(dongval) + ')'
time.sleep(0.5)
driver.find_element_by_css_selector(dong1).click()

hoval = 1
date = []
name = []
ddong = []
hho = []
ssize = []
price = []

while hoval <= 87:
    time.sleep(0.5)

    ho1 = '#ho > option:nth-child(' + str(hoval) + ')'
    elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ho1)))
    ho2 = driver.find_element_by_css_selector(ho1)
    ho2.click()

    driver.find_element_by_id("btn_search").click()

    elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="dataList"]/tr[1]')))
    f = driver.find_elements_by_xpath('//*[@id="dataList"]/tr[1]')[0]
    f_data = f.text
    d = f.text.split(' ')
    print(d)
    hoval = hoval + 1

    date.append(d[0])
    name.append(d[1])
    ddong.append(d[2])
    hho.append(d[3])
    ssize.append(d[4])
    price.append(d[5])

df = pd.DataFrame(
    {
        '날짜': date,
        '이름': name,
        '동': ddong,
        '호': hho,
        '평': ssize,
        '가격': price
    }
)

df.to_excel(f'{d[2]}.xlsx')

print("done!")

driver.quit()