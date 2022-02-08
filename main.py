import telebot
import config
import pars
import random
import time

from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    #sti = open('static/welcome.webp', 'rb')
    #bot.send_sticker(message.chat.id, sti)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    btn2 = types.KeyboardButton("❓ Задать вопрос")
    item1 = types.KeyboardButton("GAZP")
    item2 = types.KeyboardButton("SBER")
    item3 = types.KeyboardButton("MMK")
    item4 = types.KeyboardButton("В меню")
    item5 = types.KeyboardButton("😊 Как дела?")

    markup.add(item1, item2, item3, item4, item5, btn1, btn2)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>Ключевой помощник Вова</b>, бот созданный чтобы тебе было удобно следить за ценами на акциях.".format(
                         message.from_user),
                     parse_mode='html', reply_markup=markup)
    #d = message.from_user
    #print(d['first_name'])
    with open('data.txt','a') as f:
        f.write(str(message.from_user))
    print("Пользователь {0.first_name} вызвал команду: {1.username}".format(message.from_user, message.from_user))
def take_limit(name, coll):
    pass

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'AZP':
            bot.send_message(message.chat.id, str(random.randint(0, 100)))
        ####
        elif (message.text == "👋 Поздороваться"):
            bot.send_message(message.chat.id, text="Привеет.. Спасибо что читаешь статью!)")
            print('!')
        elif (message.text == "❓ Задать вопрос"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Как меня зовут?")
            btn2 = types.KeyboardButton("Что я могу?")
            back = types.KeyboardButton("Вернуться в главное меню")
            markup.add(btn1, btn2, back)
            bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)

        elif (message.text == "Как меня зовут?"):
            with open('data.txt', 'a') as f:
                f.write('привет!')
            bot.send_message(message.chat.id, "У меня нет имени..")
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add()

        elif message.text == "Что я могу?":
            bot.send_message(message.chat.id, text="Поздороваться с читателями")

        elif (message.text == "D!!Вернуться в главное меню"):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("👋 Поздороваться")
            button2 = types.KeyboardButton("❓ Задать вопрос")
            markup.add(button1, button2)
            bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
        ###
        elif message.text == 'В меню': #('В меню' or 'Вернуться в главное меню' or 'Меню'):
            welcome(message)
        elif message.text == 'GAZP':
            #addd = pars.box['gazp']['adress']
            #pris = pars.ticker(pars.box['gazp']['adress'])
            #text_price = "Цена акции Газпром: " + str(pris)
            text_price = "Цена акции Газпром: " + str(pars.ticker(pars.box['gazp']['adress']))
            bot.send_message(message.chat.id, text_price)
            #bot.send_message(message.chat.id, text_price1)

        elif message.text == 'SBER':
            #text_price = "Цена акции Сбербанк: " + str(pars.update_ticker_SBER())
            #bot.send_message(message.chat.id, text_price)
            text_price = "Цена акции Сбербанк: " + str(pars.ticker(pars.box['sber']['adress']))
            bot.send_message(message.chat.id, text_price)
        elif message.text == 'MMK':
            text_price = "Цена акции ММК: " + str(pars.ticker(pars.box['mmk']['adress']))
            bot.send_message(message.chat.id, text_price)

        elif message.text == '😊 Как дела?':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')
        with open('data.txt', 'a') as f:
                    f.write("Пользователь {0.first_name} имени: {1.username} вызвал команду: ".format(message.from_user, message.from_user))
                    f.write(str(message.text))
                    print(type(str(message.text)))
                    print('открытие файла')
                    print(str(message.text))


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Бывает 😢')

            # remove inline buttons
            #bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?",
             #                     reply_markup=None)

            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")

    except Exception as e:
        print(repr(e))


# RUN
while True:
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        print("error")
        print(e) #если у вас логгера нет,
        # или import traceback; traceback.print_exc() для печати полной инфы
        time.sleep(15)