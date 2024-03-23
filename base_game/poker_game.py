from players import Player
from poker_round import PokerRound


class PokerGame():

    def __init__(self, num_players=5, rounds=10):
        self.rounds = rounds
        self.players = self.createPlayers(num_players)

        self.num_wins = [0]*len(self.players)

        self.playGame(self.rounds)

        self.resetGame()

        pass

    def resetGame(self):
        self.players[0].resetPlayers()
        pass

    def playGame(self, rounds):
        for round in range(1, rounds+1):
            current_players = []
            for player in self.players:
                if not player.is_bankrupt:
                    current_players.append(player)
            PokerRound(current_players, round)
            self.changePlayerOrder()

    def changePlayerOrder(self):
        first_player = self.players[:1]
        other_players = self.players[1:]
        self.players = other_players + first_player
        return self.players

    def listWins(self):
        for player in self.players:
            player.record.createFile()
            print(player.getNumWins(), player.getCash())

    def createPlayers(self, n=5):
        player_list = []
        for i in range(n):
            new_player = Player()
            player_list.append(new_player)
        return player_list

    def updateNumWins(self, player_index):
        self.num_wins[player_index] += 1
        pass

    def getPlayers(self):
        return self.players

    def getNumWins(self):
        self.resetGame()
        return self.num_wins
