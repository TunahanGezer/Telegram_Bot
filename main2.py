import logging
import time
import random
from typing import Final
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes,CallbackContext
from bs4 import BeautifulSoup
import requests

print('Starting up bot...')

TOKEN: Final = 'API_KEY'
BOT_USERNAME: Final = '@TTelegramV101VBot'
API_URL="https://api.telegram.org/bot"API_KEY"/sendMessage"

"""
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
"""

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello there! I\'m a bot. What\'s up?')

async def komutlar_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    komut="/start => Selam verir\n/help =>Ne yapabileceğini söyler\n/coin =>BTC ile ETH'un güncel değerlerini gösteririr" +\
        "\n/doviz => USD ile EURO'nun güncel değerlerini gösterir.\n/zar => 1 ile 6 arasında sayı söyler" +\
        "\n/anket => Şuan ki anketimizi cevaplamış olursunuz"
    await update.message.reply_text(komut)

async def coin_command(update: Update,context: ContextTypes.DEFAULT_TYPE):
    url3 = "https://www.google.com/finance/quote/BTC-USD?hl=tr"
    sayfa3 = requests.get(url3)
    html_sayfa3 = BeautifulSoup(sayfa3.content, "html.parser")
    BTC = html_sayfa3.find("div", class_="YMlKec fxKbKc").getText()
    BTC_flo = BTC.replace(",", "").replace(",", ".")
    BTC_double = float(BTC_flo)
    BTClike = f"Bitcoin'in güncel değeri: $ {BTC_double}"

    url4 = "https://www.google.com/finance/quote/ETH-USD"
    sayfa4 = requests.get(url4)
    html_sayfa4 = BeautifulSoup(sayfa4.content, "html.parser")
    ETH = html_sayfa4.find("div", class_="YMlKec fxKbKc").getText()
    ETH_flo = ETH.replace(",", "").replace(",", ".")
    ETH_double = float(ETH_flo)
    ETHlike = f"Ethereum'un güncel değeri: $ {ETH_double}"
    Valuue1=f"₿ {BTClike}\n⧫ {ETHlike}"
    await update.message.reply_text(Valuue1)

async def doviz_command(update: Update,context: ContextTypes.DEFAULT_TYPE):
    url1="https://www.google.com/finance/quote/USD-TRY?hl=tr"
    sayfa=requests.get(url1)
    html_sayfa=BeautifulSoup(sayfa.content,"html.parser")
    USD=html_sayfa.find("div",class_ ="YMlKec fxKbKc").getText()   # Text olarak aldığımız value string olarak alıyoruz o yüzden ilk önce onu int,float değer yapılmalı
    USD = USD.replace(",", ".")
    USD_flo=float(USD)
    roundUSD=round(USD_flo,3)
    DolarLike=(f"Dolar kurunun güncel değeri: {roundUSD}")

    url2="https://www.google.com/finance/quote/EUR-TRY?hl=tr"
    sayfa2=requests.get(url2)
    html_sayfa2=BeautifulSoup(sayfa2.content,"html.parser")
    Euro=html_sayfa2.find("div",class_="YMlKec fxKbKc").getText()
    Euro=Euro.replace(",",".")
    Euro_flo=float(Euro)
    roundEuro=round(Euro_flo,3)
    EuroLike=(f"Euro kurunun güncel değeri: {roundEuro}")
    Valuee2=f"💵 Dolar kuru'nun güncel değeri: ₺ {roundUSD} \n💶 Euro kuru'nun güncel değeri: ₺  {roundEuro}"
    await update.message.reply_text(Valuee2)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Try typing anything and I will do my best to respond!')

async def zar_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    player_name = update.message.from_user.full_name
    zar_roll = random.randint(1, 6)
    zar =f"Üyemiz: {player_name}'in, zarı {zar_roll} geldi!"
    await update.message.reply_text(zar)

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command, you can add whatever text you want here.')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get basic info of the incoming message
    message_type: str = update.message.chat.type
    text: str = update.message.text

    # Print a log for debugging
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    # React to group messages only if users mention the bot directly
    if message_type == 'group':
        # Replace with your bot username
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            if new_text.startswith("coin"):
                await coin_command(update,context)
                return
        else:
            return  # We don't want the bot respond if it's not mentioned in the group

    response: str = handle_response(text)
    # Reply normal if the message is in private
    print('Bot:', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

ANKET_SORUSU = "Bugün'ün nasıl geçti?"
SECENEKLER = ["Güzel", "İdare eder", "Kötü"]
Cevaplar = {}

async def anket(update: Update, context):
    user = update.message.from_user
    await update.message.reply_text(f"Merhaba {user.full_name}! {ANKET_SORUSU}",
                                    reply_markup=ReplyKeyboardMarkup([SECENEKLER], one_time_keyboard=True))

async def anket_cevabi(update: Update, context):
    cevap = update.message.text
    user_id = update.message.from_user.id

    if user_id not in Cevaplar:
        Cevaplar[user_id] = cevap
        await update.message.reply_text("Cevabınız kaydedildi. Teşekkür ederiz!")
        return

    await update.message.reply_text("Zaten cevap verdiniz. Tekrar teşekkür ederiz!",
                                    reply_markup=ReplyKeyboardRemove())

def handle_response(text):
    # Create your own response logic
    processed: str = text.lower()

    if 'hello' in processed:
        return 'Hey there!'

    if 'how are you' in processed:
        return 'I\'m good!'

    if 'i love python' in processed:
        return 'Remember to subscribe!'

    return 'I don\'t understand'

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    app.add_handler(CommandHandler('coin', coin_command))
    app.add_handler(CommandHandler('doviz', doviz_command))
    app.add_handler(CommandHandler('zar', zar_command))
    app.add_handler(CommandHandler('komut', komutlar_command))
    app.add_handler(CommandHandler('anket', anket))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, anket_cevabi))

    # Log all errors
    app.add_error_handler(error)

    print('Polling...')
    # Run the bot
    app.run_polling(poll_interval=5)

