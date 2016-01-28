__name__ = "vutsuak"

from telegram import Updater
import os


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
            track += i + "\n"
        if flg == 1 and i == '':
            break

    bot.sendMessage(chat_id=update.message.chat_id, text=track)


dispatcher.addTelegramCommandHandler('albumname', album)


def track_send(bot, update, args):
    track = str(" ".join(args).lower()).strip()  # take track name as the argument
    dir = 'E:\PinkFloyd\Pink Floyd'
    ct = 0
    list = ['E:\PinkFloyd\Pink Floyd\Pink Floyd - The Dark Side of the Moon',
            'E:\PinkFloyd\Pink Floyd\Pink Floyd Wish You Were Here']
    for sub_dir in os.listdir(dir):
        sub_dir = 'E:\PinkFloyd\Pink Floyd' + '\\' + sub_dir

        for files in os.listdir(sub_dir):
            Files = sub_dir + "\\"+files
            if sub_dir in list:
                files = files.lower().strip()[3:]
            else:
                files = files.lower().strip()[5:]
            filename, ext = os.path.splitext(files)
            if ext == '.mp3':
                if track == files[:files.index('.')]:
                    print Files
                    bot.sendAudio(chat_id=update.message.chat_id,
                                  audio=open(Files, 'rb'))


dispatcher.addTelegramCommandHandler('track', track_send)

updater.start_polling()
