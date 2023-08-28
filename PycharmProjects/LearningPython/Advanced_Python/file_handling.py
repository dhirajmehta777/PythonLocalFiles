"""
File Handling:
"""
"""
-->To store the data permanently then we go for file handling concept.
-->To store the data temporary then we go for list, tuple, dict so it will get vanish once the execution is completed.
"""
# l=[]
# n=int(input("Enter number of values:"))
# for i in range(n):
#     x=input('Enter Value:')
#     l.append(x)
# print(l)#here once you exicute then the data will not be available for future reference because it will be store
#inside PVM as a part of heap

"""
To avoid this we go for files and database concept so that we can store the data permanently
files:if we want to store small amount of data then we go for files
database:if we want to store huge data then prefer database
bigdata technologies:more the huge data
"""

"""
here to store the data permanently we have two types of files:
1.text files:text data like names of student, marks of student
2.Binary files:images, videos, audio files etc
"""
"""
If you want to perform any operation on files then first thing we have to open the file.
we have a method called open()
open(filename,mode)
"""

"""
Example:To open the abc.text file for write operation.
f=open('abc.txt','w')
"""
"""
The allowed modes in the python are:
1. r(read operation):
The default mode will always be r mode only, provided if you not specify any mode(f=open('abc.txt'))
open an existing file for read operation.
If the specified file is not available then we will get FileNotFoundError
f=open('abc.txt','r')
==================================================================================================
w(write operation)
f=open('abc.txt','w')
open abc.txt file for write operation
if the specified file is not available then this line will create that file.
if file already contains some data...it will perform overwrite operation.
===================================================================================================
a(append operation)
f=open('abc.txt','a')
open abc.txt file for append operation
if the specified file is not available then this line will create that file.
if file already contains some data...it will not perform overwrite operation, it will always going to write continuation.
===================================================================================================
w+(write and read)
To write and then read operation
It will overwrite the existing data
===================================================================================================
r+(read and write)
To read and then write operation
and the previous data will not be deleted
===================================================================================================
a+(append and read)
first append and then read operation
It wont overwrite the existing data
===================================================================================================
x(exclusive)
f=open('abc.txt','x')
It is for write operation
compulsory file should not be available
if abc.txt is already available then we will get FileExistsError
===================================================================================================
These modes are available only for text files not for binary files
For binary files also we have 7 modes available.(rb,wb,ab,r+b,w+b,a+b,xb)
"""
"""
f=open('abc.txt','r')
here we have open the file in read mode 
After reading the file we need to close the file 
f.close()
here f is an object so the various properties of an file object are....
f.name
f.mode
f.closed
f.readable()
f.writable()
here the first three properties are variables or attributes were as the next twoare methods
"""
"""
Example1:
"""
# f=open('abc.txt','w')
# print('file name:',f.name)
# print('file mode:',f.mode)
# print('is file readable?',f.readable())
# print('is file writeable:',f.writable())
# f.close()
# print('is file closed:',f.closed)

"""
Example2:
"""
# f=open('abc.txt','w')
# f.write('Learning\n')
# f.write('Advanced\n')
# f.write('Python\n')
# f.close()
# print('write operation completed')
"""
Example3:
"""
# f=open('abc.txt','w')
# l=['sunny\n','bunny\n','chinny\n','vinny\n']
# f.writelines(l)
# f.close()
# print('write operation completed')

"""
If we want to provide the inputs dynamically here is the example:
"""
# fname=input('Enter file name:')
# f=open(fname,'w')
# feedback=input('Enter your feedback data....')
# f.write(feedback)
# f.close()

"""
Reading character data from the text files...
f.read()--->To read total data from the file.
f.read(n)--->To read n characters from the file.
f.readline()--->To read only one line
f.readlines()--->To read all lines into a lists
"""
"""
read data from one file and copy the same in another file 
"""
f1=open('abc.txt')
f2=open('def.txt','w')
f2.write(f1.read())
f1.close()
f2.close()
print('Data copied from abc.txt to def.txt')

"""
if the file has to close automatically we need not to close the file explicitly this can be done by "with statement"
"""
with open('abc.txt','w') as f:
    f.write('Durga\n')
    f.write('Software\n')
    f.write('Solutions\n')
    print('Is file closed?:',f.closed)#o/p is false because within the with block the fill will not be closed
print('Is file closed?:',f.closed)