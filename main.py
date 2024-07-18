import requests # type: ignore
import brotli
import math
import random
import time
import Log1
print('----------DEJENDOG----------')
print('By LawBNgo | https://t.me/Genloginchannels')
user_input_Hit = str(input('Do you want to HIT? (y or n): ' ))
user_input_updrage = str(input('Do you wan to updrage (y or n): '))

def send_request(url, headers, payload = {}, method = 'GET', params=None, proxy=None):
    try:
        if method == 'GET':
            response = requests.get(url, headers=headers, params=params, proxies=proxy)
        elif method == 'POST':
            response = requests.post(url, headers=headers, json=payload, proxies=proxy)
        elif method == 'PUT':
            response = requests.post(url, headers=headers, json=payload, proxies=proxy)
        else:
            raise ValueError("Unsupported HTTP method")

        if response.status_code == 200:
            return response.json()
        else:
            return response.text
    except Exception as e:
        print(f"Error during request: {e}")
        return None
try:
    def main():    
        allinitdatas = []
        try: 
            with open("initdata.txt", "r") as file: 
                for initdatas in file: 
                    allinitdatas.append(initdatas)
        except:
            print("file iframe lỗi rồi!")
        for initdatas in allinitdatas:
            initdatas_n= initdatas.rstrip('\n')
            url_login = f'https://api.djdog.io/telegram/login?{initdatas_n}'
            headers_login = {
                'Accept':'application/json, text/plain, */*',
                'Accept-Encoding':'gzip, deflate, br, zstd',
                'Accept-Language':'en-GB,en-US;q=0.9,en;q=0.8',
                'Origin':'https://djdog.io',
                'Priority':'u=1, i',
                'Sec-Ch-Ua':'"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                'Sec-Ch-Ua-Mobile':'?1',
                'Sec-Ch-Ua-Platform':"Android",
                'Sec-Fetch-Dest':'empty',
                'Sec-Fetch-Mode':'cors',
                'Sec-Fetch-Site':'same-site',
                'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36',
                'Initdata':f'{initdatas_n}',
                }
            login = send_request(url_login, headers_login, payload={}, method='POST')
            time.sleep(3)
            athorization_get = login['data']['accessToken'] 
            url_getinfo = 'https://api.djdog.io/pet/barAmount'
            headers = {
                'Accept':'application/json, text/plain, */*',
                'Accept-Encoding':'gzip, deflate, br, zstd',
                'Accept-Language':'en-GB,en-US;q=0.9,en;q=0.8',
                'Authorization':f'{athorization_get}',
                'Origin':'https://djdog.io',
                'Priority':'u=1, i',
                'Sec-Ch-Ua':'"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                'Sec-Ch-Ua-Mobile':'?1',
                'Sec-Ch-Ua-Platform':"Android",
                'Sec-Fetch-Dest':'empty',
                'Sec-Fetch-Mode':'cors',
                'Sec-Fetch-Site':'same-site',
                'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36',
                }
            if user_input_Hit == 'y':
                url_update = 'https://api.djdog.io/pet/levelUp/0'
                time.sleep(4)
                data_username = login['data']["telegramUsername"]
                print(f'Username: {data_username}')
                while True:
                    get_info = send_request(url_getinfo, headers, params={}, method='GET')
                    random_number = str(random.randint(8, 50))
                    availableAmount = int(get_info["data"]["availableAmount"])
                    url_click = f'https://api.djdog.io/pet/collect?clicks={random_number}'
                    Claim = send_request(url_click, headers, payload={}, method='POST')
                    time.sleep(10)
                    try:
                        Ketqua_hit = Claim["data"]['amount']
                        time.sleep(10)
                        aaa = int(availableAmount)
                        if aaa <= 10:
                            print('-Clicked-')
                            break
                        print(f'{Ketqua_hit} Clicked')
                        time.sleep(3)
                    except Exception as e:
                        Ketqua_hit = Claim["returnDesc"]
                        print(Ketqua_hit)
            if user_input_updrage == 'y':
                while True:
                    update = send_request(url_update, headers, payload={}, method='POST')
                    time.sleep(3)
                    get_info = send_request(url_getinfo, headers, params={}, method='GET')
                    time.sleep(3)
                    level_hientai = get_info["data"]["level"]
                    if update == {'returnCode': 400, 'returnDesc': 'Insufficient balance', 'data': None}:
                        break
                ketqua_level = f'Level UP: {level_hientai}'
                print(ketqua_level)
    Log1.chuyeniframesanginitdata()
    while True:
        if __name__ == "__main__":
            main()
finally:
    with open('initdata.txt', 'w') as file:
         pass