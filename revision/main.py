from player import Player
from player_config import PlayerConfig
from deck import Deck
from castle import Castle
from game_config import GameConfig
from hand import Hand

# Initialize game settings
game_rules = GameConfig()

# Initialize players
player_list = [
        {'name': 'player 1', 'player_type': 'human'},
        {'name': 'player 2', 'player_type': 'pc'}
    ]
for player_id, player in enumerate(player_list):
    new_player_info = player_list[player_id]
    new_player_obj = Player(PlayerConfig(), new_player_info['name'], player_id, new_player_info['player_type'])
    player_list[player_id] = new_player_obj

# Initialize Deck
deck = Deck()
deck.shuffle()

# Initialize and deal castles & hands
castles = {}
hands = {}
for player in player_list:
    new_castle = Castle(player.player_id)
    new_hand = Hand(player.player_id)
    for i in range(game_rules.face_down_castle_cnt):
        new_castle.cards_down.append(deck.cards[-1])
        deck.draw_card()
    for i in range(game_rules.starting_hand_size):
        new_hand.cards.append(deck.cards[-1])
        deck.draw_card()
    castles[player] = new_castle
    hands[player] = new_hand

# Player 1 select their top castle cards
print(f"Pick {game_rules.castle_slots} to put on your castle. Your choices:")
player_1_cards_start = hands[player_list[0]].cards
for i, cards in enumerate(hands[player_list[0]].cards):
    print(f"{i+1}: {player_1_cards_start[i].rank} of {player_1_cards_start[0].suit[1]}")
castle_top_selection = input("Please enter 3 numbers seperated by spaces: ")

# Put cards on castle
for chosen_card in castle_top_selection.split(' '):
    if chosen_card:
        player_castle = castles[player_list[0]]
        player_hand = hands[player_list[0]]
        player_castle.cards_up.append(player_hand.cards[int(chosen_card)-1])
        

    
    
    
    
    
    
