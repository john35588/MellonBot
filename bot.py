import discord

token = "Njk5NjUwMDMwNDM2NjE0MTk0.XpZswg.I5UHOM-ItuF8nze07lzNbw2u0uo"

client = discord.Client()  # starts the discord client.


@client.event  # event decorator/wrapper. More on decorators here: https://pythonprogramming.net/decorators-intermediate-python-tutorial/
async def on_ready():  # method expected by client. This runs once when connected
    print(f'We have logged in as {client.user}')  # notification of login.

@client.event
async def on_message(message):
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    await message.add_reaction("🍉")
    print(f"Added reaction: 🍉")

client.run(token)  # recall my token was saved!
