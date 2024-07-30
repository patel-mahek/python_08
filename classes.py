# # A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# # create class
# class User:
#     # constructor
#     def __init__(self,name,age,email):
#         self.email = email
#         self.name = name
#         self.age = age

#     # method
#     def greeting(self):
#         return f'My name is {self.name} and I am {self.age}'

#     def has_birthday(self):
#         self.age += 1

# # intialise a user object
# mahek = User('mahek patel',18,'mahekpatel@mail.com')

# print(mahek.greeting())
# mahek.has_birthday()
# print(mahek.greeting())

# # extend class
# class Customer(User):
#     # constructor
#     def __init__(self,name,age,email):
#         self.email = email
#         self.name = name
#         self.age = age
#         self.balance =0

#     def set_balance(self,balance):
#         self.balance = balance
    
#     def greeting(self):
#         return f'My name is {self.name} and I am {self.age} and i have balance of {self.balance}'

# # init customer object
# janet = Customer('janet',18,'janet@yahoo.com')
# janet.set_balance(500)
# print(janet.greeting())