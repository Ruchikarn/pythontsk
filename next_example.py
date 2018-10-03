students = [
    {'name': 'Hari', 'email': 'hello@yahoo.com', 'percent': 65},
    {'name': 'Shyam', 'email': 'shyam@gmail.com', 'percent': 33},
    {'name': 'Yadav', 'email': 'yadav@gmail.com', 'percent': 86},
    {'name': 'Josh', 'email': 'josh@outlook.com', 'percent': 31},
    {'name': 'Dave', 'email': 'dave@yahoo.com', 'percent': 67},
    {'name': 'Ram', 'email': 'josh@outlook.com', 'percent': 12},

]

fail_count = 0
gmail_count = 0

for student in students:
    # print('is a single student', student)
    if student['percent'] < 40:
        fail_count += 1

    email_parts = student['email'].split('@')
    print(email_parts)
    if email_parts[-1] == 'gmail.com':
        gmail_count += 1


print('Fail count is', fail_count)
print('Gmail User count is', gmail_count)
