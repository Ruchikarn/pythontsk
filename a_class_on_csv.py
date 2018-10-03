import csv

with open('data.csv', 'r', newline='\n') as read_file:
    reader = csv.DictReader(read_file)

    print(reader.fieldnames)

    highest = 0

    for row in reader:
        mark = int(row['Mark'])

        if mark > highest:
            highest = mark

    print(highest)



