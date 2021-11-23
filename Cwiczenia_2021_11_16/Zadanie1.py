import os
import os.path

path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test.txt')



def count_in_file(path):
    chars_counter = 0
    word_counter = 0
    white_chars_counter = 0
    output_list = []
    with open(os.path.join(path), 'r', encoding='utf-8') as f:
        for line in f:
            words = line.split()
            word_counter += len(words)
            for char in line:
                if not char.isspace():
                    chars_counter += 1
                else:
                    white_chars_counter += 1

        

    return [chars_counter, word_counter, white_chars_counter]

print(count_in_file(path))