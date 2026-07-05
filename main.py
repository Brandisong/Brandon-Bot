import discord
from os import getenv
from dotenv import load_dotenv
import commands # My own command library

# Load token
load_dotenv()
TOKEN = getenv("DISCORD_TOKEN")

# Help command list
help_list = ["!help", "!hello", "!echo [message]", "!daily_wisdom", "!fortune", "!random_quran"]
help_list.sort()

# Set up the client
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


# EVENTS
# State ready in console
@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

# Screen for commands
@client.event
async def on_message(message):
    # Don't bother if it doesn't start with a '!'
    if not message.content.startswith('!'):
        return
    
    # Ignore messages from self
    if message.author == client.user:
        return
    
    # !help - List possible commands
    if message.content.startswith("!help"):
        response = "Possible commands:\n```"
        for command in help_list:
            response += command + '\n'
        response += "```"
        await message.channel.send(response)
    
    # !hello - Say hello
    if message.content.startswith("!hello"):
        await message.channel.send("Hello!")

    # !brandon - Say Brandon
    if message.content.startswith("!brandon"):
        await message.channel.send("Brandon")

    # !joanna - Say heart to Joanna
    if message.content.startswith("!joanna"):
        await message.channel.send(":heart:")
    
    # !echo - Repeat last message
    if message.content.startswith("!echo"):
        response: str = message.content[5:]
        await message.channel.send(response)
    
    # !daily_wisdom - Say a random quote
    if message.content.startswith("!daily_wisdom"):
        await message.channel.send(commands.daily_wisdom())
    
    # !fortune - Returns a random fortune
    if message.content.startswith("!fortune"):
        await message.channel.send(commands.fortune())

    # !random_quran - Returns a random Quran verse
    if message.content.startswith("!random_quran"):
        await message.channel.send(commands.random_quran())


# Run the bot
client.run(TOKEN)
