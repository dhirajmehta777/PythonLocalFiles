"""
Ex2:Importing modules from two different packages
Ex3:Importing classes from different modules and packages
"""
import  sys
sys.path.append("/home/excellarate/PycharmProjects/LearningPython/Pack3")
from module3 import *

sys.path.append("/home/excellarate/PycharmProjects/LearningPython/Pack3/Pack4")
from module4 import *

display()
show()