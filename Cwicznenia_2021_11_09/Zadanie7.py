import re

def HTML_color_to_RGB(hex_color):

    match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', hex_color)
    if match:
        hex_color = hex_color[1:].lower()
        hex_letters_to_decimal = {
            '0' : 0,
            '1' : 1,
            '2' : 2,
            '3' : 3,
            '4' : 4,
            '5' : 5,
            '6' : 6,
            '7' : 7,
            '8' : 8,
            '9' : 9,
            'a' : 10,
            'b' : 11,
            'c' : 12,
            'd' : 13,
            'e' : 14,
            'f' : 15
        }
        output = []
        for i in range(0, len(hex_color), 2):
            output.append(hex_letters_to_decimal[hex_color[i]] * 16 + hex_letters_to_decimal[hex_color[i+1]])
        return output

    else:
        print("Color has to be given in hex code")
        return False


print(HTML_color_to_RGB('#FF0050'))
print(HTML_color_to_RGB('#001020'))