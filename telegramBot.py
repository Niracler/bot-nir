# -*- coding: utf-8 -*-

"""Simple Bot to reply to Telegram messages.
This program is dedicated to the public domain under the CC0 license.
This Bot uses the Updater class to handle the bot.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
import json
import threading
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from informatiom import info

# Enable logging
from tuling import get_response

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text(u'Bot:Hi!')


def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text(u'Bot:' + info.help)


def echo(bot, update):
    if info.tulingBot_Telegram == True:
        update.message.reply_text(('M醬:' + get_response(update.message.text)) or u'bot：M醬不在')
        return

    """自定义回复内容"""
    if update.message.text in info.items.keys():
        update.message.reply_text(u'Bot:' + info.items[update.message.text])


def test(bot, update):
    """调试模式"""
    test, from_str, to_str = map(str, update.message.text.split())
    info.items[from_str] = to_str  # 这已经是互异的了
    update.message.reply_text(u'Bot:指令录入成功')


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def tuling(bot, update):
    """图灵机的启动"""
    update.message.reply_text(u'Bot:M醬,出来吧')
    info.tulingBot_Telegram = True


def killTuling(bot, update):
    """图灵机的关闭"""
    update.message.reply_text(u'Bot:M醬,可以走了')
    info.tulingBot_Telegram = False


def phone(bot, update):
    update.message.reply_text(u'Bot:' + info.items['phone'])


def main():
    """Start the bot."""
    try:
        with open('telegramBot.json') as f:
            key = json.loads(f.read())['key']
    except:
        key = ''

    # Create the EventHandler and pass it your bot's token.
    updater = Updater(token=key)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("test", test))
    dp.add_handler(CommandHandler("tuling", tuling))
    dp.add_handler(CommandHandler("killTuling", killTuling))
    dp.add_handler(CommandHandler("phone", phone))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()

telegram_bot = threading.Thread(target=main)
# telegram_bot.setDaemon(True) # 将其设置为后台进程
