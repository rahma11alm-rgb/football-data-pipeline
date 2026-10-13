import os
import json
import requests
from dotenv import load_dotenv

# 1) نقرأ التوكن من ملف .env
load_dotenv()
token = os.getenv("FOOTBALL_API_TOKEN")

# 2) نجهز الطلب: PL = الدوري الإنجليزي
url = "https://api.football-data.org/v4/competitions/PL/matches"
headers = {"X-Auth-Token": token}

# 3) نرسل الطلب
response = requests.get(url, headers=headers)
print("Status code:", response.status_code)

# 4) نحفظ النتيجة كما هي (raw)
if response.status_code == 200:
    data = response.json()
    os.makedirs("data/raw", exist_ok=True)
    with open("data/raw/pl_matches.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Matches saved:", len(data["matches"]))
else:
    print("Error:", response.text)