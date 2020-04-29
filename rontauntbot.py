#!/usr/bin/env python

import logging, random, json
from telegram.ext import CommandHandler, MessageHandler, Filters, DelayQueue, Updater
from telegram.error import (TelegramError, Unauthorized, BadRequest, 
                            TimedOut, ChatMigrated, NetworkError, RetryAfter)
import telegram.bot
from telegram.utils.request import Request

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
dqueue1 = DelayQueue(burst_limit=20, time_limit_ms=60000)

def error_callback(update, context):
    try:
        raise context.error
    except Unauthorized:
        print(update)
    except BadRequest:
        print("# handle malformed requests - read more below!")
    except TimedOut:
        print("# handle slow connection problems")
    except NetworkError:
        print("# handle other connection problems")
    except RetryAfter:
        print("Rate Limited")
    except TelegramError:
        print("Telegram Error happened")

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
    if len(messageString) > 20:
        return
        
    
    stringParser = messageString.lower().split()
    storeTaunts = {
    1: "taunts/yes-3.wav",
    2: "taunts/no-2.wav",
    3: "taunts/maybe-2.wav",
    4: "taunts/need_food-2.wav",
    5: "taunts/needtimber-2.wav",
    6: "taunts/need_metal-1.wav",
    7: "taunts/needwealth-3.wav",
    8: "taunts/needoil-2.wav",
    9: "taunts/needknowledge-1.wav",
    10: "taunts/ask_resources-2.wav",
    11: "taunts/help_here-3.wav",
    12: "taunts/noob_rush-1.wav",
    13: "taunts/buildtroops-1.wav",
    14: "taunts/build_wonder-3.wav",
    15: "taunts/work_econ-1.wav",
    16: "taunts/work_airforce-2.wav",
    17: "taunts/work_navy-3.wav",
    18: "taunts/signal_attack-3.wav",
    19: "taunts/attack-3.wav",
    20: "taunts/get_em-2.wav",
    21: "taunts/guard_artillery-2.wav",
    22: "taunts/move_troops-2.wav",
    23: "taunts/grab_territory-1.wav",
    24: "taunts/gonna_boom-2.wav",
    25: "taunts/gonna_rush-1.wav",
    26: "taunts/wanna_ally-3.wav",
    27: "taunts/wanna_peace-3.wav",
    28: "taunts/means_war-3.wav",
    29: "taunts/pay_die-1.wav",
    30: "taunts/prepare_crushed-1.wav",
    31: "taunts/who_attack-3.wav",
    32: "taunts/when_attack-2.wav",
    33: "taunts/where_enemy-1.wav",
    34: "taunts/airpower-3.wav",
    35: "taunts/ships_ahoy-3.wav",
    36: "taunts/spy_spy-3.wav",
    37: "taunts/rare_resources-3.wav",
    38: "taunts/city_down-1.wav",
    39: "taunts/checkouttimer-2.wav",
    40: "taunts/setup_shop-2.wav",
    41: "taunts/wanna_bet-2.wav",
    42: "taunts/itson-1.wav",
    43: "taunts/supposed_hurt-1.wav",
    44: "taunts/fixed_problem-1.wav",
    45: "taunts/good_luck-1.wav",
    46: "taunts/works_out-1.wav",
    47: "taunts/slow_ahead-3.wav", # Voiceline much more than just "I may be slow, but I'm ahead of you."
    48: "taunts/classy-3.wav",
    49: "taunts/tutorials_noob-1.wav",
    50: "taunts/wake_done-1.wav",
    51: "taunts/get_outta-3.wav",
    52: "taunts/leavemealone-2.wav",
    53: "taunts/need_that-3.wav",
    54: "taunts/over_yet-4.wav", # Voiceline is - "Ah, excuse me! Is it over yet?" rathern than just "Is it over yet?""
    55: "taunts/parents_late-2.wav",
    56: "taunts/you_ok-1.wav",
    57: "taunts/stayout-1.wav",
    58: "taunts/bwahaha-1.wav",
    59: "taunts/stormin_castle-1.wav",
    60: "taunts/randomrandom-2.wav",
    61: "taunts/randomrandom-4.wav",
    62: "taunts/game_begin-3.wav",
    63: "taunts/dude_pickem-1.wav",
    64: "taunts/click_understand-2.wav",
    65: "taunts/what_holdup-2.wav",
    66: "taunts/ahh-1.wav",
    67: "taunts/uhh_uhh-1.wav",
    68: "taunts/ohhh-4.wav",
    69: "taunts/uhhh-2.wav",
    70: "taunts/unh-3.wav",
    71: "taunts/doomed-1.wav",
    72: "taunts/wanngiveup-2.wav",
    73: "taunts/victoryismine-3.wav",
    74: "taunts/owmyeye-1.wav",
    75: "taunts/notintheface-1.wav",
    76: "taunts/coming-4.wav",
    77: "taunts/berightthere-1.wav",
    78: "taunts/onmyway-1.wav",
    79: "taunts/send_help-1.wav",
    80: "taunts/gotchacovered-3.wav",
    81: "taunts/check-2.wav",
    82: "taunts/itshallbedone-1.wav",
    83: "taunts/rightonthat-2.wav",
    84: "taunts/sweet-3.wav",
    85: "taunts/youdaman-2.wav",
    86: "taunts/talking_about-1.wav",
    87: "taunts/takencareof-3.wav",
    88: "taunts/soundslikeaplan-2.wav",
    89: "taunts/groovy-3.wav",
    90: "taunts/color_red-1.wav",
    91: "taunts/color_blue-1.wav",
    92: "taunts/color_purple-2.wav",
    93: "taunts/color_green-1.wav",
    94: "taunts/color_yellow.wav",
    95: "taunts/color_ltblue-1.wav",
    96: "taunts/color_white-3.wav",
    97: "taunts/color_orange-2.wav",
    98: "taunts/humanity-3.wav",
    99: "taunts/getthat-3.wav",
    100: "taunts/keep_risin-1.wav",
    201: "taunts/aoe2/1.ogg",
    202: "taunts/aoe2/2.ogg",
    203: "taunts/aoe2/3.ogg",
    204: "taunts/aoe2/4.ogg",
    205: "taunts/aoe2/5.ogg",
    206: "taunts/aoe2/6.ogg",
    207: "taunts/aoe2/7.ogg",
    208: "taunts/aoe2/8.ogg",
    209: "taunts/aoe2/9.ogg",
    210: "taunts/aoe2/10.ogg",
    211: "taunts/aoe2/11.ogg",
    212: "taunts/aoe2/12.ogg",
    213: "taunts/aoe2/13.ogg",
    214: "taunts/aoe2/14.ogg",
    215: "taunts/aoe2/15.ogg",
    216: "taunts/aoe2/16.ogg",
    217: "taunts/aoe2/17.ogg",
    218: "taunts/aoe2/18.ogg",
    219: "taunts/aoe2/19.ogg",
    220: "taunts/aoe2/20.ogg",
    221: "taunts/aoe2/21.ogg",
    222: "taunts/aoe2/22.ogg",
    223: "taunts/aoe2/23.ogg",
    224: "taunts/aoe2/24.ogg",
    225: "taunts/aoe2/25.ogg",
    226: "taunts/aoe2/26.ogg",
    227: "taunts/aoe2/27.ogg",
    228: "taunts/aoe2/28.ogg",
    229: "taunts/aoe2/29.ogg",
    230: "taunts/aoe2/30.ogg",
    231: "taunts/aoe2/31.ogg",
    232: "taunts/aoe2/32.ogg",
    233: "taunts/aoe2/33.ogg",
    234: "taunts/aoe2/34.ogg",
    235: "taunts/aoe2/35.ogg",
    236: "taunts/aoe2/36.ogg",
    237: "taunts/aoe2/37.ogg",
    238: "taunts/aoe2/38.ogg",
    239: "taunts/aoe2/39.ogg",
    240: "taunts/aoe2/40.ogg",
    241: "taunts/aoe2/41.ogg",
    242: "taunts/aoe2/42.ogg"}
     
    if stringParser[0] == "taunt":
        for itm in stringParser[1:]:
            if itm.isnumeric() == True:
                tauntIndex = int(itm)
                if tauntIndex in storeTaunts.keys():
                    tauntVoice = storeTaunts.get(tauntIndex)
                    # context.bot.send_message(chat_id=update.effective_chat.id, text=tauntVoice)
                    dqueue1(context.bot.send_voice,chat_id=update.effective_chat.id, voice = open(tauntVoice, 'rb'))
                else:
                    dqueue1(context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry I don't know that taunt."))
            elif itm == "random":
                tauntIndex = random.choice(list(storeTaunts.keys()))
                tauntVoice = storeTaunts.get(tauntIndex)
                dqueue1(context.bot.send_voice,chat_id=update.effective_chat.id, voice = open(tauntVoice, 'rb'))
                break
            


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    config = json.loads(open("config.json").read())
    if not config["bot_token"] == "<your token here>":
        updater = Updater(config["bot_token"], use_context=True)
    else:
        print("Missing Bot Token")
        exit()

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # error handler
    dp.add_error_handler(error_callback)

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