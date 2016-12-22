# template for "Stopwatch: The Game"

# define global variables
import simplegui
t = 0
winning_stops = 0
total_stops = 0
is_running = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global tenths
    tenths = t % 10
    t = (t - tenths)/10
    seconds = t % 60
    t = t - seconds
    minutes = t / 60
    if seconds < 10:
        return str(minutes) + ":0" + str(seconds) + "." + str(tenths)
    else:
        return str(minutes) + ":" + str(seconds) + "." + str(tenths)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def stop_handler():
    global winning_stops
    global total_stops
    global is_running
    if is_running == True:
        if tenths == 0:
            winning_stops += 1
        total_stops += 1
    timer.stop()
    is_running = False
    
def start_handler():
    global is_running
    timer.start()
    is_running = True
    
def reset_handler():
    global winning_stops
    global total_stops
    global t
    global is_running
    winning_stops = 0
    total_stops = 0
    timer.stop()
    is_running = False
    t = 0
    
# define event handler for timer with 0.1 sec interval
def tick():
    global t
    t += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(t), [100,200], 80, "White")
    canvas.draw_text(str(winning_stops) + "/" + str(total_stops), [100,100], 50, "Red")
    canvas.draw_text("Points/Attempts",[50,50],30,"Red")
    
# create frame
frame = simplegui.create_frame("Timer", 400, 300)

# register event handlers
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)
start_button = frame.add_button("Start", start_handler, 50)
stop_button = frame.add_button("Stop",stop_handler, 50)
reset_button = frame.add_button("Reset", reset_handler, 50)

# start frame
frame.start()

# Please remember to review the grading rubric
