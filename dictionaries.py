# # A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# # Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# # create
# person = {
#     'frist_born':'john',
#     'last_name':'Doe',
#     'age':18,
# }

# print(person,type(person))

# # use a constructor
# person2 = dict(first_name='Sara',last_name='Williams')
# print(person2,type(person2))

# # Get value
# print(person['first_name'])
# print(person.get('last_name'))


# # add key/value
# person['phone'] = '555-555-5555'

# # Get keys
# print(person.keys())

# # get items
# print(person.items())

# # Copy 
# person2 = person.copy()
# person2['city'] = 'Boston'
# print(person2)

# # remove 
# del(person['age'])
# person.pop('phone')
# print(person2)

# # Clear
# person.clear()
# print(person2)

# # Get length
# print(len(person2))

# # list of Dic
# people=[
#     {'name':'mahek','age':18},
#     {'name':'shraddha','age':40}
# ]
# print(people[1]['name'])

