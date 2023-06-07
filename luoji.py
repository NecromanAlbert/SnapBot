class CardGame:
    def __init__(self, gameInfo, card_data_file='card_data.txt'):
        # Extracting information from the game_info dictionary
        self.card_info = gameInfo['cardInfo']
        self.location_info = gameInfo['locationInfo']
        self.energy = gameInfo['energy']
        self.turn = gameInfo['turn']
        
        # Create a fixed deck
        self.deck = ["Kitty", "Iceman", "Yondu", "Scorpion", "Ironheart", 
                     "Wolfsbane", "Maximus", "Wong", "Whitetiger", 
                     "Spiderwoman", "Odin", "Chavez"]
        self.card_data = self.read_card_data(card_data_file)
        self.card_tracking = [[card, self.card_data[card], False, False] for card in self.deck]
        # param 0 name, param 1 [cost, power], param 2 in hand, param 3 playable.

    # Method for the game logic
    def game_logic(self):
        dynamic_hand, current_energy = update(self)
        for card in dynamic_hand:
            if card[1][0] <= current energy:
                #adjus my hyperparameter
            if (0=0)#这里写卡权重的调整 如果当回合可以打多张卡
                #play(card[0])
                #print(card[0])
                    
    def update(self):
        current_energy = self.energy
        current_turn = self.turn
    	for card in self.card_info:
            if card.getkey
    return dynamic_hand, current_energy

    def play(name):
        

    def read_card_data(self, card_data_file):
        # Read card data from a text file
        card_data = {}
        with open(card_data_file, 'r') as f:
            for line in f:
                card, data = line.strip().split(':')
                cost, power = map(int, data.split(','))
                card_data[card] = [cost, power]
        return card_data
    
    # Getter methods to retrieve the information
    def get_card_info(self):
        return self.card_info

    def get_location_info(self):
        return self.location_info

    def get_energy(self):
        return self.energy

    def get_turn(self):
        return self.turn

    def set_card_info(self, card_info):
        self.card_info = card_info

    def set_location_info(self, location_info):
        self.location_info = location_info

    def set_energy(self, energy):
        self.energy = energy

    def set_turn(self, turn):
        self.turn = turn

game_info = {
    'cardInfo': [
        {"Kitty": [100, 100]},
        {"Iceman":[200, 100]},
        {"Yondu": [300, 100]},
        {"Wong":[400, 100]},
        {"Odin": [500, 100]}
    ],
    'locationInfo': [[1000, 1000], [2000, 1000], [3000, 1000]],
    'energy': 1,
    'turn': 1
}

c = CardGame(game_info)
for card in c.card_tracking:
    #print(card)
    pass
c.game_logic()
    