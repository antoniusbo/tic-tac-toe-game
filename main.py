while True:

    start_question = input("Would you like to play a game? Please respond 'Yes' or 'No': ")
    if start_question.lower() == "yes":
        print("Let's start it!")
    elif start_question.lower() == "no":
        print("The game is over.")
    else:
        print("Please respond 'Yes' or 'No'.")


    theBoard = {'7': ' ', '8': ' ', '9': ' ',
                '4': ' ', '5': ' ', '6': ' ',
                '1': ' ', '2': ' ', '3': ' '}

    for key in theBoard:
        board_keys.append(key)


    def printBoard(board):
        print(board['7'] + '|' + board['8'] + '|' + board['9'])
        print('-+-+-')
        print(board['4'] + '|' + board['5'] + '|' + board['6'])
        print('-+-+-')
        print(board['1'] + '|' + board['2'] + '|' + board['3'])