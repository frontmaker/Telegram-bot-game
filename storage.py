import shelve
import config


def set_chat_id(chat_id, answer):
    with shelve.open(config.shelve_path) as storage:
        storage[str(chat_id)] = answer


def remove_chat_id(chat_id):
    with shelve.open(config.shelve_path) as storage:
        del storage[str(chat_id)]


def get_chat_id(chat_id):
    with shelve.open(config.shelve_path) as storage:

        try:
            return storage[str(chat_id)]
        except KeyError:
            return None
