import random
# Generate a random number between 1 and 10
r = random.randint(1, 10)
attempts = 0

while True:
    # Prompt the user to guess a number
    n = int(input("Guess a number between 1 and 10: "))
    attempts += 1  # Increment the attempt count

    if n < r:
        print("Thoda upr ⬆️")  # Hint to guess higher
    elif n > r:
        print("Thoda neche ⬇️")  # Hint to guess lower
    else:
        print("🎉JACKPOT 🎉")  # User guessed correctly
        print(f"You took {attempts} attempts.")
        break  # Exit the loop