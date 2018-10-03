sample_file = open('hello.txt', 'w')
sample_file.write('Hello World, It will be in file.')
sample_file.close()

with open('next_hello.txt', 'w') as sample_file_1:
    sample_file_1.write('Hello World, It will be in file.')

with open('data.csv', 'r') as student_file:
    for line in student_file:
        print(line)
