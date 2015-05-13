__author__ = 'Jamie Olsen'
import os
import random


class CrapsGame(object):
    money = 500
    point_number = 0
    end_game = False
    amount = 0
    roll = 0
    dice_list = ["[0]","[0]","[0]"],["[ ]","[0]","[ ]"],["[ ]","[ ]","[ ]"],["[0]","[ ]","[0]"]
    dice_number = {1:[2,1,2],2:[2,3,2],3:[2,0,2],4:[3,2,3],5:[3,1,3],6:[3,3,3]}
    diceOne = 1
    diceTwo = 1

    def menu(self):
        choice = 0
        while choice != 4:
            print("-------------------------------")
            print("Welcome to the game of craps!")
            print("1. Play game")
            print("2. Add credits")
            print("3. How to play")
            print("4. Exit")
            print("Please make your selection:")
            choice = int(input())

            if choice == 1:
                self.play_game()
            elif choice == 2:
                pass
            elif choice == 3:
                pass
            elif choice == 4:
                break
            else:
                break

    def play_game(self):

        self.end_game = False
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

        print("Playing the game or craps!")
        print("You have {} credits".format(self.money))

        winning_numbers = [7, 11]
        losing_numbers = [2, 3, 12]
        """
        Each round has two phases: Come Out and Point. To start a round, the shooter makes one or more Come Out rolls. A Come Out
        roll of 2, 3 or 12 (called Craps, the shooter is said to 'crap out') ends the round with players losing their Pass Line bets.
        A Come Out roll of 7 or 11 (a Natural) results in a win for Pass Line bets. The shooter continues to make Come Out rolls
        until he rolls 4, 5, 6, 8, 9, or 10, which number becomes the Point."""
        """IF POINT NUMBER IS NOT SET"""
        """If the shooter rolls a 7 or 11 you win."""
        while self.end_game is False:
            self.diceOne = random.randrange(1, 6)
            self.diceTwo = random.randrange(1, 6)
            self.roll = self.diceOne + self.diceTwo
            if self.point_number == 0:
                #make a passline bet+
                bet_input = input("Would you like to make a pass line bet? [Y/n]")
                bet_input.lower()
                if bet_input == "y":
                    self.amount = input("Please enter the pass line bet: ")
                    bet_input = 0
                    self.print_dice(self.diceOne, self.diceTwo)
                if self.roll in winning_numbers:
                    self.winner()
                elif self.roll in losing_numbers:
                    """If the shooter rolls a 2, 3 or 12, you lose."""
                    self.loser()
                else:
                    self.set_point()
            elif self.roll in winning_numbers:
                self.winner()
            elif self.roll in losing_numbers:
                """If the shooter rolls a 2, 3 or 12, you lose."""
                self.print_dice(self.diceOne, self.diceTwo)
                self.end_game = True
                self.money -= int(self.amount)
                print(input("Your a loser! you lost {}".format(self.amount)))
            elif self.roll == self.point_number:
                """If the shooter rolls the point number, the result is a win for bets on the Pass Line.
                If the shooter rolls a seven (a Seven-out), the pass line loses and the round ends."""
                self.money += int(self.amount)
                self.point_number = 0
                #if point_number == roll
                #   Pass line wins!

            else:
                self.print_dice(self.diceOne, self.diceTwo)
                print(input("Press enter to roll again... "))

    """IF POINT NUMBER IS SET"""
    """The shooter must roll that number again before a seven is rolled."""
    """If that happens, you win even money for your passline bet."""
    """If a seven is rolled before the point number is rolled again, you lose."""


    def show_roll(self):
        pass

    def print_result(self, result):
        print(result)

    def set_point(self):
        self.print_dice(self.diceOne, self.diceTwo)
        print("The point number is: {}".format(self.roll))
        self.point_number = self.roll
        roll_again = input("Press enter to roll the dice again...")

    def winner(self):
        self.print_dice(self.diceOne, self.diceTwo)
        self.end_game = True
        self.point_number = 0
        print("Winner winner chicken dinner!")
        choice = input("Would you like to play again? [Y/n]")
        if choice.lower() == "y":
            self.play_game()
        else:
            pass

    def loser(self):
        self.print_dice(self.diceOne, self.diceTwo)
        self.end_game = True
        self.point_number = 0
        print(input("Your a loser!"))

    def print_dice(self, die1, die2):
        for index in range(3):
            die_1 = " ".join(self.dice_list[self.dice_number[die1][index]])
            die_2 = " ".join(self.dice_list[self.dice_number[die2][index]])
            print("{}   {}".format(die_1, die_2))
        print("You rolled a {}".format(self.roll))


    def __repr__(self, *args, **kwargs):
        return super().__repr__(*args, **kwargs)


game = CrapsGame()
game.menu()

"""
 Each round has two phases: "come-out" and "point". To start a round, the shooter
 makes one or more "come-out" rolls. A come-out roll of 2, 3 or 12 is called
 "craps" or "crapping out", and anyone betting the Pass line loses. A come-out
 roll of 7 or 11 is a "natural", and the Pass line wins. The other possible
 numbers are the point numbers: 4, 5, 6, 8, 9, and 10. If the shooter rolls one
 of these numbers on the come-out roll, this establishes the "point" - to
 "pass" or "win", the point number must be rolled again before a seven.
 The dealer flips a button to the "On" side and moves it to the point number
 signifying the second phase of the round. If the shooter "hits" the point
 value again (any value of the dice that sum to the point will do; the shooter
 doesn't have to exactly repeat the value combination of the come-out roll)
 before rolling a seven, the Pass line wins and a new round starts. If the
 shooter rolls any seven before repeating the point number (a "seven-out"),
 the Pass line loses and the dice pass clockwise to the next new shooter for
 the next round. In all the above scenarios, whenever the Pass line wins, the
 Don't Pass line loses, and vice versa, with one exception: on the come-out
 roll, a roll of 12 will cause Pass Line bets to lose, but Don't Pass bets
 are pushed (or "barred"), neither winning nor losing. (The same applies to
 "Come" and "Don't Come" bets, discussed below.)
"""