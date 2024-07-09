# 環境配置與執行方式
1. 在專案目錄下新增 .env 檔案
```
JUDGEHOST=<domjudge base 網址>
JUDGER_USERNAME=<使用者名稱>
JUDGER_PASSWORD=<使用者密碼>
CONTEST_ID=<想追蹤的比賽 ID>
```
2. 執行 `main.py`

## 專案重要檔案介紹
### `code 資料夾`
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

### `.env`
* 設置本專案會用到的重要環境變數

範例:
```
JUDGEHOST=<domjudge base 網址>
JUDGER_USERNAME=<使用者名稱>
JUDGER_PASSWORD=<使用者密碼>
CONTEST_ID=<想追蹤的比賽 ID>
```

### `config.py`
* 用來載入環境變數的 python 檔案

### `domjudge.py`
* 負責取得 Domjudge 上的學生程式碼，並存至本地的 code 資料夾中

### `main.py`
* 本專案的主程式
