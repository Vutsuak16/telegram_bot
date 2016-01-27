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


def album(bot, update, args):
    flg = 0
    track = ""
    f = open("Pink Floyd Track Listing.txt")
    album_name = str(" ".join(args).lower() + ":").strip()  # take album name as the argument
    for i in f.readlines():
        i = i.lower().strip()
        if album_name == i:
            flg = 1
            continue
        if flg == 1 and i != '':
            track += i+"\n"
        if flg == 1 and i == '':
            break

    bot.sendMessage(chat_id=update.message.chat_id, text=track)


dispatcher.addTelegramCommandHandler('albumname', album)

updater.start_polling()
