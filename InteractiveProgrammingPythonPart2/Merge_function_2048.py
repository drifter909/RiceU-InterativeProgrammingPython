"""
Merge function for 2048 game.
"""

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


#print "TEST: " + str(merge([2,0,2,4])) + " Expected: [4,4,0,0]"
#print "TEST: " + str(merge([0,0,2,2])) + " Expected: [4,0,0,0]"
#print "TEST: " + str(merge([2,2,0,0])) + " Expected: [4,0,0,0]"
#print "TEST: " + str(merge([2,2,2,2,2])) + " Expected: [4,4,2,0,0]"
#print "TEST: " + str(merge([8,16,16,8])) + " Expected: [8,32,8,0]"