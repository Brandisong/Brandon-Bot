from pathlib import Path
from random import randint

# Gets a quote from a list
def daily_wisdom() -> str:
    QUOTE_PATH = Path("./quotes.txt")
    
    if QUOTE_PATH.exists():
        # Make a list of all the lines in the file
        file = open(QUOTE_PATH, "r")
        quotes = []

        for line in file:
            quotes.append(line)
        file.close() 
        
        # Choose a random quote and return it
        return "```" + quotes[randint(0, len(quotes)-1)] + "```"
    
    else:
        return "Error: quotes file not found :("


# Gives a random fortune like a magic 8-ball
def fortune() -> str:
    fortune_list = [
        "It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "Yes",
        "Don't count on it", "My sources say no", "Unlikely", "Very doubtful", "No"]
    
    # Choose a random quote and return it
    return fortune_list[randint(0, len(fortune_list)-1)]
