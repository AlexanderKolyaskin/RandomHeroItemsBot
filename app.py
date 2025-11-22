import telebot
from service.bot import Bot

class Application:
    def __init__(self, settings):
        self.bot = Bot(settings)
        self.settings = settings

    def run(self):
        self.bot.register_handlers()
        self.bot.bot.infinity_polling()