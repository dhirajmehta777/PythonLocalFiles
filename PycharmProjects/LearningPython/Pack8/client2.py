import sys
sys.path.append("/Pack6")
from emp import Employee
obj=Employee(101,'Scott',40000)
obj.displayemp()
sys.path.append("/Pack7")
from stu import Student
obj1=Student(102,'Tom','A')
obj1.displaystu()
