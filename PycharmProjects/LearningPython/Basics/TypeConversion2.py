num1=input("enter first decimal number: \n")#10.5
num2=input("enter second decimal number: \n")#10.5
print(float(num1)+int(num2))#ValueError: invalid literal for int() with base 10: '10.5', we can't
# provide decimal value to the int datatype, int doesn't support float wereas float supports int
#float variable can hold integer value but int cannot hold float value so thats why we are getting value error
