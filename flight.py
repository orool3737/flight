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
from cralwer_flight import exract_flight

now = datetime.datetime.today()
print(now)

delta = 4 - now.weekday()
if delta <= 0:
    delta = 11 - now.weekday()

friday = [0, 0, 0, 0]
friday[0] = now
friday[1] = friday[0] + datetime.timedelta(days=delta)
friday[2] = friday[1] + datetime.timedelta(days=7)
friday[3] = friday[2] + datetime.timedelta(days=7)

print(friday[1].day)
print(friday[2].day)
print(friday[3].day)

friday_month = [0, 0, 0, 0]

j = 0
while j<3:
    if friday[0].month != friday[j+1].month:
       friday_month[j+1] = 1
    else:
       friday_month[j+1] = 0
    j = j+1

print(friday_month[1])
print(friday_month[2])
print(friday_month[3])

frist_content = exract_flight(friday[1].day, friday_month[1])
second_content = exract_flight(friday[2].day, friday_month[2])
third_content = exract_flight(friday[3].day, friday_month[3])

print(frist_content)
print(second_content)
print(third_content)

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
