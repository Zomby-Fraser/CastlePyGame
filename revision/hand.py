class Hand:
    
    def __init__(self, player_id):
        self.cards = []
        self.playable_cards = []
        self.player_id = player_id

    '''
        Returns a list of playable cards in the player's hand
        INPUTS ->
            * pile -> Class Pile
                - The active pile in the game
        RETURNS -> None; alters the class attribute
    '''
    def listPlayableCards(self, pile):
        self.playable_card = []
        for card in self.cards:
            if isCardPlayableCopyCheck(card, pile):
                self.playable_card.append(card)

    '''
        Determines if a particular card is playable at that moment in the game
        INPUTS -> 
            * card -> Class Card
                - The card being checked for playability
            * pile -> Class Pile
                - The active pile in the game
        RETURNS -> Bool
    '''
    def isCardPlayableCopyCheck(card, pile):
        pile_top_card = pile.cards[-1]
        if card.is_special:
            return True
        elif pile_top_card.special_property == 'copy':
            pile_top_non_copy = pile.nonCopyValue(pile, -1)
            return self.isCardPlayable(pile_top_non_copy, card)
        else:
            return self.isCardPlayable(pile_top_card, card)
            
    '''
        Determines if a particular card in general (internal use only, see `Hand.isCardPlayableCopyCheck`)
        INPUTS -> 
            * pile_card -> Class Card
                - The card being compared to.
            * hand_card -> Class Card
                - The card being checked for playability
        RETURNS -> Bool
    '''
    def isCardPlayable(self, pile_card, hand_card):
        if reference_card.special_property == 'reset':
            return True
        elif reference_card.special_property == 'lower' and reference_card.value > hand_card.value:
            return True
        elif reference_card.value <= hand_card.value:
            return True
        else:
            return False

    '''
        Finds the lowest value non-special card in the player's hand
        RETURNS -> Class Card
    '''
    def lowestNormalCard(self):
        lowest_normal_card = None
        for i, card in enumerate(hand.cards):
            if not lowest_normal_card:
                lowest_normal_card = card
            else:
                if card.value < lowest_normal_card.value and not card.is_special:
                    lowest_normal_card = card
       return {
           'lowest_card': lowest_normal_card,
           'idx': i
       }
