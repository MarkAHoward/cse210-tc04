from game.dealer import Dealer
from colorama import Fore, Style

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
        print(f'You have: {self.points} points')
        print("Hi")
        self.dealer.draw_card()
        while self.alive:
            self.get_choice()
            self.dealer.draw_card()
            self.determine_points()
            self.play_again()
    
    def get_choice(self):
        '''
        Ask user for 'h' or 'l' (self.choice)
        -Allison
        '''
        self.choice = input(Fore.RED + f"Higher or lower? [h/l] " + Style.RESET_ALL)
        print(Fore.GREEN + f'You have selected {self.choice}' + Style.RESET_ALL)

    def determine_points(self):
        '''
        Determine if self.choice < or > to result from dealer
        Assign or subtract points from self.points
        -Allison
        '''
        result = self.dealer.determine()
        print(Fore.BLUE + result + Style.RESET_ALL)
        if result == self.choice:
            self.points = self.points + 100
        if result != self.choice:
            self.points = self.points - 75
        print(f'You have: {self.points} points')

    def play_again(self):
        '''
        determine is self.points > 0 and if below or equal change
        self.alive to False
        -Conner
        '''
        check = self.points
        print(self.points)
        if check > 0:
            answer = input("Do you want to play again (y/n): ")
            i = 1
            while i != 0:
                if answer == "y":
                    self.alive = True
                    i -= 1
                elif answer == "n":
                    self.alive == False
                    print("Good game!")
                    i -=1
                else:
                    answer = input("Pleaser enter a valid input (y/n): ")
        else:
            self.alive == False
            print("Game Over")
