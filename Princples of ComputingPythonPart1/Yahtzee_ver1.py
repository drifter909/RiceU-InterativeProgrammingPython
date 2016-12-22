"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
import codeskulptor
import user41_FRAS2lGtvHSeBjE
codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set

def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    highest_score = 0
    temp_score = 0
    for num in range(1,max(hand) + 1):
        if num in hand:
            temp_score = num*hand.count(num)
            if temp_score > highest_score:
                highest_score = temp_score
            temp_score = 0
    return highest_score

def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    total_val = 0
    rerolled_seq = gen_all_sequences(range(1,num_die_sides + 1),num_free_dice)
    for roll in rerolled_seq:
        all_dice = roll + held_dice
        total_val += score(all_dice)
    return round(total_val*1.0 / len(rerolled_seq),2)
    
def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    all_holds = ()
    for dummy_num in range (0,len(hand) + 1):
        all_holds = all_holds + tuple(set(gen_all_sequences(hand, dummy_num)))
    return all_holds


def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    return (0.0, ())


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    
    
run_example()

#user41_FRAS2lGtvHSeBjE.run_suite_gen_all_seq(gen_all_sequences)
#user41_FRAS2lGtvHSeBjE.run_suite_score(score)
#user41_FRAS2lGtvHSeBjE.run_suite_expected_value(expected_value)
#user41_FRAS2lGtvHSeBjE.run_suite_gen_all_holds(gen_all_holds)

import poc_holds_testsuite
poc_holds_testsuite.run_suite(gen_all_holds)     
    
    
    
    



