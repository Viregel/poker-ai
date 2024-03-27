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
        self.is_forced_bet = False
        Player.player_count += 1
        self.num_wins = 0
        self.risk = random.uniform(1, 1.5)
        self.ev = 0
        self.do_I_play = True
        self.raise_val = 0
        self.is_bankrupt = False
        self.record = PlayerRecord(self)
        self.pot = 0

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
        if self.cash - num <= 0:
            self.is_bankrupt = True
        elif self.is_bankrupt:
            return 0
            # TODO: Should remove player if round happening
        else:
            self.cash -= num
        pass

    def pokerEV(self, pot, check):
        self.pot = pot
        poker_ev = expectedValue(pot, check, self.getBetValue())
        poker_ev = round(poker_ev)

        return poker_ev

    def doIPlay(self, ev, check):
        if self.is_forced_bet:
            if self.is_bankrupt:
                return False
            else:
                return True
        if ev < check:
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
        self.do_I_play = self.doIPlay(self.ev, check)
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

    def declareBankrupt(self):
        self.is_bankrupt = True
        pass

    def getNumWins(self):
        return self.num_wins

    def resetPlayers(self):
        Player.player_count = 1
        pass

    def resetCards(self):
        self.cards_held = []
        pass

    def addData(self, round_num, cash, ev, call, bet, does_play):
        self.record.addRecord(round_num,
                              cash,
                              ev,
                              call,
                              bet,
                              does_play,
                              round(self.getBetValue(), 3),
                              int(self.pot))
        pass

    def playInfo(self, pot, check):
        print("Player", self.name)
        print("Pot: ", pot, " Check: ", check)
        print("Bet value: ", self.getBetValue(), "EV: ", self.ev)
        print("Money in: ", self.raise_val)
        print("----------------------------------")
        pass
