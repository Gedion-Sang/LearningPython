# Execute the code in the file to read a line from the file

file_input = open("read.txt", 'r')
data = file_input.readlines()
print(data)

''' readline() method reads a line from one line of the file.

readlines() with a specified argument reads a certain number of lines from the file.

readlines() method reads all lines of the file and returns them as a list. '''