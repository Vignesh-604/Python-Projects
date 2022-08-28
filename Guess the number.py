import random

n1 = 1
n2 = 10
print(f"Hello Player!!\nGuess a number between {n1} to {n2}.")
def Guess():
    try:
        def game():
            numb = random.randint(n1, n2)
            guess = 0

            while guess != numb:
                guess = int(input("Enter a number: "))
                if guess < int(numb):
                    print("Go higher.")
                elif guess > int(numb):
                    print("Go lower")

            print("You got it!!")
        game()

    except ValueError:
        print("Enter a valid number.")
        Guess()
Guess()
