import os
from GameModel import GameModel
from DictionaryModel import DictionaryModel
from os.path import dirname
from utils import *

def main():

    path = dirname(os.path.realpath(__file__)) + f'\\dictionaries'
    list_of_files = get_list_of_json_files(path)

    while True:
        dictionary = DictionaryModel(path)
        user_choice = menu_1()
        clear_screen()

        if user_choice == 1:

    
            file_name = user_file_name_input(list_of_files)
            
            clear_screen()

            while user_choice != 4:    

                user_choice = menu_2()
                clear_screen()
                
                if user_choice == 1:
                    
                    fill_dictionary(dictionary.dictionary)
                
                elif user_choice == 2:
                    game = GameModel(dictionary.dictionary)
                    game.choose_option()
                elif user_choice == 3:

                    display_content_of_dictionary(dictionary.dictionary)


                elif user_choice == 4:
                    dictionary.save_flashcards(file_name)

                elif user_choice == 5:
                    dictionary.save_flashcards(file_name)
                    return
        elif user_choice == 2:

            clear_screen()

            show_files(path)
            print_spaces(5)

            choice = choose_file(len(list_of_files))
            
            file_name = list_of_files[choice - 1]
            dictionary.load_saved_flashcards(list_of_files[choice - 1])
            
            clear_screen()

            while user_choice != 4:    

                user_choice = menu_2()
                clear_screen()
                
                if user_choice == 1:
                    
                    fill_dictionary(dictionary.dictionary)
                
                elif user_choice == 2:
                    game = GameModel(dictionary.dictionary)
                    game_choice = 0 
                    while True:
                        game_choice = game.choose_option()

                        if game_choice == 1:
                            game.play()
                        
                        elif game_choice == 2:
                            break
                        elif game_choice == 3:
                            return
                    
                    
                elif user_choice == 3:

                    display_content_of_dictionary(dictionary.dictionary)


                elif user_choice == 4:
                    dictionary.save_flashcards(file_name)

                elif user_choice == 5:
                    dictionary.save_flashcards(file_name)
                    return
            
        elif user_choice == 3:
            return
        



main()

