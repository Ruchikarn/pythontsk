# n = int(input('Table for?\n'))
#
# for i in range(1, 11):
#     print('%d X %d = %d' % (n, i, n * i))

letter = '''
    Dear %s,
    
    I am fine and hope you are also fine ......
    ..................
    .........................
    ............... see you soon on vacation.
    
                                Regards,
                                %s
'''

sathi_list = ['Ram', 'Shyam', 'Hari', 'Gita', 'Sita']

for sathi in sathi_list:
    print(letter % (sathi, 'Bishnu'))
