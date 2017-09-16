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
        self.card2=Card(3,13)

    
    def test_Card_variables(self):
        self.assertEqual(self.card1.suit_names,['Diamonds','Clubs','Hearts','Spades'],"test Card's suit_names content")

        self.assertEqual(self.card1.rank_levels,list(range(1,14)),"test Card's rank_levels content")
        
        expected_dict={1:'Ace',11:'Jack',12:'Queen',13:'King'}
        self.assertTrue(isinstance(self.card1.faces,dict),"test Card's faces type")
        shared_items = set(self.card1.faces.items()) & set(expected_dict.items())        
        self.assertEqual(len(shared_items),4,"test Card's faces content")
        
        
    def test_Card_constructor(self):
        # test Card constructor without passing arguments
        self.assertEqual(self.card1.suit,'Diamonds',"test Card's default constructor")
        
        self.assertEqual(self.card1.rank,2,"test Card's default constructor")
        
        self.assertEqual(self.card1.rank_num,2,"test Card's default constructor")

        # test Card constructor by passing arguments
        self.assertEqual(self.card2.suit,'Spades',"test Card's constructor with arguments")
        
        self.assertTrue(isinstance(self.card2.rank,int) or isinstance(self.card2.rank, str))
        if(isinstance(self.card2.rank,int)):
            self.assertEqual(self.card2.rank,13,"test Card's constructor with arguments")
        else:
            self.assertEqual(self.card2.rank,'King',"test Card's constructor with arguments")
            
        self.assertEqual(self.card2.rank_num,13,"test Card's constructor with arguments")
        

    def test_Card_str_method(self):
        self.assertEqual(str(self.card1),"2 of Diamonds")
        self.assertTrue(str(self.card2)=="King of Spades" or str(self.card2)=="13 of Spades")

