"""
This is a number guessing game.  The computer will 
randomly choose a secret number, and the player will 
guess the number based on the feedback from the computer.
A new game starts if a player wins or loses, or if they
push a button changing the range.

Input will come from buttons and an input field.
All output for the game will be printed in the console.

"""
import simplegui
import random

range = 100		#initialize starting range

# helper function to start and restart the game
def new_game():
    global secret_number
    global range
    global allowed_guesses
    global count
    
    count = 0
    secret_number = random.randint(0,range)
    if range == 100:
        allowed_guesses = 7
    else:
        allowed_guesses = 10
    print "New game started.  Guess a number between 0 and " + str(range)
    print "You have " + str(allowed_guesses) + " guesses."



def range100():
#Starts a new game with the secret number between 0 and 100
    global range
    range = 100
    new_game()

def range1000():
#Starts a new game with the secret number between 0 and 1000
    global range
    range = 1000
    new_game()
    
def input_guess(guess):
    global secret_number
    global count
    print "Guess was " + guess
    guess = int(guess)
    if guess == secret_number:       			#runs if player wins
        random_message = random.randint(0,3) 	#randomized win message
        if random_message == 1:
            print "I'd rather be lucky than good too!"
        elif random_message == 2:
            print "Numbers are your jam!"
        else:
            print "You made that look easy!"
        print "Correct, you win!"
        new_game()					#starts a new game if player wins
    elif guess > secret_number:
        print "Your guess was too high, guess again"
        count += 1
        print "You have " + str(allowed_guesses - count) + " remaining."
        print""
        if allowed_guesses == count:				
            random_message = random.randint(0,3)	#randomized loser message
            if random_message == 1:
                print "La hoo...ze her"
            elif random_message == 2:
                print "Sorry, counting is difficult"
            else:
                print "Maybe next time"
            print "Sorry, you lose"
            new_game()				#starts a new game if player loses
    elif guess < secret_number:
        print "Your guess was too low, guess again"
        count += 1
        print "You have " + str(allowed_guesses - count) + " remaining."
        print ""
        if allowed_guesses == count:
            random_message = random.randint(0,3)  #randomized loser message
            if random_message == 1:
                print "La hoo...ze her"
            elif random_message == 2:
                print "Sorry, counting is difficult"
            else:
                print "Maybe next time"
            print "Sorry, you lose"
            new_game()				#starts a new game if player loses
    
# create frame, guess input, and buttons for new game
frame = simplegui.create_frame('Guessing Game', 200, 200)
frame.add_input('Enter your guess here: ', input_guess, 100)
frame.add_button("Play a new game, range of 1000", range1000, 100)
frame.add_button("Play a new game, range of 100", range100, 100)


new_game()		#initialize game to start when program runs

