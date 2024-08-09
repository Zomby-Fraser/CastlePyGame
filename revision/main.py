from player import Player
from player_config import PlayerConfig
from deck import Deck
from castle import Castle
from game_config import GameConfig
from hand import Hand
from pile i

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

# Initialize Pile
pile = Pile()

# Initialize and deal castles & hands
for player in player_list:
    new_castle = Castle(player.player_id)
    new_hand = Hand(player.player_id)
    for i in range(game_rules.face_down_castle_cnt):
        new_castle.cards_down.append(deck.cards[-1])
        deck.drawCard()
    for i in range(game_rules.starting_hand_size):
        new_hand.cards.append(deck.cards[-1])
        deck.drawCard()
    player.castle = new_castle
    player.hand = new_hand

for player in player_list:
    player.setCastle(game_rules.castle_slots)
        
while True:
    
    # Check for player with smallest card. 
    for player in player_list:
        pass
        
        
        
        
        
