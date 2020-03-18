class Player:

    win_chance = 100

    def __init__(self, first_card, second_card):
        self.first_card = first_card
        self.second_card = second_card


def main():
    # Player amount loop
    while True:
        try:
            player_amount = int(input("Player amount: "))
        except ValueError:
            continue
        break

    player_list = list()
    for i in range(0, player_amount):
        player_list.append(Player())


if __name__ == "__main__":
    main()