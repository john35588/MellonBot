import discord
#print(discord.__version__)  # check to make sure at least once you're on the right version!

token = "Njk5NjUwMDMwNDM2NjE0MTk0.XpXeQw.lnq_oP4-q83OC9N3Q9rx97JrCx4"  # I've opted to just save my token to a text file.

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
