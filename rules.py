import pygame

class Rules:
    def __init__(self, config, player_list, debug_mode = False, debug_type = "Always Playable"):
        self.debug_mode = debug_mode
        self.player_list = player_list
        self.debug_type = debug_type
        self.config = config

    def is_card_playable(self, selected_card, entire_pile, player_debug = False, debug_type = "Always Playable"):
        # print(f"Top Card: {top_pile_card}")
        # print(f"Selected Card: {selected_card}")
        if len(entire_pile) == 0:
            top_pile_card = None
        else:
            top_pile_card = entire_pile[-1]
        compare_card = None
        if top_pile_card == "Three":
            for card in entire_pile:
                if card != "Three":
                    compare_card = card
        else: 
            if len(entire_pile) > 0:
                compare_card = entire_pile[-1]
            else:
                compare_card = None
        if not top_pile_card:
            return True
        elif self.debug_mode and player_debug and debug_type == "Always Playable":
            return True
        elif self.debug_mode and player_debug and debug_type == "Never Playable":
            return False
        elif selected_card.rank in ["Two", "Three", "Seven", "Ten"]:
            return True
        elif compare_card.rank == "Seven" and compare_card.value > selected_card.value:
            return True
        elif compare_card.rank != "Seven" and compare_card.rank != "Three" and selected_card.value >= compare_card.value:
            return True
        else:
            return False
        
    def has_playable_card(self, player, entire_pile, player_debug = False, debug_type = "Always Playable"):
        for card in player.hand:
            if self.is_card_playable(card, entire_pile, player_debug, debug_type):
                return True
        return False
    
    def playable_card_list(self, player, entire_pile, player_debug = False, debug_type = "Always Playable"):
        playable_cards = []
        for card in player.hand:
            if self.is_card_playable(card, entire_pile, player_debug, debug_type):
                playable_cards.append(card)
        return playable_cards
    
    def check_four_in_a_row(self, entire_pile):
        last_card = None
        last_non_three_card = None
        consecutive_card_count = 0
        for card in entire_pile:
            if card.rank == "Three":
                if last_non_three_card is not None:
                    card = last_non_three_card
                else:
                    continue
            else:
                last_non_three_card = card
            if not last_card:
                last_card = card
                consecutive_card_count = 1
                continue
            if last_card == card:
                consecutive_card_count += 1
            else:
                consecutive_card_count = 1
                last_card = card
            if consecutive_card_count >= 4:
                return True
        return False



            

