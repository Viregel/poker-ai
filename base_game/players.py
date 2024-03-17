#Define player and game

class Player():

    player_count = 1

    def __init__(self, starting_cash=100):
        self.cards_held = []
        self.name = ""
        self.setName()
        pass

    def getCards(self):
        return self.cards_held
    
    def setCards(self, cards):
        self.cards_held = cards
        pass

    def resetCards(self):
        self.cards_held = []
        pass

    def setName(self):
        self.name = "Player " + str(Player.player_count)
        Player.player_count += 1
        pass
    
    def resetPlayers(self):
        Player.player_count = 1
        pass
        



#Store players here
#TODO: Work into a class.
    
class Players():

    def __init__(self, n):
        player_list = []
        for p in range(n):
            newPlayer = Player()
            self.player_list.append(newPlayer)
        return self.player_list


    