#dictionaries are used to store the data in key:value pair,
# they are changeable and do not ALLOW duplicate values
#to run our automation scripts on different environments we go for dictionaries
#that is running the same testcases at multiple environments.

dict1={} #it is a empty dictionary.
print(type(dict1))
dict2={1:20,2:30,3:40,4:50}
dict3={"qa":"tester", "lang":"python", "exp":"3years"}#key may be int or string and vice versa
dict4={'name1':'ram', 'job':'qa', 'city':'pune', 4:'uat'} #strings can be defined in single coat

print(dict4['city'])#just provide key it will return the value from the dictionary.
dict2[5]=80 #add a value tothe dictionary
dict4['salary']='3.2lpa'
print(dict2)# to add key and value to the existing dictionary
print(dict4)
dict4.pop(4) #this pop will remove the item from the dictionary.
print(dict4)