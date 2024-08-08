class Card:
    
    _next_id = 1  # Class variable to assign unique IDs to each card

    def __init__(self, suit, rank, value):
        self.id = Card._next_id
        Card._next_id += 1
        self.suit = suit
        self.rank = rank
        self.value = value
        
        def __str__(self):
            return f'Card #{self.id}: {self.rank} of {self.suit} with value {self.value}'
