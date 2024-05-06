import itertools as it
import random
import time
from copy import deepcopy

suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
ranks = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
deck = list(it.product(ranks, suits))
false_deck = deepcopy(deck)
random.shuffle(false_deck)


class Hand:
    # Accept a number to identify player, as well as the money they possess
    def __init__(self, number):
        self.player_num = number
        # Generate hand by choosing randomly from deck
        self.hand = [random.choice(false_deck) for x in range(2)]

    # Add a card to hand
    def hit(self):
        self.hand.append(random.choice(false_deck))

    # Do nothing
    def stay(self):
        pass

    def get_player_num(self):
        if self.player_num == 0:
            return "Dealer"

        else:
            return f"Player {self.player_num}"

    def hand_value(self):
        deck_value = 0
        count = 0

        for card in self.hand:
            if card[0] == "A":
                count += 1

            elif card[0] == "King" or card[0] == "Queen" or card[0] == "Jack":
                deck_value += 10

            else:
                deck_value += card[0]

        if count == 1 and deck_value <= 10:
            deck_value += 11

        elif count >= 1 and deck_value > 10:
            deck_value += count

        elif count > 1:
            deck_value += count

        return deck_value


def dealer_turn(dealer):
    print("It is now the dealers turn")
    while True:
        if dealer.hand_value() < 12:
            time.sleep(1)
            print("The dealer hits")
            dealer.hit()

        elif 12 <= dealer.hand_value() < 14:
            roll = random.randint(1, 2)
            if roll == 1:
                time.sleep(1)
                print("The dealer hits")
                dealer.hit()
            else:
                time.sleep(1)
                print(f"The dealer stays, they have {len(dealer.hand)} cards")
                dealer.stay()
                break

        elif 14 <= dealer.hand_value() < 18:
            roll = random.randint(1, 5)
            if roll == 1:
                time.sleep(1)
                print("The dealer hits")
                dealer.hit()
            else:
                time.sleep(1)
                print(f"The dealer stays, they have {len(dealer.hand)} cards")
                dealer.stay()
                break

        elif 18 <= dealer.hand_value() < 21:
            roll = random.randint(1, 20)
            if roll == 1:
                time.sleep(1)
                print("The dealer hits")
                dealer.hit()
            else:
                time.sleep(1)
                print(f"The dealer stays, they have {len(dealer.hand)} cards")
                dealer.stay()
                break

        else:
            time.sleep(1)
            print(f"The dealer stays, they have {len(dealer.hand)} cards")
            break

        if dealer.hand_value() > 21:
            print("The dealer busts")
            break


def turn(i):
    while True:
        move = input(
            f"{i.hand}: Points({i.hand_value()})\nWhat would you like to do? (please enter hit or stay): ").casefold()
        if move == "stay":
            i.stay()
            break

        elif move == "hit":
            i.hit()
            if i.hand_value() > 21:
                print(f"{i.get_player_num()} busts")
                break
        else:
            print("Please enter a proper move")


def comparison(player_1, player_2, ranks):
    highest_1 = 0
    highest_2 = 0

    for i in player_1.hand:
        if ranks.index(i[0]) > highest_1:
            highest_1 = ranks.index(i[0])

    for i in player_2.hand:
        if ranks.index(i[0]) > highest_2:
            highest_2 = ranks.index(i[0])

    if highest_1 > highest_2:
        return player_1

    elif highest_2 > highest_1:
        return player_2

    elif highest_2 == highest_1:
        return random.choice([player_2, player_1])


def winner(players):
    champ = []

    for i in players:
        time.sleep(1)
        print(f"{i.get_player_num()}'s Hand: {i.hand}\nPoints: {i.hand_value()}")
        if len(champ) == 0 and i.hand_value() < 22:
            champ.append(i)

        else:
            # Comparing hands
            if champ[0].hand_value() < i.hand_value() < 22:
                champ[0] = i

            # If hand values are equal compare the highest value card (For simplicity King is highest)
            elif i.hand_value() == champ[0].hand_value():
                champ[0] = comparison(i, champ[0], ranks)
    if len(champ) == 1:
        return champ[0]
    else:
        return 'none'


print("Your goal is to get the closest to 21 without going higher than 21.")
num_players = int(input("How many players will be joining us today? "))
players = [Hand(0)]

# Dealer generation

# Player Generation
for i in range(1, num_players + 1):
    player = Hand(i)
    players.append(player)

while True:
    # Playing the game
    for current in players:
        # Dealer turn
        if current.player_num == 0:
            dealer_turn(current)

        # Player turn
        elif current.player_num != 0:
            confirmation = input(f"It is now {current.get_player_num()}'s turn, please hit enter when ready. ")
            turn(current)

    results = input("It seems like everyone is content with their decks. Please hit enter to see results.")
    final = winner(players)
    break

if final == 'none':
    print("Everyone Busted")

else:
    print(f"{final.get_player_num()} won the game with {final.hand_value()} points!")
