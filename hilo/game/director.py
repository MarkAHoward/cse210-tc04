from game.dealer import Dealer

class Director:
    def __init__(self):
        self.points = 300
        self.alive = True
        self.choice = ''

    def start_game(self):
        '''
        Start the game
        -Conner
        '''

    def get_choice(self):
        '''
        Ask user for 'h' or 'l' (self.choice)
        -Allison
        '''
        self.choice = input(f"Higher or lower? [h/l] ")

    def determine_points(self):
        '''
        Determine if self.choice < or > to result from dealer
        Assign or subtract points from self.points
        -Allison
        '''
        result = dealer.determine()
        if result == self.choice:
            self.points += 100
        else:
            self.point -= 75

    def play_again(self):
        '''
        determine is self.points > 0 and if below or equal change
        self.alive to False
        -Conner
        '''
