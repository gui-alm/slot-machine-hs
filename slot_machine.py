# Guilherme Almeida Patrão

import random

class slot_machine:
    credit = 0
    playable = True # turns False when the player doesn't want to play anymore

    def __init__(self, credit):
        self.credit = credit
                
    def check_credit(self):
        return self.credit

    def add_credit(self, amount):
        self.credit += amount
    
    def remove_credit(self, amount):
        self.credit -= amount
    
    def is_playable(self):
        return self.playable

    def choose_symbols(self):
        symbols = ["A", "B", "C", "D", "E", "F", "G"]
        return random.choices(symbols, weights=(50, 40, 30, 20, 10, 5, 1), k=3)

    def calculate_credit_won(self, bet, symbol):
        # using a dictionary cause there's no switch case in python :(
        switcher = {"A" : 5,
                    "B" : 10,
                    "C" : 20,
                    "D" : 70,
                    "E" : 200,
                    "F" : 1000,
                    "G" : 100000}

        return switcher.get(symbol) * bet

    def print_result(self, result):
        slots = "-------------------------------------------------\n------|     {}     |     {}     |     {}     |------\n-------------------------------------------------"
        print(slots.format(result[0], result[1], result[2]))

    def play(self):
        bet = input("How much would you like to bet? ")
        while int(bet) > self.check_credit():
            print("You don't have enough credit. Current credit: " + str(self.check_credit()))
            bet = input("How much would you like to bet? ")

        self.remove_credit(int(bet))
        result = self.choose_symbols()
        self.print_result(result)

        if(len(set(result)) == 1):
            won = self.calculate_credit_won(int(bet), result[0])
            self.add_credit(won)
            print("Congrats! " + str(won) + " has been added to your credit amount!")
        
        if(self.check_credit() == 0):
            print("You have run out of credit. Stopping the game.")
            return

        play = input("Would you like to keep playing? [yes/no] ")
        if(play == "yes"):
            self.playable = True
        elif(play == "no"):
            print("Stopping the game.")
            self.playable = False
        else:
            print("I don't know what you mean so I'm stopping the game.")
            self.playable = False


def run():
    print("Welcome to the slot machine game! Good luck.")
    n_credit = input("How much credit would you like to deposite? ")
    machine = slot_machine(int(n_credit))

    while(machine.check_credit() > 0 and machine.is_playable()):
        machine.play()

run()