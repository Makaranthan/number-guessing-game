import random

def play_game():
    number = random.randint(1, 50)
    guess = 0
    attempts = 0

    print("Guess a number between 1 and 50")

    while guess != number:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number:
            print("Too low")
        elif guess > number:
            print("Too high")
        else:
            print(f"Correct! You guessed the number in {attempts} attempts.")

def main():
    while True:
        print("\n1. Play Game")
        print("2. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            play_game()
        elif choice == 2:
            print("Exiting game")
            break
        else:
            print("Invalid choice")

main()
