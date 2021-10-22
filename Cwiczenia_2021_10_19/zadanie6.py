from math import gcd

def Zadanie6():
    valid_input = False

    while not valid_input:
        try:
            size = int(input("Input size of the matrix: "))
            valid_input = True if size > 0 else False
        except ValueError:
            print("Size of the matrix must be positive integer!!!")


   


    l_output = []
    for i in range(1, size + 1):
        for j in range(size + 1):
            l_output.append('+' if gcd(i, j) == 1 else '.')
    
    pointer = 0
    print (" ",*[i for i in range (1, size+1)])
    for i in range(0, len(l_output)):
        if(i % size == 0 and i != 0):
            print(i//size, *l_output[pointer:i])
            pointer = i

    
Zadanie6()