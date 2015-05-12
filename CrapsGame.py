__author__ = 'Jamie Olsen'
import os
import random


class CrapsGame(object):
    money = 500
    point_number = 0
    end_game = False
    amount = 0


    def dice(self, dice):
        return True

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
                print("Playing the game or craps!")
                print("You have {} credits".format(self.money))
                self.play_game(credits)
            elif choice == 2:
                pass
            elif choice == 3:
                pass
            elif choice == 4:
                break
            else:
                break

    def play_game(self, credits):

        self.end_game = False
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

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

            if self.point_number == 0:
                #make a passline bet+
                bet_input = input("Would you like to make a pass line bet? [Y/n]")
                bet_input.lower()
                if bet_input == "y":
                    self.amount = input("Please enter the pass line bet: ")
                    bet_input = "Q"
                    diceOne = random.randrange(0, 7)
                    diceTwo = random.randrange(0, 7)
                    roll = diceOne + diceTwo
                    print("You rolled a {}".format(roll))
                if roll in winning_numbers:
                    self.end_game = True
                    self.point_number = 0
                    self.winner()
                elif roll in losing_numbers:
                    """If the shooter rolls a 2, 3 or 12, you lose."""
                    self.end_game = True
                    self.point_number = 0
                    print(input("Your a loser!"))
                else:
                    print("The point number is: {}".format(roll))
                    self.point_number = roll
                    roll_again = input("Press enter to roll the dice...")
            elif roll in winning_numbers:
                self.end_game = True
                self.point_number = 0
                self.winner()
            elif roll in losing_numbers:
                """If the shooter rolls a 2, 3 or 12, you lose."""
                self.end_game = True
                self.money -= int(self.amount)
                print(input("Your a loser! you lost {}".format(self.amount)))
            elif roll == self.point_number:
                """If the shooter rolls the point number, the result is a win for bets on the Pass Line.
                If the shooter rolls a seven (a Seven-out), the pass line loses and the round ends."""
                self.money += int(self.amount)
                self.point_number = 0
                #if point_number == roll
                #   Pass line wins!

            else:
                print(input("Press enter to roll again... "))






    """IF POINT NUMBER IS SET"""
    """The shooter must roll that number again before a seven is rolled."""
    """If that happens, you win even money for your passline bet."""
    """If a seven is rolled before the point number is rolled again, you lose."""


    def show_roll(self):
        pass

    def print_result(self, result):
        print(result)


    def winner(self):
        print("Winner winner chicken dinner!")
        choice = input("Would you like to play again? [Y/n]")
        if choice.lower() == "y":
            self.play_game()
        else:
            self.menu()


    def looser(self):
        """
            what happens when you loose a game
            :return:
            """
        pass


    def __repr__(self, *args, **kwargs):
        return super().__repr__(*args, **kwargs)


game = CrapsGame()
game.menu()

