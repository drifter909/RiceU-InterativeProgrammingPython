# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

# initialize ball_pos and ball_vel for new ball in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2,HEIGHT/2]
    ball_vel = [0,0]
    if direction == 1:
        ball_vel[0] = -1*random.randint(0,5)
    else:
        ball_vel[0] = random.randint(0,5)
    ball_vel[1] = -1*random.randint(0,5)
    

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(random.randint(0,2))
    score1, score2 = 0,0
    paddle1_pos = HEIGHT/2
    paddle2_pos = HEIGHT/2
    paddle1_vel, paddle2_vel = 0,0

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # draw ball
    canvas.draw_circle(ball_pos, 10, BALL_RADIUS, "Red")        

    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    
    # draw paddles
    canvas.draw_line([0,(paddle1_pos - HALF_PAD_HEIGHT)],[0,(paddle1_pos + HALF_PAD_HEIGHT)], 8, "White")
    canvas.draw_line([WIDTH,(paddle2_pos - HALF_PAD_HEIGHT)],[WIDTH,(paddle2_pos + HALF_PAD_HEIGHT)], 8, "White")
    
    # determine whether paddle and ball collide    
    if ball_pos[0] == PAD_WIDTH:
        if ball_pos[1] >= paddle1_pos - HALF_PAD_HEIGHT or ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT:
            ball_vel[0] = -1*(ball_vel[0] +1)
    # draw scores
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if simplegui.KEY_MAP["w"] == key:
        paddle1_vel = -5
    elif simplegui.KEY_MAP["s"] == key:
        paddle1_vel = 5
    elif simplegui.KEY_MAP["up"] == key:
        paddle2_vel = -5
    elif simplegui.KEY_MAP["down"] == key:
        paddle2_vel = 5
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    if simplegui.KEY_MAP["w"] == key:
        paddle1_vel = 0
    elif simplegui.KEY_MAP["s"] == key:
        paddle1_vel = 0
    elif simplegui.KEY_MAP["up"] == key:
        paddle2_vel = 0
    elif simplegui.KEY_MAP["down"] == key:
        paddle2_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
