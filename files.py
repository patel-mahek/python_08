# # Python has functions for creating, reading, updating, and deleting files.

# # open a file / creates a file
# myFile = open('myfile.txt','w')
# # w is for writting

# # get some info
# print('Name: ',myFile.name)
# print('Is closed: ',myFile.closed)
# # here closed is not accroding to the system byt according to the script
# print('Opening Mode: ',myFile.mode)

# # write to file
# myFile.write('I love python')
# myFile.write(' and javascript')
# myFile.close()

# # append 
# myFile = open('myfile.txt','a')
# # a is used to append 
# # w is used to override it
# myFile.write(' I also like PHP')
# myFile.close()

# # read from a file
# myFile = open('myfile.txt', 'r+')
# text = myFile.read(100)
# # reads 100 characters
# print(text)
