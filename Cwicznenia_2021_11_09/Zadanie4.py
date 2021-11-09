def cesar_encryption(word, distance):
    output = ''
    for char in word:
        if 97 <= ord(char) + distance <= 122:
            output += chr(ord(char) + distance)
        elif ord(char) + distance > 122:
            output += chr(ord(char) + distance - 26)
        elif ord(char) + distance < 97:
            output += chr(ord(char) + distance + 26)
    return output

def main():
    password = input("Podaj hasło do zaszyfrowania: ")
    
    try:
        distance = int(input("Podaj przesunięcie"))
    except ValueError:
        print("To musi być int")

    print(cesar_encryption(password, distance))
main()
#97 122