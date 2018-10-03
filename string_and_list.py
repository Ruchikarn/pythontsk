# sample_paragraph = 'Broadway Infosys offers special Python training courses in Nepal as it is considered as one of the popular programming languages that is attracting large pool of developers worldwide. The giants like Google, Yahoo and Amazon are using Python for their special projects and this has further inspired many developers to learn this programming language in Nepal'
#
#
# sample_list = sample_paragraph.split(' ')
#
# print(sample_list)
#
# print(len(sample_list))

marks = '45,35,25,10,15'

print(type(marks))

mark_list = marks.split(',')

print(type(mark_list))

print(mark_list[-1])

mark_list.append('65')

print(mark_list)


date = '2075-05-23'

parts = date.split('-')

print('Day is', parts[2])