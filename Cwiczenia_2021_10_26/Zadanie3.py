import random


def add_word(key_word, definition, dict):
    if key_word in dict:
        print("Given word already exisits in dictionary")
    else:
        dict[key_word] = definition

def get_random_word(dict):
    return random.choice(list(dict.keys()))

def exercise_3():
    dict = {}
    punkty = 0

    while True:
        
        print("""
        1. Add new word 
        2. Play
        3. Quit    
        """)
        choice = input("")
        if choice == '1':
            key_word = input("Input the new word: ")
            definition = input("Input translation: ")
            add_word(key_word, definition, dict)
        if choice == '2':
            random_key = get_random_word(dict)
            
            while True:
                user_translation = input(f'Input translation of a word(type 1 to stop approach): {random_key}: ')
                if user_translation == dict[random_key]:
                    punkty += 1
                    print("Correct!")
                else:
                    print("Incorrect!")
        if choice == '3':
            return
exercise_3()