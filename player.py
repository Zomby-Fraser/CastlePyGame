class Player:
    
    def __init__(self, player_config, player_name, player_id, player_type = 'pc', player_debug_mode_on = False):
        # Passed properties
        self.player_config = player_config
        self.player_name = player_name # 'pc' or 'human'
        self.player_id = player_id
        self.player_type = player_type
        self.player_debug_mode_on = player_debug_mode_on
        
    def playCard(self, idx = 0):
        self.hand.cards.pop(idx)
        
    def setCastle(self, castle_slots):
        if self.player_type != 'pc':
            for i, cards in enumerate(self.hand.cards):
                print(f"{i+1}: {self.hand.cards[i].rank} of {self.hand.cards[0].suit[1]}")
            castle_top_selection = input("Please enter 3 numbers seperated by spaces: ")
            
            # Put cards on castle
            for i, chosen_card in enumerate(castle_top_selection.split(' ')):
                if i >= castle_slots:
                    break
                if chosen_card:
                    self.castle.cards_up.append(self.hand.cards[int(chosen_card)-1])
                    self.playCard()
                    
        else:
            for i, card in enumerate(self.hand.cards):
                if i >= castle_slots:
                    break
                self.castle.cards_up.append(self.hand.cards[i])
                self.playCard()

    def chooseCardHuman(self):
        for i, cards
    
    def chooseCard(self):
        if self.player_type == 'human':
            chooseCardHuman(self)
        else:
            chooseCardPC(self)





           
