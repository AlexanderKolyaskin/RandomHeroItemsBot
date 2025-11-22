import telebot
from telebot import types
from service.randomizer import random_hero, random_item

class Bot:
    def __init__(self, settings):
        self.settings = settings
        self.bot = telebot.TeleBot(token=self.settings.token)
        self.items = settings.Items

    def register_handlers(self):
        @self.bot.message_handler(commands=['start'])
        def start(message):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('/help')
            btn2 = types.KeyboardButton('/выбор-рандомного-героя')
            btn3 = types.KeyboardButton('/выбор-рандомных-предметов')
            markup.add(btn2, row_width=3)
            markup.add(btn3, row_width=2)
            markup.add(btn1, row_width=1)
            self.bot.send_message(message.chat.id,
                             'Привет, впиши команду /rh для нахождения рандомного героя, а затем и /ri, для нахождения рандомных предметов',
                             reply_markup=markup)

        @self.bot.message_handler(commands=['start', 'help'])
        def send_welcome(message):
            self.bot.send_message(message.chat.id,
                             "Доступные команды:\n/start — Начать взаимодействие\n/help — Получить помощь\n"
                             "/rh - выбор рандомного героя доты")

        @self.bot.message_handler(commands=['help'])
        def helper(message):
            self.bot.send_message(message.chat.id,
                             "Доступные команды:\n/start — Начать взаимодействие\n/help — Получить помощь\n"
                             "/rh - выбор рандомного героя доты\n/ri - выбор рандомного предмета")

        @self.bot.message_handler(commands=['выбор-рандомного-героя', 'rh'])
        def random_h(message):
            self.bot.send_message(message.chat.id, "рандомный герой: " + random_hero(self.settings.Heroes))

        @self.bot.message_handler(commands=['ri', 'выбор-рандомных-предметов'])
        def random_i(message):
            self.bot.send_message(message.chat.id, "рандомный билд: " + "".join(random_item(self.items)))