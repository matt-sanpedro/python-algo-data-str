unique_list = [(1,3),(2,2)]

if (1,3) in unique_list:
    print('ok')

my_string = ''
my_string += '{}{}'.format('A',3)
print(my_string)
my_string += '{}{}'.format('C',6)
print(my_string)

test_string = 'AAAAABBBBCCCC'
for letter in test_string[1:]:
    print(letter)