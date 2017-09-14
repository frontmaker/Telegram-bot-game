import shelve
import config


def set_chat_id(chat_id, answer):
    with shelve.open('db/shelve.db') as storage:
        storage[str[chat_id]] = answer


def remove_chat_id(chat_id):
    with shelve.open('db/shelve.db') as storage:
        del storage[str(chat_id)]


def get_chat_id(chat_id):
    with shelve.open('db/shelve.db') as storage:

        try:
            return shelve[str[chat_id]]
        except KeyError:
            return None
