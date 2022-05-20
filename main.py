import requests
from time import sleep
from colorama import Fore
import os
from requests_html import HTML, HTMLSession

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
shirtlink = input("Shirt That You Would Like To Bot (LINK): ")
yourcookie = input("Your cookie that you would like to buy the shirt with")

### Getting The Shit About Price And Stuff ###
session = HTMLSession()
r = session.get(f"{shirtlink}")
r1 = r.html.find("#item-container")[0].attrs
id = r1.get("data-product-id")
item_id = r1.get("data-item-id")
info = requests.get(f"https://api.roblox.com/marketplace/productinfo?assetId={item_id}").json()
creator_id = info["Creator"].get("Id")
amount = info["PriceInRobux"]
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

### Buying loop ###
while True:
    sleep(1)
    link = f"https://economy.roblox.com/v1/purchases/products/{id}"
    buy = requests.post(link, cookies=cookie, headers=header, json={"expectedCurrency": "1", "expectedPrice": f"{amount}", "expectedSellerId": f"{creator_id}"})
    delete = requests.post("https://www.roblox.com/asset/delete-from-inventory", cookies=cookie, headers=header, json={"assetId": f"{item_id}"})
    if buy.status_code==200 and delete.status_code==200:
        print(Fore.GREEN + f"Shirt Bought | Status Code: {buy.status_code}")
    else:
        print(buy.json())
        print(Fore.GREEN + f"Something Went Wrong| Status Code: {buy.status_code}")
        

