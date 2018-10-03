for i in range(1, 6):
    print('*' * i)

print('\n' * 2)

for i in range(5, 0, -1):
    print('*' * i)

print('\n' * 2)

for i in range(1, 6):
    print(' ' * (5 - i) + '*' * i)

print('\n' * 2)

for i in range(5, 0, -1):
    print(' ' * (5 - i) + '*' * i)

print('\n' * 2)

max_number_of_stars = 5

space_count = max_number_of_stars // 2
star_count = 1
for i in range(max_number_of_stars):
    if star_count - 2 > 0:
        print(' ' * space_count + '*' + ' ' * (star_count - 2) + '*')
    else:
        print(' ' * space_count + '*')

    if i < max_number_of_stars // 2:
        space_count -= 1
        star_count += 2
    else:
        space_count += 1
        star_count -= 2

print('\n' * 2)

max_number_of_stars = 5

space_count = max_number_of_stars // 2
star_count = 1
for i in range(max_number_of_stars):
    print(' ' * space_count + '*')
    if i < max_number_of_stars // 2:
        space_count -= 1
        star_count += 2
    else:
        space_count += 1
        star_count -= 2

print('\n' * 2)

number_of_rows = 5

outer_space = number_of_rows // 2
inner_space = -1

for i in range(number_of_rows):

    if inner_space == -1:
        print(' ' * outer_space + '*')
    else:
        print(' ' * outer_space + '*' + ' ' * inner_space + '*')

    if i < number_of_rows // 2:
        outer_space -= 1
        inner_space += 2
    else:
        outer_space += 1
        inner_space -= 2
