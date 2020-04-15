import discord
from boto.s3.connection import S3Connection
s3 = S3Connection(os.environ['S3_token'])

#print(discord.__version__)  # check to make sure at least once you're on the right version!

token = process.env.token

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
