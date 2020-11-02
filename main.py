import telebot
from config import TOKEN
bot = telebot.TeleBot(TOKEN)
keyboard = telebot.types.ReplyKeyboardMarkup()
keyboard.row('usd', 'eur', 'rur')

@bot.message_handler(commands=['start'])


def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')
    bot.send_message(message.chat.id, 'Какая валюта интересует?', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'usd':
        bot.send_message(message.chat.id, 'Курс доллара сегодня')
        bot.send_message(message.chat.id, 'Какая валюта интересует?', reply_markup=keyboard)
    elif message.text.lower() == 'eur':
        bot.send_message(message.chat.id, 'Курс евро сегодня')
        bot.send_message(message.chat.id, 'Какая валюта интересует?', reply_markup=keyboard)
    elif message.text.lower() == 'rur':
        bot.send_message(message.chat.id, 'курс рубля сегодня')
        bot.send_message(message.chat.id, 'Какая валюта интересует?', reply_markup=keyboard)


bot.polling()
