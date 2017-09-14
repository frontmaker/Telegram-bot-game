import telebot
import config
import sqlite
import random
from telebot import types
import utils
import storage

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=["start"])
def start_game(message):
    db = sqlite.create_connection(config.database_path)
    rows = sqlite.count_rows(db)
    row = sqlite.select_single(db, random.randint(1, rows))

    storage.set_chat_id(message.chat.id, row[2])

    markup = utils.generate_markup(row[2], row[3])

    msg = bot.send_voice(message.chat.id, row[
                         1], reply_markup=markup, duration=20)

    sqlite.close(db)


@bot.message_handler(content_types=["text"])
def check_answer(message):

    answer = storage.get_chat_id(message.chat.id)
    keyboard_hidden = types.ReplyKeyboardRemove()

    if answer == message.text:
        bot.send_message(message.chat.id, 'Верно!',
                         reply_markup=keyboard_hidden)
    else:
        bot.send_message(message.chat.id, 'Увы, вы ошиблись!',
                         reply_markup=keyboard_hidden)
        storage.remove_chat_id(message.chat.id)


if __name__ == '__main__':
    random.seed()
    bot.polling(none_stop=True, interval=0, timeout=20)
