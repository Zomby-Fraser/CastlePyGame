import pygame
from rules import Rules
import random

class Player:
    def __init__(self, config, name, type, id, debug_mode = False, debug_type = "Always Playable"):
        self.hand = []
        self.castle = []
        self.hand_rect = []
        self.castle_rect = []
        self.id = id
        self.name = name
        self.type = type
        self.debug_mode = debug_mode
        self.debug_type = debug_type
        self.config = config

    def print_hand(self):
        for card in self.hand:
            print(card)

    def play_hand(self, event, center_pile, entire_pile, deck, player_list):
        rules = Rules(self.config, player_list, debug_mode = self.debug_mode, debug_type = self.debug_type)
        active_player = None

        #If the player is of type "human"
        if self.type == "human":
            #Check if they do not have any playable cards. They do not, they get the pile added to their hand
            if not rules.has_playable_card(self, entire_pile[-1] if entire_pile else None, self.debug_mode, self.debug_type):
                self.print_hand()
                print(entire_pile[-1])
                self.hand = self.hand + entire_pile
                for i in range(len(entire_pile)):
                    new_rect = pygame.Rect((i)*1000/len(self.hand), 0, deck.card_width, deck.card_height)
                    self.hand_rect.append(new_rect)
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
                        print(f"Clicked on card {card}")  # Print which card was clicked on
                        if (len(entire_pile) > 0 and rules.is_card_playable(self.hand[i], center_pile[-1], self.debug_mode, self.debug_type)) or len(entire_pile) == 0:
                            center_pile.append(self.hand[i])
                            entire_pile.append(self.hand[i])
                            if len(center_pile) > 4:
                                center_pile.pop(0)
                            to_remove = i
                            break
                        elif not rules.is_card_playable(self.hand[i], center_pile[-1], self.debug_mode, self.debug_type):
                            print(f"Wrong card try again: {self.hand[i].rank}")
                #If a correct card has been picked, remove it and draw a new card
                if to_remove is not None:
                    self.hand_rect.pop(to_remove)  # Remove the card's Rect from hand
                    self.hand.pop(to_remove)  # Remove the card from hand
                    if len(self.hand) < 3:
                        self.hand.append(deck.draw_card())
                        self.hand_rect.append(pygame.Rect(0, self.config.window_y-200, deck.card_width, deck.card_height))
                    active_player = self.next_turn(player_list)
                    return active_player
                
        #If player is of type "computer"
        elif self.type == "computer":
            if not rules.has_playable_card(self, entire_pile[-1] if entire_pile else None, self.debug_mode, self.debug_type):
                self.print_hand()
                print(entire_pile[-1])
                self.hand = self.hand + entire_pile
                self.hand_rect = self.hand_rect + [pygame.Rect(0,0,deck.card_width, deck.card_height)]*len(entire_pile)
                center_pile.clear()
                entire_pile.clear()
            playable_cards = rules.playable_card_list(self, entire_pile[-1] if entire_pile else None, self.debug_mode, self.debug_type)
            selected_card = random.choice(playable_cards)
            index_of_selected_card = self.hand.index(selected_card)
            center_pile.append(selected_card)
            entire_pile.append(selected_card)
            print(f"Computer played: {selected_card}")
            if len(center_pile) > 4:
                center_pile.pop(0)
            self.hand_rect.pop(index_of_selected_card)  # Remove the card's Rect from hand
            self.hand.pop(index_of_selected_card)  # Remove the card from hand
            if len(self.hand) < 3:
                self.hand.append(deck.draw_card())
                self.hand_rect.append(pygame.Rect(0, self.config.window_y-800, deck.card_width, deck.card_height))
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
    
    def refill_hand(self, deck):
        while len(self.hand) < 3:
            self.hand.append(deck.draw_card())
            self.hand_rect.append(pygame.Rect(0, self.config.window_y-200, deck.card_width, deck.card_height))
