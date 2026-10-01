import telebot
import random

TOKEN = '8668261259:AAE8f8cG2V5f_kK0DTJK9i7dC_ubZKehk-M'
bot = telebot.TeleBot(TOKEN)

user_games = {}


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = (
        "Привет. Я загадал число от 1 до 100.\n"
        "Попробуй его угадать. Просто напиши мне число."
    )
    user_games[message.chat.id] = random.randint(1, 100)
    bot.reply_to(message, welcome_text)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    chat_id = message.chat.id

    if chat_id not in user_games:
        user_games[chat_id] = random.randint(1, 100)

    try:
        user_num = int(message.text)
        secret_num = user_games[chat_id]

        if user_num < secret_num:
            bot.send_message(chat_id, "Число больше.")
        elif user_num > secret_num:
            bot.send_message(chat_id, "Число меньше.")
        else:
            bot.send_message(chat_id, f"Молодец. Угадал: {secret_num}!\nЯ загадал новое число.")
            user_games[chat_id] = random.randint(1, 100)

    except ValueError:
        bot.send_message(chat_id, "Введите целое число.")


if __name__ == '__main__':
    print("Бот запущен...")
    bot.infinity_polling()