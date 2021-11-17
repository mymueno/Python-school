# wyświetlenie sumy wszystkich liczb zapisanych we wszystkich plikach z ka-
# talogu, w którym się znajduje,
import os
import os.path


path = os.path.dirname(os.path.realpath(__file__))

def sum_of_nums_in_files():
    sum_of_all_nums = 0
    sum_of_nums_in_file = 0
    sum_in_line = 0
    num = ''
    is_number = False
    for file in os.listdir(path):
        with open(os.path.join(path, file), 'r', encoding='utf-8') as f:
            for line in f:
                for char in line:
                    if char.isdigit():
                        is_number = True
                        num += char
                    else:
                        num = int(num) if is_number is True else ''
                        is_number = False
                        sum_in_line += num if num != '' else 0
                        num = ''
                if is_number:
                    num = int(num)
                    is_number = False
                    sum_in_line += num
                num = ''
            sum_of_nums_in_file += sum_in_line
            sum_in_line = 0
        sum_of_all_nums += sum_of_nums_in_file
    return sum_of_nums_in_file


print(sum_of_nums_in_files())

# wyświetlenie nazw plików, w których znajduje się podana (jako parametr)
# fraza, wraz z liczbą wystąpień tej frazy,

def files_that_contain_phrase(phrase):
    for file in os.listdir(path):
        with open(os.path.join(path, file), 'r', encoding='utf-8') as f:
            phrase_counter_in_file = 0
            for line in f:
                phrase_counter_in_file += line.count(phrase)
            if not phrase_counter_in_file == 0:
                print(f'{file} - {phrase_counter_in_file}')

files_that_contain_phrase("siema")

# zamianę podanego znaku lub ciągu znaków na inny we wszystkich plikach z
# katalogu,
def change_given_string_in_files(old_phrase, new_phrase):
    for file in os.listdir(path):
        if file != __file__.split('\\')[-1]:
            with open(os.path.join(path, file), 'r', encoding='utf-8') as f:
                lines = []
                for line in f:
                   lines.append(line) 

            print(lines)
            with open(os.path.join(path, file), 'w+', encoding='utf-8') as f:
                for line in lines:
                    if old_phrase in line:
                        print(line)
                        line = line.replace(old_phrase, new_phrase)
                        print(line)
                        f.write(line)
                    else:
                        f.write(line)
                        

change_given_string_in_files("siema", "naura")



# wyświetlenie stosunku sumy liczb całkowitych do rzeczywistych (z wszystkich
# plików w katalogu),

def proportion_of_integers_and_real_numbers():
    for file in os.listdir(path):



# wyświetlenie plików ze względu na liczbę znaków (w kolejności rosnącej pod
# względem liczby znaków),

# połączenie wszystkich plików w jeden z pominięciem powtarzających się linii,

# porównania (diff) wybranych plików

#siema