# for key in theBoard:
#     board_keys.append(key)


theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

player1 = "X"
player2 = "O"

def make_move (player, cell):
    if theBoard[cell] == ' ':
        theBoard[cell] = player
    else:
        print("The cell is already occupied. Please choose another cell.")



game = 1

while game == True:

    start_question = input("Would you like to play a game? Please respond 'Yes' or 'No': ")
    if start_question.lower() == "yes":
        print("Let's start it! Please note that the game rules can be found in README file.")
        # print("Please write your names here below.")
        # name1 = str(input("Please write your name. You will be a Player1: "))
        # name2 = str(input("Please write your name. You will be a Player2: "))
        # if name1 and name2 != str:
        #     print("Please write a name not a number.")
        print("The board is below. Let's start!")
        printBoard(theBoard)
        for i in range(1,10):
            move = (input("Player1 your turn with X. Please choose a cell: "))
            if not move.isdigit():
                print("Please insert a cell number.")
            else:
                make_move(player1,move)
                    printBoard(theBoard)



                move = (input("Player2 your turn with O. Please choose a cell: "))
                if not move.isdigit():
                    print("Please insert a cell number.")
                else:
                    make_move(player1, move)
                    printBoard(theBoard)












    elif start_question.lower() == "no":
        print("The game is over.")
        game = False




    else:
        print("Please respond 'Yes' or 'No'.")
