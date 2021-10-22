from random import randint

def exercise_3():
    #size of matrix, and scope of generated numbers
    SCOPE = 5
    
    #lists that will contain max and minimum values of each column of the matrix
    maxes =[]
    mins = []


    #generating list of lists (matrix) with random values from -scope to scope (from -5 to 5)
    l = [[randint(-SCOPE,SCOPE)for x in range(SCOPE)] for x in range(SCOPE)]

    # finding lowest and highest element of each column by iterating through them and adding them to lists
    for i in range(len(l)):
        max_of_cols = l[i][0]
        min_of_cols = l[i][0]
        for j in range(len(l[0])):
           max_of_cols = l[j][i] if l[j][i] > max_of_cols else max_of_cols
           min_of_cols = l[j][i] if l[j][i] < min_of_cols else min_of_cols
        maxes.append(max_of_cols)
        mins.append(min_of_cols)
    
    #output 
    print('Highest values of each column: ', *maxes)
    print('Lowest values of each column: ', *mins)
    for line in l:
        print('{:>5}{:>5}{:>5}{:>5}{:>5}'.format(*line))
exercise_3()