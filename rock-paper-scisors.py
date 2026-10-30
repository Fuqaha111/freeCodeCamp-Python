import random

def game():
    list_of_choices = ["Rock", "Paper", "Scisors"]
    playing = True

    player_score = 0
    computer_score = 0
    while playing:

        #in randdint both starting and ending number are in bounds
        random_integer = random.randint(0, 2)
        computer_choice = list_of_choices[random_integer]

        # Invalid input if user writes anything besides an integer value
        try:
            number_choice = int (input("Chose the number you want\n1- Rock\n2- Paper\n3- Scisors\n4- To exit the game\n"))
        except ValueError:
             print("Invalid input")

        # If integer chosen is out of bounds
        if number_choice > 4 or number_choice < 1:
            print("Invalid input")
        
        # if user decides to exit the game
        elif number_choice == 4:
                playing = False


        else:
            player_choice = list_of_choices[(number_choice - 1)]
            print(f"You Chose: {player_choice}\ncomputer chose: {computer_choice}")

            #scenarios where the player wins
            if (player_choice == "Rock" and computer_choice == "Scisors") or (player_choice == "Paper" and computer_choice == "Rock") or (player_choice == "Scisors" and computer_choice == "Paper"):
                 player_score += 1
                 print("You won\n")

            #Draw
            elif computer_choice == player_choice:
                 print("You draw\n")

            #Computer wins
            else:
                 computer_score += 1
                 print ("You Lost\n")


    #Who won overall after player quits
    print (f"Your final score: {player_score}\nComputer Score: {computer_score}\n")
    if player_score == computer_score:
        print("It's a Draw")
    elif player_score > computer_score:
        print("You won :)")
    else:
        print("You Lost :(")



game()