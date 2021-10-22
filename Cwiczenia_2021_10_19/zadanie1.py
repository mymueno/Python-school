from random import randint


def find_max(l):
    max_item = l[0]

    for item in l:
        max_item = item if item > max_item else max_item

    return max_item 

def find_min(l):
    min_item = l[0]

    for item in l:
        min_item = item if item < min_item else min_item

    return min_item


def count_higher_than_average(l, avg):
    output = 0

    for item in l:
        if item > avg:
            output += 1

    return output

def count_lower_than_average(l, avg):
    output = 0

    for item in l:
        if item < avg:
            output += 1

    return output

def exercise_1():

    #Creating list of random integers from 1 to 10
    l = [randint(-10,10) for x in range(10)]

    print("Generated list of random integers: ", *l)

    # finding minimum and maximum value of the list by using min and max functions
    print(f'{max(l)} - max value, {min(l)} - min value')

    # finding minimum and maximum value of the list by individual approach
    print(f'{find_max(l)} - max value, {find_min(l)} - min value')

    #arithmetic average of the list elements
    avg_of_list = sum(l)/len(l)               
    print(f'avg of list = {avg_of_list}')

    #counting elements higher and lower than average

    print(f'higher than avg: {count_higher_than_average(l, avg_of_list)}')
    print(f'lower than avg: {count_lower_than_average(l, avg_of_list)}')

    #printing reversed list (just printing, not reversing orginal list)
    print(f"Reversed list: {l[::-1]}")
    


exercise_1()