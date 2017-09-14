## Do not change import statements.
import unittest
from SI507F17_project1_cards import *

## Write your unit tests to test the cards code here.
## You should test to ensure that everything explained in the code description file works as that file says.
## If you have correctly written the tests, at least 3 tests should fail. If more than 3 tests fail, it should be because multiple of the test methods address the same problem in the code.
## You may write as many TestSuite subclasses as you like, but you should try to make these tests well-organized and easy to read the output.
## You should invoke the tests with verbosity=2 (make sure you invoke them!)

###########

class TestCardClass(unittest.TestCase):
    def setUp(self):
        self.card1=Card();
        self.card2=Card(3,8)

    
    def test_Card_variables(self):
        self.assertEqual(len(self.card1.suit_names),4,"test default Card's suit_names content length")
        self.assertTrue("Diamonds" in self.card1.suit_names,"test default Card's suit_names content")
        self.assertTrue("Clubs" in self.card1.suit_names,"test default Card's suit_names content")
        self.assertTrue("Hearts" in self.card1.suit_names,"test default Card's suit_names content")
        self.assertTrue("Spades" in self.card1.suit_names,"test default Card's suit_names content")
        
        self.assertEqual(self.card1.rank_levels,list(range(1,14)),"test default Card's rank_levels content")
        
        expected_dict={1:'Ace',11:'Jack',12:'Queen',13:'King'}
        self.assertTrue(isinstance(self.card1.faces,dict),"test default Card's faces type")
        shared_items = set(self.card1.faces.items()) & set(expected_dict.items())        
        self.assertEqual(len(shared_items),4,"test default Card's faces content")
        

    def test_Card_constructor(self):
        

    def test_Card_method(self):
        pass
unittest.main(verbosity=2)
