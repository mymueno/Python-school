def count_digits(sentence):
    sum = 0
    for c in sentence:
        if c.isdigit():
           sum += int(c)
    return sum

def main():
    sentence = input("Podaj ciąg znaków: ")
    print(count_digits(sentence))

main()