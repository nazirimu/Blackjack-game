#Imports
from art import logo
import random
from replit import clear

def random_card():
    ''' Returns a random card from the deck '''
    cards_list = [11, 2 , 3 , 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards_list)

def calculate_score(cards):
    ''' Returns the total score for the hand '''
    score = sum(cards)
    
    if score == 21 and len(cards) == 2:
        score = 0
    if score > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    
    return score

def compare_scores(player, dealer):
    ''' Compares the scores and evaluates the winner '''
    if dealer == 0:
        return('The dealer has a blackjack! You lose.')
    elif player == 0:
        return('Your total is higher! You win.')
    elif player == dealer:
        return('Its a draw!.')
    elif player > 21:
        return('You are over 21. You lose!')
    elif dealer > 21:
        return('Dealer went over 21. You win!')
    elif player > dealer:
        return('Your total is higher! You win.')
    else:
        return 'You lose! the dealer was higher'

def blackjack():
    ''' Runs the game '''
    #cards
    cards_user = [random_card(),random_card()]
    cards_dealer = [random_card(),random_card()]

    
 
    user_pass = False
    while not user_pass:
        user_score = calculate_score(cards_user)
        dealer_score = calculate_score(cards_dealer)
        print(f'Your cards are {cards_user}. Total score = {sum(cards_user)}')
        print (f'The computers first card is: {cards_dealer[0]}')

        if dealer_score == 0 or user_score == 0 or user_score > 21:
            user_pass = True  
        else:
            more_cards = input("Type 'y' for another card. Type 'n' for pass: ").lower()
            if more_cards == 'y':
                cards_user.append(random_card())
            else:
                user_pass = True
    
    
    while not dealer_score != 0 and dealer_score < 17:
        cards_dealer.append(random_card())
        dealer_score = calculate_score(cards_dealer)
    
    print(compare_scores(user_score, dealer_score))
    

play = True
while play:
    start = input("Do you want to play black jack? (y/n) ").lower()
    if start == 'y':
        clear()
        print(logo)
        blackjack()
    elif start == 'n':
        print("Goodbye!")
        play= False
    else:
        print("Invalid selection. The program will exit.")
        play= False











############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []



#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

