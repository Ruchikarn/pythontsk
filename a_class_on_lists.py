sample_list = ['Ram', 'Shyam', 'Hari', 'John', 'John']

sample_list[0] = 'Josh'

print(sample_list.count('John'))
sample_list.insert(3, 'Rajesh')
print(sample_list)
print(sample_list.index('John'))

last_name = sample_list.pop()

print('Last name', last_name)
print(sample_list)

first_name = sample_list.pop(0)

print(sample_list)

sample_list.append('Last Item')

print(sample_list)