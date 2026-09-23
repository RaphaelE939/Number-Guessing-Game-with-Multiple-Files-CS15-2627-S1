import random
MAX = 100
MIN = 1

def generate_secret_number():
    secret_number = random.randint(MIN,MAX)
    return secret_number

def check_user_guess(secret_number):
    guess = prompt_valid_guess()
    if guess == secret_number:
        print("You guessed correctly!")
        return True
    elif guess < secret_number:
        print("Go higher twain")
    else:
        print("Too high buddy")
        return False
def prompt_valid_guess():
    while True:
        print(f"Try to guess a number between {MIN} and {MAX}. Don't lose all your points")
        guess = input("Whats your guess:")
        try:
            guess = int(guess)
        except ValueError:
            print("Invalid guess")
            print("Guess must be a number")
            continue
        if guess > MAX:
            print("Invalid guess")
            print(f"Out of range, can't be greater than {MAX}")
            continue
        elif guess < MIN:
            print("Invalid guess")
            print(f"Out of range, can't be less than {MIN}")
            continue
        return guess

if __name__ == "__main__":
    number_to_print = generate_secret_number()
    print(f"Secret number: {number_to_print}")

    for _ in range(3):
            print(f"Secret number: {number_to_print}")
            print("Check if the code can identify numbers above, below, and correct guess.")
            check_user_guess(number_to_print)