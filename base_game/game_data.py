import pandas as pd

game_record = pd.DataFrame(list())
game_record.to_csv("base_game/game_records/game_record.csv")


class PlayerRecord():

    def __init__(self, player):
        cols = ["round", "cash", "ev", "call", "bet"]
        self.player_data = pd.DataFrame(columns=cols)
        self.player = player

    def addRecord(self, round, cash, ev, call, bet):
        new_data = {"round": [round],
                    "cash": [cash],
                    "ev": [ev],
                    "call": [call],
                    "bet": [bet]}
        print(new_data)
        print("-----------------------------")
        new_row = pd.DataFrame(new_data)
        self.player_data = pd.concat([self.player_data, new_row])
        pass

    def createFile(self):
        record_name = "player_" + str(self.player.name) + ".csv"
        self.player_data.to_csv("base_game/game_records/"+record_name,
                                index=False)
        pass
