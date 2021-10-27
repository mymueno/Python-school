def exercise_2():
    print(number_to_verbal_notation(6))
    print(number_to_verbal_notation(14))
    print(number_to_verbal_notation(10))
    print(number_to_verbal_notation(75))
    print(number_to_verbal_notation(100))
    print(number_to_verbal_notation(1000))
    print(number_to_verbal_notation(100000))
    print(number_to_verbal_notation(1000000))

def number_to_verbal_notation(number):

    #declaration of dictionaries that represents verbal notation of specific numbers and digits

    verbal_units = {
        0: '',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine'
    }
    verbal_teens = {
        
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen'
    }
    verbal_dozens = {
        
        20: 'twenty',
        30: 'thrity',
        40: 'fourty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
    }
    
    verbal_others = {
        
        100: 'hundred',
        1000: 'thousand',
        1000000: 'milion'
    }

    # declaring string representation of number and reversing it
    num_str = str(number)
    num_str = num_str[::-1]

    # declaring list that contains 3-digits long string numbers of the input number
    # in case of making verbal notation of number we want to operate on sets of 3 digits of this number
    # starting from units 
    help_list = [num_str[set_of_3_digits:set_of_3_digits+3] for set_of_3_digits in range(0, len(num_str), 3)]
    print(help_list)

    # declaring temp variable that is going to be our iterator that helps us to specify if each iteration operates on thousands, milions etc.
    temp = 0

    output = ""

    #iterating through help list 
    for set_of_3_digits in help_list:

        #output that helps us contain verbal notation of each set
        temp_output = ""
        # finding verbal representation of each set by checking its value
        if len(set_of_3_digits) > 1:
            #reversing sets to get it in the right order
            set_of_3_digits_rev = set_of_3_digits[::-1]
            #finding dozens by taking last two digits of set
            dozens = int(set_of_3_digits_rev[-2:])
            print(dozens)
            if dozens > 19: 
                temp_output += verbal_dozens[dozens - (dozens % 10)] + ('-' if dozens % 10 != 0 else '') + verbal_units[dozens%10] +  ' '
            elif 10 <= dozens < 20:
                temp_output += verbal_teens[dozens]
            else:
                temp_output += verbal_units[dozens]
            if len(set_of_3_digits) == 3:
                hundreds = int(set_of_3_digits_rev[0])
                temp_output = (verbal_units[hundreds]) + ' ' + (verbal_others[100] if hundreds > 0 else '') + ' ' + temp_output
        #if our set is less than 10
        else:
            temp_output = verbal_units[int(set_of_3_digits)]
            set_of_3_digits_rev = int(set_of_3_digits)
        
        #adding our verbal notation of set to whole output and checking if it's thousands or milions etc. based on value of temp variable
        if temp == 0:
            output = temp_output + ' ' + output
        elif temp == 1:
            print(set_of_3_digits, set_of_3_digits_rev)
            output = temp_output + (' ' + verbal_others[1000] if int(set_of_3_digits_rev) != 0 else '') + ' ' + output
        elif temp == 2:
            print("jestem tu", set_of_3_digits_rev, print(set_of_3_digits))
            output = temp_output + (' ' + verbal_others[1000000] if int(set_of_3_digits_rev) != 0 else '') + ' ' + output
        temp += 1

    #getting rid of spaces
    output_list = output.split()
    
    return ''.join(x + ' ' for x in output_list)
    

        


    

        
    

        
    



exercise_2()
