import random
def number_guessing_game():
    print("************")
    print("Welcome to the guessing game")
    print("***********")
    print("I am thinking number 1 to 100")

    secret_number=random.randint(1,100)
    attempts=0

    guess=input("Enter your guess(or type'quit' to exit):")
    if guess.lower()== 'quit':
        print(f"Thanks for playing the number was{secret_number}")

        guess=int(guess)
        attempts+=1

        if guess<1 or guess> 100:
            print("Please enter a number between1 and 100")
        elif guess< secret_number:
            print("Too low try again")
        elif guess> secret_number:
            print("Too high try again")
        else:
            print(f"\n congratulations! you guessed it in{attempts} attempt")

if __name__ == "__main__":
    number_guessing_game()




