import json, os, random

class Dictionary:
    def __init__(self, path):
        
        self.language_dictionary = {}
        self.path = path
        

    def add_flashcard(self, key, value):
        if key in self.language_dictionary:
            print("Word already exists in dictionary")
        else:
            self.language_dictionary[key] = value

    def get_random_flashcard(self):
        return random.choice(self.language_dictionary.keys())

    def load_saved_flashcards(self):

        if os.path.isfile(self.path):
            with open(self.path, "r") as lang_dict_data:
                self.language_dictionary = json.load(lang_dict_data)
        else:
            return "There is no saved dictionary file :("

    def save_flashcards(self):
        if os.path.isfile(self.path):
            with open(self.path, "a") as lang_dict_data:
                json.dump(self.language_dictionary, lang_dict_data)