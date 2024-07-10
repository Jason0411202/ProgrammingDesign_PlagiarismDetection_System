import os
from dotenv import load_dotenv

load_dotenv()
JUDGER_USERNAME = os.getenv('JUDGER_USERNAME')
JUDGER_PASSWORD = os.getenv('JUDGER_PASSWORD')
JUDGEHOST = os.getenv('JUDGEHOST')
MOSS_ID = os.getenv('MOSS_ID')
CONTEST_ID = os.getenv('CONTEST_ID')
