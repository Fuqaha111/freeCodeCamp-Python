import random
def game():
    computer_choice = random.randint(1, 10)
    guess = 0
    guesses = 0

    while guess != computer_choice:
        try:
            guess = int(input("Guess a number between 1-10\n")) 
        except ValueError:
          print("Not a valid choice")
       
        if guess > 10 or guess < 1:
          print ("Number must be between 1-10")
        guesses += 1

        if guess != computer_choice:
          print("You are wrong")



    print (f"Your guess is correct\nnumber of guesses: {guesses}")

game()