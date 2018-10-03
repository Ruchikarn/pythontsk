names = ['ram kumar shrama', 'john doe', 'josh prasad talyor', 'dave tan']

with_middle_name = []
without_middle_name = []

for name in names:
    parts = name.split(' ')
    print('parts=>', parts)
    if len(parts) == 3:
        with_middle_name.append(name)
    else:
        without_middle_name.append(name)

print('The names with middle name are', with_middle_name)

print('The names with middle name are', without_middle_name)
