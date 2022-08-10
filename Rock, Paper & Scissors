import random

user = input("Enter your name: ")
print(f"Hello {user}!\n r: Rock, s: Scissors and p: paper")
score_a = 0
score_b = 0
score_limit = 5

while score_a < score_limit and score_b < score_limit:
    a = input("Rock, Paper or Scissors? ")
    b = random.choice(["r", "p", "s"])
    point = f"  {user}: {score_a} , Compo: {score_b}"

    if a == b:
        print("\n  IT's a TIE!!")
        print(f"  {user}: {score_a} , Compo: {score_b} \n")

    elif (a == "r" and b == "s") or (a == "s" and b == "p") or (a == "p" and b == "r"):
        print("\n  You WIN!!")
        score_a += 1
        print(f"  {user}: {score_a} , Compo: {score_b} \n")

    elif (b == "r" and a == "s") or (b == "s" and a == "p") or (b == "p" and a == "r"):
        print("\n  You LOSE!!")
        score_b = score_b + 1
        print(f"  {user}: {score_a} , Compo: {score_b} \n")

    else:
        print("\n  That's invalid.\n")

if score_a == score_limit:
    print(f"{user} WINS!!")
else:
    print("Compo WINS!!")

