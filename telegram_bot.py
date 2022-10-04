import telebot
import random
import os
from decision_class import DecisionMaker
from dotenv import load_dotenv
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


load_dotenv()  # Loading the .env file
TOKEN = os.environ["TELEGRAM_TOKEN"]  # Getting the token from the .env file

# Creating the bot
bot = telebot.TeleBot(TOKEN)


def language_markup_inline():
    markup = InlineKeyboardMarkup()
    markup.width = 2
    markup.add(InlineKeyboardButton("English", callback_data="english"),
               InlineKeyboardButton("Português", callback_data="portuguese"))

    return markup

# Creating the /start command


@bot.message_handler(commands=['start'])
def start(message):

    global user
    user = message.from_user.first_name

    # Asking the user to select the language
    text = "Select the language:"
    bot.send_message(message.chat.id, text,
                     reply_markup=language_markup_inline())


# Getting the answer from the user


@bot.callback_query_handler(func=lambda call: True if call.data == "english" or call.data == "portuguese" else False)
def language(call):
    global language
    if call.data == "english":
        language = "english"
    elif call.data == "portuguese":
        language = "portuguese"

    welcome(call)


def welcome(call):
    # Sending the welcome message
    if language == "english":
        text = f"""Hello {user}!
I'm The Great Decision Maker, I can help you make decisions.

Just send me a list of options separated by commas and I'll choose one for you.
For example: *eat pizza, eat pasta, eat salad*

You can also add weights to the options, just send me a list of numbers separated by commas.
For example: *1, 2, 1*

Just use the /choice command to make a decision."""

    elif language == "portuguese":
        text = f"""Olá {user}!
Eu sou O Grande Decisor, posso ajudá-lo a tomar decisões.

Basta me enviar uma lista de opções separadas por vírgulas e eu escolherei uma para você.
Por exemplo: *comer pizza, comer massa, comer salada*

Você também pode adicionar pesos às opções, basta me enviar uma lista de números separados por vírgulas.
Por exemplo: *1, 2, 1*

Basta usar o comando /escolha para fazer uma decisão."""

    bot.send_message(call.message.chat.id, text, parse_mode='Markdown')


# Creating the /choice command


@bot.message_handler(commands=['choice'])
def choice(message):
    global language
    language = "english"

    # Asking the user to send the options
    text = """
Enter a list of options separated by commas:
Example: 'Option 1, Option 2, Option 3'."""
    bot.send_message(message.chat.id, text)

    # waiting for the user to send the options
    bot.register_next_step_handler(message, option_list)


@bot.message_handler(commands=['escolha'])
def escolha(message):
    global language
    language = "portuguese"

    text = """
Digite uma lista de opções separadas por vírgulas:
Exemplo: 'Opção 1, Opção 2, Opção 3'."""
    bot.send_message(message.chat.id, text)

    # waiting for the user to send the options
    bot.register_next_step_handler(message, option_list)

# Creating the inline keyboard for the /choice and /escolha command


def weights_markup_inline():
    markup = InlineKeyboardMarkup()
    markup.width = 2

    if language == "english":
        markup.add(InlineKeyboardButton("Yes", callback_data="yes"),
                   InlineKeyboardButton("No", callback_data="no"))

    elif language == "portuguese":
        markup.add(InlineKeyboardButton("Sim", callback_data="yes"),
                   InlineKeyboardButton("Não", callback_data="no"))

    return markup

# # This function is a part of the /choice command
# # It is called when the user sends the options


def option_list(message):
    # Creating a list with the options
    global options
    options = message.text

    # Creating a decision maker object
    global decision
    decision = DecisionMaker(options)

    # Asking if the user wants to add weights
    if language == "english":
        text = "Would you like to add some weight to the options?"
        bot.send_message(message.chat.id, text,
                         reply_markup=weights_markup_inline())

    elif language == "portuguese":
        text = "Você gostaria de adicionar algum peso às opções?"
        bot.send_message(message.chat.id, text,
                         reply_markup=weights_markup_inline())


# This function is a part of the /choice command
# It is called when the user sends if he wants to add weights or not

