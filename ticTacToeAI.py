import math
import time


def main():

    print()

    board = {1: '   ', 2: '   ', 3: '   ',
             4: '   ', 5: '   ', 6: '   ',
             7: '   ', 8: '   ', 9: '   '}
    computerLetter = 'X'
    playerLetter = 'O'

    def play_again():

        gameState = input("Would you  like to  play again?  (y/n) ")

        if gameState.lower() == 'y':
            main()
        elif gameState.lower() == 'n':
            exit()
        else:
            print("Invalid choice.")
            play_again()

    def print_board(board=board):
        for i in range(1, 8, 3):
            print('|' + board[i] + '|' + board[i + 1] + '|' + board[i + 2] + '|')

            if i < 7:
                print('-' * 13)

        print()

    def space_is_free(position):
        if board[position] == '   ':
            return True
        else:
            return False

    def free_spaces(board=board):

        freeSpaces = 0
        for key in board.keys():
            if board[key] == '   ':
                freeSpaces += 1

        return freeSpaces

    def make_move(letter, position):

        if space_is_free(position):

            board[position] = ' ' + letter + ' '
            print_board(board)

            if check_for_win(board):

                if letter == playerLetter:
                    print("You win!!")
                    play_again()
                else:
                    print("The computer wins. Better luck next time!")
                    play_again()

            elif check_for_tie(board):
                print("It's a tie! Well played.")
                play_again()

        else:

            print("Invalid choice.")
            position = int(input("Enter new position: "))
            make_move(letter, position)

    def check_for_win(board=board):

        if board[1] == board[2] == board[3] != '   ' or board[4] == board[5] == board[6] != '   ' or board[7] == board[8] \
                == board[9] != '   ' or board[1] == board[4] == board[7] != '   ' or board[2] == board[5] == board[8] != \
                '   ' or board[3] == board[6] == board[9] != '   ' or board[1] == board[5] == board[9] != '   ' or board[3]\
                == board[5] == board[7] != '   ':
            return True
        else:
            return False

    def check_for_win_letter(letter):

        if board[1] == board[2] == board[3] == ' ' + letter + ' ' or board[4] == board[5] == board[6] == ' ' + letter + ' '\
                or board[7] == board[8] == board[9] == ' ' + letter + ' ' or board[1] == board[4] == board[7] == ' ' +\
                letter + ' ' or board[2] == board[5] == board[8] == ' ' + letter + ' ' or board[3] == board[6] == board[9]\
                == ' ' + letter + ' ' or board[1] == board[5] == board[9] == ' ' + letter + ' ' or board[3] == board[5] ==\
                board[7] == ' ' + letter + ' ':
            return True
        else:
            return False

    def check_for_tie(board=board):

        for key in board.keys():
            if board[key] == '   ':
                return False
        else:
            return True

    def player_move(playerLetter='O'):

        if free_spaces(board) >= 9:
            print_board(board)

        position = int(input("Enter your position (1-9): "))
        print()

        while not (1 <= position <= 9):
            print("Invalid choice.")
            position = int(input("Enter new position: "))
        else:
            make_move(playerLetter, position)

    def computer_move(computerLetter='X'):

        time.sleep(1.5)

        bestScore = -math.inf
        bestPosition = 0

        for key in board.keys():
            if space_is_free(key):
                board[key] = ' ' + computerLetter + ' '
                score = minimax(board)
                board[key] = '   '

                if score > bestScore:
                    bestScore = score
                    bestPosition = key

        print(f"Computer moves to {bestPosition}.")
        print()
        time.sleep(0.8)
        make_move(computerLetter, bestPosition)

    def minimax(board, is_maximising=False):

        if check_for_win_letter(computerLetter):
            return 1 * (free_spaces(board) + 1)

        elif check_for_win_letter(playerLetter):
            return -1 * (free_spaces(board) + 1)

        elif check_for_tie(board):
            return 0

        if is_maximising:

            bestScore = -math.inf

            for key in board.keys():

                if space_is_free(key):
                    board[key] = ' ' + computerLetter + ' '
                    score = minimax(board, False)
                    board[key] = '   '
                    bestScore = max(score, bestScore)

            return bestScore

        else:

            bestScore = math.inf

            for key in board.keys():

                if space_is_free(key):
                    board[key] = ' ' + playerLetter + ' '
                    score = minimax(board, True)
                    board[key] = '   '
                    bestScore = min(score, bestScore)

            return bestScore

    while not check_for_win(board):

        if free_spaces(board) >= 9:
            print("Welcome to Tic Tac Toe versus the computer!")
            print()
            time.sleep(2)
            print("The boxes are numbered 1-9, row-wise from left to right.")
            print()
            time.sleep(3)
            playerLetter = input("Choose your side (X / O): ").upper()
            print()

            computerLetter = 'X' if playerLetter == 'O' else 'O'

        if playerLetter == 'O':
            computer_move(computerLetter)
            player_move(playerLetter)
        else:
            player_move(playerLetter)
            computer_move(computerLetter)


if __name__ == "__main__":
    main()
