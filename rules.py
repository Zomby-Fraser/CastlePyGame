import pygame

class Rules:
    def __init__(self, player_list, debug_mode = False, debug_type = "Always Playable"):
        self.debug_mode = debug_mode
        self.player_list = player_list
        self.debug_type = debug_type

    def is_card_playable(self, selected_card, top_pile_card, player_debug = False, debug_type = "Always Playable"):
        if self.debug_mode and player_debug and debug_type == "Always Playable":
            return True
        elif self.debug_mode and player_debug and debug_type == "Never Playable":
            return False
        elif not top_pile_card:
            return True
        elif selected_card.rank in ["Two", "Three", "Seven", "Ten"]:
            return True
        elif top_pile_card.rank == "Seven" and top_pile_card.value > selected_card.value:
            return True
        elif selected_card.value >= top_pile_card.value:
            return True
        else:
            return False
        
    def has_playable_card(self, player, top_card, player_debug = False, debug_type = "Always Playable"):
        for card in player.hand:
            if self.is_card_playable(card, top_card, player_debug, debug_type):
                return True
        return False
    
    def playable_card_list(self, player, top_card, player_debug = False, debug_type = "Always Playable"):
        playable_cards = []
        for card in player.hand:
            if self.is_card_playable(card, top_card, player_debug, debug_type):
                playable_cards.append(card)
        return playable_cards