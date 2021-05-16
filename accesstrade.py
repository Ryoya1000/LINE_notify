
import time
import requests
import os
import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# LINE NOTIFY
def job(msg):
   url = "https://notify-api.line.me/api/notify"
   access_token = os.environ["LINE_NOTIFY_BLOG"]
   headers = {'Authorization': 'Bearer ' + access_token}
   message = msg
   params = {'message': message}
   r = requests.post(url, headers=headers, params=params,)


# # # chromedriverの設定
op = Options()
# # --headlessだけではOSによって動かない、プロキシが弾かれる、
# # CUI用の省略されたHTMLが帰ってくるなどの障害が出ます。
# # 長いですが、これら6行あって最強かつどんな環境でも動きますので、必ず抜かさないようにしてください。
op.add_argument("--disable-gpu")
op.add_argument("--disable-extensions")
op.add_argument("--proxy-server='direct://'")
op.add_argument("--proxy-bypass-list=*")
op.add_argument("--start-maximized")
op.add_argument("--headless")

browser = webdriver.Chrome(options=op)
# browser = webdriver.Chrome()

browser.get('https://www.accesstrade.ne.jp/#_ga=2.183676006.1981910440.1620909719-113966242.1593177757')

# ユーザーID入力
elem_username = browser.find_element_by_name('userId')
username = os.environ["USERNAME_BLOG"]
elem_username.send_keys(username)

# パスワード入力
elem_password = browser.find_element_by_name('userPass')
password = os.environ["PASSWORD_BLOG"]
elem_password.send_keys(password)

# ログイン押下
elem_password.submit()

# ログイン時に多少時間がかかるため５秒待機する
time.sleep(5)

# 金額抽出
elems_td = browser.find_elements_by_tag_name('td')
elems_th = browser.find_elements_by_tag_name('th')

keys = []
for th in elems_th:
    if th.text != "":
        keys.append(th.text)

val = []
for td in elems_td:
    if td.text != "":
        val.append(td.text)

hassei = val[5]
kakutei = val[9]

dt_now = datetime.datetime.now()
year = dt_now.year
month = dt_now.month

msg = "\n{}年{}月\nアクトレ収益報告\n発生金額={}\n確定金額={}".format(year, month, hassei, kakutei)
job(msg)

browser.quit()
