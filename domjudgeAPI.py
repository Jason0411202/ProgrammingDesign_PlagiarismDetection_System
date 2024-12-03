import base64
import os
import requests
from config import JUDGER_USERNAME, JUDGER_PASSWORD, JUDGEHOST, CONTEST_ID

# 回傳一個 dict, key 代表 submission_id, value 代表這個 submission_id 的評測狀態
def Getjudgement_type():
    # 取得提交的評測狀態
    base_url = JUDGEHOST + 'api/v4/contests/' + CONTEST_ID + '/judgements/'
    print(base_url)

    auth = (JUDGER_USERNAME, JUDGER_PASSWORD) # 設定認證帳密
    response = requests.get(base_url, auth=auth) # 發送 GET 請求

    if response.status_code == 200: # 若請求成功
        jsonResponse = response.json()
        returnDict = {}
        for i in range(len(jsonResponse)): # 遍歷所有評測
            returnDict[jsonResponse[i]['submission_id']] = jsonResponse[i]['judgement_type_id']
        
        #print(returnDict)
        return returnDict
    else:
        print(f'Error: Unable to fetch submission, status code: {response.status_code}')
        return None

# 回傳一個嵌套的 dict, dict[problem_id][team_id] = 最新一筆的 submission_id
def GetNewestSubmissionID():
    # 取得提交的評測狀態
    # 回傳資料由舊到新排序
    base_url = JUDGEHOST + 'api/v4/contests/' + CONTEST_ID + '/submissions' # 取得所有提交
    print(base_url)

    auth = (JUDGER_USERNAME, JUDGER_PASSWORD) # 設定認證帳密
    response = requests.get(base_url, auth=auth) # 發送 GET 請求

    if response.status_code == 200: # 若請求成功
        jsonResponse = response.json()
        judgeDict = Getjudgement_type()
        returnDict = {}
        for i in range(len(jsonResponse)): # 由舊到新的遍歷提交
            try:
                if judgeDict[jsonResponse[i]['id']] == 'AC':
                    if jsonResponse[i]['problem_id'] not in returnDict: # 若 returnDict 中沒有這個 problem_id，則創建之
                        returnDict[jsonResponse[i]['problem_id']] = {}
                    if len(jsonResponse[i]['team_id'])==9: # 為了過濾掉非學生的提交
                        returnDict[jsonResponse[i]['problem_id']][jsonResponse[i]['team_id']]=jsonResponse[i]['id'] # 更新 returnDict
            except:
                continue

        #print(returnDict)
        return returnDict # 為一個嵌套的 dict
    else:
        print(f'Error: Unable to fetch submissions, status code: {response.status_code}')
        return None

def GetProblemInfo():
    # 取得題目資訊
    base_url = JUDGEHOST + 'api/v4/contests/' + CONTEST_ID + '/problems'
    print(base_url)

    auth = (JUDGER_USERNAME, JUDGER_PASSWORD) # 設定認證帳密
    response = requests.get(base_url, auth=auth) # 發送 GET 請求

    if response.status_code == 200: # 若請求成功
        jsonResponse = response.json()
        returnDict = {}
        for i in range(len(jsonResponse)): # 遍歷所有題目
            returnDict[jsonResponse[i]['id']] = jsonResponse[i]['name']
        
        return returnDict
    else:
        print(f'Error: Unable to fetch problem info, status code: {response.status_code}')
        return None

# 回傳 contest id 跟 contest name 的對應關係 dict
def GetContestInfo():
    # 取得比賽資訊
    base_url = JUDGEHOST + 'api/v4/contests'
    print(base_url)

    auth = (JUDGER_USERNAME, JUDGER_PASSWORD) # 設定認證帳密
    response = requests.get(base_url, auth=auth) # 發送 GET 請求

    if response.status_code == 200: # 若請求成功
        jsonResponse = response.json()
        returnDict = {}
        for i in range(len(jsonResponse)): # 遍歷所有比賽
            returnDict[jsonResponse[i]['id']] = jsonResponse[i]['name']
        
        return returnDict
    else:
        print(f'Error: Unable to fetch contest info, status code: {response.status_code}')
        return None

def UpdateStudentCode():
    newestSubmissionID=GetNewestSubmissionID() # 取得最新的提交
    contestInfo=GetContestInfo()
    problemInfo=GetProblemInfo()

    for problem_id in newestSubmissionID: # 遍歷所有 problem_id
         for team_id in newestSubmissionID[problem_id]: # 遍歷所有 team_id
            base_url = JUDGEHOST + 'api/v4/contests/' + CONTEST_ID + '/submissions/' + newestSubmissionID[problem_id][team_id] + '/source-code' # 取得提交的程式碼
            auth = (JUDGER_USERNAME, JUDGER_PASSWORD) # 設定認證帳密
            response = requests.get(base_url, auth=auth) # 發送 GET 請求

            if response.status_code == 200: # 若請求成功
                jsonResponse = response.json()
                source_base64 = jsonResponse[0]['source'] # 回傳的 source-code 為base-64 編碼的程式碼
                encodings_to_try = ['utf-8', 'big5', 'gbk', 'latin-1'] # 嘗試解碼的編碼
                sourse_code = ""
                for encoding in encodings_to_try: # 嘗試解碼
                    try:
                        sourse_code = base64.b64decode(source_base64).decode(encoding) # 解碼

                        # 若目錄不存在，則創建之
                        if not os.path.exists(f'./code/[{CONTEST_ID}] {contestInfo[CONTEST_ID]}/[{problem_id}] {problemInfo[problem_id]}'):
                            os.makedirs(f'./code/[{CONTEST_ID}] {contestInfo[CONTEST_ID]}/[{problem_id}] {problemInfo[problem_id]}')

                        # 寫檔
                        with open(f'./code/[{CONTEST_ID}] {contestInfo[CONTEST_ID]}/[{problem_id}] {problemInfo[problem_id]}/[{newestSubmissionID[problem_id][team_id]}] {team_id}.c', 'w', encoding=encoding) as f:
                            f.write(sourse_code)
                        break
                    except Exception as e:
                        continue

            else:
                print(f'Error: Unable to fetch source code, status code: {response.status_code}')
                return None
    print("Update Student Code Success!")