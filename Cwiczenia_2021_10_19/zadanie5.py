from random import randint


def exercise_5():

    valid_input = False

    while not valid_input:
        try:
            scope = int(input("Input scope: "))            
            a = int(input("Input 1st number: "))
            b = int(input("Input 2nd number: "))
            valid_input = True if a > 0 and b > 0 and scope > 0 else False
            if not valid_input:
                print("Scope must be a positive integer!!!")
        except ValueError:
            print("Scope must be a positive integer!!!")


    #if user inputs higher number 1st, swap them 
    if a > b:
        temp = a
        a = b
        b = temp

    #generating scope-sized matrix filled by random numbers from a to b 
    l = [[randint(a,b) for x in range(scope)] for x in range(scope)]

    #displaying matrix
    for line in l:
        print(line)

    #variables that will contain sum of diagonal numbers and sum of elements that are on odd indexes
    sum = 0
    sum_of_odd_lists = 0
    
    #looping through list to calculate those sums
    for i in range(len(l)):
        for j in range(len(l[0])):
            sum += l[i][j] if i == j else 0
            sum_of_odd_lists += l[i][j] if i % 2 == 1 and j % 2 == 1 else 0

    
    print("Sum of numbers on diagonal: ",sum)
    print("Sum of elements on od indexes: ",sum_of_odd_lists)

    #reversing list
    l.reverse()

    #reversing sublists inside the list
    for sub_list in l:
        sub_list.reverse()
    
    #displaying reversed list
    for line in l:
        print(line)


exercise_5()