
class Player:
    
    def __init__(self, player_config, player_name, player_id, player_type = 'pc', player_debug_mode_on = False):
        # Passed properties
        self.player_config = player_config
        self.player_name = player_name # 'pc' or 'human'
        self.player_id = player_id
        self.player_type = player_type
        self.player_debug_mode_on = player_debug_mode_on
