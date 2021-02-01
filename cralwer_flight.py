from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os
import time
import datetime
import requests
from bs4 import BeautifulSoup
import telegram
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def exract_flight(flight_day, flight_month):
   url='https://flight.naver.com/flights/'

   options = webdriver.ChromeOptions()
   options.add_argument('headless')    # 웹 브라우저를 띄우지 않는 headlss chrome 옵션 적용
   options.add_argument('disable-gpu')    # GPU 사용 안함
   chrome_driver = os.path.join('chromedriver')
   driver = webdriver.Chrome(chrome_driver, options=options)
  
   driver.get(url)
   time.sleep(1)

   #편도 버튼 클릭
   driver.find_element_by_link_text("편도").click()

   #출발지 버튼 클릭
   driver.find_element_by_link_text("인천").click()
   driver.find_element_by_link_text("김해/부산").click()
  
   #도착 버튼 클릭
   driver.find_element_by_link_text("도착").click()
   driver.find_element_by_link_text("김포").click()

   #가는날 선택 버튼 클릭
   driver.find_element_by_link_text("가는날 선택").click()

   # [0]은 이번달 [1]은 다음달
   driver.find_elements_by_link_text(flight_day)[flight_month].click()

   #항공권 검색 클릭
   driver.find_element_by_link_text("항공권 검색").click()
   
   #driver.implicitly_wait(180)
   WebDriverWait(driver, 180).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))

   # 스크롤 가장 아래로 내리기
   interval = 2
   prev_height = driver.execute_script("return document.body.scrollHeight")

   while True:
       driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
       time.sleep(interval)
       current_height = driver.execute_script("return document.body.scrollHeight")
       if current_height == prev_height:
           break

       prev_height = current_height

   print("스크롤 내리기 완료")

   req = driver.page_source
   soup = BeautifulSoup(req, 'html.parser')
   company = soup.select("span.h_tit_result.ng-binding")
   department_time = soup.select("dd.txt_time.ng-binding")
   department = soup.select("dd.txt_code.ng-binding")
   price = soup.select("span.txt_pay.ng-binding")

   print(price[0].text.replace(',', ''))

   content = []
   i=0
   while soup:
       try:
           department_hour = datetime.datetime.strptime(department_time[3*i].text, '%H:%M').hour
           if department_hour >= 18 and department_hour < 19 :
              content.append(company[i].text + " " + department_time[3*i].text + " ￦" + price[i].text)
           i = i + 1
       except IndexError:
           break
   return content

# and int(price[i].replace(',', '')) < 50000
