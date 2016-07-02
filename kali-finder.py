# -*- coding: utf-8 -*-
import telebot
import logging
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

bot = telebot.TeleBot("Your Token Here")
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
        bot.reply_to(message, "Hey! im Kali finder! I will find every body who say Kali in your group with his/her username and name! You can add me to your group and enjoy of my spying :) You can contact with my developer using @farbodgame ! (Special thanks to @Polygonal and @MPS3C because of Logo and this bot belong to @linuxiha)")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
        try:
                text = message.text.lower()
                id = str(message.from_user.id)
                username = str(message.from_user.username)
                if "kali" in text or "کالی" in text:
                        if username:
                                if str(message.from_user.first_name):
                                        bot.reply_to(message, "Hey Admin! I detect a Kali user here! Username is @" + username + " and name is " + message.from_user.first_name + u'\U0001f621')
                        elif username:
                                bot.reply_to(message, "Hey Admin! I detect a Kali user here! Username is @" + username + u'\U0001f621')
                        else:
                                bot.reply_to(message, "Hey Admin! I detect a Kali user here! Id is " + id + u'\U0001f621')
        except Exception as e:
		print "We Have An Exception:"
		print e
                pass

bot.polling(True)

