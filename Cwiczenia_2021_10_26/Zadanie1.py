def exercise_1():
    word = "abacacvs"
    print(count_characters(word))

def count_characters(word):
    charaters_dict = {}
    for c in word:
        if c in charaters_dict:
            charaters_dict[c] += 1
        else:
            charaters_dict[c] = 1
    return charaters_dict
exercise_1()