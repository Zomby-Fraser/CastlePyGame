import pygame
import random

# Pygame setup
pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Card Game")

# Card class
class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return f'{self.rank} of {self.suit} with value {self.value}'

# Deck class
class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def print_deck(self):
        for card in self.cards:
            print(card)

    def build(self):
        suits = ["Clubs", "Diamonds", "Spades", "Hearts"]
        ranks = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", 
                 "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
        values = [14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

        for suit in suits:
            for rank, value in zip(ranks, values):
                self.cards.append(Card(suit, rank, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()
    
    def load_card_images(self, filename):
        card_images = {}
        ranks = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", 
                "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Joker"]
        suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
        
        # Load the sprite sheet
        sprite_sheet = pygame.image.load(filename).convert_alpha()

        # Assume each card image is 73 pixels wide and 98 pixels high
        # You'll need to change these numbers if your sprite sheet has different dimensions
        self.card_width = 100
        self.card_height = 144

        for suit in suits:
            for rank in ranks:
                if ((rank == "Joker")):
                    continue
                # Calculate the position of the card image on the sprite sheet
                x = ranks.index(rank) * self.card_width
                y = suits.index(suit) * self.card_height

                # Extract the card image
                image = sprite_sheet.subsurface(pygame.Rect(x, y, self.card_width, self.card_height))

                # Add the card image to the dictionary
                card_images[(rank, suit)] = image
        # Assume the back image is the last image in the sprite sheet
        back_x = len(ranks) * self.card_width
        back_y = 0  # adjust this if the back image is not in the first row
        back_image = sprite_sheet.subsurface(pygame.Rect(back_x, back_y, self.card_width, self.card_height))

        # Add the back image to the dictionary
        card_images["Back"] = back_image
        
        return card_images

