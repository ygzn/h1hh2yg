import telebot
from telebot import types
import base64

token = "5141864359:AAGzKYudjSJdZTO_CdUNzrCiw8ivx-XkUKs"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def welcome(message):
name = message.from_user.first_name
btn1 = types.InlineKeyboardButton('تشفير نص',callback_data='en');btn2 = types.InlineKeyboardButton('فك تشفير نص',callback_data='de')
xx = types.InlineKeyboardMarkup()
xx.add(btn1)
xx.add(btn2)
bot.reply_to(message,f'مرحبا بك عزيزي المستخدم [{name}](tg://settings)\n\n- في بوت تشفير وفك تشفير @GYYY3Y \n\n- للبدأ اضغط على الازرار',reply_markup=xx,parse_mode="markdown")

@bot.callback_query_handler(func=lambda call:True)
def code(call):
if call.data == 'en':
  bot.send_message(call.message.chat.id,'*ارسل النص الان لكي اشفرة لك*',parse_mode="markdown")
  bot.register_next_step_handler(call.message, en_text)
elif call.data == 'de':
  bot.send_message(call.message.chat.id,'*ارسل النص الان لكي افكَ تشفيرة*',parse_mode="markdown")
  bot.register_next_step_handler(call.message, de_text)
  

def en_text(message):
encode = base64.b64encode(message.text.encode("UTF-8")).decode("ascii")
bot.reply_to(message,f'*تم تشفير النص*\n\nالنص المشفر ( {encode} )',parse_mode="markdown")


def de_text(message):
decode = base64.b64decode(message.text).decode("UTF-8")
bot.reply_to(message,f'*تم فك تشفير النص*\n\n( {decode} )',parse_mode="markdown")


bot.polling()
