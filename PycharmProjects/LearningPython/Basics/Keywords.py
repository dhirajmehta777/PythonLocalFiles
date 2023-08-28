import keyword

print(keyword.kwlist) #This is the command prints all the keywords suppoprted by python 3.x
print(keyword.iskeyword("try"))

"""
But in 2.X the paranthesis () is not required 
i.e, print keyword.kwlist.
Where as in 3.X we must put the ()parantyhesis.
Removed print keyword command from 3.X
newly added keyword in python 3.X are false, None, True
In python 3.x the print command is converted as function print(). 
"""