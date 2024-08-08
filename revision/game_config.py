class GameConfig:
    
    def __init__(self, castle_slots = 3, face_down_castle_cnt = 3, hand_size = 3):
        self.castle_slots = castle_slots # Need error handling for when face_down_castle_cnt % castle_slots != 0
        self.face_down_castle_cnt = face_down_castle_cnt
        self.hand_size = hand_size
        self.starting_hand_size = face_down_castle_cnt + hand_size
        
