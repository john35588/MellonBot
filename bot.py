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

# Function to read lines in the vars.txt file. Returns contents of given line
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

# Function to send messages/reactions
async def reply(ros, message, text):
    if ros == "react":
        await message.add_reaction(text)
        print("Response: Reaction: " + text)

    elif ros == "send":
        await message.channel.send(text)
        print("Response: " + text)
        
    
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
        if read_line(0):
            replace_line(0, "f")
            print("Reactions Disabled")
            await message.channel.send("Reactions Disabled")
        else:
            replace_line(0, "t")
            print("Reactions Enabled")
            await message.channel.send("Reactions Enabled")
    
	# Message Reactions
    if read_line(0):
        if "22jhoff" in message.author.name or "Plasmathrower" in message.author.name:
            await reply("react", message, "🌈")
            await reply("react", message, "💕")
            
        elif "MelonManTakeMeByTheHand" in message.author.name:
            await reply("react", message, "🤮")
        else:
            await reply("react", message, "🍉")
	
	# Hey MelonBot response
    if "hey melonbot" in message.content.lower() or "hi melonbot" in message.content.lower():
        response = "Hey " + message.author.name + "!"
        await reply("send", message, response)

	# Gets random dad joke
    if "$joke" in message.content.lower():
        dadjoke = Dadjoke()
        joke = dadjoke.joke
        await reply("send", message, joke)
	
	# Gets XKCD comic
    if "$xkcd" in message.content.lower():
        request = message.content[6:]
        html = urlopen('https://xkcd.com/' + request + '/')
        bs = BeautifulSoup(html, 'html.parser')
        images = bs.find_all('img', {'src':re.compile('.png')})
        image = images[1]['src']
        image = image[2:]
        await reply("send", message, "http://" + image)
    
    if "$help" in message.content.lower():
        await reply("send", message, "https://docs.google.com/spreadsheets/d/1zOGoIlvEVDKHbX_6CTbjViChMRyQbHEGv74-gVvNUXM/edit?usp=sharing")
    

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
