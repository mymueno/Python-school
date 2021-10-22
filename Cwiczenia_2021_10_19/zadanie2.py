from random import randint

def exercise_2():

    #generating list with 20 random integers from 1 to 10
    l = [randint(1,10) for x in range(20)]
    
    #declaring set of l, which automatically removes duplicates which allows me to count them later 
    t = set(l)
    
    print(l)

    #counting elements from list and assigning them to set elements
    for elem in t:
        print(f'{elem} - {l.count(elem)}')

exercise_2()