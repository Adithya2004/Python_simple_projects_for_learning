import random
list_choice = ["r","p","s"]
lose_options = ["rp","ps","sr"]
while True:
    comp_guess = random.choice(list_choice)
    user_guess = input("Select your Guess:: r : p : s ::")
    if user_guess not in list_choice:
        print("Pick a Valid Option Next Time!!")
        continue
    if comp_guess == user_guess:
        print(f"TIE!! Computer Selected {comp_guess}")
    elif user_guess+comp_guess in lose_options:
        print(f"You lose!!Computer Selected {comp_guess}")
    else:
        print(f"You Win!!Computer Selected {comp_guess}")
    ch = input("Keep Playing?y/n:")
    if ch == "y":
        continue
    break