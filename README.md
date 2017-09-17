# Project1 SI 507 Fall 2017

This is the first class project of SI 507 offered by UMSI in Fall 2017.The primary functionality of the program is to simulate the process of two people playing card game of war (and play a song at the end). However, this has already been implemented in the source code provided to us. Our main practice to to write test cases for the project, in order to ensure the aforementioned functionality has been implemented in strict correspondance to the code_description 

## Prerequisites

This project is designed to run with Python 3 on Linux or Windows OS.

```
certifi==2017.7.27.1
chardet==3.0.4
idna==2.6
requests==2.18.4
urllib3==1.22
```

## Installing
If you are using a virtual environment, set up and activate it first:
```
cd path/to/virtual_environment_directory

virtualenv --python="path/to/python.exe"

source venv/Scripts/activate
```

To set up the environment for running the code, do the following(replace pip with pip3 if you are not using a virtual environment and have python 2 installed as well):

```
cd path/to/working_directory

git clone REPO_URL

cd SI507_project1

pip install -r requirements.txt 
```
## Running
After setting up the environment, run SI507F17_project1_cards.py, with an expected output as below: 

```
*** BEGIN THE GAME ***

Player 1 plays 11 of Clubs & Player 2 plays 12 of Spades
Player 2 wins a point!
Player 1 plays 10 of Clubs & Player 2 plays 13 of Clubs
Player 2 wins a point!
...
Player 1 plays 3 of Diamonds & Player 2 plays 1 of Spades
Player 1 wins a point!
Player 1 plays 3 of Hearts & Player 2 plays 8 of Hearts
Player 2 wins a point!


******
TOTAL SCORES:
Player 1: 23
Player 2: 25


Player2 wins
All I Do Is Win (feat. T-Pain, Ludacris, Snoop Dogg & Rick Ross) DJ Khaled
```

## Running the Test

run SI507F17_project1_tests.py, should expect an output displaying 3 failures being checked out:

```
test_Card_constructor (__main__.TestCardClass) ... ok
test_Card_str_method (__main__.TestCardClass) ... FAIL
test_Card_variables (__main__.TestCardClass) ... ok
test_Deck_constructor (__main__.TestDeckClass) ... ok
test_Deck_deal_hand_method (__main__.TestDeckClass) ... ok
test_Deck_replace_card_method (__main__.TestDeckClass) ... ok
test_Deck_shuffle_method (__main__.TestDeckClass) ... ok
test_Deck_sort_cards_method (__main__.TestDeckClass) ... FAIL
test_Deck_string_method (__main__.TestDeckClass) ... ok
test_Dectk_pop_card_method (__main__.TestDeckClass) ... ok
test_play_war_game_function (__main__.TestPlayWarGameFunction) ... FAIL
test_show_song_function (__main__.TestShowSong) ... Big Sky Hurrah
Win David Bowie
ok

======================================================================
FAIL: test_Card_str_method (__main__.TestCardClass)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "F:\UMich\courses\SI507\projects\project1\SI507F17_project1_tests.py", line 51, in test_Card_str_method
    self.assertTrue(str(self.card2)=="King of Spades")
AssertionError: False is not true

======================================================================
FAIL: test_Deck_sort_cards_method (__main__.TestDeckClass)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "F:\UMich\courses\SI507\projects\project1\SI507F17_project1_tests.py", line 147, in test_Deck_sort_cards_method
    self.assertEqual(str(self.deck),expected_string,"test sort_card method")
AssertionError: '1 of Diamonds\n2 of Diamonds\n3 of Diamond[657 chars]ades' != '12 of Diamonds\n8 of Clubs\n2 of Hearts\n4 of Spades'
Diff is 785 characters long. Set self.maxDiff to None to see it. : test sort_card method

======================================================================
FAIL: test_play_war_game_function (__main__.TestPlayWarGameFunction)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "F:\UMich\courses\SI507\projects\project1\SI507F17_project1_tests.py", line 183, in test_play_war_game_function
    self.assertIsInstance(result,tuple,"test first returned value's type")
AssertionError: 'Player1' is not an instance of <class 'tuple'> : test first returned value's type

----------------------------------------------------------------------
Ran 12 tests in 0.869s

FAILED (failures=3)
```


## Coding Style
PEP 8

## Contributor
Yanbang WANG

## Acknowledgments
During the process, course instructor Dr.Jaclyn Cohen and GSI Mr.Anand Pankaj Doshi has provided for me great help and support in learning the knowledge and dealing with the code.

