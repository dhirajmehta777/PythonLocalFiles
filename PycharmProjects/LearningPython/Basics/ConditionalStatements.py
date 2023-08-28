a=33
# if a>20:
#     print("True Condition")
# else:
#     print("False condition")
####################################################################
# if False:
#     print("True Condition")#if true then this will print
# else:
#     print("False Condition")#if false then this will print
#######################################################################
# if 1:
#     print("True Condition")#1 represents True
# else:
#     print("False Condition")#0 represents False
#######################################################################
if a%2==0:
    print("number is even")
else:
    print("number is odd")
#####################################################################
#Multiple Statements under if else block

if False:
    print("Statement1")#if true if block will execute
    print("Statement2")
    print("Statement3")
else:
    print("Statement4")# if false else block will execute
    print("Statement5")

print("this is not a part of if or else block")
##########################################################################
#single statements in single line
print("welcome") if True else print("python")
print("welcome") if False else print("python")
print("welcome") if 10<20 else print("python")
print("welcome") if 10>20 else print("python")
######################################################################
#multiple statement in single line
{print("welcome1"),print("python1")} if True else {print("welcome2"),print("python2")}
{print("welcome1"),print("python1")} if False else {print("welcome2"),print("python2")}
#for multiple statements we need to put them into curly braces{}
#################################################################################3
#elif command in python
b=50
if b==10:
    print("Ten")
elif b==20:
    print("twenty")
elif b==30:
    print("thirty")
else:
    print("not listed")#else block is optional for elif statement, and if we more than one condition
    #then we go for elif command.


