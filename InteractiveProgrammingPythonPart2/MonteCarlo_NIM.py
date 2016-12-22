"""
A simple Monte Carlo solver for Nim
http://en.wikipedia.org/wiki/Nim#The_21_game
"""

import random
import codeskulptor
codeskulptor.set_timeout(20)

MAX_REMOVE = 3
TRIALS = 200

def evaluate_position(num_items):
    """
    Monte Carlo evalation method for Nim
    """
    copy_num_items = int(num_items)
    score_dict = {0:0,1:0,2:0,3:0}
    
    for dummy_num in range(0,TRIALS):
        copy_num_items = int(num_items)
        while copy_num_items > 0:
            comp_choice = random.choice([0,1,2,3])
            copy_num_items -=  comp_choice
            if copy_num_items <= 0:
                score_dict[comp_choice] += 1
            else:
                human_choice = random.choice([0,1,2,3])
                copy_num_items -= human_choice
                if copy_num_items <= 0:
                    score_dict[comp_choice] -= 1
    
    print score_dict
    inverse = [(value, key) for key, value in score_dict.items()]
    return max(inverse)[1]

def play_game(start_items):
    """
    Play game of Nim against Monte Carlo bot
    """
    
    current_items = start_items
    print "Starting game with value", current_items
    while True:
        comp_move = evaluate_position(current_items)
        current_items -= comp_move
        print "Computer choose", comp_move, ", current value is", current_items
        if current_items <= 0:
            print "Computer wins"
            break
        player_move = int(input("Enter your current move"))
        current_items -= player_move
        print "Player choose", player_move, ", current value is", current_items
        if current_items <= 0:
            print "Player wins"
            break

play_game(21)
        
    
                 
    