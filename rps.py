import random

def get_user_choice():
    while True:
        user = input("'r' for rock, 'p' for paper, 's' for scissors: ")
        if user in ['r', 'p', 's']:
            return user
        else:
            print("Invalid input. Please enter 'r', 'p', or 's'.")

def play():
    user = get_user_choice()
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return f'Tie! Computer chose {computer} too.'

    if is_win(user, computer):
        return f'You Won! Computer chose {computer}.'

    return f'You Lost! Computer chose {computer}.'

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or \
       (player == 's' and opponent == 'p') or \
       (player == 'p' and opponent == 'r'):
        return True
    else:
        return False

def game():
    user_score = 0
    computer_score = 0

    while True:
        result = play()
        print(result)

        if 'You Won!' in result:
            user_score += 1
        elif 'You Lost!' in result:
            computer_score += 1

        print(f"Your score: {user_score} | Computer's score: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break

if __name__ == "__main__":
    game()
