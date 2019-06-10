print("Welcome to Alexander's Tic-Tac-Toe Game", "\n")

board = [" "for i in range(9)]


def cls():
    print('\n'*20)


def printBoard():
    row1 = "|{}|{}|{}|".format(board[0], board[1], board[2])
    row2 = "|{}|{}|{}|".format(board[3], board[4], board[5])
    row3 = "|{}|{}|{}|".format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()


def playerMove(icon):
    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2

    choice = int(input("Player {}: Enter your move: ".format(number)).strip())
    if board[choice-1] == " ":
        board[choice-1] = icon
    else:
        print("Sorry Player {}!, that space is Taken. ".format(number))


def victory(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon) or \
       (board[0] == icon and board[4] == icon and board[8] == icon) or \
       (board[2] == icon and board[4] == icon and board[6] == icon) or \
       (board[0] == icon and board[3] == icon and board[6] == icon) or \
       (board[1] == icon and board[4] == icon and board[7] == icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon):
        return True
    else:
        return False


def isDraw():
    if " " not in board:
        return True
    else:
        return False


while True:
    printBoard()
    playerMove("X")
    if victory("X"):
        cls()
        printBoard()
        print("Congratulations Player 1! You've won the game.")
        break
    if isDraw():
        cls()
        printBoard()
        print("It's draw!")
        break
    printBoard()
    playerMove("O")
    if victory("O"):
        cls()
        printBoard()
        print("Congratulations Player 2! you've won the game.")
        break
