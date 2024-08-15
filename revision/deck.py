import random
from card import Card

class Deck:
    def __init__(
        self, 
        number_of_decks = 1,
        suits = ["Clubs", "Diamonds", "Spades", "Hearts"],
        ranks = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", 
                 "Eight", "Nine", "Ten", "Jack", "Queen", "King"],
        values = [14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        is_special = [False, True, True, False, False, False, True, False, False, True, False, False, False]

        ''' 
            This determines the property of the card, if it has one.
            * None - Normal card
            * 'reset' - Resets the deck so any card can be played after this card
            * 'copy' - Copies the card before it. Three duplicates and a 'copy' card clears the deck as if 4 of the same kind were played.
            * 'lower' - Reverses the game's behavior. The number this is assigned is the upper cut off. By default this is a 7 card. If a 7 is played then 4,5,6 must be played, or another special card.
            * 'clear' - Clears the pile from play.
        '''
        special_property = [None, 'reset', 'copy', None, None, None, 'lower', None, None, 'clear', None, None, None]
    ):
        self.cards = []
    
        for deck_no in range(number_of_decks):
            for suit in enumerate(suits):
                for rank, value in zip(ranks, values, is_special, special_property):
                    self.cards.append(Card(suit, rank, value, is_special, special_property))

    def __str__(self):
        return f'Card #{self.id}: {self.rank} of {self.suit} with value {self.value}'
                    
    def shuffle(self):
        random.shuffle(self.cards)
        
    def drawCard(self):
        return self.cards.pop()
