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
    
    while True: #Main program loop
        #Check to verify the player has money to play the game.
        if money <= 0:
            print("You have no money, sorry, but you can't play.")
            print("Maybe play something that doesn't require money.")
            print("Thanks for playing, try again soon.")
            sys.exit #Bye bye
            
        #Player can bet, horray!!!
        print("You have: " + money + " to play with, let's GO!")


def getBet(maxBet):
    #cool code goes here
    
    return #this is not the cool code
    
def getDeck():
    #more cool code goes here
    
    return #this is not the cool code
    
def displayHands(playerHand, dealerHand, showDealerhand):
    #really cool code goes here.
    
    return #this is not the cool code
    
def getHandValue(cards):
    #cool code
    
    return #not cool code

def displayCards(cards):
    #cool code
    
    return #not cool code

def getMove(playerHand, money):
    #cool code
    
    return #not cool code

# RUN THE GAME!
if __name__ == '__main__':
    main()