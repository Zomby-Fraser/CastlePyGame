import pygame
import random
from itertools import chain
from deck import Card
from collections import namedtuple

CardWithRect = namedtuple('CardWithRect', ['card', 'rect'])

class Setup:
    def __init__(self, config, player_list):
        self.player_list = player_list
        self.player_y_castle = [350, 650]
        self.player_y_hand = [200, 800]
        self.config = config

    def setup_castle(self, deck):
        for i in range(-3, 0):  # i will be -3, -2, -1
            for player in self.player_list:
                card = deck.draw_card()
                x = 100 + (200 * (i + 3))
                y = self.config.window_y - self.player_y_castle[player]
                rect = pygame.Rect(x, y, deck.card_width, deck.card_height)  # Replace with the appropriate size for your cards
                player.castle[card] = rect

    def deal_init_hand(self, deck):
        for i in range(6):
            for player in self.player_list:
                card = deck.draw_card()
                x = 50 + (100 * i)
                y = self.config.window_y - self.player_y_hand[j]
                rect = pygame.Rect(x, y, deck.card_width, deck.card_height)  # Replace with the appropriate size for your cards
                player.hand[card] = rect

    def computer_place_castle_cards(self):
        for player in self.player_list:
            if player.type != "computer":
                continue
            cards_to_play = random.sample(list(player.hand.keys()), 3)
            for card in cards_to_play:
                player.castle[card] = None ## Need castle rect
                del player.hand[card]

    def find_and_place_starting_card(self, center_pile, entire_pile):
        starting_card = None
        lowest_card = None
        for i, player in enumerate(self.player_list):
            for j, card in enumerate(player.hand):
                if card.rank == "Four":
                    starting_card = card
                    center_pile.append(card)
                    entire_pile.append(card)
                    player.hand.pop(j)
                    

    def OLD_find_and_place_starting_card(self, center_pile, entire_pile):
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
