class Card:
    
    _next_id = 1  # Class variable to assign unique IDs to each card

    def __init__(self, suit, rank, value, is_special, special_property):
        self.id = Card._next_id
        Card._next_id += 1
        self.suit = suit
        self.rank = rank
        self.value = value
        self.is_special = is_special
        self.special_proprety = special_property
        
        def __str__(self):
            return f'Card #{self.id}: {self.rank} of {self.suit} with value {self.value}'
