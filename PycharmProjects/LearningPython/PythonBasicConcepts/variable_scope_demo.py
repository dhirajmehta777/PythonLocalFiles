"""
variable scope in python-boundary of variable within a python
local scope
global scope
global keyword
LEGB rule:Local-->Enclosing-->Global-->Build-in
"""
x=10#now these variable can be accessed in another function also.
def var_scope():
   # x=10#these variable cannot be accesed in another function
    print(x)


# def var():
#     print(x)
# var_scope()
# var()

def var():
  print(x)
var_scope()
var()
#######################################
#using global keyword
def var2():
    global a#here we are using global keyword hence even though
    # variable is defined inside fution it can be accessed outside the function
    a=30
    print(a)

def var3():
    print(a)
var2()
var3()
############################################
#Enclosing Scope: if there is function within a function that is called as enclosing
def var4():
    j=5
    print(j)
    def var5():
        print(j)#here local function can be accessed as its a child function of var4
    var5()
var4()

################################################################
def var6():
    j=10
    print(j)
    def var7():
        j = 20
        print(j)#here local function can be accessed as its a child function of var4
        def var8():
            j = 30
            print(j)
        var8()
    var7()
var6()
#here if local variable is not there it will go for enclosing variable else if both are not available
#then it will go for global variable.