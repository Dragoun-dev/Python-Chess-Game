""" 
Storing all information about the current state of a chess and determin valid move at the current state
It will also keep a move log
"""

class GameState():
    def __init__(self):
        # Board is an 8*8 2d list, each element of the list has 2 characters.
        # The firt character represent the color of the peace, 'b' or 'w'
        # the second character represnet the type of the pece, 'K', 'Q', 'R', 'B','N','P'
        # "--" - REPRESNET AN EMPTY SPACE WITH NO PEACE
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK","bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp","wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK","wB", "wN", "wR"]]
        
        self.whiteToMove = True
        self.moveLog = []