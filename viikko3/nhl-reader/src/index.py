import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    nationalities = []

    for player in players:
        if player.nationality not in nationalities:
            nationalities.append(player.nationality)
    
    sorted_players = sorted(players, key=lambda player: player.points, reverse=True)

    for nationality in nationalities:
        if nationality == "FIN":
            print(f"\nPlayers from {nationality}:\n")
            for player in sorted_players:
                if player.nationality == nationality:
                    print(player)


if __name__ == "__main__":
    main()
