import json

users = {}

users = {'alex': 'father',
         'Anna': 'mather',
         'dany': 'kind',
         'aliona': 'kind',
         'pet': ['turtle', 'hamster', 'kat']}

users_1 = {'alex': {'role': 'father',
                    'weight': 85,
                    'children': 2},
           'Anna': 'mather',
           'dany': 'kind',
           'aliona': 'kind',
           'pet': ['turtle', 'hamster', 'kat']}

users_1['pet'][0] = 'rafael'


print(users)
print(users_1)

'users.pop(key) - удаляет по ключу'