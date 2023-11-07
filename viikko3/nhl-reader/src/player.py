class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict["team"]
        self.nationality = dict["nationality"]
        self.goals = dict["goals"]
        self.assists = dict["assists"]
        self.games = dict["games"]
        self.penalties = dict["penalties"]
    
    def __str__(self):
        return f"{self.name}, Team: {self.team}, Goals: {self.goals}, Assists: {self.assists}"
