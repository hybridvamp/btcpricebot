import requests

import time

token = " #bot token "                 # made by @plugin posted on codeleak by @plugin

chat_id = "-1001567729793"

time_sleep = 5

def send():

    while True:

        urlt = "https://soud.me/api/Crypto"

        reqt = requests.get(urlt).json()

        btc_usdt = str(reqt['info']['BTC']['USD'])

        at = (btc_usdt.split(".", 1))

        time.sleep(2)

        url = "https://soud.me/api/Crypto"

        req = requests.get(url).json()

        btc_usd = str(req['info']['BTC']['USD'])

        a = (btc_usd.split(".", 1))

        if a > at:

            msg = f"Btc: ${a[0]} ↗️ "

            url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={msg}"

            requests.get(url)

            time.sleep(time_sleep)

        elif a < at:

            msg = f"Btc: ${a[0]} ↙️"

            url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={msg}"

            requests.get(url)

            time.sleep(time_sleep)

send()

ime

token = " #bot token "                 # made by @plugin posted on codeleak by @plugin

chat_id = "-1001567729793"

time_sleep = 5

def send():

    while True:

        urlt = "https://soud.me/api/Crypto"

        reqt = requests.get(urlt).json()

        btc_usdt = str(reqt['info']['BTC']['USD'])

        at = (btc_usdt.split(".", 1))

        time.sleep(2)

        url = "https://soud.me/api/Crypto"

        req = requests.get(url).json()

        btc_usd = str(req['info']['BTC']['USD'])

        a = (btc_usd.split(".", 1))

        if a > at:

            msg = f"Btc: ${a[0]} ↗️ "

            url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={msg}"

            requests.get(url)

            time.sleep(time_sleep)

        elif a < at:

            msg = f"Btc: ${a[0]} ↙️"

            url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={msg}"

            requests.get(url)

            time.sleep(
