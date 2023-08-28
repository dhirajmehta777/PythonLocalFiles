"""
Ex1:Importing modules from single package

"""
import sys
sys.path.append("/home/excellarate/PycharmProjects/LearningPython/Pack1");
#Approach1:
import module1
import  module2

module1.display()
module2.show()

#Approach2
from module1 import *
from module2 import *
display()
show()