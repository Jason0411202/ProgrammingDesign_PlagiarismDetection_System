import os
import mosspy
from config import MOSS_ID, CONTEST_ID
from domjudgeAPI import GetContestInfo

def Moss():
    contestInfo=GetContestInfo() # 取得比賽資訊 (生成 dir 時會用到)

    m = mosspy.Moss(MOSS_ID, "python") # 初始化 Moss

    baseDir='./code' # 設定學生程式碼所在的 base 目錄
    contestDir=baseDir+f'/[{CONTEST_ID}] {contestInfo[CONTEST_ID]}'  # base 目錄的下一層目錄為比賽名稱
    allProblemDirName = [name for name in os.listdir(contestDir)] # 取得 contestDir 下的所有目錄名稱
    for problemDirName in allProblemDirName: # 遍歷contestDir 下的所有目錄名稱
        allCodeDirName = [name for name in os.listdir(f'{contestDir}/{problemDirName}')] # 取得 problemDirName 下的所有目錄名稱
        for codeDirName in allCodeDirName: # 遍歷 problemDirName 下的所有目錄名稱
            finalDir = f'{contestDir}/{problemDirName}/{codeDirName}' # 設定 finalDir，也就是學生程式碼所在的目錄
            m.addFile(finalDir) # 將 finalDir 加入 Moss

        url = m.send() # 發送 Moss 請求
        print("Report URL: " + url) # 輸出 Moss 網址
        # 將這個 Moss 網址儲存成一個網頁
        shortcut_content = "[InternetShortcut]\nURL=" + url

        if not os.path.exists(f"report/{contestDir}/{problemDirName}"): # 如果 report/{contestDir}/{problemDirName} 不存在，則創建之
            os.makedirs(f"report/{contestDir}/{problemDirName}")

        with open(f"report/{contestDir}/{problemDirName}/reportURL.url", "w") as f: # 把 url 存起來
            f.write(shortcut_content)
        m.saveWebPage(url, f"report/{contestDir}/{problemDirName}/reportLocal.html") # 儲存 Moss 網頁
        # mosspy.download_report(url, f"report/{contestDir}/{problemDirName}/", connections=8) # 如果需要完整保存報告至本地的話使用這行