# Adding an input to the file
file_input = open("read.txt", 'a')

# Writing to the file

file_input.write("This is a new line added to the file.\n")
file_input.close()

'''	 a is the append mode, it appends the new data to the end of the file.

w is the write mode, it overwrites the whole file with the new data.

r is the read mode, it allows you to read the file. '''