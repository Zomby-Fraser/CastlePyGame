import pygame

class Rules:
    def __init__(self):
        pass

    def is_card_playable(self, selected_card, top_pile_card):
        if selected_card.rank in ["Two", "Three", "Seven", "Ten"]:
            return True
        elif top_pile_card.rank == "Seven" and top_pile_card.value > selected_card.value:
            return True
        elif selected_card.value >= top_pile_card.value:
            return True
        else:
            return False
        
    def has_playable_card(self, player, top_card):
        for card in player.hand:
            if self.is_card_playable(card, top_card):
                return True
        return False