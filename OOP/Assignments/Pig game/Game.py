from Player import PigPlayer, PigCPU
import random
import time

# Input win condition
win_condition = int(input("To how many points would you like to play? "))

# Create player and CPU
human = PigPlayer(1, win_condition)
computer = PigCPU(win_condition)

# Throw them in a list and shuffle to make turn order random at the start
players = [human, computer]
random.shuffle(players)

while True:
    for i in players:
        print(f"It is {i.get_player()}'s turn")
        time.sleep(1)

        # If player is not the computer, set their turn to be true and run the player_turn function
        if i.player_num != 0:
            i.player_turn()

        # If player is not a human player, call a method of the CPU depending on its style
        elif i.player_num == 0:
            i.cpu_turn()

    if not all([(x.points <= win_condition) for x in players]):
        time.sleep(1)
        print("It appears someone has met the win condition...")
        break

time.sleep(1)
player_scores = [(i.get_player(),i.points) for i in players]
winner = player_scores[0]
for i in player_scores:
    time.sleep(0.8)
    print(f"{i[0]}: {i[1]} Points")

for i in player_scores[1:]:
    if i[1] > winner[1]:
        winner = i

time.sleep(1)
print("Drumroll Please")
time.sleep(3)
print(f'Congratulations {winner[0]}, you win with {winner[1]} Points')
