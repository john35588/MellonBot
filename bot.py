import discord # Connects bot to discord
from dadjokes import Dadjoke # Gets random Dad Jokes
from urllib.request import urlopen # Used for getting XKCD images
from bs4 import BeautifulSoup # also for getting XKCD images
import re # Compiles images from XKCD for later access

# Function to replace lines in the vars.txt file
def replace_line(line_num, text):
    lines = open("vars.txt", "r").readlines()
    lines[line_num] = text
    out = open("vars.txt", 'w')
    out.writelines(lines)
    out.close()

# Function to read lines in the vars.txt file
def read_line(line_num):
    lines = open("vars.txt", "r")
    text = lines.readlines()
    text = text[line_num]
    lines.close()
    if text == "t":
        react = True
    else:
        react = False
    return(react)
token = "Njk5NjUwMDMwNDM2NjE0MTk0.XpZswg.I5UHOM-ItuF8nze07lzNbw2u0uo"
client = discord.Client()

# When the bot is connected
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# When a message is sent to any channel
@client.event
async def on_message(message):
	# Print: ....Channel.............Author.........Author Username..........Message.......
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
	
	# Toggles reactions
    if "$react" in message.content.lower():
        if read_line(1):
            replace_line(1, "f")
            print("Reactions Disabled")
        else:
            replace_line(1, "t")
            print("Reactions Enabled")
    
	# Message Reactions
    if read_line(1) or "Wally810" in message.author.name:
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
	
	# Hey MelonBot response
    if "hey melonbot" in message.content.lower() or "hi melonbot" in message.content.lower():
        await message.channel.send("Hey " + message.author.name + "!")
    
	# Gets random dad joke
    if "$joke" in message.content.lower():
        dadjoke = Dadjoke()
        joke = dadjoke.joke
        await message.channel.send(joke)
	
	# Gets XKCD comic
    if "$xkcd" in message.content.lower():
        request = message.content[6:]
        html = urlopen('https://xkcd.com/' + request + '/')
        bs = BeautifulSoup(html, 'html.parser')
        images = bs.find_all('img', {'src':re.compile('.png')})
        image = images[1]['src']
        image = image[2:]
        print(image)
        await message.channel.send("http://" + image)

	# Deletes MelonMan's messages
#    if "MelonManTakeMeByTheHand" in message.author.name:
#        await message.delete()

# Makes bot's messages undeletable
#@client.event
#async def on_message_delete(message):
#    if "MelonBot" in message.author.name:
#        await message.channel.send(message.content)

# Checks token authenticity with discord
client.run(token)
