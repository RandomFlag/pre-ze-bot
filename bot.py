import telebot
from telebot import types
import time
import random

from telegram import InlineKeyboardMarkup

resultPath = "trueResult.txt"
resultFile = open(resultPath, "rt", encoding="utf8")
dick = resultFile.read()
order = ['заборонив', 'дозволив', 'наказав']

TOKEN = '5264114850:AAHptmkCLkAhy8rOhGEz2WnfPk_r9yfvy8s'

bot = telebot.TeleBot(TOKEN)



@bot.message_handler(func=lambda message: True)
def button(message):
    markup = types.InlineKeyboardMarkup()
    item = types.InlineKeyboardButton('Новий указ', callback_data = 'new')
    markup.add(item)
    bot.send_message(message.chat.id, '!', reply_markup=markup)

###def echo_all(message):
###    dickList = dick.split('\n')
###    word = dickList[random.randrange(0, len(dickList))]
###    bot.send_message(message.chat.id, 'Президент ' + order[random.randrange(0, 3)] + ' ' + word[:len(word)-1] + "ь")

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == 'new':
        markup = types.InlineKeyboardMarkup()
        item = types.InlineKeyboardButton('Новий указ', callback_data = 'new')
        markup.add(item)
        dickList = dick.split('\n')
        word = dickList[random.randrange(0, len(dickList))]
        bot.send_message(call.message.chat.id, 'Президент ' + order[random.randrange(0, 3)] + ' ' + word[:len(word)-1] + "ь", reply_markup=markup)
        ###bot.send_message(call.message.chat.id, '!', )

bot.infinity_polling()