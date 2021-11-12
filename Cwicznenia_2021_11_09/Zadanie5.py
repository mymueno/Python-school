def str_to_int(user_input):
    output = ''
    multipler = 1
    last_char_was_digit = False
    we_power = False
    power = ''
    if not user_input == "" and user_input[0] in ['+', '-']:
        multipler *= -1 if user_input[0] == '-' else 1
        for index, char in enumerate(user_input[1:]):
            if char.isdigit() and not we_power:
                output += char
                last_char_was_digit = True
            elif char == 'e' and last_char_was_digit and user_input[index+2].isdigit():
                we_power = True
            elif we_power and char.isdigit():
                power += char
            elif not char.isdigit() and we_power:
                return int(output) * multipler * 10**int(power)
            elif not char.isdigit() and output:
                return int(output)
    elif not user_input == "":
        for index, char in enumerate(user_input):
            if char.isdigit() and not we_power:
                output += char
                last_char_was_digit = True
            elif char == 'e' and last_char_was_digit and user_input[index+1].isdigit():
                we_power = True
            elif we_power and char.isdigit():
                power += char
            elif not char.isdigit() and we_power:
                return int(output) * multipler * 10**int(power)
            elif not char.isdigit() and output:
                return int(output)
    
    if output != '' and not we_power:
        return int(output)
    elif we_power:
        return int(output) * multipler * 10**int(power)
    else:
        return 0
    
print(str_to_int('4235-10e2faff'))
print(str_to_int("+12"))
print(str_to_int("0001"))
print(str_to_int("991-234-23"))
print(str_to_int("+zonk"))
print(str_to_int(""))
print(str_to_int("-12e5"))
print(str_to_int("-12e-5"))    
