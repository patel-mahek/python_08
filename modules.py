# # A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# # core python modules (we dont need to install it)
# import datetime
# today = datetime.date.today()
# print(today)

# # if we just want to import the date
# from datetime import date
# today = date.today()
# print(today)

# import time
# timestamp = time.time()
# print(timestamp)

# from time import time
# timestamp = time()
# print(timestamp)

# # pip module
# from camelcase import CamelCase

# c = CamelCase()
# print(c.hump("hello this is lowercase"))

# # custom modules
# import validator
# from validator import validate_email

# email = 'test@test.com'

# if validate_email(email):
#     print("email is valid")
# else:
#     print("email is not valid")