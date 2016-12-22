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
LEFT = True
RIGHT = False

# initialize ball_pos and ball_vel for new ball in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel, LEFT, RIGHT # these are vectors stored as lists
    ball_pos = [WIDTH/2,HEIGHT/2]
    ball_vel = [0,0]
    if direction:
        ball_vel[0] = -1*random.randint(2,5)
    else:
        ball_vel[0] = random.randint(2,5)
    ball_vel[1] = -1*random.randint(1,4)
    

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(LEFT)
    score1, score2 = 0,0
    paddle1_pos = HEIGHT/2
    paddle2_pos = HEIGHT/2
    paddle1_vel, paddle2_vel = 0,0

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # draw ball
    canvas.draw_circle(ball_pos, 10, BALL_RADIUS, "Red")        
    
    #Keep paddle on the screen
    if paddle1_pos == HALF_PAD_HEIGHT and paddle1_vel < 0:
        paddle1_vel = 0
    elif paddle1_pos == HEIGHT - HALF_PAD_HEIGHT and paddle1_vel > 0:
        paddle1_vel = 0
    if paddle2_pos == HALF_PAD_HEIGHT and paddle2_vel < 0:
        paddle2_vel = 0
    elif paddle2_pos == HEIGHT - HALF_PAD_HEIGHT and paddle2_vel > 0:
        paddle2_vel = 0
        
    #Update paddle's vertical position
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    
    # draw paddles
    canvas.draw_line([0,(paddle1_pos - HALF_PAD_HEIGHT)],[0,(paddle1_pos + HALF_PAD_HEIGHT)], 8, "White")
    canvas.draw_line([WIDTH,(paddle2_pos - HALF_PAD_HEIGHT)],[WIDTH,(paddle2_pos + HALF_PAD_HEIGHT)], 8, "White")
    
    # determine whether paddle and ball collide    
    if ball_pos[0] <= PAD_WIDTH and ball_vel[0] < 1:
        if ball_pos[1] > paddle1_pos - HALF_PAD_HEIGHT and ball_pos[1] < paddle1_pos + HALF_PAD_HEIGHT:
            ball_vel[0] = -1.1 * ball_vel[0] 
        else:
            score2 += 1
            spawn_ball(RIGHT)
            
    if ball_pos[0] >= WIDTH - PAD_WIDTH and ball_vel[0] > 1:
        if ball_pos[1] > paddle2_pos - HALF_PAD_HEIGHT and ball_pos[1] < paddle2_pos + HALF_PAD_HEIGHT:
            ball_vel[0] = -1.1 * ball_vel[0] 
        else:
            score1 += 1
            spawn_ball(LEFT)
    
    if ball_pos[1] <= 0 or ball_pos[1] >= HEIGHT:
        ball_vel[1] = -1*ball_vel[1]
    # draw scores
    canvas.draw_text("Score", [260, 40], 40, "Red") 
    canvas.draw_text(str(score1) + "/" + str(score2), [275, 80], 40, "Red") 
                     
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
frame.add_button("RESET", new_game, 100)

frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# start frame
new_game()
frame.start()
