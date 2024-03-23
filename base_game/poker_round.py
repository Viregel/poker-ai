from cards import CardDeck
from hand_rankings import getPlayerHandRanking, hand_ranking_classes
import hand_rankings


class PokerRound():

    def __init__(self, players, round=0):

        self.players = players
        self.round_number = round

        if len(self.players) >= 2:

            self.cash_pool = 0

            deck = self.createDeck()

            self.dealToPlayers(self.players, deck)

            self.blind(self.players[0], 3)
            self.blind(self.players[1], 5)

            self.dealToCommunity(deck)

            self.updateCommunity(deck)

            self.updateCommunity(deck)
            self.makeBets(self.players)

            self.getPlayerRankings(self.players, deck)

            self.winner = self.determineWinner(self.players, deck)

            print("Round:", self.round_number)

        else:
            if len(self.players) == 1:
                self.winner = self.players[0]
            else:
                self.winner = "Undetermined"

    def createDeck(self):
        return CardDeck()

    def dealToPlayers(self, players, deck):
        for player in players:
            deck.dealToPlayer(player)
        pass

    def dealToCommunity(self, deck):
        deck.dealToCommunity(3)
        self.playerAccessToCommunityCards(self.players, deck)
        pass

    def updateCommunity(self, deck):
        deck.dealToCommunity()
        self.playerAccessToCommunityCards(self.players, deck)
        pass

    def getCommunityCards(self, deck):
        return deck.getCommunityCards()

    def playerAccessToCommunityCards(self, players, deck):
        for player in players:
            community_cards = self.getCommunityCards(deck)
            player.getCommunityCards(community_cards)
        pass

    def blind(self, player, n=0):
        if player.cash >= n:
            player.betBlind(n)
            self.addToCashPool(n)
        else:
            pass
        pass

    def makeBets(self, players):
        self.raise_cash = self.cash_pool
        for player in players:
            player.getPlay(self.cash_pool, self.raise_cash)
            if player.do_I_play:
                player_bet = player.raise_val
                if player_bet > self.raise_cash:
                    self.raise_cash = player_bet
                self.addToCashPool(player_bet)
            self.updatePlayerData(player)
        pass

    def addToCashPool(self, num):
        self.cash_pool += num
        pass

    def updatePlayerData(self, player):
        player.addData(self.round_number,
                       player.cash,
                       player.ev,
                       self.raise_cash,
                       player.raise_val)
        pass

    def getPlayerRankings(self, players, deck):
        player_rankings = []
        for player in players:
            player_rankings.append(getPlayerHandRanking(player, deck))
        return player_rankings

    def determineWinner(self, players, deck):
        current_highest = hand_rankings.HighCard
        current_index = hand_ranking_classes.index(current_highest)
        winner = players[0]

        for player in players:
            player_rank = getPlayerHandRanking(player, deck)
            player_index = hand_ranking_classes.index(player_rank)
            if player_index < current_index:
                current_index = player_index
                winner = player

        winner.addWin()
        winner.addCash(self.cash_pool)

        return winner

    def getWinner(self):
        return self.winner
