<h1 align="center">Decision Maker</h1>

<p align="center">Algorithm that chooses for you whatever you are undecided about</p>

<p align="center">
    <a href="#About">About</a> •
    <a href="#Getting-started">Getting Started</a> •
    <a href="#How-to-create-your-own-bot">How to create your own bot</a> •
    <a href="#Use-the-bot!">Use the bot!</a> •
    <a href="#Steps">Steps</a> 

</p>

<img src="https://img.shields.io/static/v1?label=Status&message=Developing&color=FF8C00&style=for-the-badge&logo=ghost"/>


![screenshot](https://raw.githubusercontent.com/JonathanFcosta17/Decision_maker/main/img/GifDiscordBot.gif)

## About

This project is a bot that helps you decide what to do, whether it's what to eat, what to watch, what to play, etc. It is a simple algorithm that chooses for you whatever you are undecided about.
### Example:
 
Let's say you're undecided about which TV series you should watch.
 
The options in your mind are ***Sherlock, How I Met Yor Mother, Game of Thrones, Breaking Bad and Supernatural***.
 
Just write these options and the bot will choose.

## Getting Started

### Discord bot:

To use the bot, you must first add it to your server, and then you can use the command '!help' to see all the commands, or you can use the command '!ajuda' to see all the commands in Portuguese.

### Telegram bot:

To use the bot, you must first search for it on Telegram, and then you can use the command '/help' to see all the commands, or you can use the command '/ajuda' to see all the commands in Portuguese.

### Weights for the options:

You know when you are undecided about something, you have a lot of options, and you are more likely to choose some options over others? Well, this is where the weights come in. You can give a weight to each option to make it more likely to be chosen. A higher weight means a higher chance of being chosen but not a guarantee that it will be chosen.

The weights will be used correspondingly to the options you have written. For example, if you have 2 options, so you must have 2 weights, and the first weight will be used for the first option, and the second weight will be used for the second option.

**The weights are optional, if you don't want to use them, just write 'n' when the bot asks you if you want to use weights**.

## How to create your own bot

### Discord bot:

- First you need to create a bot on the [Discord Developer Portal](https://discord.com/developers/applications), and then you must create a file called '.env' and put the token of your bot in it as follows:

```
TOKEN=YOUR_TOKEN
```

- Then you must install the dependencies with the command 'pip install -r requirements.txt'.

- And finally you use the file discord_bot.py as a base to create your own bot.

### Telegram bot: 

- First you need to create a bot on the [Telegram BotFather](https://t.me/botfather), and then you must create a file called '.env' and put the token of your bot in it as follows:

```
TOKEN=YOUR_TOKEN
```

- Then you must install the dependencies with the command:
    
```
pip install -r requirements.txt
```

- And finally you use the file telegram_bot.py as a base to create your own bot.

 ## Use the bot!
 
 You can add this bot to your discord server by clicking [here](https://discord.com/api/oauth2/authorize?client_id=1025106687734059039&permissions=2056&scope=bot)!
 
 And if you want to use it on Telegram, just click [here](https://t.me/TheGreatDecisionMakerBot)!

 ## Steps
 ### For this project to be considered completed, there are some steps to be followed:
- [x] Create logic behind the bot.
- [x] Transform it to be usable in Discord.
- [x] Push Discord bot to online server.
- [x] Transform it to be usable in Telegram's API.
- [x] Push Telegram bot to online server.

## Show your support
Give a ⭐️ if you like this project!