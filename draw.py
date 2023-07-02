import pygame 

class Draw:
    def __init__(self, window, window_x, window_y, player_list, card_images, font):
        self.window = window
        self.window_x = window_x
        self.window_y = window_y
        self.player_list = player_list
        self.card_images = card_images
        self.font = font
    # Create a function to render text
    def draw_text(self, text, surface, x, y):
        text_obj = self.font.render(text, 1, pygame.Color('White'))  # Creates a surface with the text
        text_rect = text_obj.get_rect(center=(x, y))  # Gets a rect object with the dimensions of the surface
        surface.blit(text_obj, text_rect)  # Draws the surface onto another surface

    def draw_cards(self, center_pile, entire_pile, deck):
        for player in self.player_list:
            for i, card in enumerate(player.hand):
                card_rect = player.hand_rect[i]
                card_rect[0] = (i)*self.window_x/len(player.hand)
                self.window.blit(self.card_images[(card.rank,card.suit)], (card_rect[0], card_rect[1]))
            for i, card in enumerate(player.castle):
                card_rect = player.castle_rect[i]
                if i < 3:
                    self.window.blit(self.card_images["Back"], (card_rect[0], card_rect[1]))
                else:
                    self.window.blit(self.card_images[(card.rank,card.suit)], (card_rect[0], card_rect[1]))
        for i, card in enumerate(center_pile):
            self.window.blit(self.card_images[(card.rank,card.suit)], (self.window_x/2-deck.card_width-50+(100*i), self.window_y/2-deck.card_height+50))
        if len(entire_pile) > 4:
            self.window.blit(self.card_images[entire_pile[-5].rank, entire_pile[-5].suit], (self.window_x/2-deck.card_width-300, self.window_y/2-deck.card_height+50))