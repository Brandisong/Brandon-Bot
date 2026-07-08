from pathlib import Path
from random import randint
import json
import re

# Paths
USERDATA_PATH = Path("./userdata.json")
QUOTE_PATH = Path("./assets/quotes.txt")
QURAN_PATH = Path("./assets/quran")
WORDLE_PATH = Path("./assets/wordle_words.txt")


# Envelop text in code block for formatting
def code_block(quote: str) -> str:
    return "```" + quote + "```"


# Get a random line from a single text file
def get_random_line(path: Path) -> str:
    if path.exists():
        # Make a list of all the lines in the file
        file = open(path, "r")
        quotes = []

        for line in file:
            quotes.append(line)
        file.close() 
        
        # Choose a random quote and return it
        return quotes[randint(0, len(quotes)-1)]
    
    else:
        return "Error: quotes file not found :("


# Gives a random quote from a custom miscellaneous list
def daily_wisdom() -> str:
    return code_block(get_random_line(QUOTE_PATH))


# Gives a random fortune like a magic 8-ball
def fortune() -> str:
    fortune_list = [
        "It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "Yes",
        "Don't count on it", "My sources say no", "Unlikely", "Very doubtful", "No"]
    
    # Choose a random quote and return it
    return fortune_list[randint(0, len(fortune_list)-1)]


# Gives a random single verse from the Quran
def random_quran() -> str:
    if QURAN_PATH.exists():
        verse_list = list(QURAN_PATH.glob("*.txt"))
        
        # Pick a random verse, read it, and respond with it
        random_verse_path = verse_list[randint(0, len(verse_list)-1)]
        file = open(random_verse_path, 'r')
        response = file.read()
        file.close()
        return "Surah " + random_verse_path.name[:-4] + '\n' + code_block(response)

    else:
        return "Error: Quran files not found :("
    

# Gives a random word from the list of valid wordle words
def wordle() -> str:
    return get_random_line(WORDLE_PATH)


# Retrieves, updates, and stores aura points
def aura(content: str) -> str:
    
    # Get user id and aura points from message
    mo = re.search(r"!aura <@(\d+)> (-?\d+)", content)
    
    # If mo is invalid, search with id and use 0 as the aura to add
    if mo == None:
        mo = re.search(r"!aura <@(\d+)>", content)
        aura_to_add: int = 0
    else:
        aura_to_add: int = int(mo.group(2))

    target_user: str = mo.group(1)
    
    
    # Load json file
    f = open(USERDATA_PATH, "r")
    userdata: dict = json.load(f)
    f.close()

    # Search to see if user is already in list
    isUserInList = False
    for i in range(len(userdata["users"])):
        if userdata["users"][i]["id"] == target_user:
            # Update aura score
            total_aura = int(userdata["users"][i]["aura"]) + aura_to_add
            userdata["users"][i]["aura"] = total_aura
            isUserInList = True

    # User not found in list, make a new one
    if not isUserInList:
        userdata["users"].append({"id": target_user, "aura": aura_to_add})
        print(f"Made new user: {target_user}")
        total_aura = aura_to_add
    
    # Store the userdata as a json file
    f = open(USERDATA_PATH, "w")
    json.dump(userdata, f, indent=2)
    f.close()

    # Return the message displaying their new aura count
    return f"<@{target_user}> now has {total_aura} aura points"
