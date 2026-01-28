# Librairies

from src.gamedata_path import *

# Variables

FILE_PATH = get_gamedata_path("best_score.txt")

# Functions

def read_best_score_file():

    '''
    Read the config file from the file path FILE_PATH
    For now only contains dark mode state
    ### RETURN
            [str]
    '''

    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return int([line.rstrip("\n") for line in f][0])
    
def write_best_score(score):

    with open(FILE_PATH, "w", encoding="utf-8") as f:
        f.writelines(f"{score}\n")