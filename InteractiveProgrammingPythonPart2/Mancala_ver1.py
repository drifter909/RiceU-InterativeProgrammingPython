"""
Student facing implement of solitaire version of Mancala - Tchoukaillon
Goal: Move as many seeds from given houses into the store
In GUI, you make ask computer AI to make move or click to attempt a legal move
"""

class SolitaireMancala:
    """
    Simple class that implements Solitaire Mancala
    """
    
    def __init__(self):
        """
        Create Mancala game with empty store and no houses
        """
        self.board = [0]
    
    def set_board(self, configuration):
        """
        Take the list configuration of initial number of seeds for given houses
        house zero corresponds to the store and is on right
        houses are number in ascending order from right to left
        """
        temp_board = []
        for num in range (1,len(configuration) + 1 ):
            self.board.append(configuration[-1*num])
        self.board.pop(0)
    
    def __str__(self):
        """
        Return string representation for Mancala board
        """
        return str(self.board)
    
    def get_num_seeds(self, house_num):
        """
        Return the number of seeds in given house on board
        """
        return self.board[-1*house_num - 1]

    def is_game_won(self):
        """
        Check to see if all houses but house zero are empty
        """
        for ind, house in enumerate(self.board):
            if ind != len(self.board) - 1 and house != 0:
                return False
        return True
    
    def is_legal_move(self, house_num):
        """
        Check whether a given move is legal
        """
        if house_num == self.get_num_seeds(house_num):
            return True
        return False
    
    def apply_move(self, house_num):
        """
        Move all of the stones from house to lower/left houses
        Last seed must be played in the store (house zero)
        """
        if self.is_legal_move(house_num):
            for ind, val in enumerate(self.board):
                if ind == len(self.board) - (1+house_num):
                    self.board[ind] = 0
                elif ind > len(self.board) - (1+house_num):
                    self.board[ind] += 1
        return self.board          

    def choose_move(self):
        """
        Return the house for the next shortest legal move
        Shortest means legal move from house closest to store
        Note that using a longer legal move would make smaller illegal
        If no legal move, return house zero
        """
        for num in range(1,len(self.board)):
            if self.is_legal_move(num):
                return num
                         
#[0,5,3,1,1,0,0]            
            
    
    def plan_moves(self):
        """
        Return a sequence (list) of legal moves based on the following heuristic: 
        After each move, move the seeds in the house closest to the store 
        when given a choice of legal moves
        Not used in GUI version, only for machine testing
        """
        move_list = []
        while is_game_won != True:
            move_list.append(self.choose_move())
            self.apply_move(self.choose_move())
                            
        return move_list

# Create tests to check the correctness of your code

def test_mancala():
    """
    Test code for Solitaire Mancala
    """
    
    my_game = SolitaireMancala()
    print "Testing init - Computed:", my_game, "Expected: [0]"
    
    config1 = [0, 0, 1, 1, 3, 5, 0]    
    my_game.set_board(config1)   
    
    print "Testing set_board - Computed:", str(my_game), "Expected:", str([0, 5, 3, 1, 1, 0, 0])
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(1), "Expected:", config1[1]
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(3), "Expected:", config1[3]
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(5), "Expected:", config1[5]

    print "Testing is_game_won - Computed:", my_game.is_game_won(), "Expected:", False
    my_game2 = SolitaireMancala()
    config2 = [16,0,0,0,0,0,0]
    my_game2.set_board(config2)
    print "Testing is_game_won - Computed:", my_game2.is_game_won(), "Expected:", True

    print "Testing is_legal_move - Computed:", my_game.is_legal_move(5), "Expected:", True
    print "Testing is_legal_move - Computed:", my_game.is_legal_move(3), "Expected:", False

    print "Testing apply_move - Computed:", my_game.apply_move(3), "Expected:", [0,5,3,1,1,0,0]
    print "Testing apply_move - Computed:", my_game.apply_move(5), "Expected:", [0,0,4,2,2,1,1]

    print "Testing choose_move - Computed:", my_game.choose_move(), "Expected:", 1


test_mancala()


#Import GUI code once you feel your code is correct
#import poc_mancala_gui
#poc_mancala_gui.run_gui(SolitaireMancala())
