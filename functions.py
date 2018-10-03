def even_or_odd(number):
    if number % 2 == 0:
        print('Even')
        print('Hello')
    else:
        print('Odd')


def add(a, b):
    print(a + b)


add(5, 7)


def temperature(temp):
    if temp >= 25:
        print('Hot')
    else:
        print('Cold')


temperature(34)


def positive_neg_or_zero(no):
    if no > 0:
        print('Positive')
    elif no < 0:
        print('Negative')
    else:
        print('Zero')


positive_neg_or_zero(0)


def division_calculator(marks):
    if marks >= 80:
        print('Dis')
    elif marks >= 60:
        print('1st Division')
    elif marks >= 45:
        print('2nd Division')
    elif marks >= 32:
        print('3rd Division')
    else:
        print('Fail')


division_calculator(80)


def sample_function(no):
    if no % 2 == 0:
        print('Even')
        if no % 5 == 0:
            print('Divisible by 5')
        else:
            print('Not Divisible by 5')
    else:
        print('Odd')
        if no % 5 == 0:
            print('Divisible by 5')
        else:
            print('Not Divisible by 5')
