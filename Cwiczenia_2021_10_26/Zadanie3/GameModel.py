from os import system
import random
import copy
import numpy as np

class GameModel():
    def __init__(self, dictionary) -> None:
        self.points = 0
        self.dictionary = dictionary


    @staticmethod
    def show_menu():
        print("""
        
            1. Play
            2. Go back
            3. Exit
        
        """)
    


    def choose_option(self):  
        GameModel.show_menu()
        try:
            choice = int(input("Choose option: "))
        except ValueError:
            choice = 0
        while choice == 0:
            try:
                system('cls')
                print("this must be the number from 1 to 3")
                choice = int(input("Choose option: "))
                if not 0 < choice > 3:
                    choice = 0
                    system('cls')
                    print(f'this must be the number from 1 to 3')
                    GameModel.show_menu()
            except ValueError:
                system('cls')
                print(f'this must be the number from 1 to 3')
                GameModel.show_menu()
        
        system('cls')

        return choice
    
    @staticmethod
    def levenshtein_ratio_and_distance(s, t, ratio_calc = True):


        rows = len(s)+1
        cols = len(t)+1
        distance = np.zeros((rows,cols),dtype = int)

  
        for i in range(1, rows):
            for k in range(1,cols):
                distance[i][0] = i
                distance[0][k] = k

  
        for col in range(1, cols):
            for row in range(1, rows):
                if s[row-1] == t[col-1]:
                    cost = 0 
                else:
                
                    if ratio_calc == True:
                        cost = 2
                    else:
                        cost = 1
                distance[row][col] = min(distance[row-1][col] + 1,      # Cost of deletions
                                    distance[row][col-1] + 1,          # Cost of insertions
                                    distance[row-1][col-1] + cost)     # Cost of substitutions
        if ratio_calc == True:
           
            Ratio = ((len(s)+len(t)) - distance[row][col]) / (len(s)+len(t))
            return Ratio
        else:

            return "The strings are {} edits away".format(distance[row][col])


        

    def play(self):
        playing_dictionary = copy.deepcopy(self.dictionary)
        score = 0
        for i in range(10):
            if len(playing_dictionary) > 0:
                key, value = random.choice(list(playing_dictionary.items()))
            else:
                return
            del playing_dictionary[key]
            print(f'{value}: ', end='')
            user_input = input()
            if(user_input == value):
                score += 1
            else:
                print(f'Błąd wynosi: {GameModel.levenshtein_ratio_and_distance(value, user_input)}')
        print(f"Twój wynik to: {score}")
            