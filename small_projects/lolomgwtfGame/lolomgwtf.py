import random

# Max number of digits to guess, experiment with settings (1, 10, 100, etc...)
NUM_DIGITS = 3

# Max number of guesses, experiment with settings (1, 100, etc...)
MAX_GUESSES = 10


def main():
    print("""lolomgwtf, a deductive logic game.
    I'm thinking of a {}-digit number with no repeated numbers.
    Try to guess what my number is. Clues are
    When I say          That means:
        LOL             One digit is correct but in the wrong position.
        OMG             One digit is correct and is in the correct position.
        WTF             NO digits are correct.
    
    For example, if the secret number was 248 and your guess was 843, the
    clues would be OMG LOL""".format(NUM_DIGITS))

    while True:  # Main loop
        # Store the secret number to guess
        secretNum = getSecretNum()
        print("I have thought of a number.")
        print(" You have {} guesses to get it.".format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ""
            # Keep looping until max guesses reached or valid guess is made
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print("Guess #{}: ".format(numGuesses))
                guess = input("> ")

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break  # CORRECT!
            if numGuesses > MAX_GUESSES:
                print("You ran out of guesses, sorry.")
                print("The answer was {}.".format(secretNum))

        # Ask player if they want to play again.
        print("Do you want to play again? (y or n)")
        if not input("> ").lower().startswith("y"):
            break
    print("Thanks for playing")


def getSecretNum():
    # Returns a string made up of NUM_DIGITS unique random numbers

    numbers = list('0123456789')  # Create the list of numbers.
    random.shuffle(numbers)  # Shuffle the numbers into a random order.

    # Get the first NUM_DIGITS number in the list for the secret number:
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    if guess == secretNum:
        return "YOU GOT IT! WTG!!!"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # A number in the correct place
            clues.append(
                'OMG - One digit is correct and is in the correct position.')
        elif guess[i] in secretNum:
            # A number is in the INCORRECT Place
            clues.append(
                "LOL - One digit is correct but in the wrong position.")
    if len(clues) == 0:
        # No correct numbers at all, womp womp womp
        return "WTF - NO digits are correct! HAHA"
    else:
        clues.sort
        return " ".join(clues)


# Run the program
if __name__ == "__main__":
    main()
