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

    for nationality in nationalities:
        print(f"\nPlayers from {nationality}:\n")
        for player in players:
            if player.nationality == nationality:
                print(player)


if __name__ == "__main__":
    main()