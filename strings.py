# # Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

# name = 'mahek'
# age =18

# #concatenate

# print("hello my name is " + name)
# print("hello my age is "+str(age))

# # String Formatting

# #arguments by position
# print("hello my name is {name} and i am {age}".format(name=name, age=age))
# # here {name} are called the place holders 
# # naem here name= name 
# # the first name denotes the placeholder and the second is the name of the variable 

# # F-strings
# print(f"hello my name is {name} and i am {age}")
# # here we are directly using the variables

# # String Methods
# s= "hello world"

# print(s.capitalize())

# # Make all uppercase
# print(s.upper())

# # Make all lower
# print(s.lower())

# # Swap case
# print(s.swapcase())

# # Get length
# print(len(s))

# # Replace
# print(s.replace('world', 'everyone'))

# # Count
# sub = 'h'
# print(s.count(sub))

# # Starts with
# print(s.startswith('hello'))

# # Ends with
# print(s.endswith('d'))

# # Split into a list
# print(s.split())

# # Find position
# print(s.find('r'))

# # Is all alphanumeric
# print(s.isalnum())

# # Is all alphabetic
# print(s.isalpha())

# # Is all numeric
# print(s.isnumeric())

