my_dict = {'tuple': (1, 2, 3, 'text', 2.56),
           'list': [4, 6, 8, 'example', 5.298],
           'dict': {6: 1, 7: 2, 8: 3, 9: 4, 10: 5},
           'set': {9, 0, 10.29, True, 'last'}}

# Для того, что храниться под ключом 'tuple'

print(my_dict['tuple'][-1])

# Для того, что хранится под ключом 'list'

my_dict['list'].append('last elemet')
del my_dict['list'][1]

# Для того, что хранится под ключом 'dict'

my_dict['dict'][('i am a tuple',)] = 555
del my_dict['dict'][7]

# Для того, что хранится под ключом 'set'

my_dict['set'].add('another elemet')
my_dict['set'].remove(True)

print(my_dict)
