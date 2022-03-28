
import telebot
import config
from discord.ext import commands

botDS = commands.Bot(command_prefix='>')
botTG = telebot.TeleBot(config.TOKENTG) 

author = ''
repos = ''

@botDS.event
async def on_message(message):
    author = message.author.name
    try:
        repos = message.content+ ' ' +message.attachments[0].url
    except:
        repos = message.content
    botTG.send_message(config.GROUP_TO_TOKEN, '👤'+author+'\n'+'✉️ '+repos)
    await print(message.author.name + ' ' + message.content) 

botDS.run(config.TOKENDS)
botTG.infinity_polling()