@bot.callback_query_handler(func=lambda call: True if call.data == "yes" or call.data == "no" else False)
def weights_or_not(call):
    if language == "english":
        # Asking for the weights
        if call.data == "yes":
            text = f"""This is the list of options that you entered: *{options}*

Enter the corresponding weights separated by commas as well (Example: '1, 2, 3'):"""

            bot.send_message(call.message.chat.id, text.title(),
                             parse_mode='Markdown')
            bot.register_next_step_handler(call.message, with_weights)

        elif call.data == "no":
            without_weights(call.message)

    elif language == "portuguese":
        # Asking for the weights
        if call.data == "yes":
            text = f"""Esta é a lista de opções que você digitou: *{options}*

Digite os pesos correspondentes separados por vírgulas também (Exemplo: '1, 2, 3'):"""
            bot.send_message(call.message.chat.id, text.title(),
                             parse_mode='Markdown')
            bot.register_next_step_handler(call.message, with_weights)

        elif call.data == "no":
            without_weights(call.message)


# This function is a part of the /choice command
# It is called when the user sends the weights
def with_weights(message):
    if language == "english":
        try:
            text = f"""{user} asked The Great Decision Maker what to do.
The Great Decision Maker says: *{decision.make_decision_weighted(message.text)}*"""

            bot.send_message(message.chat.id, text, parse_mode='Markdown')
        except Exception as e:
            text = f"Invalid input: {e}"
            bot.send_message(message.chat.id, text)
            bot.register_next_step_handler(message, with_weights)

    elif language == "portuguese":
        try:
            text = f"""{user} perguntou ao Grande Decisor o que fazer.
O Grande Decisor diz: *{decision.make_decision_weighted(message.text)}*"""

            bot.send_message(message.chat.id, text, parse_mode='Markdown')
        except Exception as e:
            text = f"Entrada inválida: {e}"
            bot.send_message(message.chat.id, text)
            bot.register_next_step_handler(message, with_weights)


def without_weights(message):
    if language == "english":
        try:
            text = f"""{user} asked The Great Decision Maker what to do.
The Great Decision Maker says: *{decision.make_decision_simple()}*"""

            bot.send_message(message.chat.id, text, parse_mode='Markdown')
        except Exception as e:
            text = f"Invalid input: {e}"
            bot.send_message(message.chat.id, text)
            bot.register_next_step_handler(message, without_weights)

    elif language == "portuguese":
        try:
            text = f"""{user} perguntou ao Grande Decisor o que fazer.
O Grande Decisor diz: *{decision.make_decision_simple()}*"""

            bot.send_message(message.chat.id, text, parse_mode='Markdown')
        except Exception as e:
            text = f"Entrada inválida: {e}"
            bot.send_message(message.chat.id, text)
            bot.register_next_step_handler(message, without_weights)


# Creating the /help command


@bot.message_handler(commands=['help'])
def help(message):
    text = """This bot was created by @JonathanfCosta to help you make decisions.

The commands are:
/start - Starts the bot and sets the language
/choice - Makes a decision based on a list of options.
/help - Shows this message

The bot is open source and you can find it here:    
https://github.com/JonathanFcosta17/Decision_maker
"""

    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['ajuda'])
def ajuda(message):
    text = """Este bot foi criado por @JonathanfCosta para ajudá-lo a tomar decisões.

Os comandos são:
/start - Inicia o bot e seleciona o idioma
/escolha - Faz uma decisão com base em uma lista de opções.
/ajuda - Mostra esta mensagem

O bot é de código aberto e você pode encontrá-lo aqui:
https://github.com/JonathanFcosta17/Decision_maker
"""

    bot.send_message(message.chat.id, text)


# Creating the command to get anything besides the other commands


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    imgs = os.listdir("./img/memes")  # Getting the list of memes
    # Opening a random meme
    photo = open(f"./img/memes/{random.choice(imgs)}", "rb")
    bot.send_photo(message.chat.id, photo)  # Sending the img to the user


# Running the bot
if __name__ == "__main__":
    bot.polling()
