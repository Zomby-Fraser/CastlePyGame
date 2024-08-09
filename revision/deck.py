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
    ):
        self.cards = []
    
        for deck_no in range(number_of_decks):
            for suit in enumerate(suits):
                for rank, value in zip(ranks, values):
                    self.cards.append(Card(suit, rank, value))

    def __str__(self):
        return f'Card #{self.id}: {self.rank} of {self.suit} with value {self.value}'
                    
    def shuffle(self):
        random.shuffle(self.cards)
        
    def drawCard(self):
        return self.cards.pop()
