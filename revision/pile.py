class Pile:
    
    def __init__(self):
        self.cards = []

     '''
        Recursively checks for the next card that doesn't have the speical_propery = 'copy'.
        Effectively used to tell what cards are actually playable since the 'copy' property acts as a wild card
        INPUTS -> 
            * pile -> Class Pile
                - The active pile in the game
            
        RETURNS -> `Class Card`
    '''
    def nonCopyValue(i):
        if abs(i) <= len(self.pile.cards):
            if self.pile.cards[i].special_property == 'copy':
                return nonCopyValue(i-1)
            else:
                return self.pile.cards[i]
        else:
            return None
