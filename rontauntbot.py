#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update, context):
    """Echo the user message."""
    messageString = update.message.text
    
    # Stop evaluating larger messages
    if len(messageString) > 10:
        return
    
    stringParser = messageString.lower().split()
    storeTaunts = {
    1: "taunts/.wav",
    2: "taunts/.wav",
    3: "taunts/.wav",
    4: "taunts/.wav",
    5: "taunts/.wav",
    6: "taunts/.wav",
    7: "taunts/.wav",
    8: "taunts/.wav",
    9: "taunts/.wav",
    10: "taunts/.wav",
    11: "taunts/.wav",
    12: "taunts/.wav",
    13: "taunts/.wav",
    14: "taunts/.wav",
    15: "taunts/.wav",
    16: "taunts/.wav",
    17: "taunts/.wav",
    18: "taunts/.wav",
    19: "taunts/.wav",
    20: "taunts/.wav",
    21: "taunts/.wav",
    22: "taunts/.wav",
    23: "taunts/.wav",
    24: "taunts/.wav",
    25: "taunts/.wav",
    26: "taunts/.wav",
    27: "taunts/.wav",
    28: "taunts/.wav",
    29: "taunts/.wav",
    30: "taunts/.wav",
    31: "taunts/.wav",
    32: "taunts/.wav",
    33: "taunts/.wav",
    34: "taunts/.wav",
    35: "taunts/.wav",
    36: "taunts/.wav",
    37: "taunts/.wav",
    38: "taunts/.wav",
    39: "taunts/.wav",
    40: "taunts/.wav",
    41: "taunts/.wav",
    42: "taunts/.wav",
    43: "taunts/.wav",
    44: "taunts/.wav",
    45: "taunts/.wav",
    46: "taunts/.wav",
    47: "taunts/.wav",
    48: "taunts/.wav",
    49: "taunts/.wav",
    50: "taunts/.wav",
    51: "taunts/.wav",
    52: "taunts/.wav",
    53: "taunts/.wav",
    54: "taunts/.wav",
    55: "taunts/.wav",
    56: "taunts/.wav",
    57: "taunts/.wav",
    58: "taunts/.wav",
    59: "taunts/.wav",
    60: "taunts/.wav",
    61: "taunts/.wav",
    62: "taunts/.wav",
    63: "taunts/.wav",
    64: "taunts/.wav",
    65: "taunts/.wav",
    66: "taunts/.wav",
    67: "taunts/.wav",
    68: "taunts/.wav",
    69: "taunts/.wav",
    70: "taunts/.wav",
    71: "taunts/.wav",
    72: "taunts/.wav",
    73: "taunts/.wav",
    74: "taunts/.wav",
    75: "taunts/.wav",
    76: "taunts/.wav",
    77: "taunts/.wav",
    78: "taunts/.wav",
    79: "taunts/.wav",
    80: "taunts/.wav",
    81: "taunts/.wav",
    82: "taunts/.wav",
    83: "taunts/.wav",
    84: "taunts/.wav",
    85: "taunts/.wav",
    86: "taunts/.wav",
    87: "taunts/.wav",
    88: "taunts/.wav",
    89: "taunts/.wav",
    90: "taunts/color_red-1.wav",
    91: "taunts/color_blue-1.wav",
    92: "taunts/color_purple-2.wav",
    93: "taunts/color_green-1.wav",
    94: "taunts/color_yellow.wav",
    95: "taunts/color_ltblue-1.wav",
    96: "taunts/color_white-3.wav",
    97: "taunts/color_orange-2.wav"}
     
    if stringParser[0] == "taunt":
        if stringParser[1].isnumeric() == True:
            tauntIndex = int(stringParser[1])
            if tauntIndex > 0 and tauntIndex <101: 
                tauntVoice = storeTaunts.get(tauntIndex)
                # context.bot.send_message(chat_id=update.effective_chat.id, text=tauntVoice)
                context.bot.send_voice(chat_id=update.effective_chat.id, voice = open(tauntVoice, 'rb'))


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    bot_token_file = open("bot_token.txt", "r")
    bot_token = bot_token_file.read()
    bot_token_file.close()
    updater = Updater(bot_token, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

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