__name__ = "vutsuak"

from telegram import Updater

updater = Updater(token='142198266:AAHMqzQ9fY_hzu3EOhsiv0Gi0z8Qz5x1034')

dispatcher = updater.dispatcher


def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Welcome to The Wall !!")


dispatcher.addTelegramCommandHandler('start', start)


def unknown(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="No such command")

dispatcher.addUnknownTelegramCommandHandler(unknown)

def album(bot, update,args):
    print args #take album name as the argument
    bot.sendMessage(chat_id=update.message.chat_id,text="kajaaaa")

dispatcher.addTelegramCommandHandler('albumname', album)

updater.start_polling()
