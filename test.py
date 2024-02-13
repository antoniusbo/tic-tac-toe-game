game = 1

while game == True:

    start_question = input("Would you like to play a game? Please respond 'Yes' or 'No': ")
    if start_question.lower() == "yes":
        print("Let's start it!")
    elif start_question.lower() == "no":
        print("The game is over.")
        game = False

    else:
        print("Please respond 'Yes' or 'No'.")