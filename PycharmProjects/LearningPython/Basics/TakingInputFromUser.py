num1=input("enter first number: \n")#30 treated as string
num2=input("enter second number: \n")#50 treated as string
print(num1+num2) #o/p 3050 since input function takes inputs from user
# in the form of string hencde it has concatenated to add the numbers
# we need to convert those strings into integer
print("#################################################################")
###################################################################
#converting string into integer by type casting with int
num3=int(input("enter the third number: \n"))
num4=int(input("enter the fourth number: \n"))
print(num3+num4)
print("##################################################################")
#####################OR#############################
num5=input("enter the fifth number: \n")
num6=input("enter the sixth number: \n")
print(int(num5)+int(num6))