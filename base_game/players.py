#Define player and game

from hand_rankings import getHandRanking, hand_ranking_classes

class Player():

    player_count = 1

    def __init__(self, starting_cash=100):
        self.cash = starting_cash
        self.cards_held = []
        self.name = ""
        self.setName()
        self.num_wins = 0
        pass

    def betBlind(self, num=0):
        if self.isBankrupt():
            return 0
        self.cash -= num 
        pass

    def getBet(self):
        if self.isBankrupt():
            return 0
        bet = self.getBetValue()
        if bet >= self.cash:
            bet = self.cash
        self.cash -= bet
        #TODO: If player is about to go bankrupt, shouldn't bet more than they have
        
        return bet

    def fold(self):
        #TODO
        pass

    def isBankrupt(self):
        #TODO: If this triggers, remove player from game
        if self.cash <= 0:
            return True

    def getBetValue(self):
        #TODO: Update to make this more "intelligent"
        hand_ranking = getHandRanking(self.cards_held)
        index = hand_ranking_classes.index(hand_ranking)
        bet = 15 - index
        return bet
    
    def getCommunityCards(self, community_cards):
        return community_cards

    def getCards(self):
        return self.cards_held
    
    def addWin(self):
        self.num_wins += 1
        pass

    def addCash(self, num):
        self.cash += num
        pass

    def getNumWins(self):
        return self.num_wins
    
    def setCards(self, cards):
        self.cards_held = cards
        pass

    def resetCards(self):
        self.cards_held = []
        pass

    def setName(self):
        self.name = Player.player_count
        Player.player_count += 1
        pass
    
    def resetPlayers(self):
        Player.player_count = 1
        pass
        
    def getCash(self):
        return self.cash



#Store players here
#TODO: Work into a class.
    
class Players():

    def __init__(self, n):
        player_list = []
        for p in range(n):
            newPlayer = Player()
            self.player_list.append(newPlayer)
        return self.player_list


    