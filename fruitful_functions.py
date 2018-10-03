def fruitful_even_or_odd(no):
    if no % 2 == 0:
        return True
    else:
        return False


def void_even_or_odd(no):
    if no % 2 == 0:
        print('Even')
    else:
        print('Odd')


entered_number = input('Enter a number')

if fruitful_even_or_odd(int(entered_number)):
    print('Thank you for entering even number')
else:
    print('Please try again')

# print(fruitful_even_or_odd(9))


# print(void_even_or_odd(8))

# def fruitful_add(a, b):
#     return a + b
#
#
# def void_add(a, b):
#     print(a + b)
#
#
# c = fruitful_add(5, 7)
# print(c)
# d = void_add(5, 8)
# print(d)
