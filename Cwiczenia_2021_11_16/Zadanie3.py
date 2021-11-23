import os, os.path

def sum_and_save(file_name):
    path = os.path.dirname(os.path.realpath(__file__))
    file = os.path.join(path, file_name)
    sum = 0
    if os.path.isfile(file):
        with open(file, 'a+') as f:
            f.seek(0)
            for number in f:
                x = int(number)
                sum += x
            if sum == 0:
                f.write('1' + '\n')
            else:
                f.write(str(sum) + '\n')
    else:
        with open(file, 'w') as f:
            f.write('1')


sum_and_save("test1.txt")