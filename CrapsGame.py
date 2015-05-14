__author__ = 'Jamie Olsen'
import os
import random


class CrapsGame(object):

    money = 500
    point_number = 0
    end_game = False
    amount = 0
    roll = 0
    c_out_roll = True
    point_button_list = ["     *","*","*","*"],\
                        ["   *         *"],\
                        ["  *           *"],\

    dice_row_list = ["|","[0]","[0]","[0]","|"],["|","[_]","[0]","[_]","|"],["|","[_]","[_]","[_]","|"],["|","[0]","[_]","[0]","|"]
    dice_dict = {1:[2,1,2],2:[2,3,2],3:[2,0,2],4:[3,2,3],5:[3,1,3],6:[3,3,3]}
    diceOne = 1
    diceTwo = 1

    def menu(self):
        choice = 0
        self.clear_screen()
        while choice != 4:
            self.print_welcome("craps")
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
        self.clear_screen()
        winning_numbers = self.point_number
        losing_numbers = 7
        while self.end_game is False:

            if self.point_number == 0:

                self.come_out_roll()
            else:

                self.roll_the_dice()
            if self.roll == losing_numbers:

                self.loser()
            elif self.roll == winning_numbers:

                self.winner()
            else:

                print(input("press any button to roll again..."))
                self.roll_the_dice()


    def print_welcome(self, game):
        message = "* Welcome to the game of {}! *".format(game)
        print("*" * (len(message)))
        print("{}".format(message))
        print("*" * (len(message)))

    def roll_the_dice(self):
        self.clear_screen()
        self.diceOne = random.randrange(1, 6)
        self.diceTwo = random.randrange(1, 6)
        self.roll = self.diceOne + self.diceTwo
        self.print_dice(self.diceOne, self.diceTwo)

    def print_result(self, result):
        print(result)

    def set_point(self):
        print()
        self.point_button()
        print()
        print("The point number is set at: {}".format(self.roll))
        self.point_number = self.roll

    def winner(self):
        self.end_game = True
        self.point_number = 0
        print("Winner winner chicken dinner!")
        choice = input("Would you like to play again? [Y/n]")
        if choice.lower() == "y":
            self.play_game()
        else:
            pass

    def loser(self):
        self.end_game = True
        self.point_number = 0
        print(input("Your a loser!"))
        choice = input("Would you like to play again? [Y/n]")
        if choice.lower() == "y":
            self.play_game()
        else:
            pass

    def print_dice(self, die1, die2):
        print(" _____________     _____________")
        print("|  _   _   _  |   |  _   _   _  |")
        for index in range(3):
            die_1 = " ".join(self.dice_row_list[self.dice_dict[die1][index]])
            die_2 = " ".join(self.dice_row_list[self.dice_dict[die2][index]])
            print("{}   {}".format(die_1, die_2))
        print("|_____________|   |_____________|")
        print()
        print("You rolled a {}".format(self.roll))

    def point_button(self):
        for x in range(len(self.point_button_list)):
            pointButton = " ".join((self.point_button_list[x]))
            print("{}".format(pointButton))
        print(" *    POINT    *")
        print(" *    # SET    *")
        for x in range(len(self.point_button_list)-1,-1,-1):
            pointButton = " ".join((self.point_button_list[x]))
            print("{}".format(pointButton))

    def clear_screen(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    def come_out_roll(self):
        winning_numbers = [7, 11]
        losing_numbers = [2, 3, 12]
        #make a passline bet+
        bet_input = input("Would you like to make a pass line bet? [Y/n]")
        bet_input.lower()

        if bet_input == "y":
            self.amount = input("Please enter the pass line bet: ")
            bet_input = 0
            self.roll_the_dice()
        else:
            self.roll_the_dice()

        if self.roll in winning_numbers:
            self.winner()
        elif self.roll in losing_numbers:
            self.loser()
        else:
            self.set_point()


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