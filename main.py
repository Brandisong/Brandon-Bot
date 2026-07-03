import discord
from os import getenv
from dotenv import load_dotenv

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

# Say hello
@client.event
async def on_message(message):
    # Ignore messages from self
    if message.author == client.user:
        return
    
    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")


# Run the bot
client.run(TOKEN)