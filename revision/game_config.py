class GameConfig:
    
    def __init__(self, face_down_castle_cnt = 3, hand_size = 3):
        self.face_down_castle_cnt = face_down_castle_cnt
        self.hand_size = hand_size
        self.starting_hand_size = face_down_castle_cnt + hand_size
        
