import random
import time


class PigPlayer:
    # Assign a number to each player and keep track of their total points, round points, and if it's their turn
    def __init__(self, num, condition):
        self.player_num = num
        self.points = 0
        self.round = 0
        self.turn = False
        self.win_condition = condition

    def roll(self):
        # Roll 2 dice
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)

        print(f"You rolled a {die1} and a {die2}")

        value = die1 + die2

        # Condition where if they roll two 6's they lose all total points and round points
        if die1 == 6 and die2 == 6:
            time.sleep(1)
            print("You lose all points")
            self.points = 0
            self.round = 0
            self.turn_end()

        # Condition where if they roll one 6 they lose all round points
        elif die1 ==6 or die2 == 6:
            time.sleep(1)
            print(f"You lost all points this round")
            self.round = 0
            self.turn_end()

        # If they roll normal they just add the total to the round points and can roll again
        else:
            time.sleep(1)
            self.round += value
            print(f"{self.round} is now your total points this round")

    def player_turn(self):
        self.turn = True
        self.roll()
        while self.turn:
            print(f"Points this round: {self.round}\nTotal points: {self.points}")
            time.sleep(1)
            action = input("What would you like to do?\n[roll or end]: ")

            if action == 'roll':
                self.roll()

            elif action == 'end':
                self.turn_end()

            else:
                print("Please enter a valid action")

    def turn_end(self):
        time.sleep(1)
        self.points += self.round
        print(f"Your turn is over, adding {self.round} to your total points leaves you with {self.points} points")
        self.round = 0
        self.turn = False

    def get_player(self):
        if self.player_num != 0:
            return f"Player {self.player_num}"
        else:
            return "CPU"


class PigCPU(PigPlayer):
    def __init__(self, condition):
        super().__init__(0, condition)
        self.style = self.style_chooser()
        self.roll_count = 0
        self.six_prob = (5/6) ** self.roll_count

    @staticmethod
    def style_chooser():
        return random.randint(1,3)

    def cpu_turn(self):
        self.turn = True
        self.roll_count = 2
        self.roll()
        while self.turn:
            print(f"Points this round: {self.round}\nTotal points: {self.points}")
            time.sleep(1)

            if self.style == 1:
                self.spontaneous_play()
                break

            elif self.style == 2:
                self.safe_play()
                break

            elif self.style == 3:
                self.risky_play()
                break

    def spontaneous_play(self):
        while self.turn:
            choice = random.randint(1,2)
            if self.round + self.turn >= self.win_condition:
                self.turn_end()
            elif choice == 1:
                time.sleep(1)
                self.roll_count += 2
                self.roll()
            else:
                self.turn_end()

    def safe_play(self):
        while self.turn:
            if self.round + self.turn >= self.win_condition:
                self.turn_end()
            elif self.six_prob > 0.6:
                time.sleep(1)
                self.roll_count += 2
                self.roll()
            else:
                self.turn_end()

    def risky_play(self):
        while self.turn:
            if self.round + self.turn >= self.win_condition:
                self.turn_end()
            elif self.six_prob > 0.4:
                time.sleep(1)
                self.roll_count += 2
                self.roll()
            else:
                self.turn_end()
