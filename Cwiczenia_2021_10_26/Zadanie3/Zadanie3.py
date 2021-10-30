import os
import json
from DictionaryModel import DictionaryModel
from os.path import isfile, join, dirname


def get_list_of_json_files(path):
    
    json_files = [file for file in os.listdir(path) if isfile(join(path, file)) and file.split('.')[-1] == 'json']
    return json_files


def display_list_of_json_files(list):
    i = 1
    for item in list:
        print(f'{i}. {item}')
        i += 1


def display_menu_1():
    print("""
        1. Create new dictionary
        2. Load existing dictionary
        3. Exit
    """)


def display_menu_2():
    print("""
        1. Add new Flashcard
        2. Try yourself
        3. Display all flashcards
        4. Go back
        5. Exit
    """)


def menu_1():
    display_menu_1()
    is_user_input_valid = False
    while not is_user_input_valid:
        try:
            user_choice = int(input("Input your choice: "))
            is_user_input_valid = True if user_choice in [1, 2, 3] else False
        except ValueError:
            clear_screen()
            print("This must be an integer from 1 to 3!!!!")
            display_menu_1()
        
    return user_choice


def menu_2():
    display_menu_2()
    is_user_input_valid = False
    while not is_user_input_valid:
        try:
            user_choice = int(input("Input your choice: "))
            is_user_input_valid = True if user_choice in [1, 2, 3, 4, 5] else False
        except ValueError:
            clear_screen()
            print("This must be an integer from 1 to 3!!!!")

    return user_choice


def play():
    ...


def fill_dictionary(dictionary):
    clear_screen()
    
    key = input("Input key word: ")
    value = input("Input definition: ")

    if key in dictionary:
        print("This key word already exist in dictionary :)")
    else:
        dictionary[key] = value


def display_content_of_dictionary(dictionary):
    i = 1
    for k, v in dictionary.items():
        print(f'{i}. {k}: {v}')
        i += 1
    
    print()
    input("press enter to continue......")
    clear_screen()

def user_file_name_input(list_of_files):

    file_name = input("Input name of the new dictionary: ") + '.json'

    if file_name in list_of_files:
        while file_name in list_of_files:
            print(f'Dictionary {file_name[:-5]} already exists.')
            file_name = input("Input name of the new dictionary: ") + '.json'

    return file_name


def show_files(path):
        list_of_files = get_list_of_json_files(path)
        iterator = 1

        for file in list_of_files:
            print(f'{iterator}. {file}')
            iterator += 1


def clear_screen():
    os.system('cls')

def print_spaces(num_of_spaces):
    for i in range(num_of_spaces):
        print()


def choose_file(len_of_list_of_files):
    try:
        choice = int(input("Choose file to load: "))
    except ValueError:
        choice = 0
        while choice == 0:
            try:
                clear_screen()
                choice = int(input("Choose file to load: "))
                if not 0 < choice > len_of_list_of_files:
                    choice == 0
                    print(f'this must be the number from 1 to {len_of_list_of_files}')
            except ValueError:
                print(f'this must be the number from 1 to {len_of_list_of_files}')
        
    return choice


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

                    play()
                
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

                    play()
                
                elif user_choice == 3:

                    display_content_of_dictionary(dictionary.dictionary)


                elif user_choice == 4:
                    dictionary.save_flashcards(file_name)

                elif user_choice == 5:
                    dictionary.save_flashcards(file_name)
                    return
            

            return


            
            

        elif user_choice == 3:
            return
        



main()

