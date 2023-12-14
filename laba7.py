import telebot
from telebot import types

token = "5857188351:AAFMp6Ie5IVDYd8GU3w62AFPd3OGd5HxSsA"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()


    keyboard.row("Как тебя зовут?", "/help", "/lobby")
    bot.send_message(message.chat.id, 'Привет! Я твой персональный помощник в МТУСИ! Чем могу помочь?',
                     reply_markup=keyboard)


@bot.message_handler(commands=['lobby'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()


    keyboard.row("/start", "/help", "ВУЗ", "Как тебя зовут?", "Пока")
    bot.send_message(message.chat.id, 'Выбирите нужную Вам функцию', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id,
                     'Давайте дружить! Могу Вам указать нужный путь, нажмите на кнопку "Lobby" и я Вас перенаправлю к строке команд')


@bot.message_handler(content_types={'text'})
def manipulator(message):
    if message.text == 'Как тебя зовут?':
        bot.send_message(message.chat.id, 'Алина')

    elif message.text == 'ВУЗ':
        bot.send_message(message.chat.id, 'Перенаправляю Вас на сайт МТУСИ https://mtuci.ru/')
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, 'До новых встреч!')
    elif message.text == 'Расскажи анекдот':
        bot.send_message(message.chat.id, 'Приходит сын работника Роскомнадзора домой с серьгой в ухе. отец мотрит на него и говорит:\n-знаешь сынок,испокон веков серьги носили либо геи либо пираты. Я сейчас выгляну в окно и не дай бог,там не стоит твой парень')
    elif message.text == 'Ты кто?':
        bot.send_message(message.chat.id, 'Я Ваш персональный помощник')

bot.infinity_polling()
