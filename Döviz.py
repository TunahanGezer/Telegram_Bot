from bs4 import BeautifulSoup
import requests
import time
API_URL="https://api.telegram.org/bot"API_KEY"/sendMessage"

while True:
    url1="https://www.google.com/finance/quote/USD-TRY?hl=tr"
    sayfa=requests.get(url1)
    html_sayfa=BeautifulSoup(sayfa.content,"html.parser")
    USD=html_sayfa.find("div",class_ ="YMlKec fxKbKc").getText()   # Text olarak aldığımız value string olarak alıyoruz o yüzden ilk önce onu int,float değer yapılmalı
    USD = USD.replace(",", ".")
    USD_flo=float(USD)
    roundUSD=round(USD_flo,3)
    DolarLike=(f"Dolar kurunun güncel değeri: {roundUSD}")
    print(DolarLike)

    url2="https://www.google.com/finance/quote/EUR-TRY?hl=tr"
    sayfa2=requests.get(url2)
    html_sayfa2=BeautifulSoup(sayfa2.content,"html.parser")
    Euro=html_sayfa2.find("div",class_="YMlKec fxKbKc").getText()
    Euro=Euro.replace(",",".")
    Euro_flo=float(Euro)
    roundEuro=round(Euro_flo,3)
    EuroLike=(f"Euro kurunun güncel değeri: {roundEuro}")
    print(EuroLike)

    requests.post(url=API_URL,data={"chat_id":"1398531668","text":"💵 "+DolarLike + "\n" +"💶 "+EuroLike}).json()

    time.sleep(1111111)