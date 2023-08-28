name="jhon"
age=25
sal=100000.25
#Approach1 how to print
print(name, age, sal)
#Approach2
print("Name is:", name)
print("Age is:", age)
print("Salary is:", sal)
#Approach3 using percental % operator, type is imp
print("Name:%s Age:%d Salary:%g"%(name,age,sal))
#Approach4 type is not imp but value is imp
print("Name:{} Age:{} Salary:{}".format(name,age,sal))
print("Name:{} Age:{} Salary:{}".format(age,age,age))
#Approach5 index starts from zero
print("Name:{0} Age:{1} Salary:{2}".format(name,age,sal))
print("Name:{0} Age:{0} Salary:{0}".format(name,age,sal))
