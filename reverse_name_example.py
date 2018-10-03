names = ['ram kumar shrama', 'john doe', 'josh prasad talyor', 'dave tan']

fixed_names = []
for name in names:
    parts = name.split(' ')
    reversed_parts = parts[::-1]
    joined_name = ' '.join(reversed_parts)
    fixed_names.append(joined_name)

print(fixed_names)
