import discord
from os import getenv
from dotenv import load_dotenv
import commands # My own command library - for most mid-sized commands
# import ai # Also my own library - for LLM prompting

# Load token
load_dotenv()
TOKEN = getenv("DISCORD_TOKEN")

# Help command list
help_list = ["!help", "!hello", "!echo [message]", "!daily_wisdom", "!fortune", "!random_quran", "!wordle", "!wordle_hidden",
             "!aura [@user] [optional: points to add]"]
help_list.sort()

# Set up the client
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents, activity=discord.Game(name="Use !help for commands"))


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
    
    # Attempted command - log message
    print(f"{message.author}: {message.content}")

    # COMMANDS
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
    elif message.content.startswith("!brandon"):
        await message.channel.send("Brandon")

    # !joanna - Say heart to Joanna
    elif message.content.startswith("!joanna"):
        await message.channel.send(":heart:")
    
    # !echo - Repeat last message
    elif message.content.startswith("!echo"):
        response: str = message.content[5:]
        await message.channel.send(response)
    
    # !daily_wisdom - Say a random quote
    elif message.content.startswith("!daily_wisdom"):
        await message.channel.send(commands.daily_wisdom())
    
    # !fortune - Returns a random fortune
    elif message.content.startswith("!fortune"):
        await message.channel.send(commands.fortune())

    # !random_quran - Returns a random Quran verse
    elif message.content.startswith("!random_quran"):
        await message.channel.send(commands.random_quran())
    
    # !wordle_hidden - Same as above but hides it as a spoiler
    elif message.content.startswith("!wordle_hidden"):
        await message.channel.send("||" + commands.wordle() + "||")
    
    # !wordle - Returns a random valid wordle word
    elif message.content.startswith("!wordle"):
        await message.channel.send(commands.wordle())

    # # !ask_brandon - Prompts a small local LLM (disabled as it's a work in progress)
    # elif message.content.startswith("!ask_brandon"):
    #     prompt = message.content[12:]
    #     await message.channel.send(ai.ask_brandon(prompt))

    # !aura - Store and display aura points
    elif message.content.startswith("!aura"):
        await message.channel.send(commands.aura(message.content))


# Run the bot
client.run(TOKEN)
