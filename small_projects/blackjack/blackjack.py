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
        bet = getBet(money)
        
        #Get four cards from the deck, two for player, two for dealer.
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerhand = [deck.pop(), deck.pop()]
        
        #Player interactions
        print("Bet:", bet)
        while True: #Keep looping until the player stands or goes bust (Over 21)
            displayHands(playerhand, dealerHand, False)
            print()
            
            #Check to see if the player cards total > 21
            if getHandValue(playerhand) > 21:
                break
            
            #Get player's move, H, S, or D
            move = getMove(playerhand, money - bet)
            
            #Handle player's actions
            if move == 'D':
                #Double Down
                additionalBet = getBet(min(bet,(money - bet)))
                bet += additionalBet
                print("Bet increased to [].".format(bet))
                print("Bet: ", bet)
                
            if move in('D','H'):
                #Hit or double down gets another card
                newCard = deck.pop()
                rank, suit = newCard
                print('You drew a {} of {}.'.format(rank, suit))
                playerhand.append(newCard)

                if getHandValue(playerhand) > 21:
                    #BUST! HAHAHA
                    continue
            
            if move in ('S', 'D'):
                #Stand or double stops the players turn.
                break
            
        #Handle dealer actions
        if getHandValue(playerhand) <= 21:
            while getHandValue(dealerHand) < 17:
                #Dealer hits
                print("Dealer hits for another card!")
                dealerHand.append(deck.pop())
                displayHands(playerhand, dealerHand, False)
                
                if getHandValue(dealerHand) > 21:
                    break #Dealer buster, whew, thank goodness!
                input("Press any key to continue. . .")
                print("\n\n")
                
            #Show final hands, player and dealer:
            displayHands(playerhand, dealerHand, True)
            
            playerValue = getHandValue(playerhand)
            dealerValue = getHandValue(dealerHand)
            
            #Win lose or tie?
            
            if dealerValue > 21:
                print("Dealer BUSTED! You win ${}!".format(bet))
                money += bet
            elif (playerValue > 21) or (playerValue < dealerValue):
                print("YOU LOST! LOL!")
                money -= bet
            elif playerValue > dealerValue:
                print("You won ${}!".format(bet))
                money += bet
            elif playerValue == dealerValue:
                print("It's a tie, no money gained or lost, whew.")
            
            input("Press Enter to continue. . .")
            print("\n\n")
                
def getBet(maxBet):
    #How much will the player bet?
    while True:
            print("How much do you want to bet? (1-{}, or QUIT)".format(maxBet))
            bet = input("> ").upper().strip()
            if bet == "QUIT":
                print("Thanks for playing, please try again someday.")
                sys.exit()
                
            if not bet.isdecimal(): #Not a number? Try again...
                continue
            
            bet = int(bet)
            if 1 <= bet <= maxBet:
                return bet
    
def getDeck():

    """Return a list of (rank, suit) tuples for all 52 cards."""
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit)) # Add the numbered cards.
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit)) # Add the face and ace cards.
    random.shuffle(deck)
    return deck
    
def displayHands(playerHand, dealerHand, showDealerhand):
    #really cool code goes here.
    
    return #this is not the cool code

def getHandValue(cards):
    #cool code
    
    return #not cool code
    
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