import discord
from dadjokes import Dadjoke
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

from vars import var1

print(var1)

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
    elif "MelonManTakeMeByTheHand" in message.author.name:
        await message.add_reaction("🤮")
    else:
        await message.add_reaction("🍉")
        print("Response: Added reaction: 🍉")
		
    if "hey melonbot" in message.content.lower() or "hi melonbot" in message.content.lower():
        await message.channel.send("Hey " + message.author.name + "!")
    
    if "!joke" in message.content.lower():
        dadjoke = Dadjoke()
        joke = dadjoke.joke
        await message.channel.send(joke)

    if "!xkcd" in message.content.lower():
        request = message.content[6:]
        html = urlopen('https://xkcd.com/' + request + '/')
        bs = BeautifulSoup(html, 'html.parser')
        images = bs.find_all('img', {'src':re.compile('.png')})
        image = images[1]['src']
        image = image[2:]
        print(image)
        await message.channel.send("http://" + image)
		
#    if "MelonManTakeMeByTheHand" in message.author.name:
#        await message.delete()
        
#@client.event
#async def on_message_delete(message):
#    if "MelonBot" in message.author.name:
#        await message.channel.send(message.content)
    
   
client.run(token)
