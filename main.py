import os
import requests
from dotenv import load_dotenv

load_dotenv()

# 設定 API URL 和憑證
base_url = 'http://140.123.105.184:8080/api/contests/3/judgements' # 取得提交的評測狀態
# base_url = 'http://140.123.105.184:8080/api/contests/3/submissions' # 取得所有提交


# 設定認證（例如使用 Basic 認證）
auth = (os.getenv('JUDGER_USERNAME'), os.getenv('JUDGER_PASSWORD'))

# 發送 GET 請求來獲取提交紀錄
response = requests.get(base_url, auth=auth)

# 確認請求是否成功
if response.status_code == 200:
    print(response.json())
else:
    print(f'Error: Unable to fetch submissions, status code: {response.status_code}')
