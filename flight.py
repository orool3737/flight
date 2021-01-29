from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os
import time
import datetime
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import telegram
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
driver.find_elements_by_link_text("30")[0].click()

#항공권 검색 클릭
driver.find_element_by_link_text("항공권 검색").click()

WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))

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

print("프린트 완료")

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')
company = soup.select("span.h_tit_result.ng-binding")
department_time = soup.select("dd.txt_time.ng-binding")
department = soup.select("dd.txt_code.ng-binding")
price = soup.select("span.txt_pay.ng-binding")

print(datetime.datetime.strptime("18:00", '%H:%M'))

'''
i=0
while soup:
    try:
        print(company[i].text, department[i].text, department_time[3*i].text, price[i].text)
        i = i + 1
    except IndexError:
        break
'''
'''
elem = WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul")))
#-> elem는 웹드라이버를 통해 브라우져에서 최대 10초를 기다려주고 xpath 기준으로 값에 해당하는 elem가 나올때까지 기다려줘.
elem_text = elem.text
print(elem_text)
'''

'''
s_id = "orool3737"
s_pwd = "159632qwe!"

login_id = driver.find_element_by_name('user_id')
login_id.send_keys(s_id)
login_pw = driver.find_element_by_name('password')
login_pw.send_keys(s_pwd)
login_pw.send_keys(Keys.RETURN)
time.sleep(1)

s_keyword = "\b\b\b\b\b햇빛가리게"

keyword = driver.find_element_by_name('keyword')
keyword.send_keys(s_keyword)
keyword.send_keys(Keys.RETURN)

req = driver.page_source
soup=BeautifulSoup(req, 'html.parser')
information_list = soup.select("span.date")
latest = information_list[0].text

bot = telegram.Bot(token='1302211155:AAHJNLLFl8b-d3c2MLa-5igT038s-d2MUj4')
chat_id = 1491027495 #bot.getUpdates()[-1].message.chat.id

github_token_g = os.environ['github_token']
repo_name = 'GG'
repo = Github(github_token_g).get_user().get_repo(repo_name)
res = repo.create_issue(title=issue_title, body=latest)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, 'latest.txt'), 'r+') as f_read:
    before = f_read.readline()
    if before != latest:
        bot.sendMessage(chat_id=chat_id, text='새 글이 올라왔어요!')
    else:
        bot.sendMessage(chat_id=chat_id, text='새 글이 없어요 ㅠㅠ')
    f_read.close()

with open(os.path.join(BASE_DIR, 'latest.txt'), 'w+') as f_write:
    f_write.write(latest)
'''
