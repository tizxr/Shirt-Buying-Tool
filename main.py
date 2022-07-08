import requests
from time import sleep
from colorama import Fore
import random
import os
import threading



os.system("cls")
print(Fore.RED + """

███╗░░░███╗░█████╗░░██████╗░██████╗██████╗░██╗░░░██╗██╗░░░██╗
████╗░████║██╔══██╗██╔════╝██╔════╝██╔══██╗██║░░░██║╚██╗░██╔╝
██╔████╔██║███████║╚█████╗░╚█████╗░██████╦╝██║░░░██║░╚████╔╝░
██║╚██╔╝██║██╔══██║░╚═══██╗░╚═══██╗██╔══██╗██║░░░██║░░╚██╔╝░░
██║░╚═╝░██║██║░░██║██████╔╝██████╔╝██████╦╝╚██████╔╝░░░██║░░░
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═════╝░╚═════╝░╚═════╝░░╚═════╝░░░░╚═╝░░░

Made by tizxr#3313 | Free Version.
    """)
print(Fore.RESET)
yourcookie = input("Your cookie that you would like to buy the shirt with: ")

shirtlink = input("Shirt That You Would Like To Bot (ID OF THE): ")



info = requests.get(f"https://api.roblox.com/marketplace/productinfo?assetId={shirtlink}").json()
creator_id = info["Creator"].get("Id")
amount = info["PriceInRobux"]
id = info["ProductId"]
###

### Getting YOUR robux and stuff ###
cookie = {".ROBLOSECURITY": yourcookie}
check = requests.get("https://users.roblox.com/v1/users/authenticated", cookies=cookie)
if check.status_code==200:
    token = requests.post('https://auth.roblox.com/v2/logout', cookies=cookie).headers["x-csrf-token"]
    header = {'x-csrf-token': token, 'content-type': 'application/json'}
    your_robux = requests.get("https://api.roblox.com/currency/balance", cookies=cookie, headers=header).json()["robux"]
else:
    print(Fore.GREEN + "The Cookie You Entered Was Wrong, Please Retry By Reopening The Program!")
    print(Fore.RESET)
    while True:
        sleep(1)

def token():
    cookie = {".ROBLOSECURITY": yourcookie}
    check = requests.get("https://users.roblox.com/v1/users/authenticated", cookies=cookie)
    if check.status_code==200:
        token = requests.post('https://auth.roblox.com/v2/logout', cookies=cookie).headers["x-csrf-token"]
        return token
    else:
        return False

### Buying loop ###

loop = True
while loop:
    link = f"https://economy.roblox.com/v1/purchases/products/{id}"
    buy = requests.post(link, cookies=cookie, headers=header, json={"expectedCurrency": "1", "expectedPrice": f"{amount}", "expectedSellerId": f"{creator_id}"})
    delete = requests.post("https://www.roblox.com/asset/delete-from-inventory", cookies=cookie, headers=header, json={"assetId": f"{id}"})
    if buy.status_code==200 and delete.status_code==200:
        print(Fore.GREEN + f"Shirt Bought | Status Code: 200")
    elif buy.status_code==401:
        loop = False
        print("Wrong Cookie")
    elif buy.status_code==403:
        x = token()
        if x==False:
            print("Wrong Cookie")
        else:
            header = {'x-csrf-token': str(token()), 'content-type': 'application/json'}
            loop = True
    elif buy.status_code==429:
        loop = False
        print("Sleeping  5 secs, somehow meant to stop ratelimiteds")
        sleep(5)
        loop = True
    else:
        pass
