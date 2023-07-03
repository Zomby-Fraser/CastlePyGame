import pygame
from rules import Rules
import random

class Player:
    def __init__(self, name, type, id, debug_mode = False, debug_type = "Always Playable"):
        self.hand = []
        self.castle = []
        self.hand_rect = []
        self.castle_rect = []
        self.id = id
        self.name = name
        self.type = type
        self.debug_mode = debug_mode
        self.debug_type = debug_type

    def play_hand(self, event, center_pile, entire_pile, deck, window_y, player_list):
        rules = Rules(player_list, debug_mode = self.debug_mode, debug_type = self.debug_type)
        active_player = None

        #If the player is of type "human"
        if self.type == "human":
            #Check if they do not have any playable cards. They do not, they get the pile added to their hand
            if not rules.has_playable_card(self, entire_pile[-1] if entire_pile else None, self.debug_mode, self.debug_type):
                self.hand = self.hand + entire_pile
                # print(self.hand_rect)
                self.hand_rect = self.hand_rect + [pygame.Rect(0,0,deck.card_width, deck.card_height)]*len(entire_pile)
                center_pile.clear()
                entire_pile.clear()

            #If debug mode is on so that the player never has a playable card, go to the next turn
            if self.debug_type == "Never Playable" and not self.debug_mode:
                active_player = self.next_turn(player_list)
                return active_player
            
            #If they do have a playable card and Never Playable is turned off then let them make their move
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                to_remove = None
                for i, (card_rect, card) in enumerate(zip(self.hand_rect, self.hand)):
                    if card_rect.collidepoint(mouse_x, mouse_y):
                        if (len(entire_pile) > 0 and rules.is_card_playable(self.hand[i], center_pile[-1], self.debug_mode, self.debug_type)) or len(entire_pile) == 0:
                            center_pile.append(self.hand[i])
                            entire_pile.append(self.hand[i])
                            if len(center_pile) > 4:
                                center_pile.pop(0)
                            to_remove = i
                            break
                        elif not rules.is_card_playable(self.hand[i], center_pile[-1], self.debug_mode, self.debug_type):
                            print(f"Wrong card try again: {self.hand[i].rank}")
                            # print(self.hand_rect)
                if to_remove is not None:
                    self.hand_rect.pop(to_remove)  # Remove the card's Rect from hand
                    self.hand.pop(to_remove)  # Remove the card from hand
                    self.hand.append(deck.draw_card())
                    self.hand_rect.append(pygame.Rect(0, window_y-200, deck.card_width, deck.card_height))
                    active_player = self.next_turn(player_list)
                    return active_player
                
        #If player is of type "computer"
        elif self.type == "computer":
            selected_card = random.choice(self.hand)
            index_of_selected_card = self.hand.index(selected_card)
            center_pile.append(selected_card)
            entire_pile.append(selected_card)
            if len(center_pile) > 4:
                center_pile.pop(0)
            self.hand_rect.pop(index_of_selected_card)  # Remove the card's Rect from hand
            self.hand.pop(index_of_selected_card)  # Remove the card from hand
            self.hand.append(deck.draw_card())
            self.hand_rect.append(pygame.Rect(0, window_y-800, deck.card_width, deck.card_height))
            print(f"computer played {selected_card}")
            # print("Next!")
            active_player = self.next_turn(player_list)
            return active_player
        return self
        
        
    def next_turn(self, player_list):
        found_current_player = False
        active_player = None
        for player in player_list:
            if found_current_player:
                active_player = player
            if player == self:
                found_current_player = True
        if not active_player:
            active_player = player_list[0]
        return active_player
    
    def refill_hand(self, deck, window_y):
        while len(self.hand) < 3:
            self.hand.append(deck.draw_card())
            self.hand_rect.append(pygame.Rect(0, window_y-200, deck.card_width, deck.card_height))
