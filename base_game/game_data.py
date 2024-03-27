import pandas as pd

game_record = pd.DataFrame(list())
game_record.to_csv("base_game/game_records/game_record.csv")


class PlayerRecord():

    def __init__(self, player):
        self.player_data = pd.DataFrame()
        self.player = player

    def addRecord(self,
                  round_num,
                  cash,
                  ev,
                  call,
                  bet,
                  does_play,
                  win_prob,
                  pot_value):
        new_data = {"round_num": [round_num],
                    "cash": [cash],
                    "pot_value": [pot_value],
                    "call": [call],
                    "ev": [ev],
                    "win_prob": [win_prob],
                    "does_play": [does_play],
                    "bet": [bet],
                    }
        new_row = pd.DataFrame(new_data)
        self.player_data = pd.concat([self.player_data, new_row])
        pass

    def createFile(self):
        record_name = "player_" + str(self.player.name) + ".csv"
        self.player_data.to_csv("base_game/game_records/"+record_name,
                                index=False)
        pass
