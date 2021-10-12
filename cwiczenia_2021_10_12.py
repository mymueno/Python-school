#Zadanie 1

def calc_bmi(weight, height):
    return weight / (height/100)**2

def is_bmi_proper(bmi):
    return True if 18.5 < bmi < 24.9 else False

def zadanie_1():
    weight = float(input("Podaj swoja wage:"))
    height = float(input("Podaj swoj wzrost:"))
    bmi = calc_bmi(weight, height)
    is_bmi_ok = is_bmi_proper(bmi)

    print("Twoje bmi to: ", bmi)
    print("waga prawidłowa" if is_bmi_ok else ("Nadwaga" if bmi > 24.9 else "Niedowaga"))

#Zadanie 2


def calculate_monthly_pay(price, num_of_installments):
    interest = 2.5

    if 12 < num_of_installments < 25:
        interest = 5.0
    elif num_of_installments >= 25:
        interest = 10.0
    
    price = price + price *interest/100
    
    return price / num_of_installments

def is_valid(num_of_installments):
    return True if 6 <= num_of_installments <= 48 and isinstance(num_of_installments, int) else False

def zadanie_2():
    price = float(input("Podaj cenę towaru: "))
    try:
        num_of_installments = int(input("Podaj ilość rat: "))
    except:
        num_of_installments = 0

    if is_valid(num_of_installments):
        print("Miesięczna rata wynosi: ",calculate_monthly_pay(price, num_of_installments))
    else:
        while not is_valid(num_of_installments):
            print("Podaj prawidłową ilośc rat")
            try:
                num_of_installments = int(input("Podaj ilość rat: "))
            except:
                continue
        print("Miesięczna rata wynosi: ",calculate_monthly_pay(price, num_of_installments))

#Zadanie 3

def zadanie_3():

    number = int(input("Podaj liczbe całkowitą: "))

    if number > 0:
        l = [i for i in range(1, number+1) if i%2 == 1]
        for item in l:
            print(item)



#Zadanie 4

def zadanie_4():
    number = int(input("Prosze podac liczbe: "))

    if number > 0:
        l = [2**i for i in range(0, number) if 2**i < number]
        print(l)


#Zadanie 5

def zadanie_5():
    sum = 0

    x = float(input("Podaj liczbe: "))
    while x != 0:
        sum += x
        x = float(input("Podaj liczbe: "))
    
    print(sum)

#Zadanie 6

def zadanie_6():
    sum = 0
    input_num = 1
    x = int(input("Podaj liczbe: "))
    max_num = x
    min_num = x
    while x != 0:
        sum += x
        x = int(input("Podaj liczbe: "))
        input_num += 1 if x != 0 else 0
        if x > max_num:
            max_num = x
        elif x < min_num:
            min_num = x
    
    print(f'Suma min i max = {min_num + max_num}')
    print(f'Srednia podanych liczb = {sum/input_num}')
    print(f'Srednia min i max = {(min_num + max_num)/2}')


zadanie_6()