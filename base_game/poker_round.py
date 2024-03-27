from cards import CardDeck
from hand_rankings import getPlayerHandRanking, hand_ranking_classes
import hand_rankings


class PokerRound():

    def __init__(self, players, round=0):

        self.players = []
        for p in players:
            if not p.is_bankrupt:
                self.players.append(p)

        self.round_number = round

        if len(self.players) >= 2:

            self.cash_pool = 0

            deck = self.createDeck()

            self.dealToPlayers(self.players, deck)

            self.blind(self.players[0], 3)
            self.blind(self.players[1], 5)
            self.makeBets(self.players[2:])

            self.dealToCommunity(deck)
            self.makeBets(self.players)

            self.updateCommunity(deck)
            self.makeBets(self.players)

            self.updateCommunity(deck)
            self.makeBets(self.players)

            self.getPlayerRankings(self.players, deck)

            self.winner = self.determineWinner(self.players, deck)

        else:
            if len(self.players) == 1:
                self.winner = self.players[0]
            else:
                self.winner = "Undetermined"

    def createDeck(self):
        return CardDeck()

    def dealToPlayers(self, player_list, deck):
        for player in player_list:
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

    def playerAccessToCommunityCards(self, players_pool, deck):
        for player in players_pool:
            community_cards = self.getCommunityCards(deck)
            player.getCommunityCards(community_cards)
        pass

    def blind(self, player, n=0):
        if player.cash >= n:
            player.betBlind(n)
            self.addToCashPool(n)
        else:
            self.removeBankrupt(player)
        pass

    def makeBets(self, players_pool):
        self.raise_cash = 0
        for player in players_pool:
            if player.cash <= 0:
                self.removeBankrupt(player)
            else:
                player.getPlay(self.cash_pool, self.raise_cash)
                if player.do_I_play:
                    player_bet = player.raise_val
                    self.addToCashPool(player_bet)
                self.updatePlayerData(player)
                if player_bet > self.raise_cash:
                    self.raise_cash = player_bet
        pass

    def removeBankrupt(self, player):
        player.declareBankrupt()
        self.players.remove(player)
        pass

    def addToCashPool(self, num):
        self.cash_pool += num
        pass

    def updatePlayerData(self, player):
        player.addData(self.round_number,
                       player.cash,
                       player.ev,
                       self.raise_cash,
                       player.raise_val,
                       player.do_I_play)
        pass

    def getPlayerRankings(self, players_pool, deck):
        player_rankings = []
        for player in players_pool:
            player_rankings.append(getPlayerHandRanking(player, deck))
        return player_rankings

    def determineWinner(self, players_pool, deck):
        current_highest = hand_rankings.HighCard
        current_index = hand_ranking_classes.index(current_highest)
        winner = players_pool[0]

        for player in players_pool:
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
