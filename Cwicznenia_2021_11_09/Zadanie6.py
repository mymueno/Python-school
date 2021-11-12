def is_annagram(str1, str2):

    str1 = str1.lower()
    str2 = str2.lower()
    output = True
    str1 = ''.join(filter(str.isalpha, str1)).lower()
    str2 = ''.join(filter(str.isalpha, str2)).lower()
    
    if len(str1) == len(str2):
        for char in str1:
            if char not in str2:
                return False
        
        return True
    else:
        return False



        


def main():
    word_1 = input("Input 1st word: ")
    word_2 = input("Input 2nd word: ")

    print(is_annagram(word_1, word_2))


main()