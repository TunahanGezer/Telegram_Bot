from bs4 import BeautifulSoup
import requests
import time

API_URL="https://api.telegram.org/bot"API_KEY"/sendMessage"

while True:
    url3="https://www.google.com/finance/quote/BTC-USD?hl=tr"
    sayfa3=requests.get(url3)
    html_sayfa3=BeautifulSoup(sayfa3.content,"html.parser")
    BTC=html_sayfa3.find("div",class_ ="YMlKec fxKbKc").getText()
    BTC_flo = BTC.replace(",", "")
    BTC_flo = BTC_flo.replace(",",".")
    BTC_double = float(BTC_flo)

    BTClike=(f"Bitcoin'in güncel değeri: $ {BTC_double}")
    print(BTClike)

    url4="https://www.google.com/finance/quote/ETH-USD"
    sayfa4=requests.get(url4)
    html_sayfa4=BeautifulSoup(sayfa4.content,"html.parser")
    ETH=html_sayfa4.find("div",class_="YMlKec fxKbKc").getText()
    ETH=ETH.replace(",", "")
    ETH_flo = ETH.replace(",",".")
    ETH_double = float(ETH_flo)

    ETHlike=(f"Ethereum'un güncel değeri: $ {ETH_double}")
    print(ETHlike)
    requests.post(url=API_URL, data={"chat_id": "1398531668", "text": "₿ " + BTClike + "\n" + "⧫ " + ETHlike}).json()

    time.sleep(111111)

