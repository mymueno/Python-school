def count_last(word):
    return word.count(word[-1])

def count_last_but_other_way(word):
    last_char = word[-1]
    counter = 0
    for char in word:
        if char == last_char:
            counter += 1
    return counter

def main():
    word = input("Podaj słowo: ")
    print(count_last(word))
    print(count_last_but_other_way(word))


main()    