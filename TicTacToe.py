import random
import ticTacToeAI


def main():
    global row1String, row2String, row3String, row1, row2, row3
    global choice
    choice = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    global winner

    row1 = ['|', ' ', '_', ' ', '|', ' ', '_', ' ', '|', ' ', '_', ' ', '|']
    row2 = ['|', ' ', '_', ' ', '|', ' ', '_', ' ', '|', ' ', '_', ' ', '|']
    row3 = ['|', ' ', '_', ' ', '|', ' ', '_', ' ', '|', ' ', '_', ' ', '|']

    class Player:

        def __init__(self, letter, move=0):
            self.letter = letter
            self.move = move

        def randomPlay(self):
            print()

            if chance == 1:
                row1String = "".join(row1)
                row2String = "".join(row2)
                row3String = "".join(row3)

                print(row1String)
                print(row2String)
                print(row3String)
                print()

            self.move = random.choice(choice)
            print(f"Computer makes a move to square {self.move}")
            print()

            self.game()

        def playerPlay(self):

            print()

            if chance == 1:
                row1String = "".join(row1)
                row2String = "".join(row2)
                row3String = "".join(row3)

                print(row1String)
                print(row2String)
                print(row3String)
                print()

            self.move = int(input(f"{self.letter}'s turn. Enter move (1-9): "))
            choice.remove(self.move)
            print(f"{self.letter} makes a move to square {self.move}")
            print()

            self.game()

        def game(self):

            row1String = "".join(row1)
            row2String = "".join(row2)
            row3String = "".join(row3)

            if self.move == 1 and row1[2] == '_':
                row1[2] = self.letter
                row1String = "".join(row1)
            elif self.move == 2 and row1[6] == '_':
                row1[6] = self.letter
                row1String = "".join(row1)
            elif self.move == 3 and row1[10] == '_':
                row1[10] = self.letter
                row1String = "".join(row1)

            elif self.move == 4 and row2[2] == '_':
                row2[2] = self.letter
                row2String = "".join(row2)
            elif self.move == 5 and row2[6] == '_':
                row2[6] = self.letter
                row2String = "".join(row2)
            elif self.move == 6 and row2[10] == '_':
                row2[10] = self.letter
                row2String = "".join(row2)

            elif self.move == 7 and row3[2] == '_':
                row3[2] = self.letter
                row3String = "".join(row3)
            elif self.move == 8 and row3[6] == '_':
                row3[6] = self.letter
                row3String = "".join(row3)
            elif self.move == 9 and row3[10] == '_':
                row3[10] = self.letter
                row3String = "".join(row3)

            else:
                print("Invalid move.")
                print()

            print(row1String)
            print(row2String)
            print(row3String)

    print()
    mode = int(input("Enter number of human players: "))

    if mode == 2:

        print()
        print("The boxes are numbered 1-9, row-wise from left to right.")
        print()

        playerOneLetter = input("Player One, choose your side (X / O): ").upper()
        playerTwoLetter = ''

        if playerOneLetter == 'X':
            playerTwoLetter = 'O'

        elif playerOneLetter == 'O':
            playerTwoLetter = 'X'

        else:
            print("Invalid choice.")

        print(f"Player Two's letter is {playerTwoLetter}")

        playerOne = Player(playerOneLetter)
        playerTwo = Player(playerTwoLetter)

        chance = 1

        while chance <= 9:

            if chance % 2 == 1:
                playerOne.playerPlay()

                if row1[2] == row1[6] == row1[10] == playerOneLetter or row2[2] == row2[6] == row2[
                    10] == playerOneLetter or row3[2] == row3[6] == row3[10] == playerOneLetter or row1[2] == row2[6] == \
                        row3[10] == playerOneLetter or row1[10] == row2[6] == row3[2] == playerOneLetter:
                    print()
                    print("Player One wins!! Well played.")
                    break
            else:
                playerTwo.playerPlay()

                if row1[2] == row1[6] == row1[10] == playerTwoLetter or row2[2] == row2[6] == row2[
                    10] == playerTwoLetter or row3[2] == row3[6] == row3[10] == playerTwoLetter or row1[2] == row2[6] == \
                        row3[10] == playerTwoLetter or row1[10] == row2[6] == row3[2] == playerTwoLetter:
                    print()
                    print("Player Two wins!! Well played.")
                    break

            chance += 1

        else:

            print("It's a tie!")

    elif mode == 1:

        difficulty = input("Choose difficulty: (e) Easy (d) Difficult ").lower()

        if difficulty == 'e':

            print()
            print("The boxes are numbered 1-9, row-wise from left to right.")
            print()

            playerLetter = input("Choose your side (X / O): ").upper()
            computerLetter = ''

            if playerLetter == 'X':
                computerLetter = 'O'

            elif playerLetter == 'O':
                computerLetter = 'X'

            else:
                print("Invalid choice.")

            print(f"Computer's letter is {computerLetter}")

            player = Player(playerLetter)
            computer = Player(computerLetter)

            chance = 1

            while chance <= 9:

                if chance % 2 == 1:
                    player.playerPlay()

                    if row1[2] == row1[6] == row1[10] == playerLetter or row2[2] == row2[6] == row2[
                        10] == playerLetter or row3[2] == row3[6] == row3[10] == playerLetter or row1[2] == row2[2] == row3[
                        2] == playerLetter or row1[6] == row2[6] == row3[6] == playerLetter or row1[10] == row2[10] == row3[
                        10] == playerLetter or row1[2] == row2[6] == \
                            row3[10] == playerLetter or row1[10] == row2[6] == row3[2] == playerLetter:
                        print()
                        print("You win!! Well played.")
                        break

                else:
                    computer.randomPlay()

                    if row1[2] == row1[6] == row1[10] == computerLetter or row2[2] == row2[6] == row2[
                        10] == computerLetter or row3[2] == row3[6] == row3[10] == computerLetter or row1[2] == row2[2] == \
                            row3[2] == computerLetter or row1[6] == row2[6] == row3[6] == computerLetter or row1[10] == \
                            row2[10] == row3[10] == computerLetter or row1[2] == row2[6] == \
                            row3[10] == computerLetter or row1[10] == row2[6] == row3[2] == computerLetter:
                        print()
                        print("Computer wins. Better luck next time!")
                        break

                chance += 1

            else:

                print("It's a tie!")

        elif difficulty == 'd':

            ticTacToeAI.main()

        else:

            print("Invalid choice")

    elif mode == 0:

        print("???")

    else:

        print(f"{mode} players can't play Tic-Tac-Toe.")