"""
 The dealer then moves an On button to the point number
signifying the second phase of the round.

The first roll of the dice in a betting round is the Come Out roll - a new game in Craps begins with the Come Out roll.
A Come Out roll can be made only when the previous shooter fails to make a winning roll, that is, fails to make the Point
or makes a Seven-out (rolls a seven).

A new game then begins with a new shooter. If the current shooter does make his Point, the dice are returned to him and
he then begins the new Come Out roll. This is a continuation of that shooter's roll, although technically, the Come Out
roll identifies a new game about to begin.

When the shooter fails to make his or her Point, the dice are then offered to the next player for a new Come Out roll and
the game continues in the same manner. The new shooter will be the person directly next to the left of the previous
shooter - so the game moves in a clockwise fashion around the craps table.

The dice are rolled across the craps table layout. The layout is divided into three areas - two side areas separated by a
center one. Each side area is the mirror reflection of the other and contains the following: Pass and Don't Pass line bets,
Come and Don't Come bets, Odds bet, Place bets and Field bets. The center area is shared by both side areas and contains
the Proposition bets.

Pass bets win when the come out roll is 7 or 11, while pass bets lose when the come out roll is 2, 3, or 12. Don't bets
lose when the come out roll is 7 or 11, and don't bets win when the come out roll is 2 or 3. Don't bets tie when the come
out roll is 12 (2 in some casinos; the 'Bar' roll on the layout indicates which roll is treated as a tie).

A player joining a game and wishing to play craps without being the shooter should approach the craps table and first
check to see if the dealer's 'On' button is on any of the point numbers. If the point number is Off then the table is in
the Come Out round. If the dealer's button is 'On', the table is in the Point round where most casinos will allow a Pass
Line bet to be placed. All single or multi roll 'Proposition bets' may be placed in either of the two rounds.

Between dice rolls there is a period for the dealers to make payouts and collect the losing bets, after which players
can place new bets. The stickman monitors the action at the table and decides when to give the shooter the dice, after
which no more betting is allowed.

Below is a list of the various bets you can make at craps.

Pass Line Bet - You win if the first roll is a natural (7, 11) and lose if it is craps (2, 3, 12). If a point is rolled
(4, 5, 6, 8, 9, 10) it must be repeated before a 7 is thrown in order to win. If 7 is rolled before the point you lose.

The fundamental bet in craps is the Pass Line Bet, which is a bet for the shooter to win their point number. A Pass Line
Bet is won immediately if the Come Out roll is a 7 or 11. If the Come Out roll is 2, 3 or 12, the bet loses
(known as 'crapping out'). If the roll is any other value, it establishes a Point; if that point is rolled again before
a seven, the bet wins. If, with a point established, a seven is rolled before the point is re-rolled, the bet loses
('seven out'). A Pass Line win pays even money.

Odds on Pass Line Bet - After a point is rolled you can make this additional bet by taking odds. There are different
payoffs for each point. A point of 4 or 10 will pay you 2:1; 5 or 9 pays 3:2; 6 or 8 pays 6:5. You only win if the point
is rolled again before a 7.

Come Bet - It has the same rules as the Pass Line Bet. The difference consists in the fact you can make this bet only
after the point on the pass line has been determined. On a Come Out roll the Come Bet is placed on the pass line as they
are an identical bet. After you place your bet the first dice roll will set the come point. You win if it is a natural
(7, 11) and lose if it is craps (2, 3, 12). Other rolls will make you a winner if the come point is repeated before a 7
is rolled. If a 7 is rolled first you lose.

A Come Bet is played in two rounds and is played similar to a Pass Line Bet. The main difference is that a player making
a Come Bet will bet on the first point number that 'comes' from the shooter's next roll, regardless of the table's round.
If a 7 or 11 is rolled on the first round, it wins. If a 2, 3 or 12 is rolled, it loses. If instead the roll
is 4, 5, 6, 8, 9, 10 then the Come Bet will be moved by the base dealer onto a Box representing the number the shooter threw.
This number becomes the Come Bet point and the player is allowed to add odds to the bet. The dealer will place the odds
on top of the Come Bet, but slightly off center in order to differentiate between the original bet and the odds.
The second round wins if the shooter rolls the Come Bet before a seven. If the seven comes before the number (the Come Bet),
the bet loses. On a Come Out roll for the pass line the Come Bet is in play, but traditionally the odds are not working
unless the player indicates otherwise to the dealer.

Because of the Come Bet, if the shooter makes their point, a player can find themselves in the situation where they have
a Come Bet (possibly with odds on it) and the next roll is a Come Out roll. In this situation odds bets on the come wagers
are presumed to be not working for the Come Out roll. That means that if the shooter rolls a 7 on the Come Out roll,
any players with active Come Bets waiting for a 'come point' lose their initial wager but will have their odds money
returned to them. If the 'come point' is rolled the odds do not win but the Come Bet does and the odds are returned.
The player can tell the dealer that they want their odds working, such that if the shooter rolls a number that matches
the 'come point', the odds bet will win along with the Come Bet, and if a seven is rolled both lose.

Odds on Come Bet - Exactly the same thing as the Odds on Pass Line Bet except you take odds on the Come Bet not the Pass
Line Bet.

Don't Pass Line Bet - This is the reversed Pass Line bet. If the first roll of a dice is a natural (7, 11) you lose and
if it is a 2 or a 3 you win. A dice roll of 12 means you have a tie or push with the casino. If the roll is a point
(4, 5, 6, 8, 9, 10) a 7 must come out before that point is repeated to make you a winner. If the point is rolled again
before the 7 you lose.

Don't Come Bet - The reversed Come Bet. After the come point has been established you win if it is a 2 or 3 and lose for
7 or 11. 12 is a tie and other dice rolls will make you win only if a 7 appears before them on the following throws.

Place Bets - This bet works only after the point has been determined. You can bet on a dice roll of 4, 5, 6, 8, 9 and 10.
You win if the number you placed your bet on is rolled before a 7. Otherwise you lose. The Place Bets payoffs are
different depending on the number you bet on. 4 or 10 will pay 9:5; 5 or 9 pays 7:5, and 6 or 8 pays 7:6. You can cancel
this bet anytime you want to.

Field Bets - These bets are for one dice roll only. If a 2, 3, 4, 9, 10, 11, 12 is rolled you win. A 5, 6, 7 and 8 make
you lose. Field Bets have the following different payoffs: 2 pays double (2:1) while 12 pays 3:1. Other winning dice rolls
pays even (1:1).

Big Six, Big Eight Bets - Placed at any roll of dice these bets win if a 6 or 8 comes out before a 7 is rolled. Big Six
and Big Eight are even bets and are paid at 1:1.

Proposition Bets - These bets can be made at any time and, except for the hardways, they are all one roll bets:

Any Craps: Wins if a 2, 3 or 12 is thrown. Payoff 8:1
Any Seven: Wins if a 7 is rolled. Payoff 5:1
Eleven: Wins if a 11 is thrown. Payoff 16:1
Ace Duece: Wins if a 3 is rolled. Payoff 16:1
Aces or Boxcars: Wins if a 2 or 12 is thrown. Payoff 30:1
Horn Bet: it acts as the bets on 2, 3, 11 and 12 all at once. Wins if one of these numbers is rolled. Payoff is
determined according to the number rolled. The other three bets are lost.
Hardways: The bet on a hardway number wins if it's thrown hard (sum of pairs: 1-1, 3-3, 4-4...) before it's rolled easy
and a 7 is thrown. Payoffs: Hard 4 and 10, 8:1; Hard 6 and 8, 10:1
House advantage
2 - 17%
"""