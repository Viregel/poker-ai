#Define player and game

from hand_rankings import getHandRanking, hand_ranking_classes
from decision import expectedValue
import random
import math

class Player():

    player_count = 1

    def __init__(self, starting_cash=100):
        self.cash = starting_cash
        self.cards_held = []
        self.name = ""
        self.setName()
        self.num_wins = 0
        self.risk = random.uniform(0.2, 0.8)
        self.ev = 0
        self.do_I_play = True
        self.raise_val = 0
        pass 
    
    def pokerEV(self, pot, check):
        return expectedValue(pot, check, self.getBetValue())
    
    def getPlay(self, pot, check):
        self.ev = self.pokerEV(pot, check)
        self.do_I_play = self.doIPlay(self.ev)
        if not self.do_I_play:
            self.raise_val = self.howMuchDoIRaise(self.ev)
        pass
    
    def doIPlay(self,ev):
    #This function determines whether to check or fold
    #TODO: Make slightly more complex for bluffing/not overplaying mediocre hands
        if ev < 0:
            return False
        return True

    def howMuchDoIRaise(ev):
        #This function determines whether to check or raise
        #TODO: Make more complex, as above
        assert ev >= 0
        return ev

    def betBlind(self, num=0):
        if self.isBankrupt():
            return 0
        self.cash -= num 
        pass

    def getBet(self, pot, check):
        if self.isBankrupt():
            return 0
        
        bet = math.floor()

        if self.doIFold(bet):
            #Unsure what to do with this section
            #When getBet is triggered, the player should intend to bet
            #Do potential folding a step before
            pass
        
        bet = self.betHowMuchDoIRaise(bet)

        self.cash -= bet
        
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
        index = hand_ranking_classes.index(hand_ranking) + 1
        bet = 15 - index
        return 1/bet
    
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


    