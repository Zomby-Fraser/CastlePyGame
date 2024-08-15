class Hand:
    
    def __init__(self, player_id):
        self.cards = []
        self.playable_cards = []
        self.player_id = player_id

    def listPlayableCards(self, pile):
        self.playable_card = []
        for card in self.cards:
            if isCardPlayable(card, pile):
                self.playable_card.append(card)

    '''
        Determines if a particular card is playable at that moment in the game.
        INPUTS -> 
            * card -> Class Card
                - The card being checked for playability
            * pile -> Class Pile
                - The active pile in the game
        RETURNS -> Bool
    '''
    def isCardPlayable(card, pile):
        pile_top_card = pile.cards[-1]
        if card.is_special:
            return True
        elif pile_top_card.special_property == 'copy':
            pile_top_non_copy = pile.nonCopyValue(pile, -1)
            if pile_top_card.special_property == 'reset':
                return True
            elif pile_top_card.special_property == 'lower':
                pile_top_non_copy.value > card.value

   
