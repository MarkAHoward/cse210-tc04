from game.dealer import Dealer

class Director:
    def __init__(self):
        self.points = 300
        self.alive = True
        self.choice = ''
        self.dealer = Dealer()

    def start_game(self):
        '''
        Start the game
        -Conner
        '''
        while self.alive:
            self.dealer.draw_card()
            self.get_choice()
            self.dealer.determine()
            self.determine_points()
            self.play_again
    
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
        result = self.dealer.determine()
        if result == self.choice:
            self.points += 100
        else:
            self.points -= 75

    def play_again(self):
        '''
        determine is self.points > 0 and if below or equal change
        self.alive to False
        -Conner
        '''
        if self.points > 0:
            answer = input("Do you want to play again (y/n): ")
            i = 1
            while i != 0:
                if answer == "y":
                    self.alive = True
                    i -= 1
                elif answer == "n":
                    self.alive == False
                    i -=1
                else:
                    print("Pleaser enter a valid input (y/n)")
        else:
            self.alive = False 