class TestDeckClass(unittest.TestCase):
    def setUp(self):
        self.template_card=Card()
        self.deck=Deck()

    def test_Deck_constructor(self):
        self.assertIsInstance(self.deck.cards, list, "test cards' type")
        self.assertEqual(len(self.deck.cards),52,"test cards' length")
        for i in range(1,14):
            for j in range(4):
                self.assertTrue(str(Card(j,i)) in str(self.deck),"test cards' content")

        
    def test_Deck_string_method(self):
        deck_name=str(self.deck)
        self.assertIsInstance(deck_name,str,"test __str__ method's returned type, actually a little redundant")
        lines=deck_name.split('\n')
        self.assertEqual(len(lines),52,"test whether __str__ method returns 52 lines")
        for i in range(1,14):
            for j in range(4):
                self.assertTrue(str(Card(j,i)) in lines,"test __str__ method's returned content")

    def test_Dectk_pop_card_method(self):
        expected_card1=self.deck.cards[-1]
        card1=self.deck.pop_card()
        self.assertEqual(str(card1),str(expected_card1),"test the defualt behavior of pop method")
        for i in range(1,14):
            for j in range(4):
                
                if str(Card(j,i))==str(card1):
                    continue
                self.assertTrue(str(Card(j,i)) in str(self.deck),"test defualt behavior of pop method")

        expected_card2=self.deck.cards[0]
        card2=self.deck.pop_card(0)
        self.assertEqual(str(card2),str(expected_card2),"test the pop method by passing user-defined position")

        for i in range(1,14):
            for j in range(4):
                if str(Card(j,i))==str(card1):
                    continue
                self.assertTrue(str(Card(j,i)) in str(self.deck),"test the pop method by passing user-defined position")

                
        for i in range(50):
            self.assertTrue(self.deck.pop_card(),"test whether the Deck object can keep popping when it has cards")
            # self.assertTrue(not self.deck.pop_card(),"test whether the Deck object can still pop when it is already empty")

    def test_Deck_shuffle_method(self):
        positions=[]
        # test type,length,content
        self.deck.shuffle()
        self.assertIsInstance(self.deck.cards, list, "test shuffuled cards' type")
        self.assertEqual(len(self.deck.cards),52,"test shuffuled cards' length")
        for i in range(1,14):
            for j in range(4):
                self.assertTrue(str(Card(j,i)) in str(self.deck),"test shuffuled cards' content")
                positions.append(str(self.deck).split('\n').index(str(Card(j,i))))

        # test randomness
        new_positions=[]
        # test type,length,content
        self.deck.shuffle()
        for i in range(1,14):
            for j in range(4):
                new_positions.append(str(self.deck).split('\n').index(str(Card(j,i))))
        self.assertTrue(new_positions!=positions,"test randomness of shuffling")

    def test_Deck_replace_card_method(self):
        original_name_lines=str(self.deck).split('\n')
        name30=original_name_lines.pop(30)
        original_name_lines.append(name30)
        expected_deck_name='\n'.join(original_name_lines)

        card30=self.deck.pop_card(30)
        self.deck.replace_card(card30)
        self.assertEqual(str(self.deck),expected_deck_name,"test whether 'adding new card' functions well")
        deck_name=str(self.deck)

        self.deck.replace_card(card30)
        self.assertEqual(deck_name,str(self.deck),"test whether 'adding old card' functions well")
                                            
        


    def test_Deck_sort_cards_method(self):
        for i in range(0,52):
            self.deck.pop_card()
        self.deck.replace_card(Card(3, 4))
        self.deck.replace_card(Card(2, 2))
        self.deck.replace_card(Card(0, 12))
        self.deck.replace_card(Card(1, 8))
        self.deck.sort_cards()
        expected_string="{}\n{}\n{}\n{}".format(str(Card(0, 12)),str(Card(1, 8)),str(Card(2, 2)),str(Card(3, 4)))
        self.assertEqual(str(self.deck),expected_string,"test sort_card method")

    def test_Deck_deal_hand_method(self):
        
        for i in range(3):
            self.deck.pop_card()
        original_deck_name=str(self.deck)
        hand=self.deck.deal_hand(5)
        self.assertIsInstance(hand, list,"test the type of the returned value")
        self.assertEqual(len(hand),5,"test the length of the returned list")
        self.assertIsInstance(hand[0],Card,"test the type of elements in the returned list")
        indices=[]
        for i in range(5):
            self.assertTrue(str(hand[i]) in original_deck_name.split('\n'),"test if hand's card comes from the original deck")
            index=original_deck_name.split('\n').index(str(hand[i]))
            self.assertFalse(index in indices,"test if 'hand' has any duplicate cards")
            indices.append(original_deck_name.split('\n').index(str(hand[i])))

        
        # test the case where many cards are asked to returned
        """
        original_deck_name=str(self.deck)
        hand=self.deck.deal_hand(50)
        self.assertIsInstance(hand, list,"test the type of the returned value")
        self.assertEqual(len(hand),44,"test the length of the returned list")
        self.assertIsInstance(hand[0],Card,"test the type of elements in the returned list")
        indices=[]
        for i in range(5):
            self.assertTrue(str(hand[i]) in original_deck_name.split('\n'),"test if hand's card comes from the original deck")
            index=original_deck_name.split('\n').index(str(hand[i]))
            self.assertFalse(index in indices,"test if 'hand' has any duplicate cards")
            indices.append(original_deck_name.split('\n').index(str(hand[i])))
        """
class TestPlayWarGameFunction(unittest.TestCase):
    def test_play_war_game_function(self):
        result,score1,score2=play_war_game(testing=True)
        self.assertIsInstance(result,str,"test first returned value's type")
        self.assertIsInstance(score1,int,"test second returned value's type")
        self.assertIsInstance(score2,int,"test third returned value's type")
        if score1>score2:
            self.assertEqual(result,'Player1')
        elif score1==score2:
            self.assertEqual(result,'Tie')
        else:
            self.assertEqual(result,'Player2')


if __name__=='__main__':
    unittest.main(verbosity=2)
