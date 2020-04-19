import discord
from dadjokes import Dadjoke
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def replace_line(line_num, text):
    lines = open(vars.txt, 'r').readlines()
    lines[line_num] = text
    out = open(vars.txt, 'w')
    out.writelines(lines)
    out.close()

token = "Njk5NjUwMDMwNDM2NjE0MTk0.XpZswg.I5UHOM-ItuF8nze07lzNbw2u0uo"
client = discord.Client()

t = True
f = False

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    if "$react" in message.content.lower():
        if vars.readline(1):
            replace_line(1, "f")
        else:
            replace_line(1, "t")
            
    if vars.readline(1) or "Wally810" in message.author.name:
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
    
    if "$joke" in message.content.lower():
        dadjoke = Dadjoke()
        joke = dadjoke.joke
        await message.channel.send(joke)

    if "$xkcd" in message.content.lower():
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
vars.close()
