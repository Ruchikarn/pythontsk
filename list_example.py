marks = [55, 64, 73, 43, 76]

total = 0

for mark in marks:
    total += mark

percentage = round(total / 5, 2)
print('Student total marks is', total)
print('Percentage of student is', percentage)

if percentage >= 90:
    print('A+')
elif percentage >= 80:
    print('A')
elif percentage >= 70:
    print('B+')
else:
    print('please calculate yourself')


