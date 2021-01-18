from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import requests
from bs4 import BeautifulSoup
import os
import telegram

url = "http://www.slrclub.com/"

options = webdriver.ChromeOptions()
options.add_argument('headless')    # 웹 브라우저를 띄우지 않는 headlss chrome 옵션 적용
options.add_argument('disable-gpu')    # GPU 사용 안함
driver = webdriver.Chrome("./chromedriver", options=options)

driver.get(url)
time.sleep(1)

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