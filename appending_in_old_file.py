with open('hello.txt', 'r+') as append_file:
    for line in append_file:
        pass
    append_file.write('\nIn last line')
