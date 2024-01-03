"""
print-10.py

Experiment to translate the "tiled-lines tutorial from generative artistry 
  https://generativeartistry.com/tutorials/tiled-lines/
into Python code using simple print statements. Which in turn is based on the
10 PRINT generative approach from the old Commodore 64

i.e.  10 PRINT CHR$(205.5+RND(1)); : GOTO 10

╱╲╲╱╱╲╲╱╱╱╲╲╱╱╱╱╱╲╲╲
╲╱╲╱╱╲╱╱╲╱╱╲╱╱╱╲╲╲╱╲
╲╱╱╲╱╲╲╲╲╱╲╱╱╱╲╲╲╲╱╱
╲╱╱╱╱╲╱╲╱╱╱╲╱╲╲╲╲╲╲╲
╱╱╲╱╲╲╱╲╲╲╲╱╲╱╱╲╱╱╲╱
╲╱╲╲╲╱╲╲╱╱╱╲╱╲╲╱╱╱╱╲
╱╱╱╱╱╲╱╱╲╱╲╱╲╱╲╲╲╲╱╱
╲╲╲╲╲╱╲╲╲╱╱╲╱╲╲╱╱╱╲╱
╱╲╲╱╲╲╱╲╲╱╲╱╱╲╱╲╲╱╱╱
╲╱╱╱╱╱╱╲╱╱╲╲╱╲╱╲╲╲╲╱

What I learned

- the presence of the random.choice function
- that the character set (UniCode better than ASCII) and font of your terminal can make a difference
"""

import random

global MAX_ROWS
global MAX_COLS
MAX_ROWS = 20 
MAX_COLS = 60

def print10( addRows : bool = True ):
    """
    Implement original/basic 10 PRINT algorithm by
    
    - defining an array of two characters / and \
    - then loop forever printing a random character from the array

    --- Parameters ---
    addRows : boolean
        if True then add a newline after every MAX_COLS characters
        if False then print all characters on the same line
    """

    # define the 2 characters to use
    # - ASCII versions don't look nice
    # characters = ["/", "\\"]
    # - Unicode versions line up much more nicely
    characters = ["╱", "╲"]
    # loop forever
    column = 0
    row = 0
    finished = False
    while not finished:
        #character = characters[random.randint(0, 1)]
        # - learnt about the choice function which is a bit nicer
        character = random.choice(characters)

        print(character, end="")

        column += 1
        if not addRows:
            finished = ( column == MAX_COLS * MAX_ROWS )
        elif column == MAX_COLS:
            print()
            column = 0
            row += 1
            finished = ( row == MAX_ROWS )
        

if __name__ == "__main__":

    print10()

    print()
    print10( False)