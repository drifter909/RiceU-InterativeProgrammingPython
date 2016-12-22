"""
Lightweight testing class inspired by unittest from Pyunit
https://docs.python.org/2/library/unittest.html
Note that code is designed to be much simpler than unittest
and does NOT replicate unittest functionality
"""

import poc_simpletest
               
def run_suite_gen_all_seq(gen_all_sequences):
    """
    Testing code to generate all possible yahtzee combinations
    """
    
    suite = poc_simpletest.TestSuite()
    
    suite.run_test(gen_all_sequences([1,2,3,4,5,6],1),
                   set([(1,),(2,),(3,),(4,),(5,),(6,)]), "Test #1: all_seq 1 die")
    
    suite.run_test(gen_all_sequences([1,2,3,4,5,6],2),
                   set([(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),
                      (2,1),(2,2),(2,3),(2,4),(2,5),(2,6),
                      (3,1),(3,2),(3,3),(3,4),(3,5),(3,6),
                      (4,1),(4,2),(4,3),(4,4),(4,5),(4,6),
                      (5,1),(5,2),(5,3),(5,4),(5,5),(5,6),
                      (6,1),(6,2),(6,3),(6,4),(6,5),(6,6)]), "Test #2: all_seq 2 dice")
    
    suite.report_results()
    
def run_suite_score(score):
    
    suite = poc_simpletest.TestSuite()
    
    suite.run_test(score((1,5,5,5,4,6)),15, "Test #3: Score")
    suite.run_test(score((1,1,1,1,1,4)),5, "Test #4: Score")
    suite.run_test(score((6,6)),12, "Test #5: Score")
    
    suite.report_results()
    
def run_suite_expected_value(expected_value):
    
    suite = poc_simpletest.TestSuite()
    
    suite.run_test(expected_value((1,5,5,5,4,6),6, 0),15, "Test #5: Exp Val")
    suite.run_test(expected_value((),6,2),5.06, "Test #6: Exp Val")
    
    suite.report_results()
    