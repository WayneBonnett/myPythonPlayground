"""Blackjack
The classic card game also known as 21. (This version doesn't have splitting or insurance.)
More info at: https://en.wikipedia.org/wiki/Blackjack
"""

import random
import sys

#Set up suits
HEARTS   = chr(9829) # ♥
DIAMONDS = chr(9830) # ♦
SPADES   = chr(9824) # ♠
CLUBS    = chr(9827) # ♣
BACKSIDE = 'backside' # the back of the cards

money = 10_000

def main():
    print('''Blackjack
          
        #Rules of this game:
            * Try to reach a score as close to 21 without going over. You start with $10k.
          
        #Card point values
            * Kings  10 points
            * Queens 10 points
            * Jacks  10 points
            * Aces  1 or 11 points
            * Cards 2 through 10 are worth face value

        #Game Options  
            * (H)it to have the dealer deal another card.
            * (S)tand to stop taking cards from the dealer.
            * On the first play you can (D)ouble down to double your bet but you must (H)it one more time before (S)tanding.
            * The dealer stops betting after hitting 17 or above. If there is a tie, the bet is returned to the player.
          
#Good luck!
          ''')
    money = 10_000
    
    print(money)


if __name__ == '__main__':
    main()