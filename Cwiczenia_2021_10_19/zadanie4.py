import math


def exercise_4():
    valid_input = False

    while not valid_input:
        try:
            a = int(input("Input 1st number: "))
            b = int(input("Input 2nd number: "))
            valid_input = True if a > 0 and b > 0 else False
            if not valid_input:
                print("Both numbers must be positive integers!!!")
        except ValueError:
            print("Both numbers must be positive integers!!!")
    # if user inputs higher number 1st, swap them 
    if a > b:
        temp = a
        a = b
        b = temp

    #generating list for tuples that contains odd numbers of scope from a to b, two to this odd numbers power, and their square root 
    l = [(x, 2**x, math.sqrt(x)) for x in range(a, b+1) if x % 2 == 1]
    print(*l)

exercise_4()