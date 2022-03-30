import telebot
from telebot import types
import random
from pars import usd, eur, btc, kyiv, lviv, ukr
from config import temperature
from kyiv import temperature1
from Львов import temperature2

Token = '5278220319:AAHyFzxfwbwFRzl65xHGCJ9cgi2Mj8VHg2k'

bot = telebot.TeleBot(Token)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Курс валют')
    item2 = types.KeyboardButton('Погода')
    item3 = types.KeyboardButton('Новости')
    item4 = types.KeyboardButton('Рандомное число')

    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id, 'Привет, {0.first_name},что тебя интересует сегодня?'.format(message.from_user),
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Рандомное число':
            bot.send_message(message.chat.id, 'Ваше число: ' + str(random.randint(0, 100)))
        if message.text == 'Курс валют':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('USD')
            item2 = types.KeyboardButton('EUR')
            item3 = types.KeyboardButton('BTC')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3, back)

            bot.send_message(message.chat.id, 'Курс валют', reply_markup=markup)
        if message.text == 'USD':
            bot.send_message(message.chat.id, 'Сейчас USD: ' + usd)
        if message.text == 'EUR':
            bot.send_message(message.chat.id, 'Сейчас EUR : ' + eur)
        if message.text == 'BTC':
            bot.send_message(message.chat.id, 'Сейчас BTC : ' + btc)
        if message.text == 'Погода':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Украинка')
            item2 = types.KeyboardButton('Киев')
            item3 = types.KeyboardButton('Львов')
            item4 = types.KeyboardButton('Ещё')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3, item4, back)

            bot.send_message(message.chat.id, 'Погода', reply_markup=markup)
        if message.text == 'Украинка':
            bot.send_message(message.chat.id,
                             'Сейчас в Украинке ' + (str(temperature)) + ' по цельсию.' + '\n' + '\n' + ukr)
        if message.text == 'Киев':
            bot.send_message(message.chat.id,
                             'Сейчас в Киеве ' + (str(temperature1)) + ' по цельсию.' + '\n' + '\n' + kyiv)
        if message.text == 'Львов':
            bot.send_message(message.chat.id,
                             'Сейчас во Львове ' + (str(temperature2)) + ' по цельсию.' + '\n ' + '\n' + lviv)

        if message.text == 'Новости':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Мир')
            item2 = types.KeyboardButton('Украина')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, back)
            bot.send_message(message.chat.id, 'Новости', reply_markup=markup)

        if message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Курс валют')
            item2 = types.KeyboardButton('Погода')
            item3 = types.KeyboardButton('Новости')
            item4 = types.KeyboardButton('Рандомное число')

            markup.add(item1, item2, item3, item4)

            bot.send_message(message.chat.id, 'Назад', reply_markup=markup)


bot.polling(none_stop=True)


