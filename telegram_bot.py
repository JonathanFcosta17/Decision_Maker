import telebot
import random
import os
from decision_class import DecisionMaker
from dotenv import load_dotenv


load_dotenv()  # Loading the .env file
TOKEN = os.environ["TELEGRAM_TOKEN"]  # Getting the token from the .env file

# Creating the bot
bot = telebot.TeleBot(TOKEN)

# Creating the /start command


@bot.message_handler(commands=['start'])
def welcome(message):
    text = f"""Hello {message.from_user.first_name}.
Welcome to the Decision Maker!
This is a bot to help you with your indecision.
Use /choice to start making a decision.
"""
    bot.reply_to(message, text)

# Creating the /choice command


@bot.message_handler(commands=['choice'])
def choice(message):
    text = """
Enter a list of options separated by commas:
Example: 'Option 1, Option 2, Option 3'."""
    bot.send_message(message.chat.id, text)

    # waiting for the user to send the options
    bot.register_next_step_handler(message, option_list)

# This function is a part of the /choice command
# It is called when the user sends the options


def option_list(message):
    # Creating a list with the options
    global options
    options = message.text

    # Creating a decision maker object
    global decision
    decision = DecisionMaker(options)

    # Asking if the user wants to add weights
    text = """Would you like to add some weight to the options?
Enter 'y' for yes and 'n' for no."""

    # waiting for the user to send the answer
    bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(message, weights_or_not)


# This function is a part of the /choice command
# It is called when the user sends if he wants to add weights or not


def weights_or_not(message):
    # Looping until the user enters a valid answer
    while True:
        # Waiting for the user to send the answer
        answer = message.text.lower()[0]

        if answer == 'n':
            # If the user doesn't want to add weights
            text = f"""{message.from_user.first_name} asked The Great Decision Maker what to do.
The Great Decision Maker says: *{decision.make_decision_simple()}*"""

            bot.send_message(message.chat.id, text, parse_mode='Markdown')
            break

        elif answer == 'y':
            # If the user wants to add weights
            text = f"""This is the list of options that you entered: *{options}*

Enter the weights separated by commas as well(Example: '1, 2, 3'):"""

            bot.send_message(message.chat.id, text, parse_mode='Markdown')
            # Waiting for the user to send the weights
            bot.register_next_step_handler(message, with_weights)
            break

        else:
            bot.send_message(message.chat.id, "Invalid input")
            bot.register_next_step_handler(message, weights_or_not)
            break


# This function is a part of the /choice command
# It is called when the user sends the weights
def with_weights(message):
    try:
        # Sending the decision
        text = f"""{message.from_user.first_name} asked The Great Decision Maker what to do.
The Great Decision Maker says: *{decision.make_decision_weighted(message.text)}*"""

        bot.send_message(message.chat.id, text, parse_mode='Markdown')
    except Exception:
        # If the user doesn't enter the weights correctly
        text = "Invalid input"
        bot.send_message(message.chat.id, text)
        bot.register_next_step_handler(message, with_weights)

# Creating the /help command


@bot.message_handler(commands=['help'])
def help(message):
    text = f"""Hey {message.from_user.first_name}. Don't worry, here is a list of commands that you can use with me:

Commands:
/start - Start the bot
/choice - Starts the choice
/help - Shows this message
"""
    bot.reply_to(message, text)

# Creating the command to get anything besides the other commands


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    imgs = os.listdir("Decision_Maker/img/memes")  # Getting the list of memes
    # Opening a random meme
    photo = open(f"Decision_Maker/img/memes/{random.choice(imgs)}", "rb")
    bot.send_photo(message.chat.id, photo)  # Sending the img to the user


# Running the bot
if __name__ == "__main__":
    bot.polling()
