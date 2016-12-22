# implementation of card game - Memory

import simplegui
import random
turn_count = 0
state = 0
# helper function to initialize globals
def new_game():
    global deck, exposed, turn_count
    turn_count = 0
    deck = []
    exposed = []
    label.set_text("Turns = " + str(turn_count))
    for num in range(8):
        deck.append(num)
        deck.append(num)
        random.shuffle(deck)
    for card in deck:
        exposed.append(False)
     
# define event handlers
def mouseclick(pos):
    global state, exposed, card1, card2, turn_count, card1_location, card2_location
    card_clicked = pos[0] // 50
    if exposed[card_clicked] == False:
        if state == 0:
            state = 1
            exposed[card_clicked] = True
            card1 = deck[card_clicked]
            card1_location = card_clicked
        elif state == 1:
            state = 2
            exposed[card_clicked] = True
            card2 = deck[card_clicked]
            card2_location = card_clicked
        else:
            state = 1
            if card1 != card2:
                exposed[card1_location] = False
                exposed[card2_location] = False
            exposed[card_clicked] = True
            card1 = deck[card_clicked]
            card1_location = card_clicked
            card2 = []
            
            turn_count += 1
            label.set_text("Turns = " + str(turn_count))

                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global deck, exposed
    pos = 0
    count = 0
    for card in deck:
        canvas.draw_line((pos, 0), (pos, 100), 2, "Red")
        if exposed[count] == True:
            canvas.draw_text(str(card), (pos + 20, 50) , 24, "White")
        count += 1
        pos += 50
        


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric