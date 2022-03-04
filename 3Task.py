import telebot as tel

token = '5215996555:AAG1kxJyH7IJJ7IqtG0QdgvhlWNWg59wpWM'
bot = tel.TeleBot(token)


@bot.message_handler(commands=['start'])
def startFunc(message) -> None:
    chat = message.chat.id
    bot.send_message(chat, 'Как тебя зовут?')


@bot.message_handler(content_types=['text'])
def sendName(message) -> None:
    bot.send_message(message.chat.id, 'Привет, ' + message.text + '. Где ты живёшь?')
    bot.register_next_step_handler(message, sendCity)


def sendCity(message) -> None:
    bot.send_message(message.chat.id, f'Крутяк! Я тоже живу в {message.text}. А сколько тебе лет?')
    bot.register_next_step_handler(message, getAges)


def getAges(message)-> None:
    bot.send_message(message.chat.id, f'Тебе целых {message.text} лет. А я бот и мне всего пару дней. ')

bot.infinity_polling()

