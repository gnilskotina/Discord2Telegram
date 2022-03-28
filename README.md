# Discord2Telegram
Forwards messages from Discord to Telegram channel 

---

## Setting up

Before starting, you must first configure config.py 

- Change TOKENDS (<a href="https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token">how to find token discord</a>)
- Change TOKENTG (<a href="https://core.telegram.org/bots#6-botfather">how to find token telegram</a>)
- Change GROUP_TO_TOKEN(<a href="https://stackoverflow.com/questions/33858927/how-to-obtain-the-chat-id-of-a-private-telegram-channel">how to find channel ID telegram</a>)

-----

## Running on heroku

For the bot to work on heroku, you need to create a few additional files

- Create a file named `Procfile` with code:
 ```
 worker: python main.py
 ```
- Create a file named `requirements.txt` with code:
 ```
 discord==1.7.3
 telebot==0.0.4 
 pyTelegramBotAPI==4.4.0
 ```
 - Create a heroku project and select your ***repository (must be private)***. Deploy project
 - Activate main.py in resources tab
 
---

### Advice
Don't give the discord bot admin rights. So it will be possible through the role to regulate the channels that he will read 