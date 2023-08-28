import  re
# S=input()
# pattern=r'([a-z A-Z 0-9])\1'
# m=re.search(pattern,S)
# if m:
#     print(m.groups()[0])
# else:
#     print(-1)

"""
Ex:for Regular Expression
"""
# String="Jhon has 6 cats but I think my friend Susan has 3 dogs and Mike has 8 fishes"
# s=re.findall('[A-Za-z]+ \w+ \d+ \w+',String)
# print(s)
"""
Ex:To pull out just names
"""
# String="Jhon has 6 cats but I think my friend Susan has 3 dogs and Mike has 8 fishes"
# s=re.findall('([A-Za-z]+) \w+ \d+ \w+',String)
# print(s)
"""
Ex:To pull out animals
"""
# String="Jhon has 6 cats but I think my friend Susan has 3 dogs and Mike has 8 fishes"
# s=re.findall('[A-Za-z]+ \w+ \d+ (\w+)',String)
# print(s)
"""
Ex:To pull out names,digits,animals
"""
# String="Jhon has 6 cats but I think my friend Susan has 3 dogs and Mike has 8 fishes"
# s=re.findall('([A-Za-z]+) \w+ (\d+) (\w+)',String)
# print(s)#returns [('Jhon', '6', 'cats'), ('Susan', '3', 'dogs'), ('Mike', '8', 'fishes')],list(zip(*s))
# print(list(zip(*s)))#[('Jhon', 'Susan', 'Mike'), ('6', '3', '8'), ('cats', 'dogs', 'fishes')]
"""
Ex:for group() and groups()
"""
# String="Jhon has 6 cats but I think my friend Susan has 3 dogs and Mike has 8 fishes"
# s=re.search('([A-Za-z]+) \w+ (\d+) (\w+)',String)
# print(s.group(0))#Jhon has 6 cats
# print(s.groups())#('Jhon', '6', 'cats')
# print(s.group(1))
# print(s.group(2))
# print(s.group(3))
# print(s.group(1,3))
# print(s.span(1))
# print(s.span(2))
# print(s.span(3))

"""
Ex:using for loop
"""
# String="Jhon has 6 cats but I think my friend Susan has 3 dogs and Mike has 8 fishes"
# s=re.findall('(([A-Za-z]+) \w+ (\d+) (\w+))',String)
# print(s)
# for i in s:
#     print(i[3])

"""
Ex:Using Iterator
"""
# String="Jhon has 6 cats but I think my friend Susan has 3 dogs and Mike has 8 fishes"
# s=re.finditer('([A-Za-z]+) \w+ (\d+) (\w+)',String)
# print(next(s).group())#Jhon has 6 cats
# print(next(s).group())#Susan has 3 dogs
# print(next(s).group())#Mike has 8 fishes
# print(next(s).groups())#('Jhon', '6', 'cats')
# print(next(s).groups())#('Susan', '3', 'dogs')
# print(next(s).groups())#('Mike', '8', 'fishes')

"""
Ex:Using for loop along with iterator
"""
# String="Jhon has 6 cats but I think my friend Susan has 3 dogs and Mike has 8 fishes"
# s=re.finditer('([A-Za-z]+) \w+ (\d+) (\w+)',String)
# # for element in s:
# #     print(element.group(1,3,2))
# for element in s:
#     print(element.groups())

"""
Ex:how many instances of group repeated
"""
st='ababababababab'
str=re.search('(ab)+',st)
print(str)





"""
group()
A group() expression returns one or more subgroups of the match.
Code

>>> import re
>>> m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
>>> m.group(0)       # The entire match 
'username@hackerrank.com'
>>> m.group(1)       # The first parenthesized subgroup.
'username'
>>> m.group(2)       # The second parenthesized subgroup.
'hackerrank'
>>> m.group(3)       # The third parenthesized subgroup.
'com'
>>> m.group(1,2,3)   # Multiple arguments give us a tuple.
('username', 'hackerrank', 'com')
groups()
A groups() expression returns a tuple containing all the subgroups of the match.
Code

>>> import re
>>> m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
>>> m.groups()
('username', 'hackerrank', 'com')
groupdict()
A groupdict() expression returns a dictionary containing all the named subgroups of the match, keyed by the subgroup name.
Code

>>> m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','myname@hackerrank.com')
>>> m.groupdict()
{'website': 'hackerrank', 'user': 'myname', 'extension': 'com'}
Task

You are given a string .
Your task is to find the first occurrence of an alphanumeric character in  (read from left to right) that has consecutive repetitions.

Input Format

A single line of input containing the string .

Constraints


Output Format

Print the first occurrence of the repeating character. If there are no repeating characters, print -1.

Sample Input

..12345678910111213141516171820212223
"""