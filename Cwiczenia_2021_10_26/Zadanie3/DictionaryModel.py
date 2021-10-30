import json, os, random

class DictionaryModel:
    def __init__(self, path):
        
        self.dictionary = {}
        self.path = path
        

    def add_flashcard(self, key, value):
        if key in self.dictionary:
            print("Word already exists in dictionary")
        else:
            self.dictionary[key] = value

    def get_random_flashcard(self):
        return random.choice(self.dictionary.keys())

    def load_saved_flashcards(self, file_name):
        with open(self.path + '\\' + file_name, "r") as lang_dict_data:
            self.dictionary = json.load(lang_dict_data)


    def save_flashcards(self, file_name):
        if os.path.isfile(self.path):
            with open(self.path + '\\' + file_name, "a") as lang_dict_data:
                json.dump(self.dictionary, lang_dict_data)
        else:
            with open(self.path + '\\' + file_name, "w") as lang_dict_data:
                json.dump(self.dictionary, lang_dict_data)
