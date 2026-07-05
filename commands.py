from pathlib import Path
from random import randint

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
    QUOTE_PATH = Path("./assets/quotes.txt")
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
    QURAN_PATH = Path("./assets/quran")

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
    WORDLE_PATH = Path("./assets/wordle_words.txt")
    return get_random_line(WORDLE_PATH)
