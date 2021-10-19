#Zadanie1
from random import randint
print ("""


        ZADANIE 1


""")
def Zadanie1():
    l = [randint(-10,10) for x in range(10)]
    print(l)
    # min max
    print(f'{max(l)} - max value, {min(l)} - min value')
    # samemu
    l2 = sorted(l)
    print(f'{l2[-1]} - max value, {l2[0]} - min value')
    avg = sum(l)/len(l)
    print(f'avg of list = {avg}')
    l_temp = [avg]
    l_temp = l_temp + l2
    l_temp.sort()
    pointer = l_temp.index(avg)
    print(f'num of elements lower than avg: {len(l_temp[:pointer])}, num of elements lower than avg: {len(l_temp[pointer+1:])}')
    print(f'reversed list: {l[::-1]}')
Zadanie1()

print ("""


        ZADANIE 2


""")
def zadanie2():
    l = [randint(1,10) for x in range(20)]
    t = set(l)
    print(l)
    for elem in t:
        print(f'{elem} - {l.count(elem)}')

zadanie2()

print ("""


        ZADANIE 3


""")

def Zadanie3():
    scope = 5
    maxes =[]
    mins = []
    l = [[randint(-scope,scope) for x in range(scope)] for x in range(scope)]
    for i in range(len(l)):
        max_of_cols = l[i][0]
        min_of_cols = l[i][0]
        for j in range(len(l[0])):
           max_of_cols = l[j][i] if l[j][i] > max_of_cols else max_of_cols
           min_of_cols = l[j][i] if l[j][i] < min_of_cols else min_of_cols
        maxes.append(max_of_cols)
        mins.append(min_of_cols)
    
    print(maxes)
    print(mins)
    print(l)
Zadanie3()

print ("""


        ZADANIE 4


""")
import math


def Zadanie4():
    a = int(input("Podaj lewy koniec zakresu: "))
    b = int(input("Podaj prawy koniec zakresu: "))

    l = [(x, 2**x, math.sqrt(x)) for x in range(a, b+1) if x % 2 == 1]
    print(l)

#Zadanie4()

print ("""


        ZADANIE 5


""")
def Zadanie5():
    scope = int(input("Podaj zakres tablicy: "))
    a = int(input("Podaj lewy koniec zakresu: "))
    b = int(input("Podaj prawy koniec zakresu: "))

    l = [[randint(a,b) for x in range(scope)] for x in range(scope)]
    print(l)
    sum = 0
    sum_of_odd_lists = 0
    for i in range(len(l)):
        for j in range(len(l[0])):
            sum += l[i][j] if i == j else 0
            sum_of_odd_lists += l[i][j] if i % 2 == 1 and j % 2 == 1 else 0
    print(sum)
    print(sum_of_odd_lists)
Zadanie5()