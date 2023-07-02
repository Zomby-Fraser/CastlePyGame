import pygame
import random
from deck import Card, Deck
from player import Player


# Initialize the Pygame font module
pygame.font.init()

# Create a font object
font = pygame.font.Font(None, 36)  # Choose the font size

# Create a function to render text
def draw_text(text, surface, x, y):
    text_obj = font.render(text, 1, pygame.Color('White'))  # Creates a surface with the text
    text_rect = text_obj.get_rect(center=(x, y))  # Gets a rect object with the dimensions of the surface
    surface.blit(text_obj, text_rect)  # Draws the surface onto another surface

def draw_cards():
    for i, card in enumerate(player.hand):
        card_rect = player.hand_rect[i]
        window.blit(card_images[(card.rank,card.suit)], (card_rect[0], card_rect[1]))
    for i, card in enumerate(player.castle):
        card_rect = player.castle_rect[i]
        if i < 3:
            window.blit(card_images[("Back",card.suit)], (card_rect[0], card_rect[1]))
        else:
            window.blit(card_images[(card.rank,card.suit)], (card_rect[0], card_rect[1]))
    for i, card in enumerate(computer.hand):
        card_rect = computer.hand_rect[i]
        window.blit(card_images[("Back",card.suit)], (card_rect[0], card_rect[1]))
    for i, card in enumerate(computer.castle):
        card_rect = computer.castle_rect[i]
        if i < 3:
            window.blit(card_images[("Back",card.suit)], (card_rect[0], card_rect[1]))
        else:
            window.blit(card_images[(card.rank,card.suit)], (card_rect[0], card_rect[1]))

def is_card_playable(selected_card, top_pile_card):
    if selected_card.rank in ["Two", "Three", "Seven", "Ten"]:
        return True
    elif top_pile_card.rank == "Seven" and top_pile_card.value > selected_card.value:
        return True
    elif selected_card.value > top_pile_card.value:
        return True
    else:
        return False

pygame.init()
window_x = 800  
window_y = 800
window = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption("Card Game")

# Game loop
running = True
deck = Deck()
deck.shuffle()
card_images = deck.load_card_images('CuteCards.png')
player = Player()
computer = Player()
while running:
    # Event handling
    # During the event handling phase:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for i, (card_rect, card) in enumerate(zip(player.hand_rect, player.hand)):
                if card_rect.collidepoint(mouse_x, mouse_y):
                    player.castle_rect.append(player.castle_rect[len(player.castle_rect)-3])
                    player.castle.append(card)
                    player.hand_rect.pop(i)  # Remove the card's Rect from hand
                    player.hand.pop(i)  # Remove the card from hand
                    break
    ####Setup the game

    #Create both player's initial Castle and their locations on-screen.
    if not player.castle and not computer.castle:
        for i in range(-3, 0):  # i will be -3, -2, -1
            player.castle.append(deck.draw_card())
            player.castle_rect.append((100 + (200 * (i + 3)), window_y-350))
            computer.castle.append(deck.draw_card())
            computer.castle_rect.append((100 + (200 * (i + 3)), window_y-650))

    #Create bother player's hands and their locations on screen
    if not player.hand and not computer.hand:
        for i in range(6):
            player.hand.append(deck.draw_card())
            computer.hand.append(deck.draw_card())
            player_card_pos = (50 + (100 * i), window_y-200)
            computer_card_pos = (50 + (100 * (i)), window_y-800)
            player.hand_rect.append(pygame.Rect(*player_card_pos, deck.card_width, deck.card_height))  # Create a Rect for this card
            computer.hand_rect.append(pygame.Rect(*computer_card_pos, deck.card_width, deck.card_height))  # Create a Rect for the computer's card

    #Have the computer player randomly select which cards to put on the castle.
    if len(computer.castle) == 3:
        random_numbers = sorted(random.sample(range(0, 6), 3), reverse=True)
        for card_num in random_numbers:
            computer.castle_rect.append(computer.castle_rect[len(computer.castle_rect)-3])
            computer.castle.append(computer.hand[card_num])
            computer.hand_rect.pop(card_num)  # Remove the card's Rect from hand
            computer.hand.pop(card_num)

    window.fill((0, 0, 0))  # Clear the screen
    draw_cards()  # Draw all cards
    pygame.display.flip()  # Update the display

    pygame.display.flip()  # Update the display


pygame.quit()