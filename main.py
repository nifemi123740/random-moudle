import random
def get_user_choice():
    choice=input("choose rock,paper or scissors: ").lower()
    while choice not in['rock','paper','scissors']:
        print("oops invalid choice, try again!!")
        choice=input("choose rock,paper or scissors: ").lower()
    return choice
    
def get_computer_choice():
    choice = random.choice(['rock', 'paper', 'scissors'])
    return choice

def determine_winner(user,computer):
    if user==computer:
        return"its a tie!!"
    elif (user=='rock' and computer=='scissors'):
        print(f"user selected{user}\ncomputer selected {computer}\nUser WINS!!")
        return
    elif (user=='paper' and computer=='rock'):
        print(f"user selected{user}\ncomputer selected {computer}\nUser WINS!!")
        return
    elif (user=='scissors' and computer=='paper'):
        print(f"user selected{user}\ncomputer selected {computer}\nUser WINS!!")
        return
    else:
        return f"user selected{user}\ncomputer selected {computer}\nComputer WINS!!"
    
def play_game():
    print("WELCOME TO ROCK PAPER SCISSOR GAME!")
    while True:
        user=get_user_choice()
        computer=get_computer_choice()
        print(determine_winner(user,computer))
        again=input("Play Again??(yes/no)").lower()
        if again != 'yes':
            print("Thanks for playing!!")
            break

play_game() 