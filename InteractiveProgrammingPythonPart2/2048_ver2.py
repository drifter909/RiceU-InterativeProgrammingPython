"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    def shift_left(row):
        """Function that takes a row, and moves the zeroes
        in the row to the right hand side of the row"""
        new_list = []
        zero_count = 0
        for num in row:
            if num !=0:
                new_list.append(num)
            else:
                zero_count += 1
        while zero_count > 0:
            new_list.append(0)
            zero_count -= 1
        return new_list
    
    shifted_list = shift_left(line)
    combined_list = []
    add_zero = False
    
    
    for ind, num in enumerate(shifted_list):
        if ind < len(shifted_list) - 1:
            if add_zero:
                combined_list.append(0)
                add_zero = False
            elif num == shifted_list[ind+1]:
                combined_list.append(num*2)
                add_zero = True
            else:
                combined_list.append(num)
    if add_zero:
        combined_list.append(0)
    else:
        combined_list.append(shifted_list[-1])
    
    return shift_left(combined_list)

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self.grid_height = grid_height
        self.grid_width = grid_width

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.grid = [[0 + 0 for col in range(self.grid_width)]
                                for row in range(self.grid_height)]
        
        self.new_tile()
        self.new_tile()
        
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        return self.grid

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self.grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self.grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        
        temp_grid = []
        for entry in self.grid:
            temp_grid.append(list(entry))
        
        def traverse_grid(start_cell, direction, num_steps):
            temp_list = []
            for step in range(num_steps):
                row = start_cell[0] + step * direction[0]
                col = start_cell[1] + step * direction[1]
                temp_list.append(self.grid[row][col])
            
            temp_list = merge(temp_list)    
            return temp_list
        
        def update_grid(start_cell, direction, num_steps):
            temp_list = traverse_grid(start_cell, direction, num_steps)
            temp_grid = self.grid[:]
            
            for ind, val in enumerate(temp_list):
                row = start_cell[0] + ind * direction[0]
                col = start_cell[1] + ind * direction[1]
                self.grid[row][col] = val
        
        
        if direction == 1:
            starting_cell = [0,0]
            for dummy_num in range(0,self.grid_width):
                update_grid(starting_cell,OFFSETS[direction],self.grid_height)
                starting_cell[1] += 1
            
        elif direction == 2:
            starting_cell = [self.grid_height - 1 , 0]
            for dummy_num in range(0,self.grid_width):
                update_grid(starting_cell,OFFSETS[direction],self.grid_height)
                starting_cell[1] += 1     
                
        elif direction == 3:
            starting_cell = [0,0]
            for dummy_num in range(0,self.grid_height):
                update_grid(starting_cell,OFFSETS[direction],self.grid_width)
                starting_cell[0] += 1

        elif direction == 4:
            starting_cell = [0,self.grid_width - 1]
            for dummy_num in range(0,self.grid_height):
                update_grid(starting_cell,OFFSETS[direction],self.grid_width)
                starting_cell[0] += 1        
        
        if temp_grid != self.grid:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        need_new_tile = True
        if random.random() > .10:
            new_tile_val = 2
        else:
            new_tile_val = 4
        
        while need_new_tile:
            row = random.randint(0,self.grid_height - 1)
            col = random.randint(0,self.grid_width - 1)
            if self.grid[row][col] == 0:
                self.grid[row][col] = new_tile_val
                need_new_tile = False

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        self.grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return self.grid[row][col]
    
poc_2048_gui.run_gui(TwentyFortyEight(4, 6))
