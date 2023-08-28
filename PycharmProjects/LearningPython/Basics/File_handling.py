"""
we can use file handling to read and write data to and from the file.
File Operations:
-Openning a file
-Closing a file
-writing data into the file
-Reading data into the file
-Appending data
-Looping through the data using for loop
"""
"""
Opening & Closing Files
Before reading/writing we first need to open the file. Syntex of opening a file is:
f=open(filename, mode)
After you have finished reading or writing to the file you need to close the file using: 
close() method like this, f.close() were f is a file pointer
Different modes of openning a file are:
"r":Open a file for read only.
"w":Open a file for writing, if file already exists its data will be cleared before opening.
Otherwise new file will be created.
"a":Opens a file in append mode i.e, to write a data to the end of the file.
"""
# file=open('/home/excellarate/fileIO/writedemo1.txt','w')#this will open file for writing
# file.write('This is my first line\n')
# file.write('This is my second line')
# file.close()

"""
Reading Data from the file
To read data from the file we need one of these three methods.
read([number]):this method will return number of characters from the file. if omitted it will 
read the entire contents of the file.
readline():this method will return the next line of the file
readlines():read all the lines as a list of strings in the file
"""
#Reading all the data at once:
f=open('/home/excellarate/fileIO/writedemo1.txt','r')
# print(f.read())#read entire content of file at once
print(f.read(1))#reads only 1 character and prints the same
# print(f.read(5))#reads 5 char
# print(f.read(10))#reads 10 char
f.close()

"""
Using readlines command
"""
f=open('/home/excellarate/fileIO/writedemo1.txt','r')
print(f.readlines())#read entire content of file in array format
#o/p ['This is my first line\n', 'This is my second line']
f.close()

"""
Using readline command, this will read singleline 
"""
f=open('/home/excellarate/fileIO/writedemo1.txt','r')
print(f.readline())#read single line
f.close()

"""
Appending Data:
To append the data you need to open the file in 'a' mode
"""
# f=open('/home/excellarate/fileIO/writedemo1.txt','a')
# f.write("This is my third line\n")
# f.close()

"""
Looping through the data using for loop
"""
f=open('/home/excellarate/fileIO/writedemo1.txt','r')
for line in f:
    print(line)
f.close()