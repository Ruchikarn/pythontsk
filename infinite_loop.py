while True:
    entered_number = int(input('Enter a number'))
    if entered_number <= 10:
        for i in range(1, 11):
            print(entered_number, ' X ', i, ' = ', entered_number * i)
    if input('Do you want to close?') == 'y':
        break
