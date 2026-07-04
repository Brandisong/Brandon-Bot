import discord
from os import getenv
from dotenv import load_dotenv
import commands

# Load token
load_dotenv()
TOKEN = getenv("DISCORD_TOKEN")

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
    # Ignore messages from self
    if message.author == client.user:
        return
    
    # List possible commands
    if message.content.startswith("!help"):
        await message.channel.send("Possible commands:\n"
        "!hello\n!echo [message]\n!daily_wisdom")
    
    # Say hello
    if message.content.startswith("!hello"):
        await message.channel.send("Hello!")
    
    # Echo
    if message.content.startswith("!echo"):
        response: str = message.content[5:]
        await message.channel.send(response)
    
    # Daily wisdom
    if message.content.startswith("!daily_wisdom"):
        await message.channel.send(commands.daily_wisdom())


# Run the bot
client.run(TOKEN)
