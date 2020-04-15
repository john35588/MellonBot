import discord
import os

token = os.environ.get('S3_token')

print(token)

print(discord.__version__)

client = discord.Client()  # starts the discord client.


@client.event  # event decorator/wrapper. More on decorators here: https://pythonprogramming.net/decorators-intermediate-python-tutorial/
async def on_ready():  # method expected by client. This runs once when connected
    print(f'We have logged in as {client.user}')  # notification of login.

@client.event
async def on_message(message):
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")

    if "john35588" in message.author.name:
        await message.add_reaction("🍉")

client.run(token)  # recall my token was saved!
