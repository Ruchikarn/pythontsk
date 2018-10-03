numbers = [2, 3, 4, 5]

squared_numbers = []

for no in numbers:
    squared_numbers.append(no ** 2)

print(squared_numbers)

check_even_odd = lambda n: n % 2 == 0


def check(n):
    return n % 2 == 0


my_sum = lambda a, b: a + b

print(my_sum(10, 20))

palindrome = lambda s: s == s[::-1]

import math

h = lambda p, b: math.sqrt(p ** 2 + b ** 2)

print(h(3, 4))

names = ['John', 'Josh', 'Dave']

reverse_names = []  # ['nhoJ' , ...]

reverse_string = lambda s: s[::-1]

new_way = map(reverse_string, names)

print(list(new_way))


def square_number(n):
    return n ** 2


numbers = [2, 3, 4, 5]

squared_numbers = map(square_number, numbers)

print(list(squared_numbers))

male_names = ['Ram', 'Shyam', 'John']

add_title = lambda name: 'Mr. ' + name

refine_names = map(add_title, male_names)

print(list(refine_names))

total_marks = [750, 659, 560, 450, 720, 700]

calculate_percentage = lambda total: total / 8

percentages = map(calculate_percentage, total_marks)
print(list(percentages))

new_numbers = [2, 3, 4, 5, 6, 7, 8]

check_even_odd_1 = lambda n: n % 2 == 0

filtered_numbers = filter(check_even_odd_1, new_numbers)

print(list(filtered_numbers))
