def is_palindrome(word):
    return True if word[::-1] == word else False

def main():
    word = input("Podaj słowo: ")
    
    print("Podane słowo", "nie" if not is_palindrome(word) else '', "jest palindromem")
    
main()
