import random
import telebot
from telebot import types
bot = telebot.TeleBot("1731605907:AAEpSpG28yIVFdR9WgeWTow0vQNx_DC-fA4")
@bot.message_handler(commands=['start'])
def send_welcome(message):
    global s
    s=0
    global a
    global b
    global n

    spisok=["собака", "попугай", "енот", "кошка", "кролик", "заяц", "крокодил", "ящерица", "бегемот", "слон",]
    a=random.choice(spisok)
    b=(list(a))
    n=list(("*"*len(a)))
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("а")
    item2=types.KeyboardButton("б")
    item3=types.KeyboardButton("в")
    item4=types.KeyboardButton("г")
    item5=types.KeyboardButton("д")
    item6=types.KeyboardButton("е")
    item7=types.KeyboardButton("ё")
    item8=types.KeyboardButton("ж")
    item9=types.KeyboardButton("з")
    item10=types.KeyboardButton("и") 
    item11=types.KeyboardButton("й")
    item12=types.KeyboardButton("к")
    item13=types.KeyboardButton("л")
    item14=types.KeyboardButton("м")
    item15=types.KeyboardButton("н")
    item16=types.KeyboardButton("о")
    item17=types.KeyboardButton("п")
    item18=types.KeyboardButton("р")
    item19=types.KeyboardButton("с")
    item20=types.KeyboardButton("т")
    item21=types.KeyboardButton("у")
    item22=types.KeyboardButton("ф")
    item23=types.KeyboardButton("х")
    item24=types.KeyboardButton("ц")
    item25=types.KeyboardButton("ч")
    item26=types.KeyboardButton("ш")
    item27=types.KeyboardButton("щ")
    item28=types.KeyboardButton("ъ")
    item29=types.KeyboardButton("ы")
    item30=types.KeyboardButton("ь")
    item31=types.KeyboardButton("э")
    item32=types.KeyboardButton("ю")
    item33=types.KeyboardButton("я")


    markup.add(item1,item2,item3,item4,item5,item6,item7,item8,item9,item10,item11,item12,item13,item14,item15,item16,item17,item18,item19,item20,item21,item22,item23,item24,item25,item26,item27,item28,item29,item30,item31,item32,item33)
    bot.send_message(message.chat.id, "Попробуйте угадать какого животного мы загадали!")
    bot.send_message(message.chat.id, ''.join(n))
    bot.send_message(message.chat.id, "Введите одну букву")
    bot.send_message(message.chat.id, "Количество твоих жизней: ❤❤❤❤❤",reply_markup=markup )

@bot.message_handler(content_types=["text"])
def text(message):

    global s
    if message.text in b:
        for idx, symbol in enumerate(b):
            if symbol == message.text:
                n[idx] = symbol 

                if n==b:
                    bot.send_message(message.chat.id, "Поздравляю, вы выиграли :)")
                    bot.send_message(message.chat.id, "Загаданное слово:")
                    bot.send_message(message.chat.id, ''.join(n))
                    bot.send_message(message.chat.id, "Чтобы начать заново, нажмите /start")
                    return
    else:

        bot.send_message(message.chat.id, "Данной буквы нет!")
        s+=1
        if s==1:
            bot.send_message(message.chat.id, "Осталось жизней:  ❤❤❤❤")


        if s==2:
            bot.send_message(message.chat.id, "Осталось жизней:  ❤❤❤")

        if s==3:
            bot.send_message(message.chat.id, "Осталось жизней:  ❤❤")

        if s==4:
            bot.send_message(message.chat.id, "Осталось жизней:  ❤")

        if s==5:

            bot.send_message(message.chat.id, "Вы проиграли!")
            bot.send_message(message.chat.id, "Чтобы начать заново, нажмите /start")
            return
    del message.text
    bot.send_message(message.chat.id, ''.join(n))

bot.polling(none_stop=True, interval=0)
