import discord
import os
from decision_class import DecisionMaker
from dotenv import load_dotenv
from os import environ

# Creating the bot


class MyClient(discord.Client):
    async def on_ready(self):  # When the bot is ready
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):  # When the bot receives a message
        print('Message from {0.author}: {0.content}'.format(message))

        name = message.author.mention  # Get the name of the user that sent the message

        # Creating !help command
        if message.content.startswith('!hello'):
            await message.channel.send(f"Hello {name}!")

        # Creating !choice command
        if message.content.startswith('!choice'):
            await message.channel.send(f"Welcome to the Decision Maker!{os.linesep}Enter a list of options separated by commas:{os.linesep}Example: 'Option 1, Option 2, Option 3'.")

            # Checking if the user that is using the bot is the same that sent the message
            def check(msg):
                return msg.author == message.author and msg.channel == message.channel

            # Waiting for the user to send the options
            options = await self.wait_for('message', check=check)

            # Creating a decision maker object
            decision = DecisionMaker(options.content)

            # Asking if the user wants to add weights
            await message.channel.send(f"Would you like to add some weight to the options?{os.linesep}Enter 'y' for yes and 'n' for no.")

            # Looping until the user enters a valid answer
            while True:
                # Waiting for the user to send the answer
                answer = await self.wait_for('message', check=check)
                # Getting the first letter of the answer
                answer = answer.content.lower()[0]

                if answer == 'n':
                    # If the user doesn't want to add weights
                    await message.channel.send(f"{name} asked The Great Decision Maker what to do.{os.linesep}The Great Decision Maker says: ***{decision.make_decision_simple()}***")
                    break

                elif answer == 'y':
                    # If the user wants to add weights
                    await message.channel.send(f"This is the list of options that you entered: {options.content}")
                    await message.channel.send("Enter the weights separared by commas as well(Example: '1, 2, 3'):")
                    # Waiting for the user to send the weights
                    weights = await self.wait_for('message', check=check)
                    # Sending the decision
                    await message.channel.send(f"{name} asked The Great Decision Maker what to do.{os.linesep}The Great Decision Maker says: ***{decision.make_decision_weighted(weights.content)}***")
                    break

                else:
                    await message.channel.send("Invalid input")

        # Creating !help command
        if message.content.startswith('!help'):
            await message.channel.send(f"Welcome to the Decision Maker!{os.linesep}This is a bot to help you with your indecision.{os.linesep}{os.linesep}Commands:{os.linesep}***!hello*** - Says hello to you{os.linesep}***!choice*** - Starts the bot{os.linesep}***!help*** - Shows this message")


load_dotenv()  # Loading the .env file
TOKEN = environ["DISCORD_TOKEN"]  # Getting the token from the .env file

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)
