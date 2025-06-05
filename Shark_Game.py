import time
import random
import sys


def print_pause(msg):
    """
    This function is made to display input text
    with delay 2 seconds
    """
    print(msg)
    time.sleep(2)


def get_choice():
    """
    This function is to get the choice from the player
    and the player can only enter 1 or 2
    """
    print_pause("You can Enter (1) to swim down")
    print_pause("Or You can Enter (2) to continue swimming ahead.")
    print_pause("What would you like to choose")
    print_pause("(Please enter 1 or 2)")
    choice = input().strip().lower()
    while choice not in ["1", "2"]:
        print_pause("(Please enter 1 or 2)")
        choice = input().strip().lower()
    return choice


def swim_down(total_score, has_visited):
    """
    This function is an action that player chose to do
    It has a random choice of food
    It checks if the player went down before or not
    """
    food_options = [
        "seaweeds", "smaller fishes", "worms", "plants", "shrimps"]
    food = random.choice(food_options)
    print_pause("You decided to swim down...")
    if has_visited:
        print_pause("You've already been here, there's nothing else to find.")
    else:
        print_pause(f"You found some {food}")
        print_pause("You ate them and became bigger, Awesome!")
        total_score += 2
        print_pause(f"Your Total score is: {total_score}")
        has_visited = True
    print_pause("You return to continue swimming")
    return total_score, has_visited


def cont(total_score):
    """
    This function is an action that player chose to do
    It also has a random amount of monsters
    It checks if the player enters only 1 or 2
    after that, it call another function
    """
    monsters_options = ["Eel", "Shark", "Small Whale"]
    monsters = random.choice(monsters_options)
    print_pause("You decided to continue ahead...")
    print_pause(f"Uh oh, You found a/n {monsters}")
    print_pause("Enter (1) to eat it")
    print_pause("Enter (2) to Escape from it")
    choice = input("").strip().lower()
    while choice not in ["1", "2"]:
        print_pause("(Please enter 1 or 2)")
        choice = input().strip().lower()
    if choice in "1":
        total_score = eat(total_score)
    elif choice in "2":
        total_score = escape(total_score)
    return total_score


def eat(total_score):
    """
    This function is an action that player chose to do
    If the player has 7 points or more it increments the total points by 4
    If not, then it decrements it by 4
    """
    if total_score >= 7:
        print_pause(f"You are stronger than it and you ate it")
        total_score += 4
        print_pause(f"Your total score is {total_score}")
    else:
        print_pause(f"It is way too strong, So it killed you")
        total_score -= 4
        print_pause(f"Your total score is {total_score}")
    return total_score


def escape(total_score):
    """
    This function is an action that player chose to do
    it also increments the total points
    """
    print_pause("You swam away")
    print_pause(f"Fortunatly, You are faster than it and you escaped it")
    total_score += 3
    print_pause(f"Your total score is {total_score}")
    print_pause("You continue swimming")
    return total_score


def win(total_score):
    """
    This function is called when the player wins the game
    then it calls another function
    """
    print_pause("Good Game, You win!")
    print_pause(f"Your final score is: {total_score}")
    play_again()


def lose(total_score):
    """
    This function is called when the player loses the game
    then it calls another function
    """
    print_pause("Game Over, You lost!")
    print_pause(f"Your final score is: {total_score}")
    play_again()


def error2(choice):
    """
    It checks whether you put y as Yes to restart the game or n as No to exit
    If the user input another text it will loop again
    """
    while choice not in ["y", "n"]:
        print_pause("Enter (y/n) only!")
        choice = input().strip().lower()
    return choice


def logic_question(total_score):
    """
    This function asks a logic question to the player
    If he answered correctly it increments total score by 3
    If not, then it decrements it by 3
    Also It checks if he has 0 or less, then it calls a function
    """
    print_pause("Your score is too low.")
    print_pause("Here's a logic question that gives you 3 points.")
    print_pause("But if you answered incorrectly, you'll lose 3 points.")
    print_pause("What is always in front of you but can’t be seen?")
    answer = input().strip().lower()
    if answer == "future":
        print_pause("You answered correctly!")
        total_score += 3
        print_pause(f"Your total score is {total_score}")
    else:
        print_pause("You answered incorrectly...")
        total_score -= 3
        print_pause(f"Your total score is {total_score}")
    if total_score <= 0:
        lose(total_score)
    return total_score


def play_again():
    """
    This function asks the player if they want to play again
    """
    print_pause("Would you like to play again? (y/n)")
    choice = input().strip().lower()
    choice = error2(choice)
    if choice == "y":
        play_game()
    else:
        print_pause("Thanks for playing! Goodbye.")
        sys.exit()


def play_game():
    """
    This is the main function that contains the game story
    """
    total_score = 5
    has_visited = False
    print_pause("Welcome to the Shark Adventure Game!")
    print_pause("You are a small shark swimming in the ocean.")
    print_pause("You need to find some food and grow bigger.")
    print_pause(
        "But be careful! There are some dangerous monsters in the ocean.")
    print_pause("If you find them, you have to eat them or escape from them.")
    print_pause("Let's start the game!")
    while True:
        choice = get_choice()
        if choice == "1":
            total_score, has_visited = swim_down(total_score, has_visited)
        elif choice == "2":
            total_score = cont(total_score)
            if total_score >= 20:
                win(total_score)
                break
            elif total_score <= 0:
                lose(total_score)
                break
            elif total_score < 3:
                total_score = logic_question(total_score)


play_game()
