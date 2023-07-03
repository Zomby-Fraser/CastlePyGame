import pygame
import random
from itertools import chain
from deck import Card

class Setup:
    def __init__(self, config, player_list):
        self.player_list = player_list
        self.player_y_castle = [350, 650]
        self.player_y_hand = [200, 800]
        self.config = config

    def setup_castle(self, deck):
        for i in range(-3, 0):  # i will be -3, -2, -1
            for j in range(len(self.player_list)):
                self.player_list[j].castle.append(deck.draw_card())
                self.player_list[j].castle_rect.append((100 + (200 * (i + 3)), self.config.window_y-self.player_y_castle[j]))

    def deal_init_hand(self, deck):
        for i in range(6):
            for j in range(len(self.player_list)):
                self.player_list[j].hand.append(deck.draw_card())
                card_pos = (50 + (100 * i), self.config.window_y-self.player_y_hand[j])
                self.player_list[j].hand_rect.append(pygame.Rect(*card_pos, deck.card_width, deck.card_height))

    def computer_place_castle_cards(self):
        random_numbers = sorted(random.sample(range(0, 6), 3), reverse=True)
        for card_num in random_numbers:
            for j in range(len(self.player_list)):
                if self.player_list[j].type != "computer":
                    continue
            self.player_list[j].castle_rect.append(self.player_list[j].castle_rect[len(self.player_list[j].castle_rect)-3])
            self.player_list[j].castle.append(self.player_list[j].hand[card_num])
            self.player_list[j].hand_rect.pop(card_num)  # Remove the card's Rect from hand
            self.player_list[j].hand.pop(card_num)

    def find_and_place_starting_card(self, center_pile, entire_pile):
        starting_card = Card("Spade", "Joker", 1000)
        first_card_selected = False
        all_starting_cards = list(chain.from_iterable(player.hand for player in self.player_list))
        for card in all_starting_cards:
            if starting_card.rank != "Four" and (card.rank == "Four" or card.value < starting_card.value):
                starting_card = card
        for i, player in enumerate(self.player_list):
            for j, card in enumerate(player.hand):
                if card == starting_card and not first_card_selected:
                    center_pile.append(card)
                    entire_pile.append(card)
                    player.hand.pop(j)
                    player.hand_rect.pop(j)
                    first_card_selected = True
                    # Now the next player in the list becomes active.
                    # Using modulo operator to handle the case when it's the last player's turn.
                    active_player = self.player_list[(i+1)%len(self.player_list)] 
                    break
            # Break the outer loop if a card has been selected
            if first_card_selected:
                break
        return active_player
