str=input("Enter the string:")
length=len(str)
for row in range(length):
    for col in range(row+1):
        print(str[col],end="")
    print()