

def expectedValue(win_val, op_cost, win_odds):
    """
    win_val: value up for grabs
    op_cost: amount it will cost player to play
    win_odds: probability the player will win
    """
    ev = win_val*win_odds - op_cost*(1-win_odds)
    return ev

class gameTree():
    def __init__(self, a, b):
        pass


#Extended Form game