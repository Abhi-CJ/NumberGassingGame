import random

def ask_play_again():
    """
    Prompt the user to decide whether to continue playing the game.

    The user is asked to input 'yes' or 'no':
        - If the user enters 'no', returns a message to end the game.
        - If the user enters 'yes', the function does nothing (returns None).
        - For any invalid input, the user is prompted again recursively.

    Returns:
        str or None: Returns a string message ("OK! play next time.") if the user chooses 'no',
                     otherwise returns None if the user chooses 'yes'.
    """
    play_again = input("Would you like to play again? Say 'yes' or 'no':\n").lower()
    if play_again == 'no':
        return "OK! play next time."
    elif play_again == 'yes':
        return None
    else:
        return ask_play_again()

def guess_game():
    """
    Start a simple number guessing game where the user guesses a number between 0 and 5.

    Gameplay:
        - A random number between 0 and 5 is generated each round.
        - The user inputs their guess.
            - Correct guess: Score increases by 1.
            - Incorrect guess: Score decreases by 1 (if the score is greater than 0).
        - After each guess, the user is asked if they want to continue playing.

    Input:
        - Integer input (0–5) for guessing.
        - String input ('yes' or 'no') to continue or end the game.

    Error Handling:
        - Handles non-integer inputs for guessing.
        - Prompts again for invalid inputs when deciding whether to play again.

    Note:
        - The game continues until the user chooses not to play anymore.

    Raises:
        ValueError: If non-integer input is entered when guessing.
    """
    score = 0
    print("Guess the number! If your guess is correct, you will get +1 score; otherwise, -1.")
    while True:
        try:
            comp = random.randint(0, 5)
            user_guess = int(input("Enter any number between 0 to 5:\n"))
            if 0 <= user_guess <= 5:
                if comp == user_guess:
                    result = "Your Guess is right."
                    print(result)
                    score += 1
                    print(f"Your score is {score}")
                else:
                    result = f"You failed. Your guess was {user_guess} but the actual number was {comp}."
                    print(result)
                    if score > 0:
                        score -= 1
                    print(f"Your score is {score}")
            else:
                print("Please enter a number between 0 and 5.")
            
            play_again = ask_play_again()
            if play_again == "OK! play next time.":
                print(play_again)
                break
            else:
                pass
        except ValueError:
            print("Only integer value.")

if __name__ == "__main__":
    guess_game()
