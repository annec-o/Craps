__author__ = 'Jamie Olsen'
import os
import random

class CrapsGame(object):

    def __repr__(self, *args, **kwargs):
        return super().__repr__(*args, **kwargs)

    def dice(self, dice):
        return True

    def menu(self):
        choice = ""
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
                self.play_game()
            elif choice == 3:
                self.play_game()
            elif choice == 4:
                break

    def play_game(self):
        point_number = 0

        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

        diceOne = random.randrange(0, 8)
        diceTwo = random.randrange(0, 8)
        print("Playing the game or craps!")

        """IF POINT NUMBER IS NOT SET"""
        """If the shooter rolls a 7 or 11 you win."""
        if diceOne+diceTwo == 7 or diceOne+diceTwo == 11:
            self.print_result("WINNER")
        """If the shooter rolls a 2, 3 or 12, you lose."""
        elif diceOne+diceTwo == 2 or diceOne+diceTwo == 3 or diceOne+diceTwo == 12:
            self.print_result("LOOSER")
        """If the shooter rolls any other number,that number becomes the point number."""
        else:
            point_number = diceOne + diceTwo

        """The shooter must roll that number again before a seven is rolled."""

        """If that happens, you win even money for your passline bet."""
        """If a seven is rolled before the point number is rolled again, you lose."""
    def print_result(self, result):
        print(result)
game = CrapsGame()
game.menu()