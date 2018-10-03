entered_value = input('Do you want buy it?')

if entered_value == 'y' or entered_value == 'yes':
    print('Its price is $420.')
else:
    next_input = input('Do you want another product?')
    if next_input == 'y' or next_input == 'yes':
        print('1) Iphone X ($1000)\n'
              '2) Samsung S9 ($900)')
    else:
        print('Thanks for visiting. See you again.')
