# 環境配置與執行方式
1. 在專案目錄下新增 .env 檔案
```
JUDGEHOST=<domjudge base 網址>
JUDGER_USERNAME=<使用者名稱>
JUDGER_PASSWORD=<使用者密碼>
MOSS_ID=<申請的 Moss ID>
CONTEST_ID=<想追蹤的比賽 ID>
```
2. 根據 requirements.txt 安裝所需套件
```
pip install -r requirements.txt
```
2. 執行 `main.py` 即可

## 專案重要檔案與資料夾介紹
### `code 資料夾` (程式執行後生成)
* 從 Domjudge 中取得的學生程式碼將會存放於此

file tree:
```
code
├── [contestID] contestName
│   └── [problemID] problemName
│       ├── [submisstionID] teamName.c
│       └── [submisstionID] teamName.c
│
└── [contestID] contestName
    └── [problemID] problemName
        ├── [submisstionID] teamName.c
        ├── [submisstionID] teamName.c
        └── [submisstionID] teamName.c
 
```

### `report 資料夾` (程式執行後生成)
* 比對結果將會存放於此

file tree:
```
report
└── code
       ├── [contestID] contestName
       │   └── [problemID] problemName
       │       ├── reportLocal.html
       │       └── reportURL.url
       │
       └── [contestID] contestName
           └── [problemID] problemName
               ├── reportLocal.html
               └── reportURL.url
```

### `.env`
* 設置本專案會用到的重要環境變數

範例:
```
JUDGEHOST=<domjudge base 網址>
JUDGER_USERNAME=<使用者名稱>
JUDGER_PASSWORD=<使用者密碼>
MOSS_ID=<申請的 Moss ID>
CONTEST_ID=<想追蹤的比賽 ID>
```

### `config.py`
* 用來載入環境變數的 python 檔案

### `domjudge.py`
* 負責取得 Domjudge 上的學生程式碼，並存至本地的 code 資料夾中

### `moss.py`
* 負責將學生程式碼上傳至 Moss 並取得比對結果

### `main.py`
* 本專案的主程式
