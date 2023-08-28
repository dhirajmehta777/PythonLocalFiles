try:
    print("input first number: \n")
    x=int(input())
    print("input second number: \n")
    y=int(input())
    if y==0:
        raise Exception("the denominator is Zero")
    print(x/y)
except Exception as e:
    print(e)
    print("in except block")#if there is exception then except block executes
else:
    print("in else block")#if there is no exception then else block will execute
finally:
    print("this will always executes irrespective of exception")#if there is a file which is open and
    # need to be closed but due to some exception it might not been closed in that case the
    # closing file script or method should be called in finally block so that irrespective of
    # exception file will be closed
    #here except block gets excuted only when there is exception