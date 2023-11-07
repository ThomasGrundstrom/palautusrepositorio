class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
    
    def top_scorers_by_nationality(self, nationality):        
        sorted_players = sorted(self.reader.players, key=lambda player: player.points, reverse=True)
        players_from_nation = []

        for player in sorted_players:
            if player.nationality == nationality:
                players_from_nation.append(player)
        
        return players_from_nation