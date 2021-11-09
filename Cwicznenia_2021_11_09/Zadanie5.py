def str_to_int(user_input):
    #48 - 57 cyfry
    #45 - minus
    #43 - plus
    output = ''
    multipler = 1
    last_char_was_digit = False
    we_power = False
    power = ''
    if user_input[0] in ['+', '-']:
        multipler *= -1 if user_input[0] == '-' else 1
        for char in user_input[1:]:
            if char.isdigit() and not we_power:
                output += char
                last_char_was_digit = True
            elif char == 'e' and last_char_was_digit:
                we_power = True
            elif we_power and char.isdigit():
                power += char
            elif not char.isdigit():
                return int(output) * multipler * 10**int(power)
        

print(str_to_int('-10e2faff'))
                
