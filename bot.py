import discord
import urllib.request

token = "Njk5NjUwMDMwNDM2NjE0MTk0.XpZswg.I5UHOM-ItuF8nze07lzNbw2u0uo"
client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    if "22jhoff" in message.author.name or "Plasmathrower" in message.author.name:
        await message.add_reaction("🌈")
        await message.add_reaction("💕")
        await message.add_reaction("😘")
        print("Response: Added reaction: 🌈")
    else:
        await message.add_reaction("🍉")
        print("Response: Added reaction: 🍉")
    
    if "hey melonbot" in message.content.lower() or "hi melonbot" in message.content.lower():
        await message.channel.send("Hey " + message.author.name + "!")
    
    if "@MelonBot" in message.content or "MelonManTakeMeByTheHand" in message.author.name:

        
    
    
client.run(token)
