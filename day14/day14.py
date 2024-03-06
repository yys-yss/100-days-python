import random
from art import logo, vs
from game_data import data
import os
import sys

def new_screen():
    os.system('clear')
    print(logo)

def generate_random_celebrities(celebrity = None):
    if celebrity is not None:
        first_celebrity_dict = celebrity
    else:
        first_celebrity_dict = random.choice(data)
    
    while True:
        second_celebrity_dict = random.choice(data)
        if first_celebrity_dict['follower_count'] != second_celebrity_dict['follower_count']:
            break
    return first_celebrity_dict, second_celebrity_dict

def calculate_score(chosen_celebrity, other_celebrity, score):
    chosen_celebrity_followers = chosen_celebrity['follower_count']
    other_celebrity_followers = other_celebrity['follower_count']
    if chosen_celebrity_followers < other_celebrity_followers:
        new_screen()
        new_score = score
        print(f"Sorry that's wrong. Final score: {new_score}")
        end_game()
    if chosen_celebrity_followers > other_celebrity_followers:
        new_screen()
        new_score = score + 1
        print(f"You're right. Current score: {new_score}")
        next_round(chosen_celebrity, new_score)
    
def ask_question(previous_answer = None):
    a, b = generate_random_celebrities()
    if previous_answer is not None:
        a = previous_answer
        _, b = generate_random_celebrities(a)
    
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
    print(vs)
    print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}")
    user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    if user_answer == 'a':
        user_choice = a
        other_choice = b
        return user_choice, other_choice
    elif user_answer == 'b':
        user_choice = b
        other_choice = a
        return user_choice, other_choice
    else:
        print('Invalid option')
        end_game()

def start_game():
    score = 0
    new_screen()
    user_choice, other_choice = ask_question()
    calculate_score(user_choice, other_choice, score)

def next_round(previous_answer, score):
    user_choice, other_choice = ask_question(previous_answer)
    calculate_score(user_choice, other_choice, score)

def end_game():
    sys.exit()

start_game()