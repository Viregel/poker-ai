from hand_rankings import getHandRanking, hand_ranking_classes
from decision import expectedValue
import random
from game_data import PlayerRecord


class Player():

    player_count = 1

    hand_ranking_probs = [.000032,
                          .000279,
                          .00168,
                          .026,
                          .0303,
                          .0462,
                          .0483,
                          .235,
                          .438,
                          .174]

    def __init__(self, starting_cash=100):
        self.cash = starting_cash
        self.cards_held = []
        self.name = Player.player_count
        Player.player_count += 1
        self.num_wins = 0
        self.risk = random.uniform(1, 1.5)
        self.ev = 0
        self.do_I_play = True
        self.raise_val = 0
        self.is_bankrupt = False
        self.record = PlayerRecord(self)

    def setCards(self, cards):
        self.cards_held = cards
        pass

    def getCommunityCards(self, community_cards):
        return community_cards

    def getCards(self):
        return self.cards_held

    def getCash(self):
        return self.cash

    def betBlind(self, num=0):
        if self.is_bankrupt:
            return 0
        elif self.cash - num < 0:
            self.is_bankrupt = True
        else:
            self.cash -= num
        pass

    def pokerEV(self, pot, check):
        poker_ev = expectedValue(pot, check, self.getBetValue())
        poker_ev = round(poker_ev)

        return poker_ev

    def doIPlay(self, ev):
        if ev < 0:
            return False
        if self.is_bankrupt:
            return False
        return True

    def howMuchDoIBet(self, ev, check):
        assert ev >= 0
        bet = max(ev, check)
        return bet

    def getBetValue(self):
        hand_ranking = getHandRanking(self.cards_held)
        index = hand_ranking_classes.index(hand_ranking)
        prob_highest = 1 - sum(self.hand_ranking_probs[:index])
        return prob_highest

    def getPlay(self, pot, check):
        self.ev = self.pokerEV(pot, check)
        self.do_I_play = self.doIPlay(self.ev)
        if self.do_I_play:
            self.raise_val = self.howMuchDoIBet(self.ev, check)
            if self.cash - self.raise_val < 0:
                self.raise_val = self.cash
            self.cash -= self.raise_val
        pass

    def addCash(self, num):
        self.cash += num
        pass

    def addWin(self):
        self.num_wins += 1
        pass

    def getNumWins(self):
        return self.num_wins

    def resetPlayers(self):
        Player.player_count = 1
        pass

    def resetCards(self):
        self.cards_held = []
        pass

    def addData(self, round, cash, ev, call, bet):
        self.record.addRecord(round, cash, ev, call, bet)
        pass

    def playInfo(self, pot, check):
        print("Player", self.name)
        print("Pot: ", pot, " Check: ", check)
        print("Bet value: ", self.getBetValue(), "EV: ", self.ev)
        print("Money in: ", self.raise_val)
        print("----------------------------------")
        pass
