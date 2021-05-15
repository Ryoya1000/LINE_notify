import requests
import os
import schedule
import time

def job():
   url = "https://notify-api.line.me/api/notify"
   access_token = os.environ["LINE_NOTIFY_ACCESS_TOKEN"]
   headers = {'Authorization': 'Bearer ' + access_token}
   message = "テストだよ！！！！！！！！！！"
   params = {'message': message, 'stickerId': 1, 'stickerPackageId': 1}
   r = requests.post(url, headers=headers, params=params,)
# schedule.every(2).minutes.do(job)

# while True:
#   schedule.run_pending()
#   time.sleep(1)

job()
